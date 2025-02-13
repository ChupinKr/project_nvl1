# Флаги встреченных девушек
default first_time_rapunzel = True
default first_time_elsa = True
default first_time_nagatoro = True
default can_see_info_panel = False

default first_time_forest = True  
#Суйка из геройской академии

label forest:
    scene bg forest with fade

    "Ты заходишь в лес"
    
    if charisma > 0 and first_time_rapunzel:
        jump visit_rapunzel_forest
    elif mana > 0 and first_time_elsa:
        jump visit_elsa_forest
    elif strength > 0 and first_time_nagatoro:
        jump visit_nagatoro_forest
    else:
        "Куда направишься?"

    jump forest_menu

label forest_menu:
    menu:
        "Отправиться в город":
            jump city
        "Посетить руины храма":
            jump ruined_temple
        "Осмотреться вокруг" if not first_time_rapunzel or not first_time_elsa or not first_time_nagatoro:
            jump look_around

label look_around:
    "Ты осматриваешься..."
    menu:
        "Навестить [r.name]" if not first_time_rapunzel:
            jump visit_rapunzel_forest
        "Навестить [e.name]" if not first_time_elsa:
            jump visit_elsa_forest
        "Навестить [nag.name]" if not first_time_nagatoro:
            jump visit_nagatoro_forest
        "Вернуться назад":
            jump forest