label miku_tavern_root:
    scene bg miku_room_tavern with fade
    "Ты в уютной комнате [m.name] в таверне"
    show m smirk_no_top with dissolve
    jump miku_tavern_root_menu

label miku_tavern_root_menu:
    menu:
        "Покажи" if m_love >= 50:
            call m_root_show 
            $nextTime()
            jump tavern
        "Мастурбация" if m_love >= 60: 
            call m_root_titfuck
            $nextTime()
            jump tavern
        "Горловой минет" if m_love >= 70: 
            call m_root_blowjob 
            $nextTime()
            jump tavern
        "Секс" if m_love >= 80: 
            call m_root_fuck 
            $nextTime()
            jump tavern
        "Анал" if m_love >= 90: 
            call m_root_anal 
            $nextTime()
            jump tavern
        "Сделаем это прилюдно" if m_love >= 200: 
            call m_root_fetish 
            $nextTime()
            jump tavern
        "Я передумал": 
            p "Продолжим позже, сейчас у меня есть более важные дела."
            m "Ты многое упускаешь, [hero_name]~~"
            "Ты уходишь"
            jump city

label m_root_tavern_blowjob:
    "IN PROGRESS"
    return

label m_root_show:
    m "Подожди меня тут, [hero_name]~"
    hide m with dissolve
    p "Надо же, как тут светло и чисто."
    
    scene bg m_show0_1 with dissolve
    call hide_dialog
    "Через какое-то время заходит [m.name]."
    m "Эм... Ты уверен, что хочешь это увидеть?"
    p "Конечно. Ты прекрасна, [m.name]."
    
    scene bg m_show0_2 with dissolve
    call hide_dialog
    "[m.name] всё еще прикрывает свою прекрасную грудь."
    mind "Она такая милая, её смущение только добавляет ей шарма."
    p "Давай, не стесняйся. Ты же знаешь, что я восхищаюсь тобой."
    
    scene bg m_show0_3 with dissolve
    call hide_dialog
    "[m.name] нехотя убрала одну из рук, но все еще старается прикрыться."
    m "Ты так смотришь..."
    
    scene bg m_show1 with dissolve
    call hide_dialog
    "[m.name] наклоняется, обнажив свою грудь."
    mind "Черт, это восхитительно..."
    p "Ты прекрасна, [m.name]."
    
    scene bg m_show2 with dissolve
    call hide_dialog
    "Тело [m.name] дрожит от волнения, но улыбка не сходит с ее губ."
    m "И что теперь?"
    p "Может, поднимешь юбку?"
    
    scene bg m_show3 with dissolve
    call hide_dialog
    "Она слегка поднимает короткую юбку, показывая стройные бедра."
    p "Еще чуть-чуть..."
    m "Ты уверен?"

    scene bg m_show4 with dissolve
    call hide_dialog
    "Её лицо заливается румянцем, когда она поднимает юбку ещё выше, обнажая белые трусики."
    m "Они... тебе нравятся?"
    p "Очень... Ты выглядишь потрясающе. Ну же, раздевайся!"
    
    scene bg m_show5 with dissolve
    call hide_dialog
    "[m.name] послушно сняла сарафан, покрасневшая, прикрывает руками грудь и трусики."
    mind "Она стесняется, но не останавливается. Интересно, как далеко она готова зайти?"
    p "Ты прекрасна... Не скрывайся."
    
    scene bg m_show6 with dissolve
    call hide_dialog
    "Она держит руки под грудью, словно немного подталкивая их вверх."
    m "Тебе так нравится моя грудь?"
    
    scene bg m_show7 with dissolve
    call hide_dialog
    "[m.name] слегка сжимает груди руками, её дыхание становится тяжелее."
    p "Я рад, что могу увидеть тебя такой."
    
    scene bg m_show8 with dissolve
    call hide_dialog
    "Она наклоняется, держа в руках груди, показывая их тебе."
    mind "О боже, это просто великолепно."
    p "Ты божественна, [m.name]..."
    
    scene bg m_show9 with dissolve
    call hide_dialog
    "[m.name] поворачивается спиной, обнажая свою изящную попку."
    p "Твоя фигура идеальна."
    
    scene bg m_show10 with dissolve
    call hide_dialog
    "Немного смутившись, она слегка наклоняется и приспускает трусики."
    "Ты видишь ее киску, а её глаза застилает смущённый, но игривый взгляд."
    m "Ты... правда этого хотел?"
    p "Каждую секунду мечтал об этом."
    mind "Теперь главное — удержать себя в руках."

    scene bg m_show11 with dissolve
    call hide_dialog
    "[m.name] наклонилась еще сильнее, румянец на ее лице усиливается, она смущена."
    m "Ты так внимательно смотришь... я чувствую себя такой открытой..."
    p "Потому что ты невероятно красива. Ну же, покажи мне свою киску."
    
    scene bg m_show12 with dissolve
    call hide_dialog
    m "Ты хочешь, чтобы я показала тебе всё?"
    p "Да, [m.name], покажи мне себя полностью."
    
    scene bg m_show13 with dissolve
    call hide_dialog
    "[m.name] встала на кровати на четвереньки, выпятив свою попку."
    mind "Черт... Она такая соблазнительная."
    p "Ты же понимаешь, чего именно я ожидаю?"
    
    scene bg m_show14 with dissolve
    call hide_dialog
    "[m.name] чуть выпрямляется, раздвигая ноги и готовится к чему-то."
    m "Д-да..."

    scene bg m_show15 with dissolve
    call hide_dialog
    "[m.name] опускается на колени, её пальчики медленно скользят к её киске."
    m "Боже, что я делаю...."
    p "Ты всё делаешь правильно."

    scene bg m_show15_1 with dissolve  
    call hide_dialog 
    "[m.name] начинает мастурбировать"
    pause .3 
    scene bg m_show15_2 with dissolve   
    pause .3 
    scene bg m_show15_1 with dissolve   
    pause .2
    scene bg m_show15_2 with dissolve    
    pause .2
    scene bg m_show15_1 with dissolve    
    pause .1
    scene bg m_show15_2 with dissolve    
    pause .1
    scene bg m_show15_1 with dissolve    
    pause .1
    scene bg m_show15_2 with dissolve    
    pause .1
    scene bg m_show15_1 with dissolve
    pause .1
    scene bg m_show15_2 with dissolve
    pause .1
    scene bg m_show15_1 with flash
    pause .3
    scene bg m_show16 with flash
    pause .3
    scene bg m_show17 with flash
    pause .3
    scene bg m_show18 with flash
    call hide_dialog

    "Её движения становятся всё быстрее, её дыхание учащается, а глаза закрываются от наслаждения."
    m "Я... Я... Аааааах..."

    scene bg m_show19 with dissolve
    call hide_dialog
    "Соки [m.name] стекают по её бедрам."
        
    if m_love >= 80:
        menu:
            "Секс":
                call m_root_fuck_continue
            "Продолжать сцену":
                "Ты режаешь досмотреть шоу"
    else:
        $customNotify("Недостаточно симпатии")

    scene bg m_show20 with dissolve
    call hide_dialog
    "[m.name] немного поворачивается, оттягивая попку, чтобы показать, как много соков вышло из неё."
    m "Видишь, как я старалась?"

    if m_love >= 70:
        p "Может покажешь, настоящую себя?"
        m "Д-да..."

        scene bg m_show21 with dissolve
        call hide_dialog
        "Её пальчики медленно скользят к её анусу, она начинает ласкать его, наслаждаясь каждым прикосновением."
        m "Ты правда этого х-хочешь??"
        "Ты сглатываешь.."

        scene bg m_show22 with dissolve
        call hide_dialog
        "[m.name] начинает играть со своим анусом"
        m "Это так... приятно..."

        scene bg m_show23_1 with dissolve 
        call hide_dialog  
        "Её глаза закатываются от удовольствия, а воздух становится горячее"
        "Она продолжает играть со своей попкой, комната наполняется сладкими вздохами [m.name]"
        pause .3 
        scene bg m_show23_2 with dissolve   
        pause .3 
        scene bg m_show23_1 with dissolve   
        pause .2
        scene bg m_show23_2 with dissolve    
        pause .2
        scene bg m_show23_1 with dissolve    
        pause .1
        scene bg m_show23_2 with dissolve    
        pause .1
        scene bg m_show23_1 with dissolve    
        pause .1
        scene bg m_show23_2 with dissolve    
        pause .1
        scene bg m_show23_1 with dissolve
        pause .1
        scene bg m_show23_2 with dissolve
        pause .1
        scene bg m_show23_1 with flash
        pause .3
        scene bg m_show23_3 with flash
        call hide_dialog

        "Её тело дрожит от наслаждения, её пальчики продолжают играть с её анусом, а соки стекают по её бедрам."
        p "Ты так сексуальна..."

        scene bg m_show24 with dissolve
        call hide_dialog
        "[m.name] поворачивается к тебе попкой, раздвигая её, наслаждаясь тем, что ты на неё смотришь."
        m "Тебе нравится?"
        p "Да, хорошая девочка."

        scene bg m_show25 with dissolve
        call hide_dialog
        "Она улыбается, всё ещё в той же позе, её глаза блестят от удовольствия."
        m "Я делаю это для тебя~"

        scene bg m_show26 with dissolve
        call hide_dialog
        "[m.name] немного поворачивается, растягивая свой анус, показывая свою дырочку, её улыбка становится ещё шире."
        m "Хо... Хочешь увидеть больше?"
        p "Конечно!"

        scene bg m_show27 with dissolve
        call hide_dialog
        "Её взгляд меняется на ухмылку, она явно наслаждается тем, как ты на неё смотришь."
        m "Ты такой предсказуемый..."
        mind "Я уже еле держусь!"

        if m_love >= 90:
            menu:
                "Анал":
                    call m_root_anal_continue
                "Продолжить сцену":
                    "Ты режаешь досмотреть шоу"
        else:
            $customNotify("Недостаточно симпатии")
    else:
        $customNotify("Недостаточно симпатии")

    scene bg m_show28 with dissolve
    call hide_dialog
    "[m.name] поднимается, всё ещё наклонившись, её попка всё так же соблазнительно выставлена на показ."

    scene bg m_show29 with dissolve
    call hide_dialog
    "Она встаёт, оперевшись на грудь, раздвинув ноги."
    m "Ты уже еле держишься, да, [hero_name]?"
    p "..."

    scene bg m_show30 with dissolve
    call hide_dialog
    "[m.name] встаёт на прямых раздвинутых ногах, наклонившись вниз, соки с её киски стекают по её животику на грудь."
    m "К-как тебе такое?"
    p "Вау... Ты... Просто нечто!"

    scene bg m_show31 with dissolve
    call hide_dialog
    "Она встаёт, оперевшись на грудь, но теперь повёрнута к тебе спиной, ты видишь её киску и гладкий животик."
    m "К-какую из этих дырочек ты хочешь больше?~"
    if m_love >= 200:
        menu:
            "Обе!":
                call m_root_fetish_public_continue
                #TODO "Ты хватаешь [m.name] и начинаешь жестко насиловать, на ее крики прибегают посетители"
            "Продолжить сцену":
                "Ты решаешь продолжить смотреть шоу"
    else:
        $customNotify("Недостаточно симпатии")

    p "Твоя растяжка... Это что-то!"
    scene bg m_show32 with dissolve
    call hide_dialog
    "[m.name] ложится на бок, её улыбка становится мягче, она явно наслаждается моментом."
    m "М-мне нравится, как ты на меня смотришь~~"

    scene bg m_show33 with dissolve
    call hide_dialog
    "Она ложится на спину, чуть согнув ножки в коленях, её грудь прекрасна."
    p "Не прячь свою чудесную киску, [m.name]."

    scene bg m_show34 with dissolve
    call hide_dialog
    "[m.name] поднимает ножки, лежа на спине, показывая свою киску."
    p "А теперь раздвить свою попку, хочу хорошо рассмотреть твою киску."

    scene bg m_show35 with dissolve
    call hide_dialog
    "Она смущённо придерживает свои ножки, чтобы ты лучше всё рассмотрел."
    m "Ты доволен?"
    p "Конечно!"

    scene bg m_show36 with dissolve
    call hide_dialog
    "[m.name] встаёт на ноги, наклонившись, её киска видна, соки текут по её бедрам."

    scene bg m_show37 with dissolve
    call hide_dialog
    "Она поднимает одну ножку и стоит на другой, показывая свою гибкость и соблазнительную киску."
    p "Эта растяжка нам понадобится позже."

    scene bg m_show37_2 with dissolve
    call hide_dialog
    m "Ч-чтооо?"
    p "Хаха! Ладно, ты итак молодец!"

    scene bg m_show38 with dissolve
    call hide_dialog
    "[m.name] стоит перед тобой, полностью голая, довольная тем, что у нее удалось удовлетворить твой интерес."
    m "На сегодня закончим..."
    
    "[m.name] одевается и уходит"
    "Ты тоже решаешь уйти"

    return

label m_root_titfuck:
    "IN PROGRESS"
    return

label m_root_blowjob:
    "IN PROGRESS"
    return

label m_root_fuck:
    "IN PROGRESS"
    return

label m_root_anal:
    "IN PROGRESS"
    return

label m_root_fetish:
    "IN PROGRESS"
    return