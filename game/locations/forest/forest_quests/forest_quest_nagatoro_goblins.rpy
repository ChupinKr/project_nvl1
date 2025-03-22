define first_time_forest_quest_nagatoro_goblins = True
define can_find_woblin = False
define can_talk_onna = True
define woblin_from_day = 0

label forest_quest_nagatoro_goblins:
    scene bg farm_enterence at Transform(zoom=1.5) with fade
    "Вы заходите в небольшую фермерскую деревню. Воздух пропитан запахом сена и земли, но что-то не так."
    if not first_time_forest_quest_nagatoro_goblins:
        "Деревня пуста. Ты видишь следы гоблинов, они ведут в пещеру, их там может быть еще больше."
        call go_goblin_cave
        return
    
    scene bg farm_enterence_screams at Transform(zoom=1.5) with vpunch
    "Внезапно тишину разрывают крики, доносящиеся из амбара неподалеку."
    p "Что за чертовщина? Надо проверить!"
    
    "Подбегая ближе, вы слышите обрывки разговора спрятавшихся жителей."
    old_woman "Бедная [onna.name]... Гоблины добрались и до неё..."
    "Жители деревни давно попрятались по домам, закрыв окна и двери. Никто не хочет вмешиваться."

    scene bg barn at Transform(zoom=1.5) with fade
    "Вы заглядываете в амбар."
    call barn_onna_goblin_fuck

    scene bg barn at Transform(zoom=1.5) with fade
    show goblin4 at mid with dissolve
    show goblin3 at right with dissolve
    show goblin5 at right_mid with dissolve
    call start_battle(100, 100, goblin.name, 'forest')
    hide goblin5 with dissolve
    mind "Черт, второй нападает!"
    call start_battle(100, 120, goblin.name, 'forest')
    hide goblin4 with dissolve
    mind "Да когда же вы кончитесь!"
    call start_battle(100, 150, goblin.name, 'forest')
    hide goblin3 with dissolve
    if can_talk_onna:
        show onna scared_chained with dissolve
        onna "Т-ты... они... мертвы?"
        p "Да, они мертвы, ты в безопасности."
        onna smile_chained "К-какое счастье.." with dissolve
        onna "В-воин.. Можешь ли ты мне помочь освободиться?"
        "*дзыньк*"
        show onna shy_naked with flash
        p "Меня кстати [hero_name] зовут."
        onna "Х-хорошо, [hero_name].."
        onna "Мне верно стоит отблагодарить тебя за спасение..."
        p "Я спас тебя не из корыстных целей."
        onna smile_naked "Ты добрый человек, [hero_name]." with dissolve
        $my_freya.addLove(10)
        onna closed_naked_1 "Но я все же дам тебе то, что ты заслуживаешь." with dissolve
        "[onna.name] закрыла глаза и начала читать молитвы, очень тихо."
        show onna closed_naked_2 with dissolve
        mind "Что за свечение?"
        $addChar(["str", "char", "intelligence"], 10)
        show onna smile_naked with flash
        p "Что это?! Я себя так хорошо никогда не чувствовал!"
        onna "Я наложила на тебя заклинание божественной защиты. А теперь иди, [hero_name], тебе нужно закончить начатое. Гоблинская пещера находится у холма."
    else:
        p "Хорошо, здесь разобрались. Прости, что не подоспел раньше, [onna.name]."

    scene bg farm_enterence at Transform(zoom=1.5) with fade
    "Ты выходишь из амбара и видишь следы гоблинов, они ведут в пещеру."
    mind "Их там может быть еще больше."
    call go_goblin_cave
    return

label barn_onna_goblin_fuck:
    scene bg onna_goblin_gangbang_1 at Transform(zoom=1.5) with fade
    "Перед вами жуткая сцена: несколько гоблинов окружили женщину в рваных одеждах священницы, прижимая её к земле."
    
    scene bg onna_goblin_gangbang_2 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_3 at Transform(zoom=1.5) with dissolve
    goblin "SKWI! SKWI!"

    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_5 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_5 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_5 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_5 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_5 at Transform(zoom=1.5) with dissolve
    onna "Ммммннф!"

    scene bg onna_goblin_gangbang_6 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_6 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_8 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_6 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_8 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_6 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_8 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_6 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_7 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_8 at Transform(zoom=1.5) with dissolve
    onna "Грлффф!!"

    scene bg onna_goblin_gangbang_9 at Transform(zoom=1.5) with vpunch
    "Гоблин с силой пропихивает член в ее горло"
    mind "Чертовы животные!"
    $first_time_forest_quest_nagatoro_goblins = False

    menu:
        "Что делать?"
        "Помочь [onna.name]":
            p "Я спасу тебя, [onna.name]!"
        "Немного понаблюдать":
            $can_talk_onna = False
            call barn_onna_goblin_fuck_continue
            p "Ну всё, больше медлить больше нельзя!"
    
    scene bg barn at Transform(zoom=1.5) with fade
    "Ты нападаешь на гоблинов"
    return
            

