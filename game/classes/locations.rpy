init python:
    class Location:
        def __init__(self, tag, name, canVisit):
            self.tag = tag  # Название локации
            self.name = name  # Название локации
            self.canVisit = canVisit  # Возможность посетить

    class LocList:
        def __init__(self):
            self.list = [
                Location(tag="city",name="Город", canVisit=True),
                Location(tag="forest",name="Лес", canVisit=True),
                Location(tag="rt",name="Разрушенный храм", canVisit=True),
                Location(tag="market",name="Городской рынок", canVisit=True),
                Location(tag="bm",name="Черный рынок", canVisit=False),
                Location(tag="tavern",name="Таверна", canVisit=False),
                Location(tag="room",name="Моя комната", canVisit=False),
                Location(tag="hospital",name="Больница", canVisit=False),
                Location(tag="surgency",name="Хирургия", canVisit=False),
                Location(tag="bar",name="Бар", canVisit=False),
                Location(tag="brothel",name="Бордель", canVisit=False),
                Location(tag="mt",name="Магическая башня", canVisit=False),
                Location(tag="lib",name="Библиотека", canVisit=False),
                Location(tag="guild",name="Гильдия", canVisit=False),
                Location(tag="tg",name="Тренировочная площадка", canVisit=False)
            ]
        
        def getLocByTag(self, tag):
            for loc in self.list:
                if(tag == loc.tag):
                    return loc

        def setVisit(self, tag, canVisit):
            global notices
            if self.getLocByTag(tag).canVisit != canVisit:
                self.getLocByTag(tag).canVisit = canVisit
                if canVisit:
                    notices.append("Теперь вам доступна локация "+ self.getLocByTag(tag).name)
                else:
                    notices.append("Теперь вам недоступна локация "+ self.getLocByTag(tag).name)
                renpy.show_screen('notify_plus', notices=notices)
                notices = []
                return True
            else:
                return False
    
    all_locs = LocList()


    def canVisit(locationtag):
        return all_locs.getLocByTag(locationtag).canVisit

    def updateCanVisit(locationtag, canVisit):
        return all_locs.setVisit(locationtag,canVisit)