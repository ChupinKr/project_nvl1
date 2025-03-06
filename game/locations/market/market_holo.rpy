
default can_work_with_holo = False
define h_can_go_root = False
define h_can_visit = True

label visit_holo:
    scene bg holo_market with fade
    show h smile with dissolve
    if not h_can_go_root and my_holo.love >= 50:
        h smile_shy "Охо-хо~, [hero_name], вижу ты разжился монетками! Я готова предложить тебе новый товар~"
        pause .5
        h "Подожди тут, я подготовлюсь~"
        hide h with dissolve
        h "А точнее даже услугу~ Посмотреть не желаешь?"
        show h smile_no_top with dissolve
        menu: 
            "Да":
                h smile_no_top "Охо-хо~, [hero_name], я в тебе не сомневалась!"
                h "Подойди пожалуйста поближе, не хочу, чтобы все видели~"
                "Ты подходишь ближе"
                h "Думаю моё предложение тебя заинтересует~"
                hide h with dissolve
                pause 1
                show h smile_naked with dissolve
                h smile_naked "Как тебе? На какую сумму оценишь?" with dissolve
                p "Выше всех похвал, пол царства бы отдал!"
                h smile_naked "Охо-хо~ Этой фразой ты только что обеспечил себе первую бесплатную услугу, идем~" with dissolve
                $h_can_go_root = True
                call h_root_masturbate
                jump market
            "Нет":
                $h_can_visit = False
                h angry_no_top "Похоже я в тебе ошиблась, [hero_name]!" with dissolve
                $customNotify("Ты больше никогда не увидишь [h.name]")
                jump market
    else:
        h "Охо-хо~ Ты попал в лапы мудрой волчицы, [hero_name]! Чем порадуешь меня сегодня?"
    show h smile with dissolve
    jump holo_menu

label holo_menu:
    menu:
        "Купить товары":
            h "О-хо-хо, [hero_name], неужели ты наконец разжился монетками?"
            jump holo_market_menu
        "Обслужи меня" if my_holo.love >= 50 and h_can_go_root:
            h "О-хо-хо, [hero_name], а ты уверен, что тебе хватит?"
            jump holo_market_root_menu
        "Чем тебе помочь?" if can_work_with_holo:
            menu:
                "Протереть книги(10 монет)":
                    h "Надо протереть книги! Только быстро, там уже очередь! Готов?"
                    scene bg holo_market_boxes with fade
                    call start_clean("books")
                    if last_clean_win:
                        h "Хватай следующую, быстрее!"
                        call start_clean("books")
                        if last_clean_win:
                            h "Последнюю, торопись!"
                            call start_clean("books")
                            if last_clean_win:
                                h "О-хо-хо! [hero_name], книги были проданы по выгодной цене, это успех!"
                                "Ты провёл время, помогая [h.name]"
                                $my_holo.addLove(5)
                                "[h.name] это оценила"
                                pause 3.5
                                $addMoney(10)
                            else: 
                                h "Эх, почти успели, упустили клиента."
                        else: 
                            h "Жаль, но ничего, будут еще клиенты."
                    else: 
                        h "[hero_name], это никуда не годится, работай лучше!"
                    $nextTime()
                    scene bg holo_market with fade
                    show h smile with dissolve
                    jump holo_menu
                "Избавиться от жуков(10 монет)":
                    h "Избавься от этих жуков, они везде! Только не убивай их!"
                    scene bg holo_market_boxes with fade
                    p "И как мне их убрать?"
                    h "Это уже тебе решать, [hero_name]~"
                    call bug_hunt
                    $nextTime()
                    scene bg holo_market with fade
                    show h smile_shy with dissolve
                    h "О-хо-хо! [hero_name], спасибо, не знаю, что бы я без тебя делала!"
                    $my_holo.addLove(5)
                    "Ты провёл время, помогая [h.name], она это оценила"
                    $addMoney(10)
                    jump holo_menu
                "Никакой работы":
                    h "Эй, в следующий раз обещай, что поможешь!"
                    jump holo_menu
        # "Попросить задание":
        # "Отказаться от задания" if isNoQuestNow(): 
        "Спросить, как тут заработать" if not can_work_with_holo or not canVisit("tavern"):
            p "Слушай, [h.name], а как в этом городе можно заработать денег?"
            h "О-хо-хо! [hero_name]! Я не ошиблась! Ты действительно бедный!"
            "[h.name] очень рада и кричит об этом на весь рынок, ты чувствуешь себя униженным"
            h "Ладно, подскажу по дружески, можешь, например, пойти подработать в таверну, там всегда руки нужны."
            $ updateCanVisit("tavern", True)
            h "Ну или можешь мне помогать, я тоже в долгу не останусь~"
            $ can_work_with_holo = True
            jump holo_menu
        "Уйти":
            jump market_menu

label holo_market_menu:
    "INFO: каждый предмет можно использовать несколько раз(надо использовать 3 раза)"
    "INFO: покупка некоторых предметов недоступна, тк вы не понимаете их ценности, пока не разовьете предыдущий уровень предмета"
    "INFO: использовать предметы возможно только дома(в комнате в таверне)"
    menu:
        "Купить [item_motivational_book.name]([item_motivational_book.price] монет)" if isAbleToBuy(item_motivational_book):
            "Вы купили [item_motivational_book.name]"
            $buyItem(item_motivational_book)
            $my_holo.addLove(3)
            jump holo_market_menu
        "Купить [item_mirror.name]([item_mirror.price] монет)" if isAbleToBuy(item_mirror):
            "Вы купили [item_mirror.name]"
            $buyItem(item_mirror)
            $my_holo.addLove(5)
            jump holo_market_menu
        "Купить [item_art_plus_size.name]([item_art_plus_size.price] монет)" if isAbleToBuy(item_art_plus_size):
            "Вы купили [item_art_plus_size.name]"
            $buyItem(item_art_plus_size)
            $my_holo.addLove(10)
            jump holo_market_menu
        "Купить [item_dumbbells_ez.name]([item_dumbbells_ez.price] монет)" if isAbleToBuy(item_dumbbells_ez):
            "Вы купили [item_dumbbells_ez.name]"
            $buyItem(item_dumbbells_ez)
            $my_holo.addLove(3)
            jump holo_market_menu
        "Купить [item_weight_mid.name]([item_weight_mid.price] монет)" if isAbleToBuy(item_weight_mid):
            "Вы купили [item_weight_mid.name]"
            $buyItem(item_dumbbells_ez)
            $my_holo.addLove(5)
            jump holo_market_menu
        "Купить [item_barbell.name]([item_barbell.price] монет)" if isAbleToBuy(item_barbell):
            "Вы купили [item_barbell.name]"
            $buyItem(item_barbell)
            $my_holo.addLove(10)
            jump holo_market_menu
        "Купить [item_book_math.name]([item_book_math.price] монет)" if isAbleToBuy(item_book_math):
            "Вы купили [item_book_math.name]"
            $buyItem(item_book_math)
            $my_holo.addLove(3)
            jump holo_market_menu
        "Купить [item_self_study_guide.name]([item_self_study_guide.price] монет)" if isAbleToBuy(item_self_study_guide):
            "Вы купили [item_self_study_guide.name]"
            $buyItem(item_self_study_guide)
            $my_holo.addLove(5)
            jump holo_market_menu
        "Купить [item_grimoire.name]([item_grimoire.price] монет)" if isAbleToBuy(item_grimoire):
            "Вы купили [item_grimoire.name]"
            $buyItem(item_grimoire)
            $my_holo.addLove(10)
            jump holo_market_menu
        "Купить [item_forest_guide.name]([item_forest_guide.price] монет)" if isAbleToBuy(item_forest_guide):
            "Вы купили [item_forest_guide.name]"
            $buyItem(item_forest_guide)
            $my_holo.addLove(10)
            jump holo_market_menu
        "Купить [item_combat_book.name]([item_combat_book.price] монет)" if isAbleToBuy(item_combat_book):
            "Вы купили [item_combat_book.name]"
            $buyItem(item_combat_book)
            $my_holo.addLove(10)
            jump holo_market_menu
        "Уйти":
            h "Приятно было с тобой сотрудничать"
            jump holo_menu

