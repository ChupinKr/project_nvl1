# Флаг для возможности обращаться к богине
default can_talk_to_freya = False

label ruined_temple:
    scene bg ruined_temple with fade
    pause 1.0

    "Ты у входа в разрушенный храм… колонны в трещинах, повсюду мох и заросли. Слева густой лес, а справа виднеется город."
    jump ruined_temple_menu

label ruined_temple_menu:
    menu:
        "Обратиться к богине за советом" if not can_see_info_panel:
            jump talk_to_freya
        "Пройти в лес":
            jump forest
        "Осмотреться":
            "Ты ничего не находишь"
            "IN PROGRESS"
            jump ruined_temple_menu


