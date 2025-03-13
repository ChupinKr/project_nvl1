init:
    # Инициализация переменных
    $ hero_name = ""
    $ chosen_blessing = None  # Хранит выбранное благословение
    $ health = 100  # Здоровье

    $ money = 0  # Харизма
    
    $ charisma = 1  # Харизма
    $ strength = 1  # Сила
    $ intelligence = 1  # Объем маны
    $ charisma_mod = 1  # Модификатор харизмы
    $ strength_mod = 1  # Модификатор силы
    $ intelligence_mod = 1  # Модификатор маны

    # День и время
    $ day = 1 # после вечера должно идти утро след дня
    if persistent.lang == "russian":
        $ time = "Утро" #Всего 4 времени (Утро, День, Вечер, Ночь)
    if persistent.lang == "english":
        $ time = "Morning" #Всего 4 времени (Утро, День, Вечер, Ночь)

    #До какого дня можно попасть в комнату
    $ while_room = 0

    #Текущий квест
    $ active_quest = no_quest

    # Массив доступных для главного героя заклинаний
    $ available_spells = []

    # Массив купленных товаров
    $ gg_items = []

    # Приглашенная девушка
    $ can_invite_brothel = False
    $ invited_girl = None

    #Количество смертей
    $ defeat_count = 0
