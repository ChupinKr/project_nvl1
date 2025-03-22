define eris_first_time_root = True
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

        # "Выгнать дракона":
        #     eris t_neutral "Слышал про дракона в пещере? Я давно хочу зарубить что-то большое!" with dissolve
        #     p "Ты уверена? Это серьёзный противник."
        #     eris t_smirk "Уверена? Ха! Покажу ему, кто тут главный, а ты не зевай!" with dissolve
        #     if isAbleQuest(quest_eris_dragon_hunting, my_eris.love):
        #         menu:
        #             "Выгнать дракона из пещеры"
        #             "Принять квест":
        #                 eris t_smile "Отлично! Не подведи меня, [hero_name]!" with dissolve
        #                 $ getQuest(quest_eris_dragon_hunting)
        #             "Не принимать квест":
        #                 show eris t_angry with dissolve
        #                 eris "Трусишь? Ожидаемо, слабаки мне не нужны!"
        #     else:
        #         eris t_angry "Нет, ты ещё не готов. Не позорься, подкачайся сначала!" with dissolve
        #     return

        # "Свидание":
        #     p "Может, сходим прогуляться по городу? Без драк, просто вдвоём."
        #     eris t_surprised "Свидание? Ты серьёзно? Это что, шутка такая?" with dissolve
        #     if isAbleQuest(quest_eris_date, my_eris.love):
        #         menu:
        #             "Прогуляться по городу с [eris.name]"
        #             "Принять квест":
        #                 eris t_smirk_blush "Ладно, уговорил! Но если будет скучно, я тебя прикончу!" with dissolve
        #                 $ getQuest(quest_eris_date)
        #             "Не принимать квест":
        #                 eris t_smirk "Ха, знал же, что струсил! Ну и вали тогда!" with dissolve
        #     else:
        #         eris t_smirk "Ты? Со мной? Не смеши, сначала докажи, что достоин!" with dissolve
        #     return

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
        "Минет" if :
            "IN PROGRESS"
        "Делать котят2":
            "IN PROGRESS"
        "Делать котят3":
            "IN PROGRESS"
        "Передумал":
            eris transparent_annoyed "Да и мне не очень то хотелось!" with dissolve
    return

