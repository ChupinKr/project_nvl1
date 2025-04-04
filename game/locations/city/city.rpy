define first_time_city = True

label city:
    call city_scene

    if first_time_city:
        "Ты оказываешься в оживлённом городе, где прошлое и настоящее переплелись воедино."
        "Узкие мощёные улочки ведут к шумным рынкам, где торговцы предлагают диковинные товары, а в переулках слышатся шёпоты о запретных сделках."
        "Городская стража неспешно патрулирует главные дороги, но в тени зданий кипит жизнь, неподвластная закону."
        "Перед тобой открывается множество возможностей. Куда ты отправишься?"
        $ first_time_city = False
    else:
        "Куда ты отправишься?"

    menu:
        #quests
        "Выполнить задание [e.name]" if active_quest.name in quest_elsa_crystall.name:
            call quest_elsa_crystall_start
            "Ты выбираешься из [active_quest.location]"
            $nextDay()
            call city_scene 
            "[e.name] наверняка ждет, надо ее обрадовать"
            call quest_elsa_crystall_reward
            $completeQuest(quest_elsa_crystall, my_elsa)
            "Ты выходишь в город"
            jump city
        "Пойти на свидание с [eris.name]" if (active_quest.name in quest_eris_date.name) and not isNight():
            call quest_eris_date_start
            $completeQuest(quest_eris_date, my_eris, False)
            "Ты в таверне"
            jump tavern
        "Исследовать червоточину" if active_quest.name in quest_eris_black_hole.name:
            call quest_eris_black_hole_start
            $completeQuest(quest_eris_black_hole, my_eris)
            "Ты в городе"
            jump city
        "Заняться поиском [eris.name]" if isNoQuestNow() and can_find_eris==False:
            $getQuest(quest_eris_black_hole)
            mind "Хорошо, так я не забуду о своей цели."
            jump city
        "Временно прекратить поиски [eris.name]" if active_quest.name in quest_eris_black_hole.name:
            $removeQuest()
            mind "Пока я точно не готов, стоит заняться этим позже."
            jump city

        #actions
        "Переночевать на скамейке" if not canVisit("room") and isNight():
            jump city_overnight_stay
        "Отдохнуть на скамейке" if not canVisit("room") and not isNight():
            jump city_rest
        "Комната" if canVisit("room"):
            jump room
        "Таверна" if canVisit("tavern"):
            "Здесь кипит жизнь: искатели приключений обсуждают последние слухи, а трактирщик всегда рад предложить работу за пару медяков."
            jump tavern
        "Библиотека" if canVisit("lib"):
            "Размеры и количество книг потрясаю воображение. Кажется, что на прочтение всех книг здесь не хватит и тысячи жизней."
            jump library
        "Магическая башня" if canVisit("mt") :
            "Ты смотришь вверх и видишь древнюю магическую башню, вершина которой окутана мерцающими чарами. Говорят, её двери открываются только для тех, кто жаждет знаний."
            jump magic_tower_alone
        "Тренировочная площадка" if canVisit("tg"):
            "Звуки стальных клинков и боевые кличи доносятся с тренировочной площадки, где воины оттачивают своё мастерство."
            jump training_ground
        "Гильдия бойцов" if canVisit("guild"):
            "Лязг и крики, команды, место где порядок и дисциплина прежде всего."
            jump guild
        "Больница" if canVisit("hospital"):
            "Вдали ты замечаешь больницу — высокое светлое здание, где лечат раненых, но за это берут плату."
            jump hospital
        "Городской рынок" if canVisit("market"):
            "Городской рынок полон жизни: повсюду торговцы выкрикивают цены, алхимики продают зелья, а ювелиры демонстрируют драгоценные украшения."
            jump market
        "Подпольный рынок" if canVisit("bm") and (isNight() or isEvening()):
            "Где-то в тени улиц скрывается подпольный рынок, куда заходят лишь те, кто знает, что искать..."
            jump black_market
        "Выйти за городские стены" if canVisit("forest"):
            "Ты можешь покинуть город и отправиться в дикую природу. Но будь осторожен: за стенами правят совсем другие законы."
            jump forest

label city_overnight_stay:
    "Уже слишком поздно, тебя клонит в сон"
    call city_scene("night")  
    "Тебе некуда податься, ты решаешь уснуть в центре города на холодной деревянной скамье"
    "Такая ночь неизбежно подкашивает твое здоровье"
    $minusAllChar(1)
    mind "Так и помереть можно. Надо срочно найти жилье!"
    $nextDay()
    jump city

label city_rest:
    "Ты устал и решаешь посидеть передохнуть на скамейке"
    "Не самый приятный отдых в твоей жизни"
    $rest_fuckup = renpy.random.randint(0,100) 
    if rest_fuckup < 50:
        "Проезжающая мимо телега с фруктами проехала тебе по ноге"
        $minusHealth(5)
    if rest_fuckup >= 50:
        if money >= 5:
            $minusMoney(5)
            "У тебя украли 5 монет, когда ты отвлекся"
        elif money > 0 and money < 5:
            $minusMoney(money)
            "Пока ты дремал, у тебя высыпалась вся мелочь и ее быстро кто-то подобрал"
        else:
            "Кажется кто-то хотел украсть у тебя деньги, благо их у тебя нет"
    $nextTime()
    jump city