label holo_market_root_menu:
    menu:
        "Мастурбация(30 монет)" if my_holo.love >= 50:
            if money < 30:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump market
            if my_holo.love >= 150:
                h @smile_shy "Ладно, это слишком, как постоянному клиенту сделаю для тебя скидку~"
                $minusMoney(10)
            else:
                $minusMoney(30)
            call h_root_masturbate
            $nextTime()
            jump market
        "Грудями(40 монет)" if my_holo.love >= 60:
            if money < 40:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            if my_holo.love >= 150:
                h @smile_shy "Ладно, это слишком, как постоянному клиенту сделаю для тебя скидку~"
                $minusMoney(10)
            else:
                $minusMoney(40)
            call h_root_titfuck
            $nextTime()
            jump market
        "Минет(50 монет)" if my_holo.love >= 70:
            if money < 50:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            if my_holo.love >= 150:
                h @smile_shy "Ладно, это слишком, как постоянному клиенту сделаю для тебя скидку~"
                $minusMoney(10)
            else:
                $minusMoney(50)
            call h_root_blowjob
            $nextTime()
            jump market
        "Секс(70 монет)" if my_holo.love >= 80:
            if money < 70:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            if my_holo.love >= 150:
                h @smile_shy "Ладно, это слишком, как постоянному клиенту сделаю для тебя скидку~"
                $minusMoney(10)
            else:
                $minusMoney(70)
            call h_root_fuck
            $nextTime()
            jump market
        "Анал(80 монет)" if my_holo.love >= 90:
            if money < 80:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            if my_holo.love >= 150:
                h @smile_shy "Ладно, это слишком, как постоянному клиенту сделаю для тебя скидку~"
                $minusMoney(10)
            else:
                $minusMoney(80)
            h "Ну что, [hero_name], хочешь ещё одну услугу от волчицы? Это обойдётся тебе в кругленькую сумму."
            p "Сколько на этот раз?"
            h "Двести золотых. И не пытайся сбить цену — я знаю, чего стою."
            "Ты киваешь, выкладывая монеты. Холо пересчитывает их с довольной ухмылкой."
            h "Отлично. Готовься — будет жарко."
            $minusMoney(80)
            call h_root_anal
            $nextTime()
            jump market
        "Секрет(100 монет)" if my_holo.love >= 100:
            if money < 100:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            if my_holo.love >= 150:
                h @smile_shy "Ладно, это слишком, как постоянному клиенту сделаю для тебя скидку~"
                $minusMoney(10)
            else:
                $minusMoney(100)
            call h_root_footfuck
            $nextTime()
            jump market
        "Вернуться":
            "Ты уходишь восстанавливать силы"
            r @smirk "До встречи~"
            jump market

