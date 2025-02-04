default first_time_hospital = True
default first_time_sakura = True
default first_time_surgency = True  
define bring = []

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

label surgency_tsunade_cure:
    scene bg_hospital with fade
    play music "audio/hospital_theme.mp3"

    "Ты медленно приходишь в себя, чувствуя резкую боль во всём теле."
    "Белый потолок, запах медикаментов… Похоже, ты в операционной."

    show ts neutral with dissolve

    if first_time_surgency and health == 0:
        ts "Очнулся, наконец? Не люблю возиться с пациентами, которые валяются тут днями."
        if money <= 0:
            ts "Вижу у тебя небольшие проблемы с золотом."
        ts "Повезло тебе, в первый раз я тебя подлатала бесплатно."
        $ can_visit_hospital = True
        $ first_time_surgency = False
        $ health = 100
        "Ты ощущаешь, как раны затягиваются, тело наполняется силой… но остаётся слабость."
    elif first_time_surgency:
        $ can_visit_hospital = True
        ts "Ты выглядишь здоровым, но всё равно пришёл ко мне? Или у тебя есть ко мне дело?"
    else:
        if money >= 10:
            ts "Опять ты? Уже не первый раз на моём операционном столе."  
            ts "С тебя {color=#FFD700}10 монет{/color}. Надеюсь, ты не разорился?"
            $ money -= 10
            $ health = 100
            "Ты ощущаешь, как раны затягиваются, тело наполняется силой… но остаётся слабость."
        else:
            ts "Опять приполз без денег? Так не пойдет, дорогой, надо и честь знать."
    jump surgency_tsunade_menu

label surgency_tsunade:
    scene bg_hospital with fade
    play music "audio/hospital_theme.mp3"

    show ts neutral with dissolve

    ts "Пришел вернуть долги?"

    jump surgency_tsunade_menu

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

label surgency_tsunade_menu: 
    show tsunade with dissolve
    menu:
        set bring
        "Спросить, где ты":
            ts "Ты в лечебнице. Здесь поднимают на ноги таких, как ты — тех, кто не умеет держать меч или уклоняться от ударов."
            jump surgency_tsunade_menu
        "Поинтересоваться, как заработать денег":
            ts "Ох, ты хочешь расплатиться честно? Что ж, это похвально."
            ts "В таверне всегда нужны помощники. Помоешь посуду — получишь монеты. "
            ts "А если умеешь драться, ищи работу в гильдии."
            $ can_visit_tavern = True
            $ can_visit_guild = True
            jump surgency_tsunade_menu
        "Спросить про задания" if not active_quest:
            p "У вас есть какие-нибудь задания для меня, чтобы я мог честно расплачиваться за лечение?"
            jump hospital_tsunade_quests
        "Поблагодарить и уйти":
            ts "Хоть кто-то умеет говорить «спасибо». Постарайся больше не попадать ко мне."
            jump city

label hospital_tsunade_quests:
    show ts neutral with dissolve
    ts "Задания? Хм... У меня есть кое-что для тебя."
    menu:
        "Принять задание на охоту за редким ингредиентом":
            ts "Мне нужен редкий алхимический ингредиент — клык ядовитой змеи. Можно достать его в глубине леса."
            ts "Принеси его, и я заплачу тебе."
            $ active_quest = "Добыча клыка змеи для Цунаде"
            jump surgency_tsunade_menu
        "Отказаться":
            ts "Ну, значит, не так уж и нуждаешься в деньгах."
            jump surgency_tsunade_menu