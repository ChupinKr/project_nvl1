# Определение персонажей
define battle_location_market = "market"

# Объявление переменных: love – показатель симпатии, visited_market – флаг первого посещения
default first_visit_market = True

# Сцена посещения рынка
label market:
    call market_scene
    hide h
    "Вы приходите на оживлённый рынок, где запах свежего хлеба смешивается с ароматом пряностей. Люди суетятся, обсуждают цены, и всюду слышится звон монет."

    if first_visit_market and not isNight() and not isEvening():
        $ first_visit_market = False
        "Ваш взгляд привлекает прилавок с фруктами и бочонками мёда. За ним стоит девушка с лисьими ушами и пушистым хвостом."
        show h smile with dissolve

        p "!!!!!" with vpunch
        mind "У нее ушки?! Что это такое? Я в раю?"

        h "Ох-хо, кто это к нам пожаловал? Новенький, да ещё и без товарного запаса. Совсем голодранец, что ли?"
        "Её янтарные глаза хитро поблёскивают, и на губах играет самодовольная ухмылка."
        p "Эм... Я просто осматриваюсь."
        h "Осматривайся, осматривайся. Главное, чтобы не пришлось осматривать пустой кошель... Хотя, глядя на тебя, он и так пустой, верно?"
        p "..."
        h "Хех, не обижайся. Я [h.name], мудрая волчица. Но, как видишь, теперь ещё и успешная торговка."
        
        p "[h.name]? Красивое имя... Я [hero_name]."
        h "[hero_name]? Хм... не звучит богато, но я запомню. Вдруг однажды ты разбогатеешь, и я смогу на тебе нажиться, ах-хаха!"

        h "Раз уж ты здесь, позволь задать тебе пару вопросов. Мне ведь нужно знать, с кем имею дело."
        h "Начнём с простого: какую еду ты предпочитаешь?"
        $holo_choices = 0
        menu:
            h "Какую еду ты предпочитаешь?"
            "Солёное":
                h "Хм... Значит, у тебя характер крепкий, как выдержанный сыр. Это похвально!"
            "Острое":
                h "О-о, так ты любишь острые ощущения? Осторожней, иначе сожжёшь себе язык, а потом слова благодарности сказать не сможешь!"
            "Сладкое":
                $ holo_choices += 1
                h @smile_closed_eyes "О-хо-хо! Значит, ты любишь мёд и спелые яблоки? Хороший вкус, но не обольщайся — я делиться не стану!" with dissolve
        h "Теперь серьёзный вопрос. Какое качество в людях ты ценишь больше всего?"
        menu:
            h "Какое качество в людях ты ценишь больше всего?"
            "Честность":
                $ holo_choices += 1
                h @smile_closed_eyes "Честность? Ох-хо, ты что, в сказку попал? Честные торговцы встречаются только в легендах." with dissolve
            "Храбрость":
                h "Храбрый, значит? Хорошо, но помни: даже самый смелый волк не полезет в клетку к разъярённому медведю."
            "Доброта":
                h "Доброта – вещь полезная, но в торговле за неё не дают скидку. Хотя... если мне вдруг станет скучно, я дам тебе яблоко. Может быть."

        h "Последний вопрос... и, пожалуй, самый важный."  
        h "Какие женщины тебе нравятся?"  
        menu:
            h "Какие женщины тебе нравятся?" 
            "Нежные и заботливые":
                h "Хм... Значит, тебе нужны те, кто принесёт тебе кружку тёплого молока перед сном? Скучно-о!"
            "Умные, хитрые и с характером":
                $ holo_choices += 1
                h @smile_shy "О-хо-хо! Да ты разбираешься в хороших вещах, мальчишка. Может, не так уж ты и безнадёжен?" with dissolve
            "Красивые":
                h "Красота – вещь хорошая, но если за ней пустота, то и разговаривать не о чем."
        h "Вот и славно! Теперь я знаю, что передо мной не просто болван, а кое-что интересное."  
        if (holo_choices == 3):
            $my_holo.addLove(10)
            show h smile_shy with dissolve
            "[h.name] смеётся, её хвост неторопливо покачивается из стороны в сторону. Кажется, ей понравился ваш ответ."
        h smile "Может, ещё заглянешь? Кто знает, вдруг я предложу тебе выгодную сделку... или устрою тебе ещё один экзамен." with dissolve
        hide h with dissolve
        jump market_menu
    else:
        if h_can_visit and not isNight() and not isEvening():
            "Вы снова на рынке. [h.name] замечает вас и лениво махает хвостом, но сегодня не пристаёт с вопросами – видимо, её развлекло что-то другое."
        else:
            "Вы снова на рынке."
        jump market_menu


label market_menu:
    hide h with dissolve
    menu:
        "Подойти к [h.name]" if h_can_visit and not isNight() and not isEvening():
            jump visit_holo
        "Притвориться мертвым" if not canVisit("hospital") and not isNight():
            "Ты упал и притворился мертвым"
            "Вышло настолько хорошо, что тебя схватили и куда-то понесли"
            "Ты пытался вырываться и кричать, но люди думали, что ты кричишь от боли"
            "У тебя получилось убедить всех, что ты в порядке, но тебя уже принесли в больницу"
            "Тебя уже захотели избить за такое, но тебе удалось забежать в больницу"
            $updateCanVisit("hospital", True)
            $nextTime()
            jump hospital
        "Осмотреться":
            "Ты осматриваешься"
            "Это выглядит подозрительно.."
            if renpy.random.choice([False, False, True]) > 0:
                "Лучше больше так не делать, а то можно и встрять.."
            else:
                "Какой-то мутный тип подходит к тебе"
                sg "Эй, че вылупился? Зрение слишком хорошее?!"
                call start_battle(100, renpy.random.randint(40,80), "Мутный тип", battle_location_market)
                if last_battle_win and not isNight() and not isEvening():
                    "[h.name] это видела"
                    $my_holo.addLove(10)
            $nextTime()
            jump market_menu
        "Уйти":
            jump city