label h_root_masturbate:
    scene bg holo_room with dissolve
    "[h.name] Приводит тебя к себе в комнату"
    h "Подожди тут, я переоденусь~"
    pause 1
    show h smile_no_top with fade
    call hide_dialog
    p "!!!!!" with vpunch
    h "Я вернулась, соскучиться успел?~"
    p "Ждал тебя с нетерпением!"
    hide h with fade

    scene bg h_masturbate1 with dissolve
    call hide_dialog
    mind "[h.name] Немного нагнулась ко мне, просто стоит и смотрит... Полностью обнажённая выше пояса."  
    h "Ммм~ Смотри внимательно, тебе же нравится, верно?"  
    p "Черт... Как я могу не смотреть..."  

    scene bg h_masturbate2 with dissolve 
    call hide_dialog 
    "Она слегка сжимает свою мягкую грудь, её дыхание чуть ускоряется, а глаза сверкают с хитрым огоньком."
    h "Ты ведь уже весь горишь, да?~"  
    p "Ты просто дразнишь меня..."  
    h "Хих... А что, если так и есть?"  

    scene bg h_masturbate3 with dissolve  
    call hide_dialog
    "Её пальцы медленно скользят по бедру, играя с подолом юбки..."  
    h "Ну что, терпение уже на исходе? Или ещё подождёшь?"  
    p "Ты просто играешь со мной..."  
    h "Может быть~ Но тебе ведь нравится?"  
    
    scene bg h_masturbate4 with dissolve
    call hide_dialog  
    "[h.name] выпрямляется, её руки медленно скользят по бокам юбки..."  
    h "Ну? Интересно, что под ней?"  

    scene bg h_masturbate5 with dissolve  
    call hide_dialog
    mind "Она чуть выше приподнимает юбку, и я замечаю уголок чёрных трусиков."  
    p "..."  
    h "Ты ведь не будешь смотреть просто так, верно?"  
    mind "Её голос звучит мягко, но в нём явная провокация."  

    scene bg h_masturbate6_1 with dissolve  
    call hide_dialog
    "[h.name] избавляется от юбки и медленно ползёт на кровать, опираясь на руки..."  
    h "Ну что, волк наконец раскроет свои клыки?~"  
    p "Ты действительно хочешь, чтобы я..."  
    h "А ты попробуй угадать~"  

    scene bg h_masturbate6_2 with dissolve  
    call hide_dialog
    mind "[h.name] медленно оттягивает резинку своих трусиков, позволяя мне заглянуть чуть глубже..."  
    h "Ты ведь хотел посмотреть, да?"  
    p "...Ты слишком хороша в этом."  
    h "О, я просто люблю дразнить~"  

    scene bg h_masturbate6_3 with dissolve 
    call hide_dialog 
    mind "Трусики мягко облегают её упругие бёдра..."  
    h "Хочешь снять их сам?"  
    p "..."

    scene bg h_masturbate7 with dissolve  
    call hide_dialog
    mind "[h.name] медленно снимает трусики и, не стесняясь, раздвигает ножки, демонстрируя всё..."  
    h "Ну как тебе, мой милый волчонок~"  
    p "..."
        
    scene bg h_masturbate8 with dissolve  
    call hide_dialog
    mind "[h.name] легла передо мной, полностью обнажённая. Её тело освещает мягкий свет, а лёгкая ухмылка на губах только сильнее разжигает во мне желание."  
    h "Что, слов не осталось?"  
    p "Ты... Ты слишком красива."  
    h "И это всё, что ты скажешь?"  

    scene bg h_masturbate9 with dissolve  
    call hide_dialog
    mind "Она вновь опускается на четвереньки, её хвост покачивается в воздухе, а в глазах горит игривый огонёк."  
    h "Может, тебе стоит взять инициативу в свои руки?"  
    p "Ты ведь специально провоцируешь меня..."  
    h "А ты возьми и провоцируй в ответ~"  

    scene bg h_masturbate10 with dissolve 
    call hide_dialog 
    mind "Внезапно её тёплое тело прижимается к моему... Её мягкая грудь, её кожа... Всё это заставляет сердце бешено колотиться."  
    h "Теперь ты точно не отвертишься."  
    p "Чёрт... [h.name]..."  
    mind "Её дыхание обжигает мою шею, а руки нежно касаются моего тела... С этого момента пути назад уже нет."  

    scene bg h_masturbate11 with dissolve  
    call hide_dialog
    mind "Мой напряжённый член оказывается прямо перед её лицом... [h.name] поднимает взгляд, её янтарные глаза впиваются в мои."  
    h "О, какой же ты нетерпеливый~"  
    p "Ты сама меня до этого довела..."  
    h "Хих... И мне это нравится."  

    scene bg h_masturbate12 with dissolve  
    call hide_dialog
    mind "Её тёплые ладони нежно обхватывают мой член... На губах играет знакомая ехидная улыбка."  
    h "Какой он горячий... Ты весь горишь, не так ли?"  
    p "Как я могу оставаться спокойным, когда ты делаешь такое?"  
    h "Ммм~ Тогда расслабься, я позабочусь о своём волчонке..."  

    scene bg h_masturbate13 with dissolve  
    call hide_dialog
    mind "Она медленно оседает на мои бёдра, удерживая мой член в руке... Её дыхание становится глубже, а хвост возбуждённо подрагивает."  
    h "Чувствуешь? Моё тело... Оно жаждет тебя."  
    p "[h.name]..."  
    mind "Её кожа горячая... Её взгляд полный желания... Она прижимается ко мне своими упругими бедрами..."  

    scene bg h_masturbate14 with dissolve  
    call hide_dialog
    mind "[h.name] начинает медленно двигаться, покачивая бёдрами... Тёплая мягкость её тела заставляет меня застыть от удовольствия."  
    h "Ммм~ Чувствуешь тепло моего тела?"  
    p "Ты... ты дразнишь меня."  
    h "Конечно~ А ты разве не этого хотел?"  

    scene bg h_masturbate15 with dissolve  
    call hide_dialog
    mind "Она устраивается удобнее, выпрямляя спину... Её ладонь нежно скользит по моему члену, вызывая у меня дрожь по всему телу."  
    h "Тебе нравится, когда я так делаю?"  
    p "Как я могу ответить, когда ты так меня дразнишь..."  
    h "Хих~ Тогда позволь мне насладиться этим ещё немного."  

    scene bg h_masturbate16 with dissolve  
    call hide_dialog
    mind "Её янтарные глаза внимательно изучают мой пульсирующий член..."  
    h "Ты такой большой... Как же мне справиться с тобой?"  
    p "Хочешь проверить?"  
    h "О, ещё как хочу~"  

    "[h.name] начинает двигать рукой вдоль твоего члена"
    scene bg h_masturbate16_rep with dissolve  
    pause .5
    scene bg h_masturbate16_rep2 with dissolve  
    pause .5
    scene bg h_masturbate16_rep with dissolve  
    pause .4
    scene bg h_masturbate16 with dissolve  
    pause .4
    scene bg h_masturbate16_rep with dissolve  
    pause .3
    scene bg h_masturbate16_rep2 with dissolve 
    pause .3
    scene bg h_masturbate16_rep with dissolve  
    pause .2
    scene bg h_masturbate16 with dissolve  
    pause .2
    scene bg h_masturbate16_rep with dissolve 
    pause .2
    scene bg h_masturbate16_rep2 with dissolve 
    pause .1
    scene bg h_masturbate16_rep with dissolve 
    pause .1
    scene bg h_masturbate16 with dissolve   
    pause .1
    scene bg h_masturbate16_rep with dissolve 
    pause .1
    scene bg h_masturbate16_rep2 with dissolve 
    call hide_dialog

    scene bg h_masturbate17_cum1 with flash 
    call hide_dialog 
    mind "[h.name] продолжает двигать рукой, её пальцы мягко сжимают мой член. Я чувствую, как напряжение в моём теле достигает предела, и из члена начинает выходить первая струя спермы."  
    h "Хих~ Не сдерживайся, дай мне всё, что у тебя есть~"  

    scene bg h_masturbate17_cum2_test with flash  
    call hide_dialog
    "Сперма бьёт сильнее, и [h.name] выглядит немного испуганной, но не отстраняется. Её глаза широко раскрыты."  
    h "Ох! Это... так много..."  

    scene bg h_masturbate17_cum3 with flash  
    call hide_dialog
    "Теперь часть её груди и твой пах покрыты спермой. [h.name] всё ещё выглядит немного испуганной."  
    h "Ну и дела... Ты действительно не сдерживался, да?"   

    scene bg h_masturbate17_cum4 with dissolve  
    call hide_dialog
    mind "[h.name] смотрит на меня с изумлением, её глаза широко раскрыты от количества спермы. Она явно не ожидала такого."  

    h "Это... впечатляет."  
    h "Тогда я должна позаботиться о тебе ещё больше~"  

    scene bg h_masturbate17_cum5 with dissolve  
    call hide_dialog
    mind "Она наклоняется ближе ко мне, её рука всё ещё держит мой пульсирующий член."  

    scene bg h_masturbate17_cum6 with dissolve  
    call hide_dialog
    mind "[h.name] ложится на моё тело, её пальчики нежно двигаются по уздечке моего члена. Её дыхание горячее, а взгляд полон желания."  

    if charisma < 30:
        $customNotify("Недостаточно харизмы")
        p "Сколько мне доплатить, чтобы тебя трахнуть?" with vpunch
        h "!!!!!"
        scene bg holo_room with dissolve
        show h angry_naked_cummed with dissolve
        call hide_dialog
        h "Какой же ты иногда хам!"
        $minusLove("h", 10)
        "[h.name] ушла, закрыв за собой дверь, кажется стоит научиться общаться с женщинами"
        return


    scene bg h_masturbate18 with dissolve 
    call hide_dialog 
    mind "[h.name] села напротив меня, её лицо и грудь покрыты спермой. Она смотрит на меня с лёгкой ухмылкой, но в её глазах видно, что она хочет еще большего."  
    h "Ну что, мой волчонок, ты уже готов к следующему раунду?"  
    p "Ты просто неугомонная..."  
    h "Хих~ Тогда давай не будем терять время~"  

    scene bg h_masturbate19_t_0 with dissolve  
    call hide_dialog
    mind "[h.name] снова берёт мой член в руку, смотря мне в глаза. Её движения уверенные, а взгляд полон обещаний."  
    h "Ммм~ Ты всё ещё такой твёрдый..."  

    scene bg h_masturbate19_t_0 with dissolve  
    pause .5
    scene bg h_masturbate19_t_1 with dissolve  
    pause .5
    scene bg h_masturbate19_t_2 with dissolve  
    pause .4
    scene bg h_masturbate19_t_1 with dissolve  
    pause .4
    scene bg h_masturbate19_t_0 with dissolve  
    pause .3
    scene bg h_masturbate19_t_1 with dissolve  
    pause .3
    scene bg h_masturbate19_t_2 with dissolve
    pause .3
    scene bg h_masturbate19_t_1 with dissolve
    pause .2
    scene bg h_masturbate19_t_0 with dissolve
    pause .2
    scene bg h_masturbate19_t_1 with flash
    pause .2
    scene bg h_masturbate19_t_2 with flash
    call hide_dialog

    scene bg h_masturbate20_t_cum1 with flash  
    call hide_dialog
    "[h.name] продолжает смотреть тебе в глаза, горячая струя спермы летит в её лицо. Она не отворачивается, её взгляд полон удовольствия."  
    h "Я обожаю это чувство~"  

    scene bg h_masturbate20_t_cum2 with flash 
    call hide_dialog 
    "[h.name] закрывает глаза и открывает рот, её язык высунут, а сперма продолжает лететь на неё. Она выглядит так, будто наслаждается каждым моментом."  

    h "Аааааа~~"

    scene bg h_masturbate20_t_cum3 with flash 
    call hide_dialog 
    mind "[h.name] продолжает доить мой член, сперма летит на её лицо, покрывая её всё больше. Её движения становятся быстрее, а дыхание глубже."  

    scene bg h_masturbate20_t_cum4 with flash  
    call hide_dialog
    "Спермы становится ещё больше, она стекает по её волосам и лицу на грудь и капает на кровать. [h.name] полностью погружена в процесс."  

    scene bg h_masturbate20_t_cum5 with flash  
    call hide_dialog
    "Ты наконец заканчиваешь, только небольшая струйка спермы свисает с твоего члена. [h.name] с ухмылкой смотрит тебе в глаза, а её рука всё ещё держит твой член."  
    h "Ну что, мой волчонок, устал?"

    if my_holo.love < 70:
        $customNotify("Недостаточно симпатии")
        p "Да, спасибо за этот день"
        h "Всё для моего волчонка~"
        scene bg holo_room with dissolve
        show h angry_naked_cummed with dissolve
        call hide_dialog
        "[h.name] ушла в душ"
        mind "Мне тоже следует уходить."
        return

    scene bg h_masturbate21_t with dissolve 
    call hide_dialog 
    mind "[h.name] закрывает глаза и принюхивается к моему члену. Её дыхание горячее, а губы слегка приоткрыты."  

    h "Мне так нравится твой запах~~"  

    scene bg h_masturbate22_t with dissolve 
    call hide_dialog 
    "[h.name] целует головку твоего члена, высасывая последние капли спермы. Её движения нежные, а взгляд полон любви."  
    h "Мммммм~"  

    scene bg h_masturbate23_t with dissolve  
    call hide_dialog
    "[h.name] открывает глаза, всё ещё целуя твой член. Её взгляд полон любви, а губы продолжают нежно касаться твоего члена."  

    p "[h.name]... Ты... Ты невероятна..."  

    
    "Довольная [h.name] встает"
    scene bg holo_room with fade
    show h smile_naked_cummed with dissolve
    call hide_dialog
    h "Спасибо за покупку~"
    p "Хах, мне понравилось."
    h "Приходи еще, я буду ждать, [hero_name]!"
    hide h
    mind "Уверен она пошла в душ."
    mind "Мне тоже следует уходить."

    return  



