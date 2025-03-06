define first_time_training_ground = True
define battle_location_training_ground = "training_ground"
define eris_first_time_root = True

label training_ground:
    call training_ground_scene

    if first_time_training_ground and isMorning():
        $ first_time_training_ground = False
        "Ты попадаешь на тренировочную площадку — просторную открытую зону, где собрались бойцы разного уровня. Кто-то молотит деревянные манекены, кто-то спаррингует, а кто-то отдыхает, потирая синяки."
        "Воздух звенит от ударов, выкриков и хриплого дыхания. Пахнет землёй, потом и чуть-чуть кровью. Вдалеке виднеются стойки с оружием: деревянные мечи, копья, тренировочные топоры."

        "Ты осматриваешься, когда вдруг замечаешь кое-что необычное."
        "В углу площадки стоит девушка с огненно-рыжими волосами, сжимающая деревянный меч. Она с бешеной скоростью и яростью рубит манекен, оставляя на нём глубокие вмятины."
        
        "Поглощённая тренировкой, она словно не видит ничего вокруг."

        show eris t_neutral with dissolve
        "Но в один момент её резкий удар срывает манекен с подставки... и он летит прямо в тебя!"

        menu:
            "Манекен летит прямо на тебя!"
            "Попытаться увернуться":
                if strength > 20:
                    "Ты мгновенно отступаешь в сторону, и манекен с глухим стуком падает рядом."
                    show eris t_surprised with dissolve
                    eris "Ого! Да ты шустрый!"
                else:
                    "Ты не успеваешь среагировать, и манекен сшибает тебя с ног, придавливая к земле."
                    show eris t_smirk with dissolve
                    eris "Ха! Не можешь даже от манекена уйти? Что ты вообще тут делаешь?"

            "Попытаться остановить манекен":
                if strength > 30:
                    "Ты выставляешь руки и ловишь манекен, удерживая его на весу. Тяжело, но ты справляешься."
                    show eris t_surprised with dissolve
                    eris "О! Да ты не слабак, оказывается!"
                else:
                    "Ты пытаешься поймать манекен, но он сносит тебя с ног, и ты падаешь на спину."
                    show eris t_smirk with dissolve
                    eris "Ха! Переоценил себя, да?"

            "Не двигаться":
                "Ты стоишь как вкопанный, надеясь, что обойдётся."
                "Зря. Манекен сбивает тебя с ног, и ты грохаешься на землю."
                show eris t_smirk with dissolve
                eris "Пф! Даже не шевельнулся? Ты кто вообще такой?"

        "Девушка наконец замечает тебя и подходит, небрежно закинув меч на плечо."
        show eris t_neutral with dissolve
        eris "Чего ты тут торчишь, как столб? Не тренируешься — вали с площадки!"

        p "Эм... я только пришёл. Осматриваю место."
        show eris t_smirk with dissolve
        eris "Осматриваешь? Пфф! Бойцы не глазеют — они бьют!"
        "Она резко тычет мечом в сторону кучи деревянного оружия."
        eris "Бери что-нибудь и покажи, на что годишься!"

        menu:
            eris "Бери что-нибудь и докажи, что не зря сюда припёрся!"
            "Взять деревянный меч":
                "Ты берёшь деревянный меч и встаёшь в стойку."
                show eris t_smirk with dissolve
                eris "Ха! Ну, попробуй хотя бы ударить нормально!"

                "[eris.name] бросается на тебя с резким выпадом!"

                call start_battle(120, eris_str, eris.name, battle_location_training_ground)
                
                if last_battle_win:
                    "Ты успеваешь отбить её удар и даже немного теснишь её назад."
                    show eris t_smile with dissolve
                    eris "Ого! Да ты не совсем бесполезный!"
                    "Она кивает с одобрением, опуская меч."
                    $my_eris.addLove(10)
                else:
                    "Ты не успеваешь среагировать, и её удар валит тебя с ног."
                    show eris t_angry with dissolve
                    eris "Фу, скукота какая!"
                show eris t_smile with dissolve
                eris "Захочешь ещё разок — ищи меня тут по утрам."
                $nextTime()

            "Отказаться":
                p "Знаешь, я пока не готов драться."
                show eris t_angry with dissolve
                eris "Не готов? Что значит 'не готов'? Это же тренировка, а не прогулка! Трус, что ли?"
                "Она фыркает и отворачивается к манекену."
                show eris t_angry with dissolve
                eris "Передумаешь — я тут по утрам. Не мешай."
                $nextTime()

        "Ты понимаешь, что эта девушка — сущий вихрь. Тренировки с ней точно будут не из лёгких."

    "Ты на тренировочной площадке в городе."
    jump training_ground_menu

