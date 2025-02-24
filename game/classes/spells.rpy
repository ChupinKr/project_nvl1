python:
    # Класс для заклинаний
    class Spell:
        def __init__(self, name, intelligence_cost, location):
            self.name = name  # Название заклинания
            self.intelligence_cost = intelligence_cost  # Стоимость маны
            self.location = location  # Место, где заклинание можно найти

    # Массив всех доступных заклинаний
    all_spells = [
        Spell("Огненный шар", 10, "Изучается в магической школе."),
        Spell("Ледяной дождь", 15, "Задания у ледяного мастера."),
        Spell("Молния", 12, "Можно найти в храме молний."),
        Spell("Щит", 8, "Получено за выполнение квеста защиты.")
    ]