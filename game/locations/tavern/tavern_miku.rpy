label miku_tavern_root:
    scene bg miku_room_tavern at bg_size with fade
    "Ты в уютной комнате [m.name] в таверне"
    show m smirk_no_top with dissolve
    m "Чем займемся сегодня, [hero_name]?"
    jump miku_tavern_root_menu

label miku_tavern_root_menu:
    menu:
        "Покажи" if my_miku_love >= 50:
            call m_root_show 
            $nextTime()
            jump tavern
        "Грудями" if my_miku_love >= 60: 
            call m_root_titfuck
            $nextTime()
            jump tavern
        "Горловой минет" if my_miku_love >= 70: 
            call m_root_blowjob 
            $nextTime()
            jump tavern
        "Секс" if my_miku_love >= 80: 
            call m_root_fuck 
            $nextTime()
            jump tavern
        "Анал" if my_miku_love >= 90: 
            call m_root_anal 
            $nextTime()
            jump tavern
        "Сделаем это прилюдно" if my_miku_love >= 200: 
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

label m_root_show(is_preview=False):
    m "Подожди меня тут, [hero_name]~"
    hide m with dissolve
    p "Надо же, как тут светло и чисто."
    
    scene bg m_show0_1 at bg_size with dissolve
    call hide_dialog
    "Через какое-то время заходит [m.name]."
    m "Эм... Ты уверен, что хочешь это увидеть?"
    p "Конечно. Ты прекрасна, [m.name]."
    
    scene bg m_show0_2 at bg_size with dissolve
    call hide_dialog
    "[m.name] всё еще прикрывает свою прекрасную грудь."
    mind "Она такая милая, её смущение только добавляет ей шарма."
    p "Давай, не стесняйся. Ты же знаешь, что я восхищаюсь тобой."
    
    scene bg m_show0_3 at bg_size with dissolve
    call hide_dialog
    "[m.name] нехотя убрала одну из рук, но все еще старается прикрыться."
    m "Ты так смотришь..."
    
    scene bg m_show1 at bg_size with dissolve
    call hide_dialog
    "[m.name] наклоняется, обнажив свою грудь."
    mind "Черт, это восхитительно..."
    p "Ты прекрасна, [m.name]."
    
    scene bg m_show2 at bg_size with dissolve
    call hide_dialog
    "Тело [m.name] дрожит от волнения, но улыбка не сходит с ее губ."
    m "И что теперь?"
    p "Может, поднимешь юбку?"
    
    scene bg m_show3 at bg_size with dissolve
    call hide_dialog
    "Она слегка поднимает короткую юбку, показывая стройные бедра."
    p "Еще чуть-чуть..."
    m "Ты уверен?"

    scene bg m_show4 at bg_size with dissolve
    call hide_dialog
    "Её лицо заливается румянцем, когда она поднимает юбку ещё выше, обнажая белые трусики."
    m "Они... тебе нравятся?"
    p "Очень... Ты выглядишь потрясающе. Ну же, раздевайся!"
    
    scene bg m_show5 at bg_size with dissolve
    call hide_dialog
    "[m.name] послушно сняла сарафан, покрасневшая, прикрывает руками грудь и трусики."
    mind "Она стесняется, но не останавливается. Интересно, как далеко она готова зайти?"
    p "Ты прекрасна... Не скрывайся."
    
    scene bg m_show6 at bg_size with dissolve
    call hide_dialog
    "Она держит руки под грудью, словно немного подталкивая их вверх."
    m "Тебе так нравится моя грудь?"
    
    scene bg m_show7 at bg_size with dissolve
    call hide_dialog
    "[m.name] слегка сжимает груди руками, её дыхание становится тяжелее."
    p "Я рад, что могу увидеть тебя такой."
    
    scene bg m_show8 at bg_size with dissolve
    call hide_dialog
    "Она наклоняется, держа в руках груди, показывая их тебе."
    mind "О боже, это просто великолепно."
    p "Ты божественна, [m.name]..."
    
    scene bg m_show9 at bg_size with dissolve
    call hide_dialog
    "[m.name] поворачивается спиной, обнажая свою изящную попку."
    p "Твоя фигура идеальна."
    
    scene bg m_show10 at bg_size with dissolve
    call hide_dialog
    "Немного смутившись, она слегка наклоняется и приспускает трусики."
    "Ты видишь ее киску, а её глаза застилает смущённый, но игривый взгляд."
    m "Ты... правда этого хотел?"
    p "Каждую секунду мечтал об этом."
    mind "Теперь главное — удержать себя в руках."

    scene bg m_show11 at bg_size with dissolve
    call hide_dialog
    "[m.name] наклонилась еще сильнее, румянец на ее лице усиливается, она смущена."
    m "Ты так внимательно смотришь... я чувствую себя такой открытой..."
    p "Потому что ты невероятно красива. Ну же, покажи мне свою киску."
    
    scene bg m_show12 at bg_size with dissolve
    call hide_dialog
    m "Ты хочешь, чтобы я показала тебе всё?"
    p "Да, [m.name], покажи мне себя полностью."
    
    scene bg m_show13 at bg_size with dissolve
    call hide_dialog
    "[m.name] встала на кровати на четвереньки, выпятив свою попку."
    mind "Черт... Она такая соблазнительная."
    p "Ты же понимаешь, чего именно я ожидаю?"
    
    scene bg m_show14 at bg_size with dissolve
    call hide_dialog
    "[m.name] чуть выпрямляется, раздвигая ноги и готовится к чему-то."
    m "Д-да..."

    scene bg m_show15 at bg_size with dissolve
    call hide_dialog
    "[m.name] опускается на колени, её пальчики медленно скользят к её киске."
    m "Боже, что я делаю...."
    p "Ты всё делаешь правильно."

    scene bg m_show15_1 at bg_size with dissolve  
    call hide_dialog 
    "[m.name] начинает мастурбировать"
    pause .3 
    scene bg m_show15_2 at bg_size with dissolve   
    pause .3 
    scene bg m_show15_1 at bg_size with dissolve   
    pause .2
    scene bg m_show15_2 at bg_size with dissolve    
    pause .2
    scene bg m_show15_1 at bg_size with dissolve    
    pause .1
    scene bg m_show15_2 at bg_size with dissolve    
    pause .1
    scene bg m_show15_1 at bg_size with dissolve    
    pause .1
    scene bg m_show15_2 at bg_size with dissolve    
    pause .1
    scene bg m_show15_1 at bg_size with dissolve
    pause .1
    scene bg m_show15_2 at bg_size with dissolve
    pause .1
    scene bg m_show15_1 at bg_size with flash
    pause .3
    scene bg m_show16 at bg_size with flash
    pause .3
    scene bg m_show17 at bg_size with flash
    pause .3
    scene bg m_show18 at bg_size with flash
    call hide_dialog

    "Её движения становятся всё быстрее, её дыхание учащается, а глаза закрываются от наслаждения."
    m "Я... Я... Аааааах..."

    scene bg m_show19 at bg_size with dissolve
    call hide_dialog
    "Соки [m.name] стекают по её бедрам."
        

    scene bg m_show20 at bg_size with dissolve
    call hide_dialog
    "[m.name] немного поворачивается, оттягивая попку, чтобы показать, как много соков вышло из неё."
    m "Видишь, как я старалась?"

    if not is_preview:
        if my_miku_love >= 80:
            menu:
                "Секс":
                    p "Надеюсь ты готова.."
                    m "Ммм?"
                    call m_root_fuck_continue
                    return
                "Продолжать сцену":
                    "Ты режаешь досмотреть шоу"
        else:
            $customNotify("Необходимо 80 симпатии")

    if my_miku_love >= 65 or is_preview:
        p "Может покажешь, настоящую себя?"
        m "Д-да..."

        scene bg m_show21 at bg_size with dissolve
        call hide_dialog
        "Её пальчики медленно скользят к её анусу, она начинает ласкать его, наслаждаясь каждым прикосновением."
        m "Ты правда этого х-хочешь??"
        "Ты сглатываешь.."

        scene bg m_show22 at bg_size with dissolve
        call hide_dialog
        "[m.name] начинает играть со своим анусом"
        m "Это так... приятно..."

        scene bg m_show23_1 at bg_size with dissolve 
        call hide_dialog  
        "Её глаза закатываются от удовольствия, а воздух становится горячее"
        "Она продолжает играть со своей попкой, комната наполняется сладкими вздохами [m.name]"
        pause .3 
        scene bg m_show23_2 at bg_size with dissolve   
        pause .3 
        scene bg m_show23_1 at bg_size with dissolve   
        pause .2
        scene bg m_show23_2 at bg_size with dissolve    
        pause .2
        scene bg m_show23_1 at bg_size with dissolve    
        pause .1
        scene bg m_show23_2 at bg_size with dissolve    
        pause .1
        scene bg m_show23_1 at bg_size with dissolve    
        pause .1
        scene bg m_show23_2 at bg_size with dissolve    
        pause .1
        scene bg m_show23_1 at bg_size with dissolve
        pause .1
        scene bg m_show23_2 at bg_size with dissolve
        pause .1
        scene bg m_show23_1 at bg_size with flash
        pause .3
        scene bg m_show23_3 at bg_size with flash
        call hide_dialog

        "Её тело дрожит от наслаждения, её пальчики продолжают играть с её анусом, а соки стекают по её бедрам."
        p "Ты так сексуальна..."

        scene bg m_show24 at bg_size with dissolve
        call hide_dialog
        "[m.name] поворачивается к тебе попкой, раздвигая её, наслаждаясь тем, что ты на неё смотришь."
        m "Тебе нравится?"
        p "Да, хорошая девочка."

        scene bg m_show25 at bg_size with dissolve
        call hide_dialog
        "Она улыбается, всё ещё в той же позе, её глаза блестят от удовольствия."
        m "Я делаю это для тебя~"

        scene bg m_show26 at bg_size with dissolve
        call hide_dialog
        "[m.name] немного поворачивается, растягивая свой анус, показывая свою дырочку, её улыбка становится ещё шире."
        m "Хо... Хочешь увидеть больше?"
        p "Конечно!"

        scene bg m_show27 at bg_size with dissolve
        call hide_dialog
        "Её взгляд меняется на ухмылку, она явно наслаждается тем, как ты на неё смотришь."
        m "Ты такой предсказуемый..."
        mind "Я уже еле держусь!"
        if not is_preview:
            if charisma >= 90:
                menu:
                    "Анал":
                        call m_root_anal_continue
                        return
                    "Продолжить сцену":
                        "Ты режаешь досмотреть шоу"
            else:
                $customNotify("Необходимо 90 харизмы")
    else:
        $customNotify("Необходимо 90 симпатии")

    scene bg m_show28 at bg_size with dissolve
    call hide_dialog
    "[m.name] поднимается, всё ещё наклонившись, её попка всё так же соблазнительно выставлена на показ."

    scene bg m_show29 at bg_size with dissolve
    call hide_dialog
    "Она встаёт, оперевшись на грудь, раздвинув ноги."
    m "Ты уже еле держишься, да, [hero_name]?"
    p "..."

    scene bg m_show30 at bg_size with dissolve
    call hide_dialog
    "[m.name] встаёт на прямых раздвинутых ногах, наклонившись вниз, соки с её киски стекают по её животику на грудь."
    m "К-как тебе такое?"
    p "Вау... Ты... Просто нечто!"

    scene bg m_show31 at bg_size with dissolve
    call hide_dialog
    "Она встаёт, оперевшись на грудь, но теперь повёрнута к тебе спиной, ты видишь её киску и гладкий животик."
    
    if not is_preview:
        if my_miku_love >= 200:
            m "К-какую из этих дырочек ты хочешь больше?~"
            menu:
                "Обе!":
                    scene bg miku_public_continue0 at bg_size with dissolve
                    "Ты хватаешь [m.name] и начинаешь ее насиловать изо всех сил, на ее крики прибегают посетители.."
                    call m_root_fetish_public_continue
                    return
                "Продолжить сцену":
                    "Ты решаешь продолжить смотреть шоу"
        else:
            $customNotify("Необходимо 20 симпатии")

    p "Твоя растяжка... Это что-то!"
    scene bg m_show32 at bg_size with dissolve
    call hide_dialog
    "[m.name] ложится на бок, её улыбка становится мягче, она явно наслаждается моментом."
    m "М-мне нравится, как ты на меня смотришь~~"

    scene bg m_show33 at bg_size with dissolve
    call hide_dialog
    "Она ложится на спину, чуть согнув ножки в коленях, её грудь прекрасна."
    p "Не прячь свою чудесную киску, [m.name]."

    scene bg m_show34 at bg_size with dissolve
    call hide_dialog
    "[m.name] поднимает ножки, лежа на спине, показывая свою киску."
    p "А теперь раздвить свою попку, хочу хорошо рассмотреть твою киску."

    scene bg m_show35 at bg_size with dissolve
    call hide_dialog
    "Она смущённо придерживает свои ножки, чтобы ты лучше всё рассмотрел."
    m "Ты доволен?"
    p "Конечно!"

    scene bg m_show36 at bg_size with dissolve
    call hide_dialog
    "[m.name] встаёт на ноги, наклонившись, её киска видна, соки текут по её бедрам."

    scene bg m_show37 at bg_size with dissolve
    call hide_dialog
    "Она поднимает одну ножку и стоит на другой, показывая свою гибкость и соблазнительную киску."
    p "Эта растяжка нам понадобится позже."

    if not is_preview:
        if charisma >= 60:
            p "Может даже прямо сейчас..."
            menu:
                "Секс":
                    scene bg m_show37_2 at bg_size with dissolve
                    call hide_dialog
                    m "Ч-чтооо?"
                    p "Подставляй задницу!"
                    scene bg m_show20 at bg_size with fade
                    "[my_miku.name] послушно поворачивается к тебе попкой."
                    call m_root_fuck_continue
                    return
                "Ничего":
                    scene bg m_show37_2 at bg_size with dissolve
                    call hide_dialog
                    m "Ч-чтооо?"
                    p "Хаха! Ладно, ты итак молодец!"
        else:
            $customNotify("Необходимо 60 харизмы")
            scene bg m_show37_2 at bg_size with dissolve
            call hide_dialog
            m "Ч-чтооо?"
            p "Хаха! Ладно, ты итак молодец!"
    else:
        scene bg m_show37_2 at bg_size with dissolve
        call hide_dialog
        m "Ч-чтооо?"
        p "Хаха! Ладно, ты итак молодец!"


    scene bg m_show38 at bg_size with dissolve
    call hide_dialog
    "[m.name] стоит перед тобой, полностью голая, довольная тем, что у нее удалось удовлетворить твой интерес."
    m "На сегодня закончим..."
    
    "[m.name] одевается и уходит"
    "Ты тоже решаешь уйти"

    return

