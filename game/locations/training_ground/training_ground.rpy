define first_time_training_ground = True
define battle_location_training_ground = "training_ground"
label training_ground:
    scene bg training_ground with fade

    if first_time_training_ground:
        $ first_time_training_ground = False
        "IN PROGRESS *Большое описание тренировочной площадки*"
    "Ты на тренировочной площадке в городе"
    jump training_ground_menu

label training_ground_menu:
    menu:
        "Качаться":
            call start_muscule
            if last_muscule_win:
                "Я определенно становлюсь все лучше!"
                $addChar(["str"], 2)
                jump training_ground_menu
            else:
                "Надо больше заниматься"
                jump training_ground_menu
        "Осмотреться вокруг":
            jump training_ground_look_around
        "Отправиться в город":
            jump city

label training_ground_look_around:
    "Ты осматриваешься..."
    "IN PROGRESS"
    jump training_ground_menu
    # menu:
    #     "Навестить [.name]" if not first_time_rapunzel:
    #         jump visit_rapunzel_forest
    #     "Навестить [e.name]" if not first_time_elsa:
    #         jump visit_elsa_forest
    #     "Навестить [nag.name]" if not first_time_nagatoro:
    #         jump visit_nagatoro_forest
    #     "Вернуться назад":
    #         jump forest