label barn_onna_goblin_fuck_continue:
    mind "Надо дождаться подходящего момента..."
    scene bg onna_goblin_gangbang_10 at Transform(zoom=1.5) with fade
    "Гоблины решили активнее работать с задними дарками [onna.name]."

    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_12 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg onna_goblin_gangbang_10 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_12 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_10 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_12 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_10 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_12 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_10 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_11 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg onna_goblin_gangbang_12 at Transform(zoom=1.5) with flash
    onna "Аааах!"
    
    scene bg onna_goblin_gangbang_13 at Transform(zoom=1.5) with flash
    pause .5
    scene bg onna_goblin_gangbang_14 at Transform(zoom=1.5) with flash
    "Гоблины наполняют ее дырочки спермой."

    scene bg onna_goblin_gangbang_15 at Transform(zoom=1.5) with flash
    mind "Кажется [onna.name] теряет сознание."

    scene bg onna_goblin_gangbang_16 at Transform(zoom=1.5) with fade
    "Наполненная гоблинской спермой, обессиленная и скованная [onna.name] упала без сознания на сено."
    return

label go_goblin_cave:
    scene bg goblin_cave_enterence at Transform(zoom=1.5) with fade
    "Ты идешь по следам гоблинов и спускаешь будто под землю"
    p "Неужели они живут в этих пещерах? Как же здесь неуютно."
    "Ты решаешь медленно и тихо проходить глубже, нужно поставить точку."
    scene bg goblin_cave1 at Transform(zoom=1.5) with fade
    "Ты проходишь всё дальше. Свет все еще пробивается в пещеру, но нигде не видно гоблинов."
    scene bg goblin_cave2 at Transform(zoom=1.5) with fade
    "Ты зашел очень глубоко в их пещеры, здесь очень темно."
    scene bg goblin_cave3 at Transform(zoom=1.5) with fade
    mind "Я готов ко всему, даже если это ловушка!"
    p "..."
    scene bg goblin_cave4 at Transform(zoom=1.5) with dissolve
    "Постепенно твое зрение адаптируется и ты замечаешь, что эту непроглядную тьму слегка освещают люминисцентные растения и светящиеся камни."
    mind "Впервые вижу такие источники света."
    "Здесь никого нет."
    menu:
        "Здесь никого нет."
        "Идти дальше":
            mind "Надо быть тише, и вырезать их по одному, возможно они меня еще не заметили."
            show goblin1 at mid with dissolve
            "Вы подходите к гоблину, охраняющему какую-то комнату."
            menu:
                "Что мне делать?"
                "Попытаться обхитрить гоблина":
                    if intelligence > 30:
                        "Ты решаешь "
                        p "skwi skwi"
                        goblin "skwik?"
                        mind "Ха, это сработало, он идет сюда."
                        p "Хыа!"
                        hide goblin1 with dissolve
                        "Ты быстро вырубаешь [goblin.name] с одного удара по затылку."
                        "Проход свободен."
                    else:
                        $customNotify("Недостаточно интеллекта")
                        "Ты кидаешь в гоблина камень, он сразу нападает на тебя."
                        call start_battle(100, 120, goblin.name, 'forest')
                        p "С одним справился, хорошо, что он не закричал. Надо торопиться."
                "Честно сразиться":
                    p "Эй гоблин! Подойти и встреть свою смерть с честью!"
                    goblin "SKWIIIIIIIIK!"
                    p "Черт, кажется он позвал подмогу..."
                    "Подоспел еще один гоблин"
                    show goblin3 at right with dissolve
                    call start_battle(100, 120, goblin.name, 'forest')
                    hide goblin3 with dissolve
                    goblin "S-skwii!"
                    call start_battle(100, 100, goblin.name, 'forest')
                    p "Неужели это всё, что у вас есть?"
                    hide goblin1 with dissolve
                    show goblin2 at right_mid with vpunch
                    $health -= 10
                    $customNotify("Тебя ударили в спину")
                    if health <= 0:
                        jump battle_loss
                    "Внезапно нападает еще один гоблин сзади."
                    call start_battle(100, 110, goblin.name, 'forest')
                    hide goblin2 with dissolve
                    p "Со всеми справился. Честная битва прославит меня!"
        "Закричать":
            p "Эй гоблины! Я пришел уничтожить всех вас!"
            p "..."
            p "....."
            p "Сероьезно? Они меня испугались?"
            if charisma > 50:
                "Вы слышите, как маленькие шаги очень быстро отдаляются."
                p "Действительно испугались."
            else:
                $customNotify("Недостаточно харизмы")
                show goblin1 at mid with dissolve
                show goblin3 at right with dissolve
                show goblin2 at right_mid with dissolve
                "Все гоблины, что были в этой пещере сбежались к тебе и окружили, это была явно не лучшая идея, кричать в логове врага."
                call start_battle(100, 80, goblin.name, 'forest')
                p "По одному, черти!"
                mind "Skwi skwi.."
                hide goblin2 with dissolve
                show goblin5 at right_mid with dissolve
                call start_battle(100, 90, goblin.name, 'forest')
                goblin "S-skwii!"
                hide goblin3 with dissolve
                show goblin4 at right with dissolve
                call start_battle(100, 100, goblin.name, 'forest')
                p "ХАХАХА! Вы ничтожества!"
                hide goblin1 with dissolve
                call start_battle(100, 110, goblin.name, 'forest')
                p "Да, больше, нападайте!"
                goblin "Skwi.. s-skwik?"
                hide goblin5 with dissolve
                call start_battle(100, 120, goblin.name, 'forest')
                goblin "Skwiiiik!"
                hide goblin4 with dissolve
                "Остальные гобюлины убегают прочь. Наврядли они вернутся в здешние леса."
                p "Уже всё? Вы трусы!"
                mind "Миссия должно быть окончена, пора возвращаться."
                show hopgoblin1 at mid with dissolve
                "Внезапно прямо перед вами появляется огромный гоблин"
                hopgoblin "Skrig.. Sgrik.."
                p "Черт.. Это будет не просто."
                call start_battle(200, 150, hopgoblin.name, 'forest')
                hide hopgoblin1 with dissolve
                "[hopgoblin.name] повержен!"
                p "Ха ха! Да! Так вам!"
    "Вы двигаетесь дальше, скорее всего где-то здесь есть их потомство, надо их всех перебить."
    
    scene bg goblin_cave5_1 at Transform(zoom=1.5) with fade
    "Ты находишь комнату с массой детенышей гоблинов и их маткой."
    mind "Отлично!"
    scene bg goblin_cave5_2 at Transform(zoom=1.5) with fade
    "Ты тихо прошел и избавился от каждого."
    menu:
        "Что делать с маткой?"
        "Пощадить":
            p "Я слышал, что гоблинши довольно умные, по сравнению с мужскими особями."
            mind "И эти формы... Нельзя такое терять!"
            scene bg goblin_cave6 at Transform(zoom=1.5) with fade
            show woblin scared with dissolve
            woblin "А? *Skwik*?!"
            "Ты пригрожаешь ей расправой."
            p "Замолчи! А то закончишь, как твои дети."
            woblin sad "..." with dissolve
            p "Ты меня понимаешь? Кивни, если да."
            woblin nods "*кивает*" with dissolve
            show woblin sad with dissolve
            mind "Джекпот!"
            p "Отлично, я тебя пощажу, если ты хорошо услужишь мне."
            woblin @blush_nods "*кивает*" with dissolve
            show woblin sad with dissolve
            p "Веди меня к выходу, и без шуток, а то поплатишься жизнью."
            woblin @nods "*кивает*" with dissolve
            show woblin sad with dissolve
            "[woblin.name] выводит тебя из извилистых гоблинских пещер."
            call forest_scene 
            show woblin sad with dissolve
            p "Всё, мы ушли. Ты можешь говорить на человеческом языке?"
            woblin @sad_open_mouth "Д-да... Ч-что тебе от меня нужно?" with dissolve
            menu:
                woblin "Что тебе от меня нужно?"
                "Твоя помощь":
                    p "Я подарил тебе жизнь. Теперь ты будешь служить мне."
                    woblin @sad_open_mouth "Н-но что если я откажусь?" with dissolve
                    p "..."
                    woblin scared "Я *skwik* поняла.." with dissolve
                    p "Ты очень похожа на человека. Тебе лишь стоит носить мантию, и тебя никто не отличит. Ты даже говоришь почти как человек."
                    woblin sad_open_mouth "Спасибо... Но к чему ты клонишь?" with dissolve
                    show woblin sad with dissolve
                    p "Я хочу, чтобы ты помогала мне с тренировками и деньгами."
                    if can_invite_brothel:
                        p "У меня как раз есть работенка для тебя. Думаю никто не будет против."
                        mind "[my_mao.name] будет даже рада."
                    woblin sad_open_mouth "Х-хорошо, я *skwik* всё сделаю." with dissolve
                    show woblin sad with dissolve
                    mind "Какая послушная попалась."
                    p "Чтобы не пошли подозрения - я буду навещать тебя только в лесу утром и ночью."
                    "Ты уходишь."
                    $woblin_from_day = day
                "Твоё тело":
                    p "Я хочу твоё тело."
                    woblin blush_surprised "Ч-человек?! Хочет?! Моё тело?!" with dissolve
                    if can_invite_brothel:
                        mind "Хм, я и не подозревал, что здесь такие вкусы у населения."
                    p "Вставай на колени, быстро!"
                    call woblin_root_blowjob
                    call forest_scene 
                    show woblin blush_cummed with dissolve
                    p "Ты хороша. Решено, ты будешь меня обслуживать и дальше. В замен на это можешь охотиться на дичь в лесу, никто тебя не тронет."
                    woblin blush_cummed_say "Х-хорошо..." with dissolve
                    show woblin blush_cummed with dissolve
                    p "Я буду изредка навещать тебя в лесу утром и ночью."
                    "Ты уходишь."
            $customNotify("Ты сможешь найти [woblin.name] в лесу")
            $can_find_woblin = True
        "Избавиться от нее":
            "Ты избавляешься от [woblin.name]."
            scene bg goblin_cave6 at Transform(zoom=1.5) with fade
            mind "Миссия выполнена. Остатки гоблинов разбежались, бросив матку. Они больше не смогут размножаться."
            "Ты уходишь, оставляя гору гоблинских трупов в пещере."
            call forest_scene
    return
        
