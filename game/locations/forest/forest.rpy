# Флаги встреченных девушек
default first_time_rapunzel = True
default first_time_elsa = True
default first_time_nagatoro = True
default can_see_info_panel = False

default first_time_forest = True  
#Суйка из геройской академии

label forest:
    scene bg forest with fade
    
    if charisma > 1 and first_time_rapunzel:
        jump visit_rapunzel_forest
    elif mana > 1 and first_time_elsa:
        jump visit_elsa_forest
    elif strength > 1 and first_time_nagatoro:
        jump visit_nagatoro_forest
    else:
        "Ты заходишь в лес"
        "Куда направишься?"

    jump forest_menu

label forest_menu:
    menu:
        "Посетить руины храма":
            jump ruined_temple
        "Осмотреться вокруг" if not first_time_rapunzel or not first_time_elsa or not first_time_nagatoro:
            jump look_around
        "Искать неприятности" if strength > 10:
            jump look_for_enemy
        "Отправиться в город":
            jump city

label look_around:
    "Ты осматриваешься..."
    menu:
        "Навестить [r.name]" if not first_time_rapunzel and can_go_r:
            jump visit_rapunzel_forest
        "Навестить [e.name]" if not first_time_elsa:
            jump visit_elsa_forest
        "Навестить [nag.name]" if not first_time_nagatoro:
            jump visit_nagatoro_forest
        "Вернуться назад":
            jump forest

label look_for_enemy:
    "Ты заходишь чуть глубже в лес, отходишь от протоптанной тропинки"
    $rand_emeny = renpy.random.randint(1, 100) 
    if rand_emeny < 20:
        "Ты видишь зайца с рогом, от тебя еще не видит, что будешь делать?"
        menu:
            "Напасть":
                call start_battle(60, renpy.random.randint(1, 30) , "Заяц", 'return_to_this')
                if last_battle_win:
                    "Ты прибил бедного зайку, тебе должно быть стыдно"
                    $ addChar(["str"],1)
                    jump forest_menu
            "Уйти":
                jump forest_menu
    if rand_emeny >= 20 and rand_emeny < 40:
        "Ты видишь большого и красивого оленя, кажется он уже доедает зайца?!"
        "Он тебя еще не видит, что будешь делать?"
        menu:
            "Напасть":
                call start_battle(100, renpy.random.randint(30, 50) , "Плотоядный олень", 'return_to_this')
                if last_battle_win:
                    "Охота на оленя без оружия, неплохо, я справляюсь"
                    $ addChar(["str"],2)
                    jump forest_menu
            "Уйти":
                jump forest_menu
    if rand_emeny >= 40 and rand_emeny < 60:
        "Ты видидишь кабана, он сразу замечает тебя и бежит в твою сторону!"
        call start_battle(150, renpy.random.randint(40, 80) , "Дикий кабан", 'return_to_this')
        if last_battle_win:
            "Справился с диким кабаном, это успех!"
            $ addChar(["str"],3)
            jump forest_menu
    if rand_emeny >= 60 and rand_emeny < 80:
        "Ты видидишь волка, он сразу замечает тебя и набрасывается!"
        call start_battle(60, renpy.random.randint(90, 120) , "Волк", 'return_to_this')
        if last_battle_win:
            "Мне повезло справиться с волком Или я уже настолко силен?"
            $ addChar(["str"],4)
            jump forest_menu
    if rand_emeny >= 80 and rand_emeny < 100:
        "Ты видидишь медведя, он моментально тебя замечает, спрятаться и убежать не выйдет!"
        call start_battle(200, renpy.random.randint(120, 160) , "Бурый медведь", 'return_to_this')
        if last_battle_win:
            "Это было очень опасно, хорошо, что я справился!"
            $ addChar(["str"],5)
            jump forest_menu