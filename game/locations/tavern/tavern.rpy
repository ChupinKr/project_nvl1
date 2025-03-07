define battle_location_tavern = "tavern"
define correct_answers = 0  # Счётчик правильных ответов
define first_time_tavern = True
define m_can_go_root = False
define shoot_tits = False
define can_go_m = True

# Сцена с таверной
label tavern:
    call tavern_scene
    "Вы в таверне"
    menu:
        "Пойти в комнату" if canVisit("room"):
                jump room
        "Подойти к [m.name]" if can_go_m:
            jump go_to_miku_stand
        "Подойти к сомнительному столу" if not canVisit("bm"):
            jump suspicious_table
        "Пойти в тайный бордель" if canVisit("brothel"):
            jump brothel
        "Подойти к доске объявлений":
            jump tavern_task_board
        "Выйти в город":
                jump city

label go_to_miku_stand:
    scene bg bar_counter with fade
    show m smile with dissolve
    if first_time_tavern:
        $ first_time_tavern = False
        $ m.name = "Мику"
        m @open_smile "Привет-привет! Добро пожаловать в таверну \"Звездные осколки\"!" with dissolve
        m @smile_closed_eyes "Я Мику, хозяйка этого местечка! Если что-то нужно – просто спрашивай, не стесняйся!" with dissolve 
    else:
        m @open_smile "Ой, [hero_name]! Чего желаешь сегодня?" with dissolve
    jump miku_stand_menu

label miku_stand_menu:
    menu:
        "Поговорить":
            if not canVisit("room"):
                m @open_smile "Чем могу помочь?" 
            jump talk_miku_menu
        "Что за сомнительный столик?" if not canVisit("bm"):
            m @angry "Они всегда здесь, что-то мутят... но если решите подойти, будьте осторожны."
            jump miku_stand_menu 
        "Уйти":
            m @smile_closed_eyes "Была рада вас видеть!"
            jump tavern

label talk_miku_drinks_menu:
    m smile "У нас тут не только пиво, но и магические напитки! Что будешь?" with dissolve
    menu:
        m "Что будешь пить?"
        "Энергетический эль (10 золота)":
            m "Этот эль действительно придаст тебе сил!"
            if money >= 10:
                m @open_smile "Ооо, хорошенький выбор! Попробуй – освежает!" with dissolve
                $minusMoneyPlusChar(10, ["str"], 2)
            else:
                m "Эх, золотишка не хватает... Может, сначала квестик возьмёшь?"
        "Магический ликёр (10 золота)":
            m "Опьяняет и слегка пробуждает магическое чутье!"
            if money >= 10:
                m @open_smile  "Этот напиток буквально искрит энергией! На, попробуй!" with dissolve
                $minusMoneyPlusChar(10, ["intelligence"], 2)
            else:
                m "Эй, кажется, у тебя не хватает монеток!"
        "Чёрный ром (10 золота)":
            m "Тяжелый черный ром, после него все твое тело скажет \"Спасибо\"!"
            if money >= 10:
                m @open_smile "Ого, крепкое же пойло ты выбрал! Только не переборщи!" with dissolve
                $minusMoneyPlusChar(10, ["intelligence", "str"], 1)
            else:
                m "Хм... похоже, придётся немного подкопить!"
        "Не хочу пить":
            m @smile_closed_eyes "Окей, если передумаешь – я тут!" with dissolve
    jump talk_miku_menu


label talk_miku_menu:
    menu:
        "Обслужи меня" if my_miku.love >= 50 and m_can_go_root:
            show m smile_blush with dissolve
            m "Поднимайся по лестнице, ты знаешь, где моя комната~"
            jump miku_tavern_root
        "Снять комнату" if not canVisit("room"):
            m smile "Комната стоит 10 золотых в неделю." with dissolve
            menu:
                "Снять комнату?"
                "Беру" if money >= 10:
                    $ minusMoney(10)
                    $ updateCanVisit("room", True)
                    $ while_room = day + 2
                    jump room
                "Мне пока не по карману":
                    jump talk_miku_menu
        "Попросить что-нибудь выпить":
            m "Что есть в меню?"
            jump talk_miku_drinks_menu
        "Чем тебе помочь?":
            m "Помощь? Отличная идея! Вот что у меня для тебя есть!"
            jump talk_miku_work
        "Попросить информацию":
            jump talk_miku_info
        "Ничего":
            jump miku_stand_menu

