define first_root_d = True
define can_go_d = True

label guild_d_menu:
    "Ты находишь [d.name]"
    if d_love >= 50:
        show d smile_shy with fade
    else:
        show d neutral with fade
    menu:
        "А где тут у вас туалет?" if not first_root_d and d_love >= 80:
            jump toilet
        "Тебя пора наказать" if not first_root_d:
            jump guild_d_root_menu
        "Научи меня":
            call start_battle(d_str, 50, d.name, battle_location_guild)
            if last_battle_win:
                d @smile_shy "А-а-аах, ты победил меня, великую воительницу~"
                $addLove("d", 5)
                $addChar(["str"], 3)
                $addNPCStr("d", 20)
                if d_love >= 50:
                    d @smile_shy "Теперь ты можешь делать со мной все, что захочешь~"
                    d @smile_shy "Что же ты со мной сделаешь?"
                    menu:
                        "Издеваться":
                            jump guild_d_root_menu
                        "Ничего":
                            d @angry "Ах, какой ты благородный юноша, [hero_name].."
                            jump guild_d_menu
                jump guild_menu
            else:
                d @angry "Бежал из боя, трус!"
                $minusLove("d", 5)
                "Стоило достойно принять поражение"
                jump guild_menu
        "Спросить про задание" if isNoQuestNow():
            jump guild_d_quests
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
        "Публичный туалет" if d_love >= 90:
            d @smile_shy "Ах, ты так жесток, все эти мужчины, о боже~"
            call d_root_toilet
            jump guild_menu
        "БДСМ изнасилование" if d_love >= 80:
            d @smile_shy "Прошу, начинай, хочу отмучиться побыстрее~"
            call d_root_bdsm
            jump guild_menu
        "Публичный секс" if d_love >= 70:
            d @smile_shy "О нет, что ты за злодей такой~"
            call d_root_public_fuck
            jump guild_menu
        "Публичное обнажение" if d_love >= 60:
            d @smile_shy "Ах, не, за что ты так со мной~"
            call d_root_public_naked
            jump guild_menu
        "Публично покажи сиськи" if d_love >= 50:
            d @smile_shy "О боже, только не это~~"
            call d_root_public_partly_naked
            jump guild_menu
        "Передумал":
            d @angry "Ах, какой вы благородный юноша, [hero_name].."
            jump guild_menu