label training_ground_menu:
    hide eris
    menu:
        "Качаться":
            call start_muscule("Подход", 2.3)
            if last_muscule_win:
                call start_muscule("Подход", 2.5)
                if last_muscule_win:
                    call start_muscule("Ещё подход", 2.7)
                    if last_muscule_win:
                        call start_muscule("Сотру со лба я лёгкий пот", 2.7)
                        if last_muscule_win:
                            "Я явно становлюсь лучше!"
                            $addChar(["str"], 2)
            $nextTime()
            "Надо больше тренироваться."
            jump training_ground_menu
        "Подойти к [eris.name]" if isMorning():
            "Ты подходишь к [eris.name]."
            jump training_ground_eris_menu
        "Отправиться в город":
            jump city

label training_ground_eris_menu:
    show eris t_neutral with dissolve
    menu:
        "Спарринг":
            call start_battle(120, eris_str, eris.name, battle_location_training_ground)
            if last_battle_win:
                "IN PROGRESS"
                $addChar(["str"], 2)
                $my_eris.addLove(5)
                $my_eris.addNPCStr(10)
            else:
                "IN PROGRESS"
            $nextTime()
            jump training_ground_menu
        "Сделать котят" if not eris_first_time_root:
            eris t_smirk_blush "Так не терпится?" with dissolve
            call eris_root
            $nextTime()
            jump tavern
        "Пойти на задание вдвоём":
            if isNoQuestNow() and (my_eris.love >= 40 or charisma >= 50):
                eris "Отличная мысль! Выбирай, что будем делать!"
                call eris_quest_menu
            else:
                eris t_angry "Нет, я тебе не доверяю, может быть потом!" with dissolve
            jump training_ground_eris_menu
        "Вернуться":
            jump training_ground

label eris_quest_menu:
    show eris t_smile with dissolve
    menu:
        "Охота на гоблинов":
            p "Готов поохотиться на гоблинов вместе?"
            eris t_neutral "Гоблины — мелочь, но их слишком много. Надо их проредить, пока не полезли к людям." with dissolve
            if isAbleQuest(quest_eris_goblin_hunting, my_eris.love):
                menu:
                    "Охота на гоблинов в лесной чаще"
                    "Принять квест":
                        eris t_smirk "Вот это настрой! Бери меч и не отставай!" with dissolve
                        $ getQuest(quest_eris_goblin_hunting)
                    "Не принимать квест":
                        eris t_angry "Что, кишка тонка? Ну и ладно, сам справлюсь!" with dissolve
            else:
                eris t_smirk "Ха, да ты пока слабак для такого. Приходи, когда подкачаешься!" with dissolve
            return

        "Выгнать дракона":
            eris t_neutral "Слышал про дракона в пещере? Я давно хочу зарубить что-то большое!" with dissolve
            p "Ты уверена? Это серьёзный противник."
            eris t_smirk "Уверена? Ха! Покажу ему, кто тут главный, а ты не зевай!" with dissolve
            if isAbleQuest(quest_eris_dragon_hunting, my_eris.love):
                menu:
                    "Выгнать дракона из пещеры"
                    "Принять квест":
                        eris t_smile "Отлично! Не подведи меня, [hero_name]!" with dissolve
                        $ getQuest(quest_eris_dragon_hunting)
                    "Не принимать квест":
                        show eris t_angry with dissolve
                        eris "Трусишь? Ожидаемо, слабаки мне не нужны!"
            else:
                eris t_angry "Нет, ты ещё не готов. Не позорься, подкачайся сначала!" with dissolve
            return

        "Свидание":
            p "Может, сходим прогуляться по городу? Без драк, просто вдвоём."
            eris t_surprised "Свидание? Ты серьёзно? Это что, шутка такая?" with dissolve
            if isAbleQuest(quest_eris_date, my_eris.love):
                menu:
                    "Прогуляться по городу с [eris.name]"
                    "Принять квест":
                        eris t_smirk_blush "Ладно, уговорил! Но если будет скучно, я тебя прикончу!" with dissolve
                        $ getQuest(quest_eris_date)
                    "Не принимать квест":
                        eris t_smirk "Ха, знал же, что струсил! Ну и вали тогда!" with dissolve
            else:
                eris t_smirk "Ты? Со мной? Не смеши, сначала докажи, что достоин!" with dissolve
            return

        "Я передумал":
            eris t_angry "Серьёзно? Зря время тратил, уходи!" with dissolve
            return
    return

label eris_root:
    "Вы идете к [eris.name] домой, это небольшая комната в таверне"
    scene bg eris_room with fade
    "Подожди минутку, я подготовлюсь"
    "..."
    "....."
    "......."
    show eris transparent_shy with dissolve
    call eris_root_menu
    return

label eris_root_menu:
    menu:
        "Делать котят":
            "IN PROGRESS"
        "Делать котят2":
            "IN PROGRESS"
        "Делать котят3":
            "IN PROGRESS"
        "Передумал":
            eris transparent_annoyed "Да и мне не очень то хотелось!" with dissolve
    return