label m_root_titfuck(is_preview=False):
    scene bg miku_titfuck1 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] отталкивает тебя на кровать и слегка приподнимает юбку так, что ты можешь увидеть ее белые трусики"
    m "Расслабься, [hero_name], сейчас я покажу тебе настоящий сервис~"
    p "Э-э, подожди, что ты задумала?"
    m "Тсс, не спорь с профессионалом!"

    scene bg miku_titfuck2 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] стоит ровно перед тобой"
    m "Ну что, настроился?"
    p "Ты серьезно?"

    scene bg miku_titfuck3 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] убирает часть костюма прикрывающую грудь"
    m "Ха! Так ведь привычнее, да?"
    p "..."

    scene bg miku_titfuck3_2 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name], смущаясь, наклоняется. Она снимает свою юбку, открывая отличный вид на ее киску"
    m "Ой, кажется, я немного увлеклась... Нравится?"

    scene bg miku_titfuck4 at bg_size with dissolve
    pause 0.7
    scene bg miku_titfuck4_2 at bg_size with dissolve
    call hide_dialog
    "Она полностью снимает верх, ты видишь ее шикарную большую грудь"
    m "Ну, как тебе вид?"
    p "Это... впечатляет."
    m "Хи-хи, я знала, что тебе понравится!"

    scene bg miku_titfuck5 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] садится на колени и прижимается своими грудями между твоих ног, смотря просящим взглядом"

    scene bg miku_titfuck6 at bg_size with dissolve
    call hide_dialog
    "Внезапно твой член выскакивает у нее между грудей и слегка шлепает по ее личику, прикасаясь к ее губам"
    m "!!!"

    scene bg miku_titfuck7 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] осматривает твой член с восторгом"
    m "Вау, он просто огромный!"
    p "Эм... спасибо?"

    scene bg miku_titfuck8_1 at bg_size with dissolve
    call hide_dialog
    "Она нежно проводит языком по твоему члену"
    m "Сейчас попробуем на вкус~"

    scene bg miku_titfuck8_2 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck8_3 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_5 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck8_5 at bg_size with dissolve
    call hide_dialog
    m "Ммм..."

    scene bg miku_titfuck9 at bg_size with dissolve
    call hide_dialog
    m "Как тебе мой язычок, а, [hero_name]?"
    if charisma < 25 and not is_preview:
        $customNotify("Необходимо 25 харизмы")
        p "Не так уж это и заводит..."
        scene bg miku_titfuck5 at bg_size with dissolve
        m "Я... Тебя не возбудила?"
        $minusLove(my_miku, -5)
        m "Тебе пора идти, [hero_name]!"
        return
    p "Ты просто невероятна!"

    scene bg miku_titfuck10 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck11 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] обхватывает грудями твой член"
    m "Серьезно? А я ведь только разогреваюсь!"
    p "Ты точно официантка, а не волшебница?"
    m "Хе-хе, я многопрофильный талант!"

    scene bg miku_titfuck11_1 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck11_4 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .3
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_1 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_4 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_1 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .1
    scene bg miku_titfuck11_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_1 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_3 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_1 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_2 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_4 at bg_size with dissolve
    pause .03
    scene bg miku_titfuck11_4 at bg_size with flash
    call hide_dialog
    p "Аргх!"

    scene bg miku_titfuck12 at bg_size with flash
    pause .5
    scene bg miku_titfuck13 at bg_size with flash
    call hide_dialog
    "[my_miku.name] сжимает твой член, и ты выпускаешь весь поток спермы"

    scene bg miku_titfuck14 at bg_size with flash
    call hide_dialog
    "Ты начинаешь кончать, струя спермы летит в лицо [my_miku.name]"

    scene bg miku_titfuck15 at bg_size with flash
    call hide_dialog
    "[my_miku.name] закрывает глаза и открывает рот, стараясь поймать как можно больше твоей спермы"
    m "Ааааа.."

    scene bg miku_titfuck16 at bg_size with flash
    call hide_dialog
    "[my_miku.name] все еще с закрытыми глазами получает твою сперму в рот и на лицо"

    scene bg miku_titfuck17 at bg_size with dissolve
    call hide_dialog
    "Ты наконец останавливаешься. [my_miku.name] открыла глаза и держит твой член грудями, открыв рот, показывая, как много спермы у нее во рту"

    scene bg miku_titfuck18 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] улыбается, глотая твою сперму"

    scene bg miku_titfuck19 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] наклоняется, открывая свой пустой ротик, показывая, что всё проглотила"

    if not is_preview:
        if strength >= 70:
            menu:
                "Минет":
                    p "Тебе придется продолжить ротиком."
                    m "!!!"
                    call m_root_blowjob_continue
                    return
                "Продолжить":
                    m "Ааааа..."
        else:
            $customNotify("Необходимо 70 силы")

    scene bg miku_titfuck20 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] улыбается, смотря на тебя и упираясь своим личиком на твой член"
    m "Ну что, как ощущения?"

    scene bg miku_titfuck21 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] наклоняется, приближаясь к твоему члену губами"
    m "Подожди, тут еще осталось немного..."

    scene bg miku_titfuck22 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] закрывает глаза и вытягивает губы"

    scene bg miku_titfuck23 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] слизывает сперму с твоего члена"
    m "Ммм..."

    scene bg miku_titfuck24 at bg_size with dissolve
    call hide_dialog
    "После этого она смотрит на тебя с улыбкой"
    m "Ну, как тебе мой фирменный стиль?"

    scene bg miku_titfuck25 at bg_size with dissolve
    call hide_dialog
    m "Ну что, [hero_name]? Это было покруче любого шоу!"

    scene bg miku_titfuck26 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] сжимает свою грудь, залитую твоей спермой"
    m "Как тебе мои девочки в деле, а?"
    p "Они... Н-настоящие звезды."

    scene bg miku_titfuck27 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] ложится на кровать, сперма всё ещё стекает по её телу, и она смотрит на тебя с кокетливой улыбкой."
    m "Вот так я забочусь о своих любимчиках! Заходи еще, [hero_name], не пожалеешь!"
    p "После такого точно вернусь."
    "Ты уходишь, оставляя ее прибирать беспорядок."
    return

