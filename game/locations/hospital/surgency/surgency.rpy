
default first_time_surgency = True  

label surgency_tsunade_cure:
    $ bring = []
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
    $ bring = []
    scene bg_hospital with fade
    play music "audio/hospital_theme.mp3"

    show ts neutral with dissolve

    ts "Пришел вернуть долги?"

    jump surgency_tsunade_menu

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
            jump surgency_tsunade_menu
        "Спросить про задания" if not active_quest:
            p "У вас есть какие-нибудь задания для меня, чтобы я мог честно расплачиваться за лечение?"
            jump surgency_tsunade_quests
        "Поблагодарить и уйти":
            ts "Хоть кто-то умеет говорить «спасибо». Постарайся больше не попадать ко мне."
            jump city

label surgency_tsunade_quests:
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