label woblin_root_blowjob:
    woblin sad_open_mouth "Слушаюсь..." with dissolve
    scene bg woblin_blowjob1 at Transform(zoom=1.5) with fade
    "Вы отошли на небольшую полянку в лесу, там, где вас никто не побеспокоит. [woblin.name] послушно села перед тобой на колени."
    
    scene bg woblin_blowjob2 at Transform(zoom=1.5) with fade
    mind "Как же она хороша, руки сами тянутся к ней."

    scene bg woblin_blowjob3 at Transform(zoom=1.5) with vpunch
    woblin "Skwi!"

    scene bg woblin_blowjob4_1 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob4_2 at Transform(zoom=1.5) with dissolve
    p "Начинай..."

    scene bg woblin_blowjob5 at Transform(zoom=1.5) with dissolve
    mind "Кажется она всё еще в шоке."
    woblin "Ты точно человек, а не [hopgoblin.name]?"
    p "Я человек..."

    scene bg woblin_blowjob6_1 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob6_2 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob6_3 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob6_2 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob6_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob6_3 at Transform(zoom=1.5) with dissolve
    p "Так и продолжишь лизать? Хорошо обслужи меня!"
    woblin "Х-хорошо.."

    scene bg woblin_blowjob7 at Transform(zoom=1.5) with dissolve
    "Она прикоснулась губками к головке твоего члена и жалобно смотрит на тебя."
    p "Поторопись!"

    scene bg woblin_blowjob8 at Transform(zoom=1.5) with dissolve
    p "Раз у тебя не получается, я тебе помогу."
    scene bg woblin_blowjob9 at Transform(zoom=1.5) with dissolve
    "Ты силой насаживаешь ее рот на свой член."
    
    scene bg woblin_blowjob10_1 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob10_2 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob10_2 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob10_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg woblin_blowjob10_4 at Transform(zoom=1.5) with dissolve
    p "Аргх!"
    
    scene bg woblin_blowjob11 at Transform(zoom=1.5) with dissolve
    "Ты притягиваешь ее голову на всю длину своего члена."
    
    scene bg woblin_blowjob12 at Transform(zoom=1.5) with dissolve
    p "Арх! Молодец!"
    
    scene bg woblin_blowjob13 at Transform(zoom=1.5) with flash
    "Ты начинаешь кончать в ее глотку."
    woblin "Мммн!"
    
    scene bg woblin_blowjob14 at Transform(zoom=1.5) with flash
    p "Получай!"
    
    scene bg woblin_blowjob15 at Transform(zoom=1.5) with flash
    "[woblin.name] изо всех сил старается глотать всю твою сперму"
    
    scene bg woblin_blowjob16 at Transform(zoom=1.5) with flash
    woblin "Ммнффф!"
    
    scene bg woblin_blowjob17 at Transform(zoom=1.5) with flash
    pause .2
    scene bg woblin_blowjob18 at Transform(zoom=1.5) with dissolve
    p "Эй! Я тебя не отпускал!"
    
    scene bg woblin_blowjob19 at Transform(zoom=1.5) with dissolve
    woblin "А-ааах"
    
    scene bg woblin_blowjob20 at Transform(zoom=1.5) with dissolve
    "[woblin.name] жалобно смотрит на тебя, ожидая твоей реакции."
    p "Ладно, ты хорошо постаралась."
    
    scene bg woblin_blowjob21 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg woblin_blowjob22 at Transform(zoom=1.5) with dissolve
    "Она широко улыбается тебе."
    mind "Неплохо... Для начала неплохо."

    return

