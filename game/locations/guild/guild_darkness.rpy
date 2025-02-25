define first_root_d = True
define can_go_d = True

label guild_d_menu:
    "Ты находишь [d.name]"
    if d_love >= 50:
        show d smile_shy with dissolve
    else:
        show d neutral with dissolve
    menu:
        "А где тут у вас туалет?" if not first_root_d and d_love >= 80:
            jump toilet
        "Тебя пора наказать" if not first_root_d:
            jump guild_d_root_menu
        "Научи меня":
            call start_battle(d_str, 60, d.name, battle_location_guild)
            if last_battle_win:
                d @smile_shy "А-а-аах, ты победил меня, великую воительницу~"
                $addLove("d", 5)
                $addChar(["str"], 2)
                $addNPCStr("d", 20)
                if d_love >= 50:
                    d @smile_shy "Теперь ты можешь делать со мной все, что захочешь~"
                    d @smile_shy "Что же ты со мной сделаешь?"
                    menu:
                        d "Что же ты со мной сделаешь?"
                        "Издеваться":
                            jump guild_d_root_menu
                        "Ничего":
                            d @angry "Ах, какой ты благородный юноша, [hero_name].."
            else:
                d @angry "Бежал из боя, трус!"
                $minusLove("d", 5)
                "Стоило достойно принять поражение"
            $nextTime()
            jump guild_d_menu
        "Спросить про задание" if isNoQuestNow():
            call guild_d_quests from _call_guild_d_quests
            jump guild_d_menu
        "Отказаться от задания" if isActualQuestOfCharacter("d"):
            p "Я не буду выполнять твое задание."
            d @smile_shy "Ааах, ты так жесток~"
            $ removeQuest()
            jump guild_d_menu
        "Уйти": 
            p "Я думаю, что мне стоит уйти."
            d @smile "Если понадоблюсь - я буду здесь~"
            jump guild

label toilet:
    scene bg toilet with fade
    menu:
        "Позвать [d.name]" if d_love >= 90:
            jump toilet_root_d
        "Позвать [nag.name]" if nag_love >= 90:
            jump toilet_root_nag
        "Позвать [d.name] и [nag.name]" if nag_love >= 100 and d_love >= 100:
            jump toilet_root_d_and_nag
        "Ничего":
            jump guild


label guild_d_root_menu:
    $first_root_d = False
    menu:
        "Покажи сиськи" if d_love >= 50:
            d @smile_shy "О боже, только не это~~"
            call d_root_public_partly_naked from _call_d_root_public_partly_naked
            $nextTime()
            jump guild_menu
        "Разденься" if d_love >= 60:
            d @smile_shy "Ах, не, за что ты так со мной~"
            call d_root_public_naked from _call_d_root_public_naked
            $nextTime()
            jump guild_menu
        "Секс" if d_love >= 70:
            d @smile_shy "О нет, что ты за злодей такой~"
            call d_root_public_fuck from _call_d_root_public_fuck
            $nextTime()
            jump guild_menu
        "Публичный туалет" if d_love >= 80:
            d @smile_shy "Ах, ты так жесток, все эти мужчины, о боже~"
            call d_root_toilet from _call_d_root_toilet
            $nextTime()
            jump guild_menu
        "Изнасилование" if d_love >= 90:
            d @smile_shy "Прошу, начинай, хочу отмучиться побыстрее~"
            call d_root_group_fuck from _call_d_root_group_fuck
            $nextTime()
            jump guild_menu
        "Какая-то жесть" if d_love >= 200:
            d @ahegao "Нет! Прошу! Только не это!"
            call d_root_jest from _call_d_root_jest
            $nextTime()
            jump guild_menu
        "Передумал":
            d @angry "Ах, какой вы благородный юноша, [hero_name].."
            jump guild_menu

label guild_d_quests:
    "IN PROGRESS"
    return 