label h_root_titfuck:
    scene bg holo_room with dissolve
    "[h.name] Приводит тебя к себе в комнату"
    show h smile_shy with fade
    h "[hero_name], знаешь, у меня совсем не много опыта в этом.."

    hide h with fade
    show bg h_titfuck1 with dissolve
    call hide_dialog
    "[h.name] стягивает с себя юбку"
    p "Ничего страшного, нехватку опыта ты покроешь другими своими достоинствами."
    h "Охохо~ Ты о моей груди?"
    p "Ну конечно, очень хорошая сделка выходит!"
    
    show bg h_titfuck2 with dissolve
    call hide_dialog
    h "Дааа? Можешь любоваться~"
    "[h.name] немного наклонилась вперед, выпятив свою округлую грудь"
    mind "Сегодня [h.name] еще радостнее, чем обычно, интересно, с чем это связано?"
    h "И это не единственное мое достоинство!"
    
    show bg h_titfuck4 with dissolve
    call hide_dialog
    "[h.name] развернулась в тебе спиной, теперь ты видишь ее нежную попку попку"
    h "Как тебе с другого ракурса?~"
    
    show bg h_titfuck4_2 with dissolve
    call hide_dialog
    mind "Она не перестает меня удивлять, с какой стороны не посмотри."
    p "..."

    show bg h_titfuck4_3 with dissolve
    call hide_dialog
    h "Хах~ Язык проглотил, я готовилась~"
    "[h.name] слегка раздвигает свои ягодицы, играясь со своей попкой"
    p "Ох, я начинаю заводиться."

    show bg h_titfuck4_4 with dissolve
    call hide_dialog
    h "Ах, эти трусики так неудобно сидят~"
    
    show bg h_titfuck4_5 with dissolve
    call hide_dialog
    p "!!!!!" with vpunch
    h "Хахаха! Видел бы ты свое лицо!"
    
    show bg h_titfuck5_1 with dissolve
    call hide_dialog
    "Ты встаешь, чтобы схватить [h.name] за задницу, но она ловко ловит твои руки и прижимает к груди."
    h "Сегодня мы ограничимся моими девочками~"
    p "..."

    show bg h_titfuck5_2 with dissolve
    call hide_dialog
    "[h.name] приподнимает футболку, и прижимает твои руки к своей груди"
    mind "Какие мягкие, блаженство."
    h "Охо~ Вижу тебе понравилось~"

    show bg h_titfuck5_3 with dissolve
    call hide_dialog
    p "Очень понравилось."

    show bg h_titfuck5_4 with dissolve
    call hide_dialog
    h "Неужто ты хотел стоять и мять мою грудь?"

    show bg h_titfuck6 with dissolve
    call hide_dialog
    "[h.name] отталкивает тебя на кровать, стягивает футболку и медленно подползает к тебе"
    p "Как же это сексуально."
    
    show bg h_titfuck7 with dissolve
    call hide_dialog
    mind "Она уже забралась на меня, неужели так соскучилась по моему члену?"
    h "Ну же, доставай его скорее~"
    
    if my_holo.love > 80:
    
        show bg h_titfuck8 with dissolve
        call hide_dialog
        "[h.name] сняла с тебя штаны, и перед ее лицом оказался огромный член"
        h "Ну здравствуй, давно не виделись~"


        show bg h_titfuck12 with dissolve
        call hide_dialog
        h "Ах, мой любимый размер~ Я так скучала~"
        p "Эй, я вообще тоже тут!"
    
    else:
        show bg h_titfuck9 with dissolve
        call hide_dialog
        h "!!!!!" with vpunch
        
        show bg h_titfuck10 with dissolve
        call hide_dialog
        "[h.name] с ужасом смотрит на твой член"
        h "Я никогда к нему не привыкну!"

        show bg h_titfuck11 with dissolve
        call hide_dialog
        h "Тебе не тяжело с ним ходить, [hero_name]?"
        h "Так, берем себя в руки, услуга должна быть указана!"

    show bg h_titfuck13 with dissolve
    call hide_dialog
    "[h.name] проводит языком по головке"
    h "Ммм~ Как же мне нравится твой вкус~"
    
    show bg h_titfuck14 with dissolve
    call hide_dialog
    "[h.name] немного увлажнила твой член"
    h "Так достаточно?"
    p "Ммм, ах, даа, продолжай.."

    show bg h_titfuck15 with dissolve
    call hide_dialog
    "Она неуверенно прижимается грудью. Ты чувствуешь ее горячее тело и теплое дыхание"
    p "[h.name]... Попробуй поместить его между грудей.."
    
    show bg h_titfuck16 with dissolve
    call hide_dialog
    "[h.name] неуверенно обхватывает грудями твой твердный член"
    mind "Как же приятно."
    
    show bg h_titfuck17 with dissolve
    call hide_dialog
    "Стараясь поместить твой член между своих грудей, [h.name] коснулась головки твоего члена губами"
    h "Ахм"
    p "Тебе нужно руками поддерживать свою грудь."

    show bg h_titfuck18 with dissolve
    call hide_dialog
    "[h.name] сжимает член своими грудями"
    p "А-ах... Хорошая девочка..."
    
    show bg h_titfuck19_ with dissolve
    call hide_dialog
    "Она уведила твои реакцию и поняла, что ты уже получаешь удовольствие, на ее лице появляется легкая ухмылка"
    h "Тебе так нравится моя грудь?~"
    
    show bg h_titfuck20_1 with dissolve
    call hide_dialog
    "Твой член запульсировал и вышло немного предспермы"
    p "..."
    h "[hero_name]~ Вижу, очень нравится~"

    "[h.name] начала активнее двигаться"
    

    scene bg h_titfuck20_2 with dissolve  
    pause .5
    scene bg h_titfuck20_3 with dissolve  
    pause .5
    scene bg h_titfuck20_4 with dissolve  
    pause .4
    scene bg h_titfuck20_3 with dissolve  
    pause .4
    scene bg h_titfuck20_2 with dissolve  
    pause .3
    scene bg h_titfuck20_1 with dissolve  
    pause .3
    scene bg h_titfuck20_2 with dissolve  
    pause .3
    scene bg h_titfuck20_3 with dissolve  
    pause .3
    scene bg h_titfuck20_4 with dissolve  
    pause .3
    scene bg h_titfuck20_3 with dissolve  
    pause .2
    scene bg h_titfuck20_4 with dissolve  
    pause .2
    scene bg h_titfuck20_3 with dissolve  
    pause .2
    scene bg h_titfuck20_2 with dissolve  
    pause .2
    scene bg h_titfuck20_1 with dissolve  
    pause .2
    scene bg h_titfuck20_2 with dissolve  
    pause .2
    scene bg h_titfuck20_3 with dissolve  
    pause .1
    scene bg h_titfuck20_4 with dissolve  
    pause .1
    scene bg h_titfuck20_3 with flash  
    pause .1
    scene bg h_titfuck20_4 with flash  

    
    scene bg h_titfuck21_cum1 with flash  
    call hide_dialog
    "Струя спермы вырывается из твоего члена"
    
    scene bg h_titfuck21_cum2 with flash  
    call hide_dialog
    h "Ааааааа..."
    "[h.name] открыла ротик и высунула язык"
    mind "Она уже знает, что меня это заводит сильнее всего."

    scene bg h_titfuck21_cum3 with flash  
    call hide_dialog
    p "Арргх!"
    "Еще большее количество спермы выходит из тебя, [h.name] будто доит твой член своими грудями"

    scene bg h_titfuck21_cum4 with flash  
    call hide_dialog
    "[h.name] не смогла поймать всё в ротик, теперь все ее лицо покрыто твоим семенем"
    p "А-а-ах.."
    
    scene bg h_titfuck21_cum5 with flash  
    call hide_dialog
    "Поток спермы остановился, сперма стекает с ее лица"
    h "Спасибо за угощение~~"
    
    scene bg h_titfuck21_cum6 with dissolve 
    call hide_dialog 
    "Довольная собой, [h.name], улыбается тебе"

    scene bg holo_room with fade
    show h smile_naked_cummed with dissolve
    call hide_dialog
    h "Спасибо за покупку~"
    p "Хах, мне понравилось."
    h "Приходи еще, я буду ждать, [hero_name]!"
    hide h
    mind "Уверен она пошла в душ."
    mind "Мне тоже следует уходить."

    return  


