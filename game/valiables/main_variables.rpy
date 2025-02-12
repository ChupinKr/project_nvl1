init:
    # Инициализация переменных
    $ hero_name = ""
    $ chosen_blessing = None  # Хранит выбранное благословение
    $ health = 100  # Здоровье

    $ money = 0  # Харизма
    
    $ charisma = 0  # Харизма
    $ strength = 0  # Сила
    $ mana = 0  # Объем маны
    $ charisma_mod = 0  # Модификатор харизмы
    $ strength_mod = 0  # Модификатор силы
    $ mana_mod = 0  # Модификатор маны

    # День и время
    $ day = 0 # после вечера должно идти утро след дня
    $ time = 0 #Всего 3 времени (0 - раннее утро, 1 - день, 2 - вечер)

    #Текущий квест
    $ active_quest = no_quest

    # Массив доступных для главного героя заклинаний
    $ available_spells = []

    #Количество смертей
    $ death_count = 0

    #Доступы
    $ can_visit_home = False
    $ can_visit_bar = False
    $ can_visit_tavern = False
    $ can_visit_guild = False
    $ can_visit_magic_tower = False
    $ can_visit_library = False
    $ can_visit_training_ground = False
    $ can_visit_hospital = False
    $ can_visit_black_market = False
    $ can_visit_market = True
    $ can_visit_forest = True
    $ can_visit_ruined_temple = True
    $ can_visit_monster_forest = True
