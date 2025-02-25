
# Сцена с комнатой игрока
label room:
    scene bg room with fade
    if not canVisit("room"):
        show m with dissolve
        m smile "[hero_name], срок аренды закончился, комната стоит 10 монет в неделю..." with dissolve
        menu:
            "Арендовать комнату на неделю?"
            "Беру" if money >= 10:
                p "Понял, вот оплата на неделю."
                $ minusMoney(10)
                $ updateCanVisit("room", True)
                $ while_room = day + 6
                m smile "Спасибо, приятного отдыха~"
            "Мне пока не по карману":
                m smile "Тогда пожалуйста покинь комнату и приходи ко мне подработать~" with dissolve
                "Ты уходишь"
                jump city
    "Ты у себя в комнате"
    menu:
        "Тренироваться" if len(gg_items) > 0:
            "За дело!"
            call room_training
            jump room
        "Отдохнуть":
            "Как же давно я не мог просто отдохнуть"
            $addHealth(10)
            $nextTime()
            jump room
        "Провести ночь":
            jump room_sleep
        "Покинуть комнату":
            "Вы идете в таверну"
            jump tavern
        "Пойти в город":
            "Вы вышли в город"
            jump city

label room_sleep:
    "Пора спать. Ты проводишь ночь в теплой постели."
    $addHealth(100)
    $nextDay()
    jump room


label room_training:
    p "Хм, чем бы заняться?"
    menu:
        "Использовать [gg_items[0].name]" if (len(gg_items) > 0 and gg_items[0].countUsage > 0):
            "Был использован [gg_items[0].name]"
            $gg_items[0].executeItem()
            "Осталось использований [gg_items[0].countUsage]"
            $nextTime()
        "Использовать [gg_items[1].name]" if (len(gg_items) > 1 and gg_items[1].countUsage > 0):
            "Был использован [gg_items[1].name]"
            $gg_items[1].executeItem()
            "Осталось использований [gg_items[1].countUsage]"
            $nextTime()
        "Использовать [gg_items[2].name]" if (len(gg_items) > 2 and gg_items[2].countUsage > 0):
            "Был использован [gg_items[2].name]"
            $gg_items[2].executeItem()
            "Осталось использований [gg_items[2].countUsage]"
            $nextTime()
        "Использовать [gg_items[3].name]" if (len(gg_items) > 3 and gg_items[3].countUsage > 0):
            "Был использован [gg_items[3].name]"
            $gg_items[3].executeItem()
            "Осталось использований [gg_items[3].countUsage]"
            $nextTime()
        "Использовать [gg_items[4].name]" if (len(gg_items) > 4 and gg_items[4].countUsage > 0):
            "Был использован [gg_items[4].name]"
            $gg_items[4].executeItem()
            "Осталось использований [gg_items[4].countUsage]"
            $nextTime()
        "Использовать [gg_items[5].name]" if (len(gg_items) > 5 and gg_items[5].countUsage > 0):
            "Был использован [gg_items[5].name]"
            $gg_items[5].executeItem()
            "Осталось использований [gg_items[5].countUsage]"
            $nextTime()
        "Использовать [gg_items[6].name]" if (len(gg_items) > 6 and gg_items[6].countUsage > 0):
            "Был использован [gg_items[6].name]"
            $gg_items[6].executeItem()
            "Осталось использований [gg_items[6].countUsage]"
            $nextTime()
        "Использовать [gg_items[7].name]" if (len(gg_items) > 7 and gg_items[7].countUsage > 0):
            "Был использован [gg_items[7].name]"
            $gg_items[7].executeItem()
            "Осталось использований [gg_items[7].countUsage]"
            $nextTime()
        "Использовать [gg_items[8].name]" if (len(gg_items) > 8 and gg_items[8].countUsage > 0):
            "Был использован [gg_items[8].name]"
            $gg_items[8].executeItem()
            "Осталось использований [gg_items[8].countUsage]"
            $nextTime()
        "Использовать [gg_items[9].name]" if (len(gg_items) > 9 and gg_items[9].countUsage > 0):
            "Был использован [gg_items[9].name]"
            $gg_items[9].executeItem()
            "Осталось использований [gg_items[9].countUsage]"
            $nextTime()
        "Использовать [gg_items[10].name]" if (len(gg_items) > 10 and gg_items[10].countUsage > 0):
            "Был использован [gg_items[10].name]"
            $gg_items[10].executeItem()
            "Осталось использований [gg_items[10].countUsage]"
            $nextTime()
        "Использовать [gg_items[11].name]" if (len(gg_items) > 11 and gg_items[11].countUsage > 0):
            "Был использован [gg_items[11].name]"
            $gg_items[11].executeItem()
            "Осталось использований [gg_items[11].countUsage]"
            $nextTime()
        "Использовать [gg_items[12].name]" if (len(gg_items) > 12 and gg_items[12].countUsage > 0):
            "Был использован [gg_items[12].name]"
            $gg_items[12].executeItem()
            "Осталось использований [gg_items[12].countUsage]"
            $nextTime()
        "Использовать [gg_items[13].name]" if (len(gg_items) > 13 and gg_items[13].countUsage > 0):
            "Был использован [gg_items[13].name]"
            $gg_items[13].executeItem()
            "Осталось использований [gg_items[13].countUsage]"
            $nextTime()
        "Использовать [gg_items[14].name]" if (len(gg_items) > 14 and gg_items[14].countUsage > 0):
            "Был использован [gg_items[14].name]"
            $gg_items[14].executeItem()
            "Осталось использований [gg_items[14].countUsage]"
            $nextTime()
        "Передумал":
            jump room

    jump room