# Сцена глубокого минета с [h.name]
label h_root_blowjob:
    scene bg holo_room with fade
    "[h.name] приводит тебя в свою комнату."
    show h smile_panties with dissolve
    h "Знаешь, [hero_name], я немало практиковалась для твоего размера~"

    # 1. [h.name] в трусиках показывает тело
    scene bg h_blowjob1 at Transform(zoom=1.5) with fade
    call hide_dialog
    "[h.name] с лёгкой насмешкой встаёт на четвереньки на кровати в одних трусиках, покачивая бёдрами."
    h "Ну как тебе? Волчица ведь не зря хвалится своим товаром."
    p "Ты... правда красива."

    scene bg h_blowjob2 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] ложится на кровать, сжимая свою пышную грудь."
    h "Смотри, какая аппетитная грудь у твоей волчицы."

    scene bg h_blowjob3 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] хмыкает, будто что-то её стесняет, и медленно стягивает трусики."

    scene bg h_blowjob4 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    h "Они только мешают. Так куда лучше, согласен?"
    "Её обнажённое тело теперь перед тобой, и она смотрит с хитрой ухмылкой."

    scene bg h_blowjob5 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] садится на колени напротив, её движения плавные и уверенные."
    h "Ну что, начнём? Ты ведь за этим сюда явился."
    p "Да..."
    call h_root_blowjob_continue
    return

