
default can_work_with_holo = False
define h_can_go_root = False
define h_can_visit = True

label visit_holo:
    show h smile with dissolve
    if not h_can_go_root and h_love >= 50:
        h smile_shy "Охо-хо~, [hero_name], вижу ты разжился монетками! Я готова предложить тебе новый товар~"
        pause .5
        h smile_no_top "А точнее даже услугу~ Посмотреть не желаешь?"
        menu: 
            "Да":
                h smile_no_top "Охо-хо~, [hero_name], я в тебе не сомневалась!"
                h "Подожди тут, я подготовлюсь~"
                hide h with dissolve
                pause 1
                show h smile_naked with dissolve
                h smile_naked "Как тебе? На какую сумму оценишь?"
                p "Выше всех похвал, пол царства бы отдал!"
                h smile_naked "Охо-хо~, этой фразой ты только что обеспечил себе первую бесплатную услугу, идем~"
                call h_root_masturbate
                jump holo_menu
            "Нет":
                $h_can_visit = False
                h angry_no_top "Похоже я в тебе ошиблась, [hero_name]!"
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
                "Протереть книги(5 монет)":
                    h "Надо протереть книги! Только быстро, там уже очередь! Готов?"
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
                                "[h.name] это оценила"
                                $addLove("h",5)
                                pause 3.5
                                $addMoney(5)
                            else: 
                                h "Эх, почти успели, упустили клиента."
                        else: 
                            h "Жаль, но ничего, будут еще клиенты."
                    else: 
                        h "[hero_name], это никуда не годится, работай лучше!"
                    jump holo_menu
                "Избавиться от жуков(5 монет)":
                    h "Избавься от этих жуков, они везде!"
                    p "И как я по твоему должен от них избавиться?"
                    h "Это уже тебе решать, [hero_name]~"
                    "IN PROGRESS"
                    #call start_reaction
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
            $addLove("h",4)
            jump holo_market_menu
        "Купить [item_art_plus_size.name]([item_art_plus_size.price] монет)" if isAbleToBuy(item_art_plus_size):
            "Вы купили [item_art_plus_size.name]"
            $buyItem(item_art_plus_size)
            $addLove("h",5)
            jump holo_market_menu
        "Купить [item_dumbbells_ez.name]([item_dumbbells_ez.price] монет)" if isAbleToBuy(item_dumbbells_ez):
            "Вы купили [item_dumbbells_ez.name]"
            $buyItem(item_dumbbells_ez)
            $addLove("h",3)
            jump holo_market_menu
        "Купить [item_weight_mid.name]([item_weight_mid.price] монет)" if isAbleToBuy(item_weight_mid):
            "Вы купили [item_weight_mid.name]"
            $buyItem(item_dumbbells_ez)
            $addLove("h",4)
            jump holo_market_menu
        "Купить [item_barbell.name]([item_barbell.price] монет)" if isAbleToBuy(item_barbell):
            "Вы купили [item_barbell.name]"
            $buyItem(item_barbell)
            $addLove("h",5)
            jump holo_market_menu
        "Купить [item_book_math.name]([item_book_math.price] монет)" if isAbleToBuy(item_book_math):
            "Вы купили [item_book_math.name]"
            $buyItem(item_book_math)
            $addLove("h",3)
            jump holo_market_menu
        "Купить [item_self_study_guide.name]([item_self_study_guide.price] монет)" if isAbleToBuy(item_self_study_guide):
            "Вы купили [item_self_study_guide.name]"
            $buyItem(item_self_study_guide)
            $addLove("h",4)
            jump holo_market_menu
        "Купить [item_grimoire.name]([item_grimoire.price] монет)" if isAbleToBuy(item_grimoire):
            "Вы купили [item_grimoire.name]"
            $buyItem(item_grimoire)
            $addLove("h",5)
            jump holo_market_menu
        "Купить [item_forest_guide.name]([item_forest_guide.price] монет)" if isAbleToBuy(item_forest_guide):
            "Вы купили [item_forest_guide.name]"
            $buyItem(item_forest_guide)
            $addLove("h",5)
            jump holo_market_menu
        "Купить [item_combat_book.name]([item_combat_book.price] монет)" if isAbleToBuy(item_combat_book):
            "Вы купили [item_combat_book.name]"
            $buyItem(item_combat_book)
            $addLove("h",5)
            jump holo_market_menu
        "Уйти":
            h "Приятно было с тобой сотрудничать"
            jump holo_menu