label m_root_blowjob(is_preview=False):
    m "Подожди меня тут, [hero_name]~"
    hide m with dissolve
    "..."
    "....."
    "......."
    scene bg m_blowjob1 at bg_size with dissolve
    call hide_dialog
    "Она вошла в комнату полностью обнаженная"

    scene bg m_blowjob2 at bg_size with dissolve
    call hide_dialog
    "Она слегка подпрыгнула, а ее груди качнулись"
    m "Хе-хе, нравится, как они танцуют?"

    scene bg m_blowjob3 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] садится на колени, и медленно подползает к тебе"
    m "Тебе же нравится моя грудь, да?"
    p "Трудно не заметить..."

    scene bg m_blowjob4 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] быстро стянула с тебя штаны и твой эрегированный член уперся в ее личико"
    m "Ого, кто-то тут уже в полной готовности!"
    p "Ты сама виновата."

    scene bg m_blowjob5 at bg_size with dissolve
    pause .3
    scene bg m_blowjob6 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] прижимается грудью к твоим ногам, зажимая твой член"
    m "Я знаю, что тебе понравится еще больше~"
    p "Ты слишком самоуверенна."
    m "Просто смотри и наслаждайся!"

    scene bg m_blowjob7_0 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] берет кончик твоего члена в ротик и водит язычком"
    m "Ммм, какой вкусный~"

    scene bg m_blowjob7_1 at bg_size with dissolve
    pause .1
    scene bg m_blowjob7_2 at bg_size with dissolve
    pause .1
    scene bg m_blowjob7_3 at bg_size with dissolve
    pause .05
    scene bg m_blowjob7_2 at bg_size with dissolve
    pause .05
    scene bg m_blowjob7_1 at bg_size with dissolve
    pause .05
    scene bg m_blowjob7_2 at bg_size with dissolve
    pause .05
    scene bg m_blowjob7_3 at bg_size with dissolve
    pause .05
    scene bg m_blowjob7_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_1 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_3 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_1 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_3 at bg_size with dissolve
    pause .03
    scene bg m_blowjob7_2 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] вылизывает головку твоего члена до блеска"
    if charisma < 40 and not is_preview:
        $customNotify("Необходимо 40 харизмы")
        p "Ааах... Как же ты хороша..."
        scene bg m_blowjob6 at bg_size with dissolve
        m "Да? Рада, что тебе понравилось!"
        m "В таком случае можешь идти, у меня еще полно работы."
        return
    p "Отлично, продолжай"

    scene bg m_blowjob8 at bg_size with dissolve
    call hide_dialog
    "Теперь она берет головку твоего члена целиком в свой рот и начинает двигаться"
    m "Мрф... нравится?"

    scene bg m_blowjob9 at bg_size with dissolve
    pause .2
    scene bg m_blowjob10 at bg_size with dissolve
    pause .2
    scene bg m_blowjob9 at bg_size with dissolve
    pause .1
    scene bg m_blowjob8 at bg_size with dissolve
    pause .1
    scene bg m_blowjob9 at bg_size with dissolve
    pause .1
    scene bg m_blowjob10 at bg_size with dissolve
    pause .05
    scene bg m_blowjob9 at bg_size with dissolve
    pause .05
    scene bg m_blowjob8 at bg_size with dissolve
    pause .05
    scene bg m_blowjob9 at bg_size with dissolve
    pause .05
    scene bg m_blowjob10 at bg_size with dissolve
    pause .05
    scene bg m_blowjob9 at bg_size with dissolve
    pause .05
    scene bg m_blowjob8 at bg_size with dissolve
    pause .02
    scene bg m_blowjob9 at bg_size with dissolve
    pause .02
    scene bg m_blowjob10 at bg_size with dissolve
    pause .02
    scene bg m_blowjob9 at bg_size with dissolve
    pause .02
    scene bg m_blowjob8 at bg_size with dissolve
    pause .02
    scene bg m_blowjob9 at bg_size with dissolve
    pause .02
    scene bg m_blowjob10 at bg_size with dissolve
    pause .02
    scene bg m_blowjob9 at bg_size with dissolve
    pause .02
    scene bg m_blowjob8 at bg_size with dissolve
    pause .02
    scene bg m_blowjob9 at bg_size with dissolve
    pause .02
    scene bg m_blowjob10 at bg_size with dissolve
    call hide_dialog
    call m_root_blowjob_continue
    return