label h_root_blowjob_continue:
    scene bg h_blowjob5_2 at Transform(zoom=1.5) with fade
    call hide_dialog
    "Ты расстёгиваешь штаны, и [h.name] склоняет голову."
    h "Ох, какой лакомый кусочек... Не зря ты столько заплатил."
    "Она облизывает губы, её глаза хитро блестят."

    scene bg h_blowjob6 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] устраивается между твоих ног, твой член прямо перед её лицом, а она смотрит тебе в глаза."

    scene bg h_blowjob7 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name], упираясь грудью в твой уже твёрдый член, заставляет его подрагивать."

    scene bg h_blowjob8_1 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] наклоняется ближе и медленно проводит языком вдоль головки, дразня тебя."
    scene bg h_blowjob8_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob8_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob8_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob8_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob8_2 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg h_blowjob9 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    h "Ммм... сладковато. Что ты такое ел? Волчице по вкусу."
    p "[h.name]..."

    scene bg h_blowjob10 at Transform(zoom=1.5) with dissolve
    "[h.name] трётся щекой о твой член с явной ухмылкой."
    h "Как думаешь, ему будет уютно у меня во рту?"

    scene bg h_blowjob11_0 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Не дождавшись твоего ответа, она обхватывает твой член губами и начинает сосать."

    scene bg h_blowjob11_1 at Transform(zoom=1.5) with dissolve
    pause .3
    scene bg h_blowjob11_2 at Transform(zoom=1.5) with dissolve
    pause .3
    scene bg h_blowjob11_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob11_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob11_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob11_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob11_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob11_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob11_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob11_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob11_3 at Transform(zoom=1.5) with dissolve
    pause .1
    h "Ммф... не дёргайся, дай мне повеселиться."
    scene bg h_blowjob12 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Её тёплое дыхание и ловкий язык заставляют тебя сжаться от напряжения."

    scene bg h_blowjob_deep1 at Transform(zoom=1.5) with vpunch
    call hide_dialog
    p "Чёрт, [h.name]... это слишком..."
    "[h.name] наклоняется ниже, заглатывая твой член целиком. Её горло сжимается, и она слегка мычит."
    h "Ммгх..."
    "[h.name] ускоряет движения, заглатывая ещё глубже."
    scene bg h_blowjob_deep2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob_deep3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob_deep5 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob_deep3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob_deep5 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob_deep5 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_blowjob_deep3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep5 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep5 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep5 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_blowjob_deep5 at Transform(zoom=1.5) with flash
    pause .1

    # 8. ГГ кончает в горло [h.name]
    scene bg h_blowjob_deep5_cum1 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты не выдерживаешь и кончаешь."
    scene bg h_blowjob_deep5_cum2 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Поток спермы заполняет её горло. [h.name] глотает, стараясь не отстраниться."
    scene bg h_blowjob_deep5_cum3 at Transform(zoom=1.5) with flash
    call hide_dialog
    "На глазах у [h.name] проступают слёзы."
    h "Ммммф..."

    scene bg h_blowjob_cum4 at Transform(zoom=1.5) with flash
    call hide_dialog
    "[h.name] понимает, что ей не хватает воздуха, и резко поднимается по твоему стволу, пока сперма брызжет наружу."

    scene bg h_blowjob_cum5 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] держит кончик твоего члена во рту, стараясь проглотить всё, что может."

    scene bg h_blowjob_cum6 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    h "Ааах..."

    scene bg h_blowjob_cum7 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name], вся покрытая спермой, открывает рот с улыбкой, показывая, что всё проглотила."

    scene bg h_blowjob_cum8 at Transform(zoom=1.5) with dissolve
    pause .5
    scene bg h_blowjob_cum9 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    h "Ну как, [hero_name]? Мои тренировки стоили того, правда?"

    scene bg h_blowjob_after1 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] ложится напротив тебя и ухмыляется, её лицо и грудь покрыты спермой."
    h "Ну что, стоило своих монет? Волчица умеет угодить, да?"
    p "Ты... невероятна."

    scene bg h_blowjob_after2 at Transform(zoom=1.5) with dissolve
    "[h.name] встаёт на четвереньки, сперма капает с её груди и лица на кровать."
    h "Спасибо за угощение~"
    if my_holo.love >= 90:
        scene bg h_blowjob_after3 at Transform(zoom=1.5) with dissolve
        call hide_dialog
        h "Вижу по твоим глазам, [hero_name], тебе мало."

        scene bg h_blowjob_after4 at Transform(zoom=1.5) with dissolve
        call hide_dialog
        h "Хочешь продолжить?"
        menu:
            h "Хочешь продолжить?"
            "Анал":
                p "Только надень юбку, меня это заводит."
                "..."
                "....."
                "......."
                scene bg pull_skirt1 at Transform(zoom=1.5) with fade
                pause .7
                scene bg pull_skirt2 at Transform(zoom=1.5) with fade
                call hide_dialog
                h "Так?"
                call h_root_anal_continue
                return
            "На этом всё":
                p "На сегодня всё."

    scene bg holo_room with fade
    show h smile_naked_cummed with dissolve
    h "Что ж, [hero_name], было славно. Приноси ещё золота, если захочешь повторить."
    "Она подмигивает и уходит, оставляя тебя одного в комнате."
    "Ты уходишь."
    return

