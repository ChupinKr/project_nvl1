# Инициализация переменных
default  hero_name = ""
default  chosen_blessing = None  # Хранит выбранное благословение
default  health = 100  # Здоровье
default  money = 0  # Монеты

default  charisma = 1  # Харизма
default  strength = 1  # Сила
default  intelligence = 1  # Объем маны
default  charisma_mod = 1  # Модификатор харизмы
default  strength_mod = 1  # Модификатор силы
default  intelligence_mod = 1  # Модификатор маны
# День и время
default  day = 1 # после вечера должно идти утро след дня
default  time = "" # после вечера должно идти утро след дня
#До какого дня можно попасть в комнату
default  while_room = 0
#Текущий квест
default  active_quest = no_quest
# Массив доступных для главного героя заклинаний
default  available_spells = []
# Массив купленных товаров
default  gg_items = []
# Текущее местоположение
default  current_location = "forest"
# Приглашенная девушка
default  can_invite_brothel = False
default  invited_girl = None
#Количество смертей
default  defeat_count = 0
