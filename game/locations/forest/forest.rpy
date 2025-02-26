# Флаги встреченных девушек
default first_time_rapunzel = True
default first_time_elsa = True
default first_time_nagatoro = True
default can_see_info_panel = False

default first_time_forest = True  
#Суйка из геройской академии

label forest:
    call forest_scene 
    
    if charisma > 1 and first_time_rapunzel:
        jump visit_rapunzel_forest
    elif intelligence > 1 and first_time_elsa:
        jump visit_elsa_forest
    elif strength > 1 and first_time_nagatoro:
        jump visit_nagatoro_forest
    else:
        "Ты в лесу"
        "Куда направишься?"
        
    jump forest_menu

label forest_menu:
    menu:
        "Выполнить задание [e.name]" if active_quest.name in quest_elsa_materials.name:
            call forest_quest_elsa_materials
            "Ты выбираешься из [active_quest.location]"
            $nextDay()
            call forest_scene 
            "[e.name] наверняка ждет, надо ее обрадовать"
            call forest_quest_elsa_materials_reward
            $completeQuest(quest_elsa_materials)
            "Ты выходишь в город"
            jump city

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
        "Навестить [r.name]" if not first_time_rapunzel and can_go_r and not isNight() and not isEvening():
            jump visit_rapunzel_forest
        "Навестить [e.name]" if not first_time_elsa and not isNight():
            jump visit_elsa_forest
        "Навестить [nag.name]" if not first_time_nagatoro and can_visit_nagatoro and not isNight():
            jump visit_nagatoro_forest
        "Вернуться назад":
            jump forest

label look_for_enemy:
    "Ты заходишь чуть глубже в лес, отходишь от протоптанной тропинки"
    if strength >= 80:
        "Ты настолько развил свои навыки, что можешь сам выслеживать добычу"
        menu:
            "Кого выследить?"
            "Слизь":
                call start_battle(60, renpy.random.randint(1, 10) , "Слизь", 'scene')
                if last_battle_win:
                    "Ты размазал слизьня"
                    $ addChar(["str"],1)
                $nextTime()
                jump forest_menu
            "Рогатый заяц":
                call start_battle(60, renpy.random.randint(1, 20) , "Рогатый заяц", 'scene') 
                if last_battle_win:
                    "Ты прибил бедного зайку, тебе должно быть стыдно"
                    $ addChar(["str"],2)
                $nextTime()
                jump forest_menu
            "Плотоядный олень":
                call start_battle(100, renpy.random.randint(30, 50) , "Плотоядный олень", 'scene') 
                if last_battle_win:
                    "Охота на оленя без оружия, неплохо, я справляюсь"
                    $ addChar(["str"],3)
                $nextTime()
                jump forest_menu
            "Дикий кабан":
                call start_battle(150, renpy.random.randint(40, 80) , "Дикий кабан", 'scene') 
                if last_battle_win:
                    "Справился с диким кабаном, это успех!"
                    $ addChar(["str"],4)
                $nextTime()
                jump forest_menu
            "Волк":
                call start_battle(60, renpy.random.randint(90, 120) , "Волк", 'scene') 
                if last_battle_win:
                    "Мне повезло справиться с волком Или я уже настолко силен?"
                    $ addChar(["str"],5)
                $nextTime()
                jump forest_menu
            "Бурый медведь":
                call start_battle(200, renpy.random.randint(120, 160) , "Бурый медведь", 'scene')
                if last_battle_win:
                    "Это было очень опасно, хорошо, что я справился!"
                    $ addChar(["str"],6)
                $nextTime()
                jump forest_menu
    $rand_emeny = renpy.random.randint(1, 100) 
    if rand_emeny < 35:
        "Ты видишь слизь, она даже убежать не сможет"
        menu:
            "Ты видишь слизь, она даже убежать не сможет"
            "Напасть":
                call start_battle(60, renpy.random.randint(1, 10) , "Слизь", 'scene') 
                if last_battle_win:
                    "Ты размазал слизьня"
                    $ addChar(["str"],1)
                $nextTime()
                jump forest_menu
            "Уйти":
                jump forest_menu
    if rand_emeny >= 35 and rand_emeny < 55:
        "Ты видишь зайца с рогом, он тебя еще не видит, что будешь делать?"
        menu:
            "Ты видишь зайца с рогом, он тебя еще не видит, что будешь делать?"
            "Напасть":
                call start_battle(60, renpy.random.randint(1, 20) , "Заяц", 'scene') 
                if last_battle_win:
                    "Ты прибил бедного зайку, тебе должно быть стыдно"
                    $ addChar(["str"],2)
                $nextTime()
                jump forest_menu
            "Уйти":
                jump forest_menu
    if rand_emeny >= 55 and rand_emeny < 70:
        "Ты видишь большого и красивого оленя, кажется он уже доедает зайца?!"
        "Он тебя еще не видит, что будешь делать?"
        menu:
            "Он тебя еще не видит, что будешь делать?"
            "Напасть":
                call start_battle(100, renpy.random.randint(30, 50) , "Плотоядный олень", 'scene') 
                if last_battle_win:
                    "Охота на оленя без оружия, неплохо, я справляюсь"
                    $ addChar(["str"],3)
                $nextTime()
                jump forest_menu
            "Уйти":
                jump forest_menu
    if rand_emeny >= 70 and rand_emeny < 85:
        "Ты видидишь кабана, он сразу замечает тебя и бежит в твою сторону!"
        call start_battle(150, renpy.random.randint(40, 80) , "Дикий кабан", 'scene') 
        if last_battle_win:
            "Справился с диким кабаном, это успех!"
            $ addChar(["str"],4)
        $nextTime()
        jump forest_menu
    if rand_emeny >= 85 and rand_emeny < 95:
        "Ты видидишь волка, он сразу замечает тебя и набрасывается!"
        call start_battle(60, renpy.random.randint(90, 120) , "Волк", 'scene') 
        if last_battle_win:
            "Мне повезло справиться с волком Или я уже настолко силен?"
            $ addChar(["str"],5)
        $nextTime()
        jump forest_menu
    if rand_emeny >= 95 and rand_emeny < 100:
        "Ты видидишь медведя, он моментально тебя замечает, спрятаться и убежать не выйдет!"
        call start_battle(200, renpy.random.randint(120, 160) , "Бурый медведь", 'scene') 
        if last_battle_win:
            "Это было очень опасно, хорошо, что я справился!"
            $ addChar(["str"],6)
        $nextTime()
        jump forest_menu