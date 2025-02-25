# Флаг для возможности обращаться к богине
default can_talk_to_freya = False

label ruined_temple:
    call ruined_temple_scene from _call_ruined_temple_scene
    pause 1.0

    "Ты у входа в разрушенный храм… колонны в трещинах, повсюду мох и заросли. Слева густой лес, а справа виднеется город."
    jump ruined_temple_menu

label ruined_temple_menu:
    menu:
        "Обратиться к богине за советом" if not can_see_info_panel:
            jump talk_to_freya
        "Осмотреться":
            "Ты ничего не находишь"
            "IN PROGRESS"
            jump ruined_temple_menu
        "Пройти в лес":
            jump forest


