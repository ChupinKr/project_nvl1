define first_time_guild = True
define battle_location_guild = "guild"
label guild:
    scene bg guild with fade

    if first_time_guild:
        $first_time_guild = False
        "IN PROGRESS *Большое описание гильдии бойцов*"
        "IN PROGRESS *Диалог с Нагаторо*"
        "IN PROGRESS *Знакомство с наставницей*"
    "Ты в гильдии"
    jump guild_menu

label guild_menu:
    menu:
        "Тренироваться в спарринге":
            call start_battle(100, strength, "Противник", battle_location_training_ground)
            if last_battle_win:
                "Я определенно становлюсь все лучше!"
                $addChar(["str"], 3)
                jump guild_menu
            else:
                "Надо больше заниматься"
                jump guild_menu
        "Качаться":
            call start_muscule
            if last_muscule_win:
                "Я определенно становлюсь все лучше!"
                $addChar(["str"], 2)
                jump guild_menu
            else:
                "Надо больше заниматься"
                jump guild_menu
        "Найти наставницу":
            jump training_ground_look_around
        "Отправиться в город":
            jump city

label guild_look_around:
    "Ты осматриваешься..."
    "IN PROGRESS"
    jump guild_menu
    # menu:
    #     "Навестить [.name]" if not first_time_rapunzel:
    #         jump visit_rapunzel_forest
    #     "Навестить [e.name]" if not first_time_elsa:
    #         jump visit_elsa_forest
    #     "Навестить [nag.name]" if not first_time_nagatoro:
    #         jump visit_nagatoro_forest
    #     "Вернуться назад":
    #         jump forest
