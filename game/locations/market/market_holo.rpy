
default can_work_with_holo = False
define h_can_go_root = False
define h_can_visit = True

label visit_holo:
    scene bg holo_market with fade
    show h smile with dissolve
    if not h_can_go_root and h_love >= 50:
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
                call h_root_masturbate from _call_h_root_masturbate
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
        "Обслужи меня" if h_love >= 50 and h_can_go_root:
            h "О-хо-хо, [hero_name], а ты уверен, что тебе хватит?"
            jump holo_market_root_menu
        "Чем тебе помочь?" if can_work_with_holo:
            menu:
                "Протереть книги(10 монет)":
                    h "Надо протереть книги! Только быстро, там уже очередь! Готов?"
                    scene bg holo_market_boxes with fade
                    call start_clean("books") from _call_start_clean
                    if last_clean_win:
                        h "Хватай следующую, быстрее!"
                        call start_clean("books") from _call_start_clean_1
                        if last_clean_win:
                            h "Последнюю, торопись!"
                            call start_clean("books") from _call_start_clean_2
                            if last_clean_win:
                                h "О-хо-хо! [hero_name], книги были проданы по выгодной цене, это успех!"
                                "Ты провёл время, помогая [h.name]"
                                $addLove("h",5)
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
                    call bug_hunt from _call_bug_hunt
                    $nextTime()
                    scene bg holo_market with fade
                    show h smile_shy with dissolve
                    h "О-хо-хо! [hero_name], спасибо, не знаю, что бы я без тебя делала!"
                    $addLove("h",5)
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
            $addLove("h",3)
            jump holo_market_menu
        "Купить [item_mirror.name]([item_mirror.price] монет)" if isAbleToBuy(item_mirror):
            "Вы купили [item_mirror.name]"
            $buyItem(item_mirror)
            $addLove("h",5)
            jump holo_market_menu
        "Купить [item_art_plus_size.name]([item_art_plus_size.price] монет)" if isAbleToBuy(item_art_plus_size):
            "Вы купили [item_art_plus_size.name]"
            $buyItem(item_art_plus_size)
            $addLove("h",10)
            jump holo_market_menu
        "Купить [item_dumbbells_ez.name]([item_dumbbells_ez.price] монет)" if isAbleToBuy(item_dumbbells_ez):
            "Вы купили [item_dumbbells_ez.name]"
            $buyItem(item_dumbbells_ez)
            $addLove("h",3)
            jump holo_market_menu
        "Купить [item_weight_mid.name]([item_weight_mid.price] монет)" if isAbleToBuy(item_weight_mid):
            "Вы купили [item_weight_mid.name]"
            $buyItem(item_dumbbells_ez)
            $addLove("h",5)
            jump holo_market_menu
        "Купить [item_barbell.name]([item_barbell.price] монет)" if isAbleToBuy(item_barbell):
            "Вы купили [item_barbell.name]"
            $buyItem(item_barbell)
            $addLove("h",10)
            jump holo_market_menu
        "Купить [item_book_math.name]([item_book_math.price] монет)" if isAbleToBuy(item_book_math):
            "Вы купили [item_book_math.name]"
            $buyItem(item_book_math)
            $addLove("h",3)
            jump holo_market_menu
        "Купить [item_self_study_guide.name]([item_self_study_guide.price] монет)" if isAbleToBuy(item_self_study_guide):
            "Вы купили [item_self_study_guide.name]"
            $buyItem(item_self_study_guide)
            $addLove("h",5)
            jump holo_market_menu
        "Купить [item_grimoire.name]([item_grimoire.price] монет)" if isAbleToBuy(item_grimoire):
            "Вы купили [item_grimoire.name]"
            $buyItem(item_grimoire)
            $addLove("h",10)
            jump holo_market_menu
        "Купить [item_forest_guide.name]([item_forest_guide.price] монет)" if isAbleToBuy(item_forest_guide):
            "Вы купили [item_forest_guide.name]"
            $buyItem(item_forest_guide)
            $addLove("h",10)
            jump holo_market_menu
        "Купить [item_combat_book.name]([item_combat_book.price] монет)" if isAbleToBuy(item_combat_book):
            "Вы купили [item_combat_book.name]"
            $buyItem(item_combat_book)
            $addLove("h",10)
            jump holo_market_menu
        "Уйти":
            h "Приятно было с тобой сотрудничать"
            jump holo_menu

label holo_market_root_menu:
    menu:
        "Мастурбация(30 монет)" if h_love >= 50:
            if money < 30:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump market
            $minusMoney(30)
            call h_root_masturbate from _call_h_root_masturbate_1
            $nextTime()
            jump market
        "Грудями(40 монет)" if h_love >= 60:
            if money < 40:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            $minusMoney(40)
            call h_root_titfuck from _call_h_root_titfuck
            $nextTime()
            jump market
        "Минет(50 монет)" if h_love >= 70:
            if money < 50:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            $minusMoney(50)
            call h_root_blowjob from _call_h_root_blowjob
            $nextTime()
            jump market
        "Секс(70 монет)" if h_love >= 80:
            if money < 70:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            $minusMoney(70)
            call h_root_fuck from _call_h_root_fuck
            $nextTime()
            jump market
        "Анал(80 монет)" if h_love >= 90:
            if money < 80:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            $minusMoney(80)
            call h_root_anal from _call_h_root_anal
            $nextTime()
            jump market
        "Фетиш(200 монет)" if h_love >= 200:
            if money < 200:
                h @angry "Ну уж нет, без денег я тебя не обслужу"
                jump holo_menu
            h @smile_shy "Ладно, это слишком, сделаю для тебя скидку~"
            $minusMoney(100)
            call h_root_fetish from _call_h_root_fetish
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

    if h_love < 70:
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
    
    if h_love > 80:
    
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