label m_root_blowjob_continue:
    scene bg m_blowjob11_1 at bg_size with dissolve
    call hide_dialog
    "Ты берешь [my_miku.name] за волосы и оттягиваешь"
    "[my_miku.name] ухмыляется"
    m "Что, не выдержал моего темпа?"
    if strength < 40:
        $customNotify("Необходимо 40 силы")
        "Ты тянешь ее голову на свой член, но у тебя не получается."
        p "А, ой, нет, прости, не хотел испортить твою прическу."
        scene bg m_blowjob11_2 at bg_size with dissolve
        m "Мы закончили, можешь уходить, и даже не думай испортить мою прическу..."
        return
    p "Скорее, решил взять все в свои руки."

    scene bg m_blowjob11_2 at bg_size with dissolve
    call hide_dialog
    p "Считай это помощью."
    m "Эй, подожди-ка..."

    scene bg m_blowjob11_3 at bg_size with dissolve
    call hide_dialog
    "Выражение лица [my_miku.name] сменилось на испуганное и не зря"
    m "К-как помочь? Ты что задумал?!"
    p "Увидишь."

    scene bg m_blowjob12_2 at bg_size with dissolve
    call hide_dialog
    "Ты с силой берешь голову [my_miku.name] и насаживаешь на свой член, начиная жестко ебать ее в рот"

    scene bg m_blowjob12_3 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_4 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_3 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_2 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_3 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_4 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_3 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_2 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_3 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_4 at bg_size with dissolve
    pause .1
    scene bg m_blowjob12_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_4 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_4 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_4 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_4 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_2 at bg_size with dissolve
    pause .03
    scene bg m_blowjob12_4 at bg_size with flash
    call hide_dialog
    m "М-мм... глх!"

    scene bg m_blowjob13_1 at bg_size with dissolve
    pause .1
    scene bg m_blowjob13_2 at bg_size with flash
    call hide_dialog
    p "Давай глубже!"
    m "Мрф-ф!"

    scene bg m_blowjob14_1 at bg_size with flash
    call hide_dialog
    "Выражение лица [my_miku.name] тебя возбуждает еще сильнее"
    m "Мрфффрррр!"

    scene bg m_blowjob14_2 at bg_size with dissolve
    pause .1
    scene bg m_blowjob14_3 at bg_size with flash
    call hide_dialog
    m "Грлллфф!"

    scene bg m_blowjob14_4 at bg_size with flash
    call hide_dialog
    p "Даа! Отлично берёшь!"
    m "Брррлллл!"

    scene bg m_blowjob15_1 at bg_size with dissolve
    call hide_dialog
    "Ты отпускаешь голову [my_miku.name]"

    scene bg m_blowjob15_2 at bg_size with flash
    call hide_dialog
    "Сперма брызжет из ее рта и носа"
    m "Кхрф!"

    scene bg m_blowjob16_1 at bg_size with dissolve
    call hide_dialog
    "Наконец [my_miku.name] поднимает голову и вдыхает"
    m "А-ааах!"

    scene bg m_blowjob16_2 at bg_size with dissolve
    call hide_dialog
    "Из ее рта вытекает твоя сперма"
    p "Какая растрата..."

    scene bg m_blowjob17 at bg_size with dissolve
    pause .4
    scene bg m_blowjob18 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] закрывает ротик и сглатывает"

    scene bg m_blowjob19 at bg_size with dissolve
    call hide_dialog
    p "Хорошая девочка."
    m "Угум..."

    scene bg m_blowjob20 at bg_size with fade
    call hide_dialog

    if intelligence >= 60:
        menu:
            "Секс":
                p "Подставляй задницу!"
                scene bg m_show20 with fade
                "[my_miku.name] вытирает слёзы и послушно поворачивается к тебе"
                call m_root_fuck_continue
                return
            "Продолжить":
                m "Ааааа..."
    else:
        $customNotify("Необходимо 60 интеллекта")

    p "Тут стало так грязно, я пожалуй пойду."
    "Ты встаешь и уходишь."
    return

