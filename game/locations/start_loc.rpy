
label f_get_info:
    hide ls_sphere
    hide str_sphere
    hide mc_sphere

    show f smile with dissolve
    f "Я могу даровать тебе одно из трёх благословений, которые изменят твою судьбу."

    "Она сделала лёгкий жест рукой, и перед тобой возникли три сияющих символа, как если бы сама реальность зависела от твоего выбора."
    hide f smile with dissolve

    show str_sphere at mid_left with dissolve
    f "Первое благословение — Дар Выносливости. "
    f "На первый взгляд, это может показаться не таким уж впечатляющим, но это лишь начало. "
    f "Ты будешь выносливым, как никогда, сможешь легко преодолевать физические трудности и восстанавливать силы быстрее, чем обычные смертные. "
    f "Но это только потенциал, и для того, чтобы раскрыть его полностью, тебе нужно будет тренироваться и развиваться."

    show mc_sphere at mid_mid with dissolve
    f "Второе благословение — Дар Магического Потенциала. "
    f "В самом начале ты будешь лишь на пороге магии, с небольшими способностями, но со временем ты сможешь развить их в невероятную силу. "
    f "Ты будешь учиться магии, открывать новые заклинания, но всё это потребует усилий и времени. "
    f "Ты начнёшь как ученик, но в будущем твои способности будут потрясающими."

    show ls_sphere at mid_right with dissolve
    f "И, наконец, третье — Дар Соблазнителя. "
    f "О, этот дар тоже не даст тебе всего сразу. "
    f "Ты будешь обладать базовыми умениями манипулировать эмоциями и желаниями других, но на этом всё не заканчивается. "
    f "Со временем ты научишься использовать этот дар всё более искусно, и тогда начнётся настоящее волшебство. "
    f smile "Помни, чем сильнее ты будешь в этом искусстве, тем больше соблазнительных возможностей откроется для тебя."

    "Она смотрела на тебя, её взгляд был одновременно игривым и загадочным, как будто она уже знала твой выбор. "
    "С её улыбкой было сложно быть уверенным в своём решении."

    f @ closed_smile "Обдумай всё, ведь от твоего выбора зависит то, каким ты станешь в этом новом мире."
    return

label f_ask_more_info:
    hide ls_sphere
    hide str_sphere
    hide mc_sphere
    show f smile with dissolve
    f "Ты хочешь узнать больше? Ну, это вполне естественно. Хорошо, я расскажу тебе немного о каждом из благословений, чтобы твой выбор был осознанным."

    call f_get_info 
    jump start_ask_god

label start_ask_god:
    menu:
        "Принять одно из благословений.":
            jump blessings_choice
        "Попытаться уговорить богиню дать больше информации.":
            call f_ask_more_info
        "Отказаться":
            jump refuse

label refuse:
    "Ты решаешь отказаться от благословений и от всего, что она предлагает. В этот момент пространство вокруг тебя начинает меркнуть, и ты чувствуешь, как теряешь сознание..."
    #TODO Тогда я превращаю тебя в слизь
    $ chosen_blessing = available_blessings[3]
    show screen daytime
    jump forest
    return

label blessings_choice:
    menu:
        "Выбрать Дар Выносливости":
            $ chosen_blessing = available_blessings[0]
            $ strength = strength + 2
            $ strength_mod = 2
            hide ls_sphere
            hide str_sphere
            hide mc_sphere
            show f smile with dissolve
            f "Ты выбрал благословение [chosen_blessing.name]. Мне любопытно, как ты распорядишься моим подарком. Ты ведь понимаешь, что это только начало?"
        "Выбрать Магический Потенциал":
            $ chosen_blessing = available_blessings[1]
            $ intelligence = intelligence + 2
            $ intelligence_mod = 2
            hide ls_sphere
            hide str_sphere
            hide mc_sphere
            show f smile with dissolve
            f "Ты выбрал благословение [chosen_blessing.name]. Этот дар не сделает тебя всемогущим, но... если ты будешь мудр, он приведёт тебя к величию."
        "Выбрать Дар Соблазнителя":
            $ chosen_blessing = available_blessings[2]
            $ charisma = charisma + 2
            $ charisma_mod = 2
            hide ls_sphere
            hide str_sphere
            hide mc_sphere
            show f smile_shy with dissolve
            f "Ты выбрал благословение [chosen_blessing.name]. Ты нравишься мне, [hero_name]… иначе я бы не выбрала тебя."
        "Подожди":
            p "Подожди, дай мне еще подумать."
            f @smile_shy_hold "Не хочешь уходить от меня?"
            jump start_ask_god
    # Вспышка света, переход к перерождению
    scene bg haven_bright1 with dissolve
    scene bg haven_bright2 with dissolve
    scene bg haven_bright3 with dissolve
    pause 1.0

    "Ну что ж... Пришло время отправить тебя в новый мир."

    "Открой глаза… и начни свой путь."

    # Переход в новый мир
    "Ты открываешь глаза и осознаёшь, что лежишь на прохладной траве, где ты?"
    show screen daytime
    jump forest
    