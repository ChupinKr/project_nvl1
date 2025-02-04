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

label hospital_sakura_quests:
    show sakura neutral with dissolve
    s "Ты хочешь помочь? Хорошо, у нас в больнице всегда есть работа."
    
    menu:
        "Принять задание на доставку лекарств":
            s "Отлично! Вот список необходимых трав. Их можно найти в ближайшем лесу."
            s "Будь осторожен, в лесу могут быть монстры."
            $ active_quest = "Сбор трав для Сакуры"
            jump hospital
        "Отказаться":
            s "Если передумаешь, возвращайся."
            jump hospital

label hospital_sakura_menu:
    menu:
        "Спросить, где можно найти главного медика":
            s "Ты имеешь в виду Цунаде? Она лучшая лекарь в этом городе."
            s "Сейчас она в операционной. Если тебе нужно серьёзное лечение, направляйся туда."
            jump hospital_sakura_menu
        "Спросить про лечение":
            s "Лечение стоит 10 монет. Если у тебя их нет, придётся найти способ заработать."
            if money >= 10:
                menu:
                    "Заплатить за лечение (10 монет)":
                        $ money -= 10
                        "Сакура осматривает тебя и использует медицинские техники."
                        "Ты чувствуешь, как боль исчезает, а силы возвращаются."
                        $ health = 100
                    "Отказаться":
                        "Ты решаешь пока не тратить деньги на лечение."
            jump hospital_sakura_menu
        "Перейти в операционную":
            jump surgency_tsunade
        "Спросить про задания" if not active_quest:
            jump hospital_sakura_quests
        "Вернуться в город":
            jump city