label m_root_fuck(is_preview=False):
    m "Подожди тут, я сейчас вернусь... в новом образе~"
    hide m with dissolve
    p "..."
    p "....."
    p "......."

    scene bg m_fuck1_1 at bg_size with fade
    call hide_dialog
    "В комнату заходит [my_miku.name], переодетая в костюм развратной студентки, покачивая бёдрами, с её фирменной ослепительной улыбкой."
    p "!!!"
    m "Ну что, [hero_name], соскучился по своей любимой официантке? Сегодня я подаю нечто... особенное~"
    p "Это что, новый костюм?!"

    scene bg m_fuck1_2 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] подходит ближе и грациозно облокачивается на кровать, пока её роскошные груди манят тебя."
    m "В нашем меню сегодня горячая порция меня, милый~ Как тебе такой заказ?"
    p "*сглатывает*"

    scene bg m_fuck1_3 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] разворачивается спиной, и под юбочкой мелькают её белые стринги."
    m "Ой-ой, вижу, как глазки загорелись~ Нравится мой новый образ?"

    scene bg m_fuck1_4 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] медленно стягивает юбочку вниз, и слегка оттопыривает попку, дразня тебя."
    
    scene bg m_fuck1_5 at bg_size with dissolve
    call hide_dialog
    m "Хороший вид, а, [hero_name]?"

    scene bg m_fuck1_6 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name], сияя улыбкой, стягивает стринги, открывая тебе всё, что скрывалось под тканью."
    m "Эти тесные трусики только мешают... Мне стоит их снять, как думаешь?"
    p "*сглатывает*"
    
    scene bg m_fuck1_7 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] раздвигает попку руками, и бросает на тебя лукавый взгляд."
    
    scene bg m_fuck1_8 at bg_size with dissolve
    call hide_dialog
    "Она оборачивается, а её рубашка соскальзывает с плеч, обнажая грудь."
    
    scene bg m_fuck1_9 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] легла на кровать, голая, чуть прикрывая грудь, и кокетливо склоняет голову."
    m "Ты так смотришь... Мне даже неловко~"
    
    scene bg m_fuck1_10 at bg_size with dissolve
    call hide_dialog
    "Она встаёт на четвереньки, повернувшись попкой к тебе, и оттягивает анус."
    m "Хах, шучу, наслаждайся шоу~"
    call m_root_fuck_continue(is_preview)
    return