label talk_miku_work:
    menu:
        "Помыть посуду (10 монет)":
            m "Надо мыть посуду! Только быстро, там уже очередь! Готов?"
            scene bg tavern_sink with fade
            call start_clean("dish")
            if last_clean_win:
                m "Следующую! У нас много гостей, поторопись!"
                call start_clean("dish")
                if last_clean_win:
                    m "Последнюю, быстрее!"
                    call start_clean("dish")
                    if last_clean_win:
                        m @smile_closed_eyes "Все сыты и пьяны, то что надо, так держать, [hero_name]!"
                        "Ты провёл время, помогая [m.name]"
                        "[m.name] это оценила"
                        $my_miku.addLove(5)
                        pause 3.5
                        $addMoney(10)
                    else: 
                        m "Эх, почти успели, упустили клиента."
                else: 
                    m "Жаль, но ничего, этого я знаю, он еще вернется."
            else: 
                m @angry "[hero_name], тебе не нужны деньги? Почему так плохо?!" with dissolve
            $nextTime()
            scene bg bar_counter with fade
            show m smile with dissolve
            jump talk_miku_menu
        "Прогнать шумных гостей (10 монет)":
            scene bg tavern_battle with fade
            show m angry at left with dissolve
            m "Эти парни никак не угомонятся! Выгони их, и будет тебе награда!" with dissolve
            if renpy.random.choice([False, True]) > 0:
                "Ты поговорил с клиентами, и они ушли, хоть и неохотно."
                $addMoney(10)
            else:
                "Ты поговорил с клиентами, и они не захотели уходить по хорошему"
                "Самый большой из них встает и замахивается на тебя"
                call start_battle(100, renpy.random.randint(10,150), "Бандит", battle_location_tavern)
                if last_battle_win:
                    "[m.name] это оценила"
                    m smile "Спасибо, [hero_name], ты меня снова выручил." with dissolve
                    $my_miku.addLove(10)
                    pause 3.5
                    $addMoney(10)
            scene bg bar_counter with fade
            show m smile at center with dissolve
            $nextTime()
            jump talk_miku_menu
        "Никакой работы":
            m angry "Эх, ну ладно... Может, в другой раз!" with dissolve
    jump talk_miku_menu

