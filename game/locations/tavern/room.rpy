
# Сцена с комнатой игрока
label room:
    scene room_bg with fade
    "Ты у себя в комнате"
    menu:
        "Тренироваться" if len(gg_items) > 0:
            "За дело!"
            jump room_training
        "Отдохнуть":
            "Как же давно я не мог просто отдохнуть"
            $addHealth(10)
            jump room
        "Провести ночь":
            "Пора спать"
            $addHealth(100)
            jump room
        "Покинуть комнату":
            "Вы идете в таверну"
            jump tavern
        "Пойти в город":
            "Вы вышли в город"
            jump city

label room_training:
    p "Хм, чем бы заняться?"
    menu:
        "Использовать [gg_items[0].name]" if (len(gg_items) > 0 and gg_items[0].countUsage > 0):
            "Был использован [gg_items[0].name]"
            $gg_items[0].executeItem()
            "Осталось использований [gg_items[0].countUsage]"
            jump room_training
        "Использовать [gg_items[1].name]" if (len(gg_items) > 1 and gg_items[1].countUsage > 0):
            "Был использован [gg_items[1].name]"
            $gg_items[1].executeItem()
            "Осталось использований [gg_items[1].countUsage]"
            jump room_training
        "Использовать [gg_items[2].name]" if (len(gg_items) > 2 and gg_items[2].countUsage > 0):
            "Был использован [gg_items[2].name]"
            $gg_items[2].executeItem()
            "Осталось использований [gg_items[2].countUsage]"
            jump room_training
        "Использовать [gg_items[3].name]" if (len(gg_items) > 3 and gg_items[3].countUsage > 0):
            "Был использован [gg_items[3].name]"
            $gg_items[3].executeItem()
            "Осталось использований [gg_items[3].countUsage]"
            jump room_training
        "Использовать [gg_items[4].name]" if (len(gg_items) > 4 and gg_items[4].countUsage > 0):
            "Был использован [gg_items[4].name]"
            $gg_items[4].executeItem()
            "Осталось использований [gg_items[4].countUsage]"
            jump room_training
        "Использовать [gg_items[5].name]" if (len(gg_items) > 5 and gg_items[5].countUsage > 0):
            "Был использован [gg_items[5].name]"
            $gg_items[5].executeItem()
            "Осталось использований [gg_items[5].countUsage]"
            jump room_training
        "Использовать [gg_items[6].name]" if (len(gg_items) > 6 and gg_items[6].countUsage > 0):
            "Был использован [gg_items[6].name]"
            $gg_items[6].executeItem()
            "Осталось использований [gg_items[6].countUsage]"
            jump room_training
        "Использовать [gg_items[7].name]" if (len(gg_items) > 7 and gg_items[7].countUsage > 0):
            "Был использован [gg_items[7].name]"
            $gg_items[7].executeItem()
            "Осталось использований [gg_items[7].countUsage]"
            jump room_training
        "Использовать [gg_items[8].name]" if (len(gg_items) > 8 and gg_items[8].countUsage > 0):
            "Был использован [gg_items[8].name]"
            $gg_items[8].executeItem()
            "Осталось использований [gg_items[8].countUsage]"
            jump room_training
        "Использовать [gg_items[9].name]" if (len(gg_items) > 9 and gg_items[9].countUsage > 0):
            "Был использован [gg_items[9].name]"
            $gg_items[9].executeItem()
            "Осталось использований [gg_items[9].countUsage]"
            jump room_training
        "Использовать [gg_items[10].name]" if (len(gg_items) > 10 and gg_items[10].countUsage > 0):
            "Был использован [gg_items[10].name]"
            $gg_items[10].executeItem()
            "Осталось использований [gg_items[10].countUsage]"
            jump room_training
        "Использовать [gg_items[11].name]" if (len(gg_items) > 11 and gg_items[11].countUsage > 0):
            "Был использован [gg_items[11].name]"
            $gg_items[11].executeItem()
            "Осталось использований [gg_items[11].countUsage]"
            jump room_training
        "Использовать [gg_items[12].name]" if (len(gg_items) > 12 and gg_items[12].countUsage > 0):
            "Был использован [gg_items[12].name]"
            $gg_items[12].executeItem()
            "Осталось использований [gg_items[12].countUsage]"
            jump room_training
        "Использовать [gg_items[13].name]" if (len(gg_items) > 13 and gg_items[13].countUsage > 0):
            "Был использован [gg_items[13].name]"
            $gg_items[13].executeItem()
            "Осталось использований [gg_items[13].countUsage]"
            jump room_training
        "Использовать [gg_items[14].name]" if (len(gg_items) > 14 and gg_items[14].countUsage > 0):
            "Был использован [gg_items[14].name]"
            $gg_items[14].executeItem()
            "Осталось использований [gg_items[14].countUsage]"
            jump room_training
        "Не хочу тренироваться":
            jump room