# Поиск Эльзы (всегда успешно) с меню взаимодействий
label find_elsa:
    scene bg tower_training with fade
    show e neutral at center with dissolve

    "Я нашёл Эльзу в тренировочном зале. "
    "Она как раз заканчивала очередное упражнение, заставляя ледяные копья исчезать в воздухе."

    show e smirk with dissolve
    e "Решил проверить, насколько ты жалок сегодня?"
    jump find_elsa_menu

label find_elsa_menu:
    show e smile with dissolve
    menu:
        "Потренироваться с ней":
            show e smile with dissolve
            "[e.name] начала тренировку, и я попытался повторять её движения..."
            p "[e.name], ты говорила, что можешь меня потренировать."
            e smirk "Хорошо. Ты должен почувствовать, тот момент, когда твоя энергия доходит до пика и выплеснуть всё~" with dissolve
            show e smile at right with fade
            call start_magic_training(intelligence)
            if last_reaction_win:
                $addChar(["intelligence"], 3)
                jump win_elsa_training
            else:
                jump fail_elsa_training
            jump find_elsa_menu
        "Попросить квест" if isNoQuestNow():
            show e neutral with dissolve
            e "Квест? Есть пара дел, но предупреждаю – они тебе вряд ли понравятся." with dissolve
            call elsa_quests_magic_tower
            jump find_elsa_menu
        "Отказаться от квеста" if isActualQuestOfCharacter("e"):
            p "Я откажусь от выполнения квеста."
            e smile "Ничего страшного, но если передумаешь - приходи!" with dissolve
            $ removeQuest()
            jump find_elsa_menu
        "Уйти":
            "Я решил оставить Эльзу в покое и не мешать её тренировке."
            jump magic_tower_hub

label elsa_quests_magic_tower:
    menu:
        "Собирать магические материалы":
            p "Я готов собирать магические материалы."
            e "Хорошо, мне нужно несколько редких трав и минералов. Ты можешь найти их в этих лесах."
            $ getQuest(quest_elsa_materials)
        "Стать испытуемым":
            p "Я готов стать подпытным кроликом."
            e "Я вижу, что ты довольно крепкий, если у тебя все еще хватает ума заходить в этот лес."
            e "Твоё тело мне пригодится~"
            $ getQuest(quest_elsa_test)
            call elsa_test
        "Я передумал":
            return
    return

label win_elsa_training:
    show e smile at center with dissolve
    e "Вау, да у тебя талант!"
    p "Надо будет повторить, мне понравилось."
    e @smile_shy "Мне тоже~~"
    $addLove("e", 5)
    jump find_elsa_menu

label fail_elsa_training:
    show e laugh at center with dissolve
    e "Это потрясающе!"
    p "Что? У меня же не вышло."
    e "Да, меня потрясло то, насколько ты необучаем."
    jump find_elsa_menu