label talk_miku_info:
    if my_miku.love >= 10 and not canVisit("lib"):
        m "Знаешь, ты неплохой! "
        m "Ладно, расскажу тебе одну тайну... "
        m "В городе есть **тайная библиотека**, где можно найти запрещённые магические знания!"
        m "*Описание того, как найти библиотеку*"
        $ updateCanVisit("lib", True)
    elif my_miku.love >= 20 and not canVisit("tg"):
        m "Ты мне нравишься!"
        m "Дам тебе наводку: неподалёку есть место, где любой желающий может стать сильнее."
        m "*Описание того, как попасть на тренировочную площадку*"
        m "Если хочешь стать сильнее – тебе туда!"
        $ updateCanVisit("tg", True)
    elif my_miku.love >= 30 and not canVisit("bar"):
        m "Ты определённо мой типаж!"
        m "В городе есть **закрытый бар**, куда пускают только своих."
        m "Там можно найти очень... полезных знакомств!"
        m "*Описание того, как найти закрытый бар*"
        m "Скажи, что ты от меня и тебя пропустят."
        m "Ах да, бар по утрам не работает, не забудь."
        $ updateCanVisit("bar", True)
    elif my_miku.love >= 40 and not shoot_tits:
        m "Хммм, дай ка подумать.."
        show m smile_closed_eyes with dissolve
        pause 1
        m smile_stretched_buttons1 "Кажется я тебе уже всё рассказал..."
        show m smile_stretched_buttons2 with dissolve
        "Ттрррсссс.."
        show m smile_stretched_buttons3 with dissolve
        "Внезапно пуговица на ее сарафане выстреливает тебе прямо в лоб"
        show m smile_stretched_buttons4 with flash
        pause 1
        show m smile_stretched_buttons5 with dissolve
        $health -= 10
        $customNotify("Ты получил 10 единиц урона")
        $shoot_tits = True
        if health <= 0:
            $health = 0
            "Тебя добила пуговица, стоит быть аккуратнее."
            m "О нет, ты в порядке?"
            "Ты теряешь сознание"
            jump surgency_tsunade_cure
        else:
            m "О нет, ты в порядке?"
            p "Ай.. Да... Жить буду."
            "Ты пялишься на ее грудь"
            m "Прости меня, как я могу загладить свою вину?"
            menu:
                m "Как я могу загладить свою вину?"
                "Налей мне":
                    "[m.name] застегивает сарафа и дрожащими руками наливает тебе Эль"
                    show m smile_closed_eyes with dissolve
                    m smile_closed_eyes "Вот твой напиток!"
                    "[m.name] подскальзывается и проливает немного на себя"
                    m surprised_wet_top "В-вооот! Держи!" with dissolve
                    $addChar(["str"], 2)
                    p "Спасибо! Очень освежает"
                    show m smile_wet_top with dissolve
                    "[m.name] улыбается тебе"
                "Сама придумай":
                    "[m.name] снимает верх сарафана"
                    show m smile_no_top with dissolve
                    m "Эммм... Я... Я видела, как ты пялился, такого извинения будет достаточно?"
                    p "Хаха! Да, пойдет, отлично шоу, [m.name]!"
    elif my_miku.love >= 50 and not m_can_go_root:
        $m_can_go_root = True
        m "Мне нравится, что ты не просто клиент."
        m "Мне больше нечего тебе рассказать.."
        show m smile_no_top with dissolve
        m "Но я могу показать тебе нечто особенное... но только если ты готов к этому~"
        menu:
            m "Но я могу показать тебе нечто особенное, ты готов?"
            "Всегда готов":
                m "Поднимайся на второй этаж, дверь налево. Я подойду через минуту~~"
                "Ты идешь на второй этаж и заходишь в комнату [m.name]"
                scene bg miku_room_tavern with fade
                "..."
                "....."
                "........"
                show m smirk_no_top with dissolve
                m "Я долго этого ждала~~"
                call m_root_show
                jump tavern
            "Не готов":
                p "С тобой? Не думаю."
                "Ты дурак?!"
                $can_go_m = False
                show m angry with dissolve
                m "Ты! Дурак!"
                hide m with dissolve
                "[m.name] отвернулась и плачет"
                $customNotify("Ты больше не сможешь поговорить с [m.name]")
                jump tavern
    elif my_miku.love >= 60:
        m "Ты мне так много помогаешь, [hero_name]..."
        show m smile_no_top with dissolve
        m "Я долго думала, как тебе отплатить за доброту.."
        m "Думаю, тебе понравится~"
        "[m.name] встает на колени и снимает с тебя штаны"
        call m_root_tavern_blowjob
        scene bg bar_counter with fade
        show m smile_naked_cummed with dissolve
        m "Спасибо за угощение~"
        m "Мне пора переодеться, пока меня никто не увидел"
        hide m with dissolve
        show m smile_blush with dissolve
    else:
        m "Хмм, пока ты ещё не заслужил моего доверия! Может, поможешь мне с парочкой дел?"
    jump talk_miku_menu

label tavern_task_board:
    m "Эй! Смотри, не стесняйся, у нас всегда найдётся интересное задание!"
    menu:
        "Помочь стражникам (10 золота)":
            if renpy.random.randint(0,100) > 70:
                $addMoney(10)
            else:
                "Ты встретил нарушителя порядка, его надо задержать!"
                call start_battle(100, renpy.random.randint(50,120), "Бандит", battle_location_tavern)
                if last_battle_win:
                    "Ты успешно справился с противником"
                    $addMoney(10)
            $nextTime()
            "Ты провёл какое-то время, помогая стражникам следить за порядком."
        "Собрать лечебные травы (5 золота)":
            "Ты нашёл полезные травы, которые пригодятся целителям."
            $ money += 5
            $ intelligence += 1 * intelligence_mod
            $nextTime()
        "Охота на гоблинов (15 золота)":
            "Ты сразился с гоблинами и одержал победу!"
            $ money += 15
            $ strength += 1 * strength_mod
            $nextTime()
        "Уйти":
            "Ты отодишь от доски объявлений"
    jump city

