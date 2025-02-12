# Флаги встреченных девушек
default first_time_rapunzel = True
default first_time_elsa = True
default first_time_nagatoro = True
default can_see_info_panel = False

# Флаг для возможности обращаться к богине
default can_talk_to_freya = False

label ruined_temple:
    scene bg ruined_temple with fade
    pause 1.0

    "Ты у входа в разрушенный храм… колонны в трещинах, повсюду мох и заросли. Слева густой лес, а справа виднеется город."

    if charisma > 0 and first_time_rapunzel:
        jump visit_rapunzel_ruined_temple
    elif mana > 0 and first_time_elsa:
        jump visit_elsa_ruined_temple
    elif strength > 0 and first_time_nagatoro:
        jump visit_nagatoro_ruined_temple
    else:
        "Куда направишься?"

    jump ruined_temple_menu

label ruined_temple_menu:
    menu:
        "Обратиться к богине за советом" if not can_see_info_panel:
            jump talk_to_freya
        "Отправиться в город":
            jump city
        "Попробовать пройти в лес чудовищ":
            jump monster_forest
        "Осмотреться вокруг" if not first_time_rapunzel or not first_time_elsa or not first_time_nagatoro:
            jump look_around

label look_around:
    "Ты осматриваешься..."
    menu:
        "Навестить [r.name]" if not first_time_rapunzel:
            jump visit_rapunzel_ruined_temple
        "Навестить [e.name]" if not first_time_elsa:
            jump visit_elsa_ruined_temple
        "Навестить [nag.name]" if not first_time_nagatoro:
            jump visit_nagatoro_ruined_temple
        "Вернуться назад":
            jump ruined_temple