label h_root_fuck:
    scene bg holo_room with fade
    "[h.name] приводит тебя в свою комнату, её глаза блестят хитринкой, а кончик волчьего хвоста слегка покачивается."
    show h smile_shy with dissolve
    h "Ну что, [hero_name], готов к настоящему угощению от волчицы?"

    # 1. Холо раздевается с элементами зверя
    scene bg h_fuck1_1 at Transform(zoom=1.5) with fade
    call hide_dialog
    "[h.name] садится перед тобой и смотрит с игривой насмешкой."

    scene bg h_fuck1_2 at Transform(zoom=1.5) with dissolve
    pause .4
    scene bg h_fuck1_1 at Transform(zoom=1.5) with dissolve
    pause .4
    scene bg h_fuck1_2 at Transform(zoom=1.5) with dissolve
    pause .4
    scene bg h_fuck1_1 at Transform(zoom=1.5) with dissolve
    pause .4
    scene bg h_fuck1_2 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] шевелит ушками и хвостиком, дразня тебя."
    h "Ну как, нравится смотреть на волчицу?"

    scene bg h_fuck2 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Она встаёт и смотрит с лукавой ухмылкой."
    h "Готовься, смертный, сейчас будет жарко!"

    scene bg h_fuck3 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] медленно стягивает юбку ниже по бёдрам, не открывая киску."
    h "Терпение, [hero_name], я знаю, чего ты ждёшь."

    scene bg h_fuck4 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] игриво снимает юбку и приподнимает рубашку, показывая киску и грудь."

    scene bg h_fuck5 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] стоит перед тобой абсолютно голая и уверенная в себе."
    h "Вот тебе волчица во всей красе — наслаждайся!"
    p "Ты... просто невероятна."

    scene bg h_fuck7 at Transform(zoom=1.5) with fade
    call hide_dialog
    "[h.name] садится обратно на колени в немного дикой позе и смотрит на тебя как на добычу."
    h "Ну что, готов к охоте, смертный?"

    scene bg h_fuck8 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Каким-то образом за хвостиком [h.name] появляется красный дилдо."
    h "Смотри, какая у меня игрушка — почти как ты, только чуть скромнее."

    scene bg h_fuck9 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] приближает дилдо к своей киске, слегка касаясь его."
    h "Хочешь, чтобы волчица разогрелась перед тобой?"

    scene bg h_fuck10 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] с той же ухмылкой пристраивается к дилдо, дразня киской."

    scene bg h_fuck11 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] начинает тереться о дилдо, её лицо искажается от возбуждения."
    h "Ммм..."

    scene bg h_fuck12_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck12_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck12_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck12_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck12_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck12_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck12_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck12_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck12_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck12_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck12_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck12_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck12_1 at Transform(zoom=1.5) with flash
    pause .03
    scene bg h_fuck12_2 at Transform(zoom=1.5) with flash
    pause .5
    scene bg h_fuck13 at Transform(zoom=1.5) with flash
    call hide_dialog
    h "Ааах..."
    call h_root_fuck_continue
    return

label h_root_fuck_continue:

    "Ты не выдерживаешь и набрасываешься на [h.name]."
    scene bg h_fuck14 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Твой член уже в киске [h.name], и ты готов её взять."
    h "Ах... Покажи, чего стоишь!"

    scene bg h_fuck15_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck15_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck15_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck15_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck15_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck15_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck15_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck15_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck15_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck15_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck15_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck15_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck15_3 at Transform(zoom=1.5) with flash
    pause .03
    scene bg h_fuck15_1 at Transform(zoom=1.5) with flash
    pause .5
    scene bg h_fuck16 at Transform(zoom=1.5) with flash
    call hide_dialog
    p "Вот тебе!"
    h "Ах... Да!"
    "У [h.name] текут слёзы. Ты заполняешь киску [h.name] спермой, но тебе мало, и ты меняешь позу."

    scene bg h_fuck18 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    p "Стой смирно, волчица!"

    if strength < 50:
        $customNotify("Недостаточно силы")
        "Ты не смог удержать [h.name]"
        scene bg holo_room with fade
        show h angry_naked_cummed with dissolve
        h "Что ж, [hero_name], было хорошо, но и меру надо знать!"
        "Она уходит, оставляя тебя одного в комнате."
        "Ты уходишь."
        return

    scene bg h_fuck18_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck18_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck18_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck18_4 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_fuck18_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck18_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck18_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck18_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_fuck18_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_4 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_fuck18_3 at Transform(zoom=1.5) with flash
    pause .03
    scene bg h_fuck18_4 at Transform(zoom=1.5) with flash
    pause .5
    scene bg h_fuck19 at Transform(zoom=1.5) with flash
    call hide_dialog
    p "Ещё порция для тебя!"
    h "Ааааах!"

    scene bg h_fuck20 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты продолжаешь наполнять её киску спермой, она брызжет наружу и течёт по бёдрам."
    h "Ммм... Ааах.."

    scene bg h_fuck21 at Transform(zoom=1.5) with fade
    call hide_dialog
    "[h.name] падает на кровать от усталости, сперма вытекает из её киски."
    h "Ох..."

    scene bg h_fuck22 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Но ты ещё не закончил и продолжаешь покрывать её тело спермой."
    p "Получай ещё, волчица!"

    scene bg h_fuck23 at Transform(zoom=1.5) with flash
    call hide_dialog
    p "И последняя порция!"
    h "..."

    scene bg holo_room with fade
    "[h.name] всё ещё лежит в огромной луже спермы, а ты уходишь."
    return

label h_root_anal:
    scene bg holo_room with fade
    "[h.name] приводит тебя в свою комнату."
    show h smile_no_top with fade
    h "Присаживайся, [hero_name], и наслаждайся."

    # 1. Холо раздевается
    scene bg h_anal1 at Transform(zoom=1.5) with fade
    call hide_dialog
    "[h.name] дразняще показывает тебе грудь."
    h "Ну как тебе мои сокровища? Волчица ведь знает, как завлечь."
    p "Сложно их не заметить..."

    scene bg h_anal2 at Transform(zoom=1.5) with fade
    call hide_dialog
    h "Ха, и верно! А сегодня я покажу тебе кое-что ещё интереснее."

    scene bg h_anal3 at Transform(zoom=1.5) with fade
    call hide_dialog
    "[h.name] приподнимает юбку, ты видишь, что на ней нет трусиков."
    h "Нравится моя юбка? Или то, что под ней?"

    scene bg h_anal4 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] встаёт на четвереньки боком к тебе в одной юбке."

    scene bg h_anal5 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] немного разворачивается спиной, открывая тебе вид на её анус и киску."
    h "Ну как? Волчица в самом соку, не находишь?"

    scene bg h_anal5 at Transform(zoom=1.5) with dissolve
    pause .3
    scene bg h_anal6 at Transform(zoom=1.5) with dissolve
    pause .3
    scene bg h_anal5 at Transform(zoom=1.5) with dissolve
    pause .3
    scene bg h_anal6 at Transform(zoom=1.5) with dissolve
    pause .3
    scene bg h_anal5 at Transform(zoom=1.5) with dissolve
    pause .3
    scene bg h_anal6 at Transform(zoom=1.5) with dissolve
    "[h.name] слегка покачивает попкой, дразня тебя."

    # 3. Холо подготавливает попку пальцами
    scene bg h_anal7 at Transform(zoom=1.5) with fade
    call hide_dialog
    "[h.name] немного оттягивает попку, показывая тебе свой анус."
    p "Обожаю эту аппетитную попку..."

    scene bg h_anal8 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] оттягивает край своего ануса."

    scene bg h_anal9 at Transform(zoom=1.5) with fade
    call hide_dialog
    "Она нежно вводит два пальца в свой анус."
    h "Надо подготовиться, верно? Волчица не любит скучать."

    scene bg h_anal10_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal10_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal10_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal10_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal10_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal10_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal10_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal10_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal10_2 at Transform(zoom=1.5) with flash
    pause .03
    scene bg h_anal10_3 at Transform(zoom=1.5) with flash
    pause .2
    scene bg h_anal11 at Transform(zoom=1.5) with flash
    call hide_dialog

    scene bg h_anal12 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Она заканчивает играть со своей попкой и медленно вытаскивает пальцы."

    scene bg h_anal13 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] расслабляет анус и растягивает его пальцами, дразня тебя."
    h "Ну что, [hero_name], готов ли я?"
    p "Сейчас помогу."

    # ГГ подходит, его рука тянется к попке Холо
    scene bg h_anal14 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Ты подходишь ближе, и твоя рука касается её попки."
    h "Давай, покажи, на что способен."
    "Ты вводишь два палец, её тело слегка вздрагивает."
    p "Какая тёплая..."
    h "Ха, а ты ждал ледяную волчицу?"
    "Ты двигаешь рукой, и по её лицу видно, что [h.name] наслаждается."

    scene bg h_anal15_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal15_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal15_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal15_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal15_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal15_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal15_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal15_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal15_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal15_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal15_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal15_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal15_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal15_2 at Transform(zoom=1.5) with flash
    pause .03
    scene bg h_anal15_3 at Transform(zoom=1.5) with flash
    pause .2
    scene bg h_anal16 at Transform(zoom=1.5) with flash
    call hide_dialog
    h "Ах... ну же!"

    scene bg h_anal17 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Ты суёшь большой палец ей в попку, слегка двигая."
    p "Теперь ты готова."
    h "Сейчас ты меня..."
    call h_root_anal_continue
    return