label forest_quest_nagatoro_goblins_reward:
    show nag neutral with dissolve
    p "О, [nag.name]! У меня хорошие новости!"
    nag grin "У тебя? Что такого хорошего может выйти у такого, как ты?" with dissolve
    p "Я перебил всех гоблинов!"
    nag normal_shy "Серьезно? Это поразительно..." with dissolve
    p "Да!"
    "Ты показываешь ей уши убитых гоблинов."
    nag happy "Ты действительно справился!" with dissolve
    nag grin "Иди за мной, у меня есть награда для тебя!" with dissolve
    p "И что же это?"
    nag "Конечно же тренировка! Иди за мной, это рядом!"
    call dodjo_scene
    show nag normal_shy with dissolve
    "Вы пришли в Додзё"
    nag "Я назвала эту тренировку - \"Растирание грудными мыщцами\""
    menu:
        "INFO: В этой сцене пришлось сделать грудь [nag.name] значительно больше."
        "Продолжить":
            call nagatoro_root_titfuck  
        "Вернуться":
            nag "Ты и не представляешь, что потерял!"
            jump city
    return

label visit_woblin_forest:
    show woblin smile with dissolve
    woblin smile_say "Рада вас видеть, х-хозяин!" with dissolve
    show woblin smile with dissolve
    call visit_woblin_forest_menu
    return