label m_root_fuck_continue(is_preview=False):
    scene bg m_fuck2 at bg_size with vpunch
    call hide_dialog
    "Ты не выдерживаешь и врываешься в её тугую киску."
    m "Ах!~"
    "[my_miku.name] начинает двигаться на тебе, словно исполняя ритмичный танец."

    scene bg m_fuck3_1 at bg_size with dissolve
    pause .15
    scene bg m_fuck3_2 at bg_size with dissolve
    pause .15
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .15
    scene bg m_fuck3_4 at bg_size with dissolve
    pause .1
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .1
    scene bg m_fuck3_2 at bg_size with dissolve
    pause .1
    scene bg m_fuck3_1 at bg_size with dissolve
    pause .05
    scene bg m_fuck3_2 at bg_size with dissolve
    pause .05
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .05
    scene bg m_fuck3_4 at bg_size with dissolve
    pause .05
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .05
    scene bg m_fuck3_2 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_4 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_4 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_4 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck3_4 at bg_size with flash
    pause .03
    scene bg m_fuck3_3 at bg_size with flash
    pause .03
    scene bg m_fuck3_4 at bg_size with flash
    call hide_dialog

    "[my_miku.name] ускоряет темп, её грудь подпрыгивает."
    m "Ох, [hero_name]... Моя киска... Горит..."

    "Ты чувствуешь, как всё внутри сжимается, и начинаешь кончать в её киску."
    scene bg m_fuck4 at bg_size with flash
    m "Ах! Давай, [hero_name], кончи в меня~"
    scene bg m_fuck5 at bg_size with flash
    pause .7
    scene bg m_fuck6 at bg_size with flash
    call hide_dialog
    p "Умничка, [my_miku.name]."

    scene bg m_fuck7 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] смотрит на тебя с сияющей улыбкой. Ты оттягиваешь её попку, наблюдая, как твоя сперма вытекает."

    scene bg m_fuck8 at bg_size with dissolve
    call hide_dialog
    m "Ммм... Так тепло внутри..."

    scene bg m_fuck9 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] хватает свою попку одной рукой и бросает на тебя озорной взгляд."

    scene bg m_fuck10 at bg_size with dissolve
    call hide_dialog
    if not is_preview:
        if charisma >= 90:
            m "Я хорошо знаю тебя, [hero_name]... Тебе ведь мало, верно?"
            menu:
                m "Продолжим?"
                "Анал":
                    p "Ты читаешь мои мысли..."
                    call m_root_anal_continue
                    return
                "Достаточно":
                    p "Пока хватит, звезда моя."
        else:
            $customNotify("Необходимо 90 харизмы")
    
    m "Мы ведь повторим, да, [hero_name]?"
    p "Обязательно."
    "Ты встаёшь и уходишь, оставляя её убирать беспорядок."
    return

