default first_time_hospital = True
default first_time_sakura = True

label hospital:
    scene bg_hospital with fade
    play music "audio/hospital_theme.mp3"

    if first_time_hospital:
        "Ты входишь в просторное помещение, где медики суетятся вокруг пациентов."
        "Люди сидят в очереди, ожидая лечения, а по коридорам проходят лекари."
        "Среди них ты замечаешь девушку с розовыми волосами, которая, похоже, здесь за главную."
        $ first_time_hospital = False
    else:
        "Ты снова в больнице, где всегда кипит работа."
    if first_time_sakura:
        show sakura neutral with dissolve
        s "О, новый пациент? Или ты просто интересуешься нашей работой?"
        s "Я Сакура, один из главных медиков города. Если тебе нужно лечение, обращайся."
        s "Но помни, лечение стоит денег."
        $ first_time_sakura = False
    else:
        show sakura smile with dissolve
        s "Опять ты? Надеюсь, не сильно пострадал."
    jump hospital_sakura_menu

label hospital_sakura_menu:
    menu:
        "Спросить, где можно найти главного медика" if first_time_sakura:
            s "Ты имеешь в виду Цунаде? Она лучшая лекарь в этом городе."
            s "Сейчас она в операционной. Если тебе нужно серьёзное лечение, направляйся туда."
            jump hospital_sakura_menu
        "Спросить про лечение" if health < 100:
            s "Частичное лечение стоит 5 монет. Если у тебя их нет, придётся найти способ заработать."
            if money >= 5:
                menu:
                    "Заплатить за лечение (5 монет)":
                        $minusMoney(5)
                        pause 3.5
                        $addHealth(20)
                        "Сакура осматривает тебя и использует медицинские техники."
                        "Ты чувствуешь, как боль исчезает, а силы возвращаются."
                    "Отказаться":
                        "Ты решаешь пока не тратить деньги на лечение."
            jump hospital_sakura_menu
        "Перейти в операционную":
            jump surgency_tsunade
        "Спросить про задания" if active_quest.name == no_quest.name:
            jump hospital_sakura_quests
        "Отказаться от выполнения задания" if isActualQuestOfCharacter("s"):
            p "Я не смогу выполнить это задание."
            s "Жаль, но потребность в травах есть всегда, если захочешь помочь - приходи."
            $ removeQuest()
            jump hospital_sakura_menu
        "Вернуться в город":
            jump city

label hospital_sakura_quests:
    show sakura neutral with dissolve
    s "Ты хочешь помочь? Хорошо, у нас в больнице всегда есть работа."
    
    menu:
        "Задание на сбор трав":
            s "Хочешь помочь? Отлично! Вот список необходимых трав. Их можно найти в ближайшем лесу."
            if isAbleQuest(quest_sakura_materials, s_love):
                s "За хороший набор я неплохо заплачу."
                menu:
                    "Принять квест":
                        s "Будь осторожен, в лесу могут быть монстры."
                        $ getQuest(quest_sakura_materials)
                        jump hospital_sakura_menu
                    "Не принимать квест":
                        s "А мог бы и помочь, теперь придется самой всё собирать."
                        jump hospital_sakura_menu
            else:
                s "Подожди, я вижу, ты пока не подходишь для этой работы, возвращайся, когда станешь сильнее."
                jump hospital_sakura_menu
        "Отказаться":
            s "Если передумаешь, только спроси"
            jump hospital_sakura_menu