label visit_woblin_forest_menu:
    $woblins_money = (woblin_from_day - (day + 2)) * 10
    menu:
        "Что я могу для вас сделать?"
        "Что удалось добыть?" if woblin_from_day > 0:
            p "Удалось добыть что-то для меня?"
            if woblin_from_day >= day + 2:
                woblin happy_say "Конечно! Вот!" with dissolve
                show woblin happy with dissolve
                "[woblin.name] показывает вам [woblins_money] монет."
                p "Хорошая работа!"
                $addMoney(woblins_money)
                $woblin_from_day = day
            else:
                woblin sad_open_mouth "Простите, хозяин.. Я еще не успела ничего заработать" with dissolve
                show woblin sad with dissolve
                p "Ничего страшного, я вернусь позже."
                woblin sad_open_mouth "Х-хорошо.." with dissolve
                show woblin sad with dissolve
            jump visit_woblin_forest_menu
        "Научи меня":
            woblin happy_say "Мне нечему вас учить, хозяин." with dissolve
            show woblin happy with dissolve
            jump visit_woblin_forest_menu
        "Обслужи меня":
            woblin little_scared "Д-да..." with dissolve
            menu:
                "Минет":
                    call woblin_root_blowjob
                    call forest_scene 
                    show woblin blush_cummed with dissolve
                    woblin blush_cummed_say "Мне нужно переодеться, пока хищники не учуяли запах." with dissolve
                    show woblin blush_cummed with dissolve
                    p "Хорошо, увидимся позже"
                    $nextTime()
                    jump forest
                "Передумал":
                    p "Я передумал"
                    jump visit_woblin_forest_menu
        "Уйти":
            p "Мне пора, встретимся позже."
            woblin "Буду вас ждать, хозяин!"
            jump forest
