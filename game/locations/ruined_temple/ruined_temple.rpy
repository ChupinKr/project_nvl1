# Флаги встреченных девушек
default first_time_rapunzel = True
default first_time_elsa = True
default first_time_esdeath = True
default first_time_ruined_temple = True

# Флаг для возможности обращаться к богине
default can_talk_to_freya = False

label ruined_temple:
    show screen buttons
    scene bg_ruined_temple with fade
    pause 1.0

    "Разрушенный храм… колонны в трещинах, повсюду мох и заросли, сквозь дыры в крыше пробиваются лучи солнца."

    if charisma > 0 and first_time_rapunzel:
        jump visit_rapunzel_ruined_temple
    elif mana > 0 and first_time_elsa:
        jump visit_elsa_ruined_temple
    elif strength > 0 and first_time_esdeath:
        jump visit_esdeath_ruined_temple
    elif first_time_ruined_temple:
        "Похоже, тебе придётся самому искать путь…"
        $ first_time_ruined_temple = False
    else:
        "Куда направишься?"
        
    jump ruined_temple_menu

label ruined_temple_menu:
    menu:
        "Обратиться к богине за советом" if (charisma > 10):
            jump talk_to_freya
        "Отправиться в город":
            jump city
        "Попробовать пройти в лес чудовищ":
            jump monster_forest
        "Осмотреться вокруг" if not first_time_rapunzel or not first_time_elsa or not first_time_esdeath:
            jump look_around

label look_around:
    "Ты осматриваешься..."
    menu:
        "Навестить Рапунцель" if not first_time_rapunzel:
            jump visit_rapunzel_ruined_temple
        "Навестить Эльзу" if not first_time_elsa:
            jump visit_elsa_ruined_temple
        "Навестить Эсдес" if not first_time_esdeath:
            jump visit_esdeath_ruined_temple
        "Вернуться назад":
            jump ruined_temple



