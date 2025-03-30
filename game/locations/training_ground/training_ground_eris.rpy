define eris_first_time_root = True
label training_ground_eris_menu:
    show eris t_neutral with dissolve
    menu:
        "Спарринг":
            call start_battle(120, my_eris_str, eris.name, battle_location_training_ground)
            if last_battle_win:
                "IN PROGRESS"
                $addChar(["str"], 5)
                $addLove(my_eris,7)
                $addNPCStr(my_eris,10)
            else:
                "IN PROGRESS"
            $nextTime()
            jump training_ground_menu
        "Сделать котят" if not eris_first_time_root:
            eris t_smirk_blush "Так не терпится?" with dissolve
            call eris_root
            $nextTime()
            "Ты выходишь из комнаты [my_eris.name]"
            jump tavern
        "Пойти на задание вдвоём" if isNoQuestNow():
            if isNoQuestNow() and (my_eris_love >= 40 or charisma >= 50):
                eris "Отличная мысль! Выбирай, что будем делать!"
                call eris_quests_menu
            else:
                eris t_angry "Нет, я тебе не доверяю, может быть потом!" with dissolve
            jump training_ground_eris_menu
        "Отказаться от квеста" if isActualQuestOfCharacter("eris"):
            p "Я откажусь от выполнения квеста."
            eris t_angry "Большего и не ожидала!" with dissolve
            $ removeQuest()
            jump training_ground_eris_menu
        "Вернуться":
            jump training_ground

label eris_quests_menu:
    show eris t_smile with dissolve
    menu:
        "Охота на гоблинов":
            p "Ты готова поохотиться на гоблинов вместе?"
            eris t_neutral "Гоблины — мелочь, но их слишком много. Надо их проредить, пока не полезли к людям." with dissolve
            if isAbleQuest(quest_eris_goblin_hunting, my_eris_love):
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
            if isAbleQuest(quest_eris_dragon_hunting, my_eris_love):
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
            if isAbleQuest(quest_eris_date, my_eris_love):
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
    scene bg eris_room at bg_size with fade
    "Подожди минутку, я подготовлюсь"
    "..."
    "....."
    "......."
    show eris transparent_shy with dissolve
    call eris_root_menu
    return

label eris_root_menu:
    menu:
        "Минет" if isQuestCompleted(quest_eris_goblin_hunting):
            show eris smile_naked_cover with dissolve
            "[my_eris.name] сбрасывает с себя одежду и встает на колени перед тобой, прижимаясь к тебе своей грудью."
            call eris_root_blowjob
            "[my_eris.name] поднимается."
            scene bg eris_room at bg_size with fade
            show eris angry_naked_cummed_cover with dissolve
            eris "Знаешь, [hero_name], мог бы и предупредить о таком."
            mind "Мне надо бежать, пока не получил."
        "Внучную" if isQuestCompleted(quest_eris_dragon_hunting):
            call eris_root_handjob
            scene bg eris_room at bg_size with fade
            show eris transparent_smile with dissolve
            "Довольная собой [my_eris.name] проводит тебя до выхода."
            eris "Еще увидимся, [hero_name]~"
        "Сделать котят" if isQuestCompleted(quest_eris_date):
            call eris_root_vaginal
            "[my_eris.name] лежит без сил. Ты уходишь."
        "Передумал":
            eris transparent_annoyed "Да и мне не очень то хотелось!" with dissolve
            "Ты уходишь."
    return



label eris_root_handjob:
    $ eris_first_time_root = False
    "[eris.name] садит тебя на кровать и встает перед тобой в полупрозрачной белой ночнушке."
    scene bg eris_root_handjob1 at bg_size with fade
    "Она слегка приподнимает итак полупрозрачную сорочку, показывая свои белые кружевные трусики."
    p "..."
    scene bg eris_root_handjob2 at bg_size with dissolve
    "[eris.name] смущается и слегка поворачивается к тебе боком."

    scene bg eris_root_handjob2_say at bg_size with dissolve
    eris "Тебе нравится, [hero_name]?"

    scene bg eris_root_handjob2 at bg_size with dissolve
    p "Да, ты выглядишь потрясающе."

    scene bg eris_root_handjob2_smile at bg_size with dissolve
    "[eris.name] явно рада тому, что тебе нравится ее наряд."

    scene bg eris_root_handjob3 at bg_size with fade
    "Она садится перед тобой на колени, готовясь к тому, что увидит."

    scene bg eris_root_handjob3_say at bg_size with dissolve
    eris "Д-доставай его!"
    p "Как прикажешь."

    scene bg eris_root_handjob4_1 at bg_size with dissolve
    pause .3
    scene bg eris_root_handjob4_2 at bg_size with dissolve
    eris "Ииик!"
    p "Что? Уже передумала?"

    scene bg eris_root_handjob4_3 at bg_size with dissolve
    eris "..."

    scene bg eris_root_handjob5 at bg_size with dissolve
    "[eris.name] быстро берет себя в руки и хватает твой член."

    scene bg eris_root_handjob5_say at bg_size with dissolve
    eris "Ты получишь свою награду, [hero_name]."

    scene bg eris_root_handjob5 at bg_size with dissolve
    "[eris.name] начинает поглаживать твой член."

    scene bg eris_root_handjob6_1 at bg_size with fade
    pause .3
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .3
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .3
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .3
    scene bg eris_root_handjob6_1 at bg_size with dissolve
    eris "Мне продолжать?~"
    p "Только не останавливайся."

    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .2
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_handjob6_1 at bg_size with dissolve
    pause .2
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_handjob6_4 at bg_size with flash
    p "Аргх!"

    scene bg eris_root_handjob7_1 at bg_size with flash
    eris "Ммм."

    scene bg eris_root_handjob7_2 at bg_size with flash
    eris "Аааа..."

    scene bg eris_root_handjob7_3 at bg_size with flash
    "[eris.name] открыла свой ротик и ловит сперму."

    scene bg eris_root_handjob7_4 at bg_size with dissolve
    "Ты покрываешь всё лицо [eris.name] спермой."

    scene bg eris_root_handjob7_5 at bg_size with dissolve
    eris "*сглатывает*"

    scene bg eris_root_handjob7_6 at bg_size with dissolve
    "[eris.name] с ухмылкой смотрит на тебя."

    scene bg eris_root_handjob8 at bg_size with dissolve
    eris "Спасибо за угощение~"
    
    return