label m_root_anal_continue:
    scene bg m_fuck11_1 at bg_size with vpunch
    call hide_dialog
    "Ты резко хватаешь [my_miku.name], врываясь в её узкую задницу."
    m "Ааах!"

    scene bg m_fuck11_2 at bg_size with dissolve
    pause .2
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .2
    scene bg m_fuck11_4 at bg_size with dissolve
    pause .2
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .2
    scene bg m_fuck11_2 at bg_size with dissolve
    pause .1
    scene bg m_fuck11_1 at bg_size with dissolve
    pause .1
    scene bg m_fuck11_2 at bg_size with dissolve
    pause .1
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .1
    scene bg m_fuck11_4 at bg_size with dissolve
    pause .1
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .1
    scene bg m_fuck11_2 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_4 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_4 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_4 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_3 at bg_size with dissolve
    pause .03
    scene bg m_fuck11_4 at bg_size with flash
    call hide_dialog
    m "Да! ДА! Дааа! "

    scene bg m_fuck12 at bg_size with flash
    call hide_dialog
    "Ты кончаешь."
    m "Ах! Да! Заполни меня~"

    scene bg m_fuck13 at bg_size with flash
    call hide_dialog
    "Поток спермы усиливается, и [my_miku.name] стонет."
    m "Аааах~~"

    scene bg m_fuck14 at bg_size with flash
    call hide_dialog
    "Ты выплёскиваешь всё до последней капли."

    scene bg m_fuck15 at bg_size with dissolve
    call hide_dialog
    "Ты вытаскиваешь член, а [my_miku.name] дрожит, всё ещё в экстазе, пока сперма вытекает из её ануса."

    scene bg m_fuck17 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] падает на кровать, изнеможённая, пока её анус сочится твоим семенем."
    p "Отличное шоу, ещё вернусь за добавкой!"

    scene bg m_fuck16 at bg_size with dissolve
    call hide_dialog
    m "А-агааа~"
    "Ты уходишь, оставляя ее отдыхать в беспорядке, который вы устроили."
    return