# Сцена с сомнительным столом
label suspicious_table:
    call tavern_scene
    guy1 "Ну что, парниша, выглядишь, как тот, кто может сделать нужные вещи. Хочешь поговорить о том, как войти в темные дела?"
    guy2 "Тебе нужно знать кое-что, если ты хочешь быть частью нашего круга. Но для этого нужно доказать, что ты не ссышь."

    guy3 "Ты оказался в ситуации, когда враг держит твоих людей. Что будешь делать?"
    menu:
        guy3 "Ты оказался в ситуации, когда враг держит твоих людей. Что будешь делать?"
        "Взять его семью в заложники и пригрозить, что расправлюсь с ними.":
            $ correct_answers += 1  # Правильный ответ
            guy3 "Вот это я понимаю! Важно, чтобы враг знал, что у него нет выбора. Любая слабость — это шанс на поражение."
        "Попробую заплатить за их свободу, может, повезет.":
            guy2 "Слабый ход, ты не понимаешь, что с таким подходом тебя могут выдать."
        "Просто устроить засаду и уничтожить его людей, а его оставить в живых для допроса.":
            guy1 "Слишком долго думаешь, чувак, ты должен быть быстрее и жестче."

    guy1 "Тебя поймали на незаконной сделке, и стража хочет забрать твою голову. Как выберешься?"
    menu:
        guy1 "Тебя поймали на незаконной сделке, и стража хочет забрать твою голову. Как выберешься?"
        "Подкупить стражу, отстегну баблишка в сделке и они тоже будут замешаны.":
            $ correct_answers += 1  # Правильный ответ
            guy2 "Сыграно по-крупному. Крути им яйца, пока не отсохнут."
        "Сдаться и заплатить за свои грехи.":
            guy3 "Сдавайся, и ты обречен. Такие как ты, сдаются первым, а потом их используют."
        "Устроить взрыв на складе с товаром, чтобы отвлечь их внимание, и сбежать.":
            guy1 "Вот это по делу! Но у меня вопрос: как ты потом будешь уходить из города, чтобы не попасться?"

    guy2 "Как выкрутиться, если ты попал в плен к врагу, но у тебя есть информация о его слабостях?"
    menu:
        guy2 "Как выкрутиться, если ты попал в плен к врагу, но у тебя есть информация о его слабостях?"
        "Воспользоваться слабостями, загнать их в ловушку, предложить сделку, от которой не смогут отказаться и подставить.":
            $ correct_answers += 1  # Правильный ответ
            guy3 "Вот это поворот! Играй с их умом, дави каждого, кто может помешать."
        "Предложить сделку, но не раскрывать все карты.":
            guy2 "Тебя сожрут. Ты думаешь, они поверят в твои обманки?"
        "Сделать вид, что ты сошел с ума и не помнишь, что ты им должен.":
            guy1 "Ты что, с ума сошел? Если ты не будешь жестким, тебя съедят."

    guy3 "Ты оказался в засаде. Ты и твоя группа. Ты единственный, кто не был пойман. Если ты убьешь одного из своих, враги уйдут, а ты сможешь спастись. Что будешь делать?"
    menu:    
        guy3 "Ты оказался в засаде. Ты и твоя группа. Ты единственный, кто не был пойман. Если ты убьешь одного из своих, враги уйдут, а ты сможешь спастись. Что будешь делать?"
        "Убью того, кто слаб и ничего не принесет для нашей группы. Я живу — значит, всё, что важно.":
            $ correct_answers += 1  # Правильный ответ
            guy2 "Вот это решение! Правильный подход. Ты ставишь себя выше всех остальных, даже если придется идти по трупам."
        "Попробую уговорить остальных сдаться, чтобы выжить, может, враги пощадят нас.":
            guy3 "Тебя сожрут. Никто не щадит слабых, ты либо идешь по головам, либо умираешь."
        "Попробую спрятаться и надеяться, что меня не заметят. Возможно, кто-то сможет выбраться.":
            guy1 "Ты слаб. Сильные идут вперед, и не боятся идти по трупам ради своего спасения."

    guy2 "Твои товарищи схвачены, но ты успел скрыться. Враги заставляют тебя выбрать: один из твоих товарищей будет казнен, а все остальные получат свободу. Как поступишь?"
    menu:
        guy2 "Твои товарищи схвачены, но ты успел скрыться. Враги заставляют тебя выбрать: один из твоих товарищей будет казнен, а все остальные получат свободу. Как поступишь?"
        "Выберу того, кто может быть слабым звеном и принесет больше проблем. Отпущу остальных.":
            $ correct_answers += 1  # Правильный ответ
            guy1 "Вот это реально решение. Ты не теряешь время на чувства, ты спасешь себя и своих."
        "Попробую договориться, но знаю, что это приведет к последствиям для меня.":
            guy2 "Не будь идиотом. Договориться с ними — это как просить их убить тебя помедленнее."
        "Сдамся и скажу, что готов принять смерть, чтобы другие выжили.":
            guy3 "Слабак. Такая слабость — это твоя смерть. Мы не находимся в этом мире, чтобы мучиться."

    # Проверка правильности ответов
    if correct_answers >= 5:
        $ updateCanVisit("bm", True)
        guy3 "Ты понимаешь, что такое жесткость и сила. Заходи в старый амбар на окраине города, и забудь обо всех остальном. За тебя словечко замолвим."
    else:
        guy1 "Тебе не место среди нас, если ты не готов убить ради выгоды. Слишком мягок, брат."

    $nextTime()
    jump tavern