label holo_market_root_menu:
    menu:
        "Мастурбация" if h_love >= 50:
            call h_root_masturbate
            jump holo_menu
        "Грудями" if h_love >= 60:
            call h_root_titfuck
            jump holo_menu
        "Минет" if h_love >= 70:
            call h_root_blowjob
            jump holo_menu
        "Секс" if h_love >= 80:
            call h_root_fuck
            jump holo_menu
        "Анал" if h_love >= 90:
            call h_root_anal
            jump holo_menu
        "Фетиш" if h_love >= 200:
            call h_root_fetish
            jump holo_menu
        "Вернуться":
            "Ты уходишь восстанавливать силы"
            r @smirk "До встречи~"
            jump market

label h_root_masturbate:
    scene bg holo_room with dissolve
    show h smile_shy with fade
    "[h.name] Приводит тебя к себе в комнату"
    h "Подожди тут, я переоденусь~"
    hide h with fade
    pause 1
    show h smile_no_top with fade
    p "!!!!!"
    h "Я вернулась, соскучиться успел?~"
    p "Ждал тебя с нетерпением!"
    hide h with fade
    scene bg h_masturbate1 with dissolve
    mind "[h.name] Немного нагнулась ко мне, просто стоит и смотрит... Полностью обнажённая выше пояса."  

    h "Как тебе моя грудь? Правда красивая?~"
    p "Она... великолепна..."  
    mind "Я пытаюсь удерживать взгляд, но тепло разливается по всему телу."  

    show h squeeze_breasts with dissolve  
    h "Ммм~ Смотри внимательно, ведь тебе же нравится, верно?"  
    p "Черт... Как я могу не смотреть..."  
    mind "Она слегка сжимает свою мягкую грудь, её дыхание чуть ускоряется."  

    scene bg h_m2 with dissolve  
    mind "[h.name] нагнулась чуть ближе, её глаза сверкают с хитрым огоньком."  

    h "Ты ведь уже весь горишь, да?~"  
    p "Ты просто дразнишь меня..."  
    h "Хих... А что, если да?"  

    scene bg h_m3 with dissolve  
    mind "Её пальцы медленно скользят по бедру, играя с подолом юбки..."  

    h "Ну что, терпение уже на исходе? Или ещё подождёшь?"  
    p "Ты... просто играешь со мной..."  
    h "Может быть~ Но тебе ведь нравится?"  
    
    scene bg h_m4 with dissolve  
    mind "[h.name] выпрямляется, её руки медленно скользят по бокам юбки..."  

    h "Ну? Интересно, что под ней?"  
    p "Ты... слишком хорошо знаешь, что делаешь."  
    h "Хих~ Конечно знаю."  

    scene bg h_m5 with dissolve  
    mind "Она чуть выше приподнимает юбку, и я замечаю уголок чёрных трусиков."  

    p "..."  
    h "Ты ведь не будешь смотреть просто так, верно?"  
    mind "Её голос звучит мягко, но в нём явная провокация."  

    scene bg h_m6 with dissolve  
    mind "[h.name] избавляется от юбки и медленно ползёт на кровать, опираясь на руки..."  

    h "Ну что, волк наконец раскроет свои клыки?~"  
    p "Ты действительно хочешь, чтобы я..."  
    h "А ты попробуй угадать~"  
    scene bg h_m6_2 with dissolve  
    mind "[h.name] медленно оттягивает резинку своих трусиков, позволяя мне заглянуть чуть глубже..."  

    h "Ты ведь хотел посмотреть, да?"  
    p "...Ты слишком хороша в этом."  
    h "О, я просто люблю дразнить~"  

    scene bg h_m6_3 with dissolve  
    mind "Трусики мягко облегают её упругие бёдра... Они уже кажутся лишними."  

    h "Хочешь снять их сам?"  
    p "Ты не оставляешь мне выбора..."  
    h "Хих, как будто ты сопротивлялся."  

    scene bg h_m7 with dissolve  
    mind "[h.name] медленно снимает трусики и, не стесняясь, раздвигает ножки, демонстрируя всё..."  

    h "Ну что, мой милый волчонок... Теперь ты точно не устоишь~"  
    p "..."  
    mind "Как... Как мне теперь сдержаться?" 
        
    scene bg h_m8 with dissolve  
    mind "[h.name] стоит передо мной, полностью обнажённая. Её тело освещает мягкий свет, а лёгкая ухмылка на губах только сильнее разжигает во мне желание."  

    h "Что, слов не осталось?"  
    p "Ты... Ты слишком красива."  
    h "И это всё, что ты скажешь?"  

    scene bg h_m9 with dissolve  
    mind "Она вновь опускается на четвереньки, её хвост покачивается в воздухе, а в глазах горит игривый огонёк."  

    h "Может, тебе стоит взять инициативу в свои руки?"  
    p "Ты ведь специально провоцируешь меня..."  
    h "А ты возьми и провоцируй в ответ~"  

    scene bg h_m10 with dissolve  
    mind "Внезапно её тёплое тело прижимается к моему... Её мягкая грудь, её кожа... Всё это заставляет сердце бешено колотиться."  

    h "Теперь ты точно не отвертишься."  
    p "Чёрт... [h.name]..."  
    mind "Её дыхание обжигает мою шею, а руки нежно касаются моего тела... С этого момента пути назад уже нет."  

    scene bg h_m11 with dissolve  
    mind "Мой напряжённый член оказывается прямо перед её лицом... [h.name] поднимает взгляд, её янтарные глаза впиваются в мои."  

    h "О, какой же ты нетерпеливый~"  
    p "Ты сама меня до этого довела..."  
    h "Хих... И мне это нравится."  

    scene bg h_m12 with dissolve  
    mind "Её тёплые ладони нежно обхватывают мой член... На губах играет знакомая ехидная улыбка."  

    h "Какой он горячий... Ты весь горишь, не так ли?"  
    p "Как я могу оставаться спокойным, когда ты делаешь такое?"  
    h "Ммм~ Тогда расслабься, я позабочусь о своём волчонке..."  

    scene bg h_m13 with dissolve  
    mind "Она медленно оседает на мои бёдра, удерживая мой член в руке... Её дыхание становится глубже, а хвост возбуждённо подрагивает."  

    h "Чувствуешь? Моё тело... Оно жаждет тебя."  
    p "Холо..."  
    mind "Её кожа горячая... Её взгляд полный желания... Её тело уже полностью прижалось ко мне..."  

    scene bg h_m14 with dissolve  
    mind "[h.name] начинает медленно двигаться, покачивая бёдрами... Тёплая мягкость её тела заставляет меня застыть от удовольствия."  

    h "Ммм~ Чувствуешь, как я скользю по тебе?"  
    p "Ты... ты дразнишь меня."  
    h "Конечно~ А ты разве не этого хотел?"  

    scene bg h_m15 with dissolve  
    mind "Она устраивается удобнее, выпрямляя спину... Её ладонь нежно скользит по моему члену, вызывая у меня дрожь по всему телу."  

    h "Тебе нравится, когда я так делаю?"  
    p "Как я могу ответить, когда ты так меня дразнишь..."  
    h "Хих~ Тогда позволь мне насладиться этим ещё немного."  

    scene bg h_m16 with dissolve  
    mind "Её янтарные глаза внимательно изучают мой пульсирующий член... Ракурс сменился, и теперь он кажется ещё внушительнее в её маленькой руке."  

    h "Ты такой большой... Интересно, как же ты справишься со мной?"  
    p "Ты точно хочешь это узнать?"  
    h "О, ещё как хочу~"  

    "[h.name] начинает двигать рукой вдоль твоего члена"
    scene bg h_m16_rep with dissolve  
    pause .5
    scene bg h_m16_rep2 with dissolve  
    pause .5
    scene bg h_m16_rep with dissolve  
    pause .4
    scene bg h_m16 with dissolve  
    pause .4
    scene bg h_m16_rep with dissolve  
    pause .3
    scene bg h_m16_rep2 with dissolve 
    pause .3
    scene bg h_m16_rep with dissolve  
    pause .2
    scene bg h_m16 with dissolve  
    pause .2
    scene bg h_m16_rep with dissolve 
    pause .2
    scene bg h_m16_rep2 with dissolve 
    pause .2
    scene bg h_m16_rep with dissolve 
    pause .2
    scene bg h_m16 with dissolve   
    pause .2
    scene bg h_m16_rep with dissolve 
    pause .2
    scene bg h_m16_rep2 with dissolve 

    return