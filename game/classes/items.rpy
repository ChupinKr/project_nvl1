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
            global can_escape_every_time
            self.countUsage -=1
            if self.char:
                addChar([self.char], self.bonus)
            else:
                can_escape_every_time = True
                customNotify("Теперь ты можешь бежать вечно")
            return True  

    if persistent.lang == "russian":
        item_motivational_book = Item(name="Мотивирующая книга", price=20,
        countUsage=3, lvl=1, bonus=5, char="char")
        item_mirror = Item(name="Зеркало", price=50,
        countUsage=3, lvl=2, bonus=10, char="char")
        item_art_plus_size = Item(name="Артефакт \"PlusSize\"", price=100,
        countUsage=3, lvl=3, bonus=15, char="char")

        item_dumbbells_ez = Item(name="Легкие гантели", price=20,
        countUsage=3, lvl=1, bonus=5, char="str")
        item_weight_mid = Item(name="Гиря", price=50,
        countUsage=3, lvl=2, bonus=10, char="str")
        item_barbell = Item(name="Штанга", price=100,
        countUsage=3, lvl=3, bonus=15, char="str")

        item_book_math = Item(name="Книга по математике", price=20,
        countUsage=3, lvl=1, bonus=5, char="intelligence")
        item_self_study_guide  = Item(name="Самоучитель по магии", price=50,
        countUsage=3, lvl=2, bonus=10, char="intelligence")
        item_grimoire = Item(name="Гримуар", price=100,
        countUsage=3, lvl=3, bonus=15, char="intelligence")

        item_forest_guide = Item(name="Путеводитель по лесу", price=100,
        countUsage=1, lvl=0, bonus=0, char="")
        item_combat_book = Item(name="Купить краткий экскурс по ведению боя", price=100,
        countUsage=1, lvl=0, bonus=0, char="")
    if persistent.lang == "english":
        item_motivational_book = Item(name="Motivational book", price=20,
        countUsage=3, lvl=1, bonus=5, char="char")
        item_mirror = Item(name="Mirror", price=50,
        countUsage=3, lvl=2, bonus=10, char="char")
        item_art_plus_size = Item(name="Artifact \"PlusSize\"", price=100,
        countUsage=3, lvl=3, bonus=15, char="char")

        item_dumbbells_ez = Item(name="Light Dumbbells", price=20,
        countUsage=3, lvl=1, bonus=5, char="str")
        item_weight_mid = Item(name="Weight", price=50,
        countUsage=3, lvl=2, bonus=10, char="str")
        item_barbell = Item(name="Barbell", price=100,
        countUsage=3, lvl=3, bonus=15, char="str")

        item_book_math = Item(name="Book of Mathematics", price=20,
        countUsage=3, lvl=1, bonus=5, char="intelligence")
        item_self_study_guide = Item(name="Self-study Guide to Magic", price=50,
        countUsage=3, lvl=2, bonus=10, char="intelligence")
        item_grimoire = Item(name="Grimoire", price=100,
        countUsage=3, lvl=3, bonus=15, char="intelligence")

        item_combat_book = Item(name="Buy a brief excursion on combat", price=200,
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