label h_root_anal_continue:
    scene bg h_anal18 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    h "Ииик!"
    "Ты резко вводишь свой член в попку [h.name]."

    scene bg h_anal19_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal19_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_anal19_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal19_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_anal19_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_anal19_2 at Transform(zoom=1.5) with flash
    pause .03
    scene bg h_anal19_3 at Transform(zoom=1.5) with flash
    pause .2
    scene bg h_anal20 at Transform(zoom=1.5) with flash
    call hide_dialog
    h "Ааааах!"
    "Ты кончаешь в ее попку."

    scene bg h_anal21 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты выпускаешь огромную порцию спермы."
    p "Получай!"
    h "Ах! Ах! Сколько же тебя!"

    scene bg h_anal22_after1 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты вытаскиваешь член из её попки и продолжаешь кончать на её спину и ягодицы."
    p "Вот так!"

    scene bg h_anal22_after2 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты испускаешь последнее, [h.name] держит попку приподнятой, её анус раскрыт, принимая остатки."
    h "Ммм... Ааах..."

    scene bg h_anal22_after3 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Слезы текут по щекам [h.name], она ложится на живот, сперма сочится из её попки и покрывает спину."

    scene bg h_anal22_after5 at Transform(zoom=1.5) with dissolve
    pause .7
    scene bg h_anal22_after4 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] улыбается и слегка приподнимает попку, показывая, сколько спермы ты оставил внутри."

    scene bg holo_room with fade
    show h smile_naked_cummed with dissolve
    "Юбка падает с бёдер [h.name]."
    "Она встаёт, её тело дрожит, но она гордо ухмыляется."
    h "Ну что, [hero_name], сделка удалась. Приноси ещё монет, если захочешь добавки."
    "Она подмигивает и уходит, оставляя тебя одного в комнате."
    hide h with dissolve
    "Ты уходишь."
    return

label h_root_footfuck:
    scene bg h_foot1 at Transform(zoom=1.5) with fade
    # Холо сидит на стуле или кровати, вытягивая ноги к ГГ
    "[h.name] садится напротив тебя, вытягивая свои стройные ноги и шевеля пальцами."
    h "Смотри, какие у волчицы лапки. Удобно устроился, [hero_name]?"

    scene bg h_foot2 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    p "Холо, что ты задумала?"
    h "Ха, скоро узнаешь. Волчица хочет поиграть!"

    # 2. ГГ возбуждается, Холо касается ногами его члена
    scene bg h_foot3_1 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    # Холо касается ногами промежности ГГ, он напрягается
    "Ты чувствуешь, как её прохладные ступни касаются твоей промежности, и твой член мгновенно твердеет."
    h "Ох, какой ты шустрый! Я ещё ничего толком не сделала, а ты уже наготове."
    "Она хихикает, её пальцы ног слегка сжимают тебя через ткань."
    p "Холо... это слишком..."

    # Анимация: Холо ускоряет движения ногами
    scene bg h_foot3_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_foot3_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg h_foot3_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_foot3_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_foot3_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_foot3_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg h_foot3_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_foot3_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_foot3_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_foot3_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_foot3_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_foot3_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_foot3_1 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg h_foot3_2 at Transform(zoom=1.5) with flash
    call hide_dialog
    h "Ха, ты весь дрожишь, [hero_name]! Неужто мои лапки так тебя завели?"
    p "Холо... я не выдержу долго..."

    # 4. ГГ обильно кончает
    scene bg h_foot4 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты не выдерживаешь, и мощный поток спермы вырывается, заливая её ступни и лодыжки."

    scene bg h_foot5 at Transform(zoom=1.5) with flash
    call hide_dialog
    h "Ох... сколько же ты припас! Волчица довольна таким уловом!"

    scene bg h_foot6 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Сперма сочится из твоего члена и стекает по её ногам, а она ухмыляется."
    h "Ммм... ну и напор у тебя!"

    scene bg h_foot7 at Transform(zoom=1.5) with flash
    call hide_dialog
    p "Ах... Холо..."
    h "Хо-хо, [hero_name], ты так изголодался по моим ножкам?"

    # 5. Холо показывает ноги, покрытые спермой
    scene bg h_foot8 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    # Холо поднимает ноги, демонстрируя сперму
    "[h.name] приподнимает ноги, показывая, как твоя сперма блестит на её коже, и слегка разводит пальцы."
    h "Ну что скажешь, [hero_name]? Мои лапки теперь все в твоём... даре."
    "Она хихикает, её хвост игриво дёргается."

    scene bg h_foot9 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    p "Ты... это слишком много для меня..."
    h "Ха, слишком? Волчица знает, как удивить!"

    scene bg h_foot10 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[h.name] показывает, как сперма стекает по её ножкам."
    h "Тепло и липко... мне нравится."

    scene bg h_foot11 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    h "Неужто мы на этом закончим?"
    menu:
        "Минет":
            call h_root_blowjob_continue
            return
        "Секс":
            p "Нет, мы точно продолжим!"
            call h_root_fuck_continue
            return
        "Анал":
            p "Надень юбку, это меня заводит."
            "..."
            "....."
            "......."
            scene bg pull_skirt1 at Transform(zoom=1.5) with fade
            pause .7
            scene bg pull_skirt2 at Transform(zoom=1.5) with fade
            h "Вот так?"
            call h_root_anal_continue
            return
        "На этом всё":
            p "Хватит на сегодня."

    scene bg holo_room with fade
    show h smile_naked at center with dissolve
    "[h.name] встаёт, её ноги всё ещё покрыты спермой, и она смотрит на тебя с лукавой улыбкой."
    h "Вот так волчица развлекается, [hero_name]. Приходи ещё, если захочешь новых игр."
    "Она подмигивает и уходит, оставляя тебя одного в комнате."
    return