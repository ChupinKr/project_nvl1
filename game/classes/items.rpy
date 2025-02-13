init python:
    class Item:
        def __init__(self, name, price, 
        countUsage, lvl, bonus, char):

            self.name = name  # Название предметов
            self.countUsage = countUsage  # Количество использований
            self.price = price  # Цена

            self.lvl = lvl  # уровень сложности
            self.bonus = bonus  # Награда в стате
            self.char = char  # Какая стата увеличится
        
        
        def executeItem(self):
            self.countUsage -=1
            minusMoneyPlusChar(0, [self.char], self.bonus)
            return True  

    item_motivational_book = Item(name="Мотивирующая книга", price=20,
    countUsage=3, lvl=1, bonus=1, char="char")
    item_mirror = Item(name="Зеркало", price=50,
    countUsage=3, lvl=2, bonus=3, char="char")
    item_art_plus_size = Item(name="Артефакт \"PlusSize\"", price=100,
    countUsage=3, lvl=3, bonus=5, char="char")

    item_dumbbells_ez = Item(name="Легкие гантели", price=20,
    countUsage=3, lvl=1, bonus=1, char="str")
    item_weight_mid = Item(name="Гиря", price=50,
    countUsage=3, lvl=2, bonus=3, char="str")
    item_barbell = Item(name="Штанга", price=100,
    countUsage=3, lvl=3, bonus=5, char="str")

    item_book_math = Item(name="Книга по математике", price=20,
    countUsage=3, lvl=1, bonus=1, char="mana")
    item_self_study_guide  = Item(name="Самоучитель по магии", price=50,
    countUsage=3, lvl=2, bonus=3, char="mana")
    item_grimoire = Item(name="Гримуар", price=100,
    countUsage=3, lvl=3, bonus=5, char="mana")

    item_forest_guide = Item(name="Путеводитель по лесу", price=100,
    countUsage=1, lvl=0, bonus=0, char="")
    item_combat_book = Item(name="Купить краткий экскурс по ведению боя", price=100,
    countUsage=1, lvl=0, bonus=0, char="")

    def getDoneItemsByChar(character):
        result = []
        for it in gg_items:
            if it.char == character:#если характеристика совпадает с искомой
                if it.countUsage == 0:# если не осталось возможности выполнять
                    result.append(it)
        return result   

    def getMaxLvlOfItems(items):
        result = 0
        for it in items:
            if it.lvl > result:
                result = it.lvl
        return result   

    #Проверить, что можешь купить предмет
    def isAbleToBuy(item):
        result = False
        #renpy.watch(str(quest.req_str))
        #renpy.watch(str(strength))
        if money >= item.price:
            if item.lvl == 0:
                for it in gg_items:
                    if item.name == it.name:
                        return False
                return True

            if item.lvl == 1:
                for it in gg_items:
                    if item.name == it.name:
                        return False
                return True

            if item.lvl > 1:
                for it in gg_items:
                    if item.name == it.name:
                        return False
                if ((item.lvl - 1) == getMaxLvlOfItems(getDoneItemsByChar(item.char))):
                    return True
        return False

    def isAbleToExecuteItem(item):
        result = False
        if it.countUsage > 0:
                result = True
        return result   