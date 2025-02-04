init:
    # Инициализация переменных
    $ hero_name = ""
    $ chosen_blessing = None  # Хранит выбранное благословение
    $ health = 100  # Здоровье

    $ money = 0  # Харизма
    $ charisma = 0  # Харизма
    $ strength = 0  # Сила
    $ mana = 0  # Объем маны

    #Текущий квест
    $ active_quest = None

    # Массив доступных для главного героя заклинаний
    $ available_spells = []

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
    $ can_visit_forest = True
    $ can_visit_ruined_temple = True
    $ can_visit_monster_forest = True