label m_root_anal(is_preview=False):
    m "Подожди тут, я сейчас вернусь... в новом образе~"
    hide m with dissolve
    p "..."
    p "....."
    p "......."
    
    scene bg m_anal1 at bg_size with dissolve
    call hide_dialog
    "Дверь комнаты открывается, и в неё вплывает [my_miku.name], одетая в голубое бикини — яркое, обтягивающее, с её длинными бирюзовыми хвостиками, покачивающимися в такт шагам."
    m "Ну что, [hero_name]? Как тебе мой новый костюмчик для особого обслуживания?~"
    
    scene bg m_anal2 at bg_size with dissolve
    call hide_dialog
    "Она подходит ближе и с улыбкой сжимает свои большие, упругие груди."
    
    scene bg m_anal3_1 at bg_size with dissolve
    pause .7
    scene bg m_anal3_2 at bg_size with dissolve
    call hide_dialog
    m "Ммм, они такие тяжёлые сегодня... Хочешь помочь мне их разгрузить?~"
    p "*сглатывает*"

    scene bg m_anal4 at bg_size with dissolve
    pause .7
    scene bg m_anal4_2 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] хихикает, затем оттягивает резинку своих трусиков и отпускает её, позволяя ткани звонко шлёпнуть по её упругой попке."
    m "Ой! *смеётся* Кажется, я сама себя наказала~ Нравится такой ритм, [hero_name]?"
    
    scene bg m_anal5 at bg_size with dissolve
    call hide_dialog
    "Она медленно приподнимает верх бикини, открывая тебе вид на её роскошную грудь — соски уже слегка напряжены, а кожа блестит в мягком свете комнаты."

    scene bg m_anal6 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] сбрасывает верх бикини на пол."

    scene bg m_anal7 at bg_size with dissolve
    call hide_dialog
    "Она поворачивается спиной и наклоняется, выставляя свою попку на показ."
    scene bg m_anal7_2 at bg_size with dissolve
    m "Ну как, [hero_name]? Эта часть шоу тебе по вкусу?~"
    
    scene bg m_anal8_1 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] спускает трусики по бедрам, показывая тебе самое сокровенное."
    m "Не так хорош образ, как то, что скрывается под ним~"
    
    scene bg m_anal8_2 at bg_size with dissolve
    pause .7
    scene bg m_anal8_3 at bg_size with dissolve
    call hide_dialog
    "Она полностью спустила трусики и оттянула попку так, чтобы ты получше рассмотрел ее анус."

    scene bg m_anal9 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] тянется к своему анусу и начинает дразнить его кончиками пальцев, слегка постанывая в ритм своим движениям."
    m "Сегодня мне точно надо подготовиться, я знаю, с чем мне придется иметь дело~"
    
    scene bg m_anal9_1 at bg_size with dissolve
    pause .2
    scene bg m_anal9_2 at bg_size with dissolve
    pause .2
    scene bg m_anal9_3 at bg_size with dissolve
    pause .2
    scene bg m_anal9_4 at bg_size with dissolve
    pause .2
    scene bg m_anal9_3 at bg_size with dissolve
    pause .1
    scene bg m_anal9_2 at bg_size with dissolve
    pause .1
    scene bg m_anal9_3 at bg_size with dissolve
    pause .1
    scene bg m_anal9_4 at bg_size with dissolve
    pause .1
    scene bg m_anal9_3 at bg_size with dissolve
    pause .1
    scene bg m_anal9_2 at bg_size with dissolve
    pause .1
    scene bg m_anal9_3 at bg_size with dissolve
    pause .1
    scene bg m_anal9_4 at bg_size with dissolve
    pause .1
    scene bg m_anal9_3 at bg_size with dissolve
    pause .03
    scene bg m_anal9_4 at bg_size with dissolve
    pause .03
    scene bg m_anal9_3 at bg_size with dissolve
    pause .03
    scene bg m_anal9_4 at bg_size with dissolve
    pause .03
    scene bg m_anal9_5 at bg_size with dissolve
    pause .03
    scene bg m_anal9_4 at bg_size with dissolve
    pause .03
    scene bg m_anal9_5 at bg_size with dissolve
    pause .03
    scene bg m_anal9_4 at bg_size with dissolve
    pause .03
    scene bg m_anal9_5 at bg_size with dissolve
    pause .03
    scene bg m_anal9_6 at bg_size with dissolve
    pause .03
    scene bg m_anal9_5 at bg_size with dissolve
    pause .03
    scene bg m_anal9_4 at bg_size with dissolve
    pause .03
    scene bg m_anal9_5 at bg_size with dissolve
    pause .03
    scene bg m_anal9_6 at bg_size with dissolve
    pause .03
    scene bg m_anal9_5 at bg_size with dissolve
    pause .03
    scene bg m_anal9_6 at bg_size with dissolve
    pause .03
    scene bg m_anal9_5 at bg_size with flash
    pause .03
    scene bg m_anal9_6 at bg_size with flash
    m "А-аах... "

    scene bg m_anal10 at bg_size with dissolve
    "[my_miku.name] оттягивает свой анус."
    m "Тут нужен твой главный инструмент, а, что думаешь?~"
    
    scene bg m_anal11 at bg_size with vpunch
    call hide_dialog
    "Твоё терпение лопается. Ты резко хватаешь [my_miku.name] за бёдра и врываешься в её тугую попку своим членом."
    m "Ааах!"
    
    scene bg m_anal12_1 at bg_size with dissolve
    pause .2
    scene bg m_anal12_2 at bg_size with dissolve
    pause .2
    scene bg m_anal12_3 at bg_size with dissolve
    pause .2
    scene bg m_anal12_2 at bg_size with dissolve
    pause .1
    scene bg m_anal12_1 at bg_size with dissolve
    pause .1
    scene bg m_anal12_2 at bg_size with dissolve
    pause .1
    scene bg m_anal12_3 at bg_size with dissolve
    pause .2
    scene bg m_anal12_2 at bg_size with dissolve
    pause .1
    scene bg m_anal12_1 at bg_size with dissolve
    pause .1
    scene bg m_anal12_2 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_2 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_2 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_2 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_4 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_2 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_4 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_4 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_4 at bg_size with dissolve
    pause .03
    scene bg m_anal12_3 at bg_size with dissolve
    pause .03
    scene bg m_anal12_4 at bg_size with flash
    call hide_dialog
    "[my_miku.name] стонет всё громче, её голос дрожит, под твоими резкими толчками."
    m "Ах! Аах! А-аах!"

    scene bg m_anal13 at bg_size with flash
    call hide_dialog
    "Ты начинаешь кончать в ее тугую попку."

    scene bg m_anal14 at bg_size with flash
    call hide_dialog

    scene bg m_anal15 at bg_size with flash
    call hide_dialog
    p "Аргх!"

    scene bg m_anal16 at bg_size with flash
    call hide_dialog
    "Ты заканчиваешь, а тело [my_miku.name] дрожит."

    scene bg m_anal17 at bg_size with dissolve
    call hide_dialog

    scene bg m_anal18 at bg_size with dissolve
    call hide_dialog
    "Ты скидываешь [my_miku.name] на кровать, из ее ануса текут струи спермы, а сама она не в силах подняться."
    p "Ну же, я уже ухожу."
    m "Аааа..."

    scene bg m_anal19 at bg_size with dissolve
    call hide_dialog
    "[my_miku.name] всё еще дрожит, не в силах подняться."
    p "Ты в порядке, [my_miku.name]?"
    m "...."
    m "Ууу... А-агаааа..."

    scene bg m_anal20 at bg_size with dissolve
    call hide_dialog
    p "Я ухожу."
    m "Так... рада... Ещё..."
    "Ты оставляешь её лежать на полу и уходишь."
    return

label m_root_fetish:
    "IN PROGRESS"
    return