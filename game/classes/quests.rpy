init python:
    class GirlQuest:
        def __init__(self, whatToDo, forWho, repeatable, location, countObj, 
        req_character=0, req_str=0, req_mana=0,req_char=0,
        reward_money=0, reward_character=0, 
        str_bonus=0, mana_bonus=0, char_bonus=0):
            self.name = whatToDo + " для " + forWho  # Название квеста
            self.whatToDo = whatToDo  # Что сделать
            self.forWho = forWho  # Для кого делаем
            self.repeatable = repeatable  # Повторяемый

            self.location = location  # Локация
            self.countObj = countObj  # Количество

            self.req_character = req_character  # Требуемая сила
            self.req_str = req_str  # Требуемая сила
            self.req_mana = req_mana  # Требуемая мана
            self.req_char = req_char  # Требуемая харизма

            self.reward_money = reward_money  # Награда в деньгах
            self.reward_character = reward_character  # Награда в отношении

            self.str_bonus = str_bonus  # Награда в стате силы
            self.mana_bonus = mana_bonus  # Награда в стате магии
            self.char_bonus = char_bonus  # Награда в стате харизмы

    allQuests = [
        #elsa quests
        GirlQuest(whatToDo="Сбор материалов", forWho="Эльза", repeatable=True,
        location="Лесная чаща", countObj=10, 
        req_character=0, req_str=0, req_mana=0, req_char=0, 
        reward_money=10, reward_character=10, 
        str_bonus=0, mana_bonus=5, char_bonus=0
        ),
        #rapunzel quests
        GirlQuest(whatToDo="Сбор грибов", forWho="Рапунцель", repeatable=True,
        location="Травянистая поляна", countObj=10, 
        req_character=0, req_str=0, req_mana=0, req_char=0, 
        reward_money=10, reward_character=10, 
        str_bonus=0, mana_bonus=0, char_bonus=3
        ),
        GirlQuest(whatToDo="Приглашать дам", forWho="Рапунцель", repeatable=True,
        location="Темный переулок", countObj=3, 
        req_character=0, req_str=0, req_mana=0, req_char=0, 
        reward_money=15, reward_character=10, 
        str_bonus=0, mana_bonus=0, char_bonus=10
        ),
        #esdeath quests
        GirlQuest(whatToDo="Убить гоблинов", forWho="Эсдес", repeatable=True,
        location="Лесная чаща", countObj=5, 
        req_character=0, req_str=0, req_mana=0, req_char=0, 
        reward_money=15, reward_character=10, 
        str_bonus=3, mana_bonus=0, char_bonus=0
        ),
        GirlQuest(whatToDo="Зачистить лес", forWho="Эсдес", repeatable=True,
        location="Лес монстров", countObj=5, 
        req_character=0, req_str=0, req_mana=0, req_char=0, 
        reward_money=25, reward_character=10, 
        str_bonus=5, mana_bonus=0, char_bonus=0
        ),
        GirlQuest(whatToDo="Убить бандитов", forWho="Эсдес", repeatable=True,
        location="Темный переулок", countObj=3, 
        req_character=0, req_str=0, req_mana=0, req_char=0, 
        reward_money=35, reward_character=10, 
        str_bonus=7, mana_bonus=0, char_bonus=0
        ),
    ]

    def getAbleQuestsFor(forWho):
        result = []
        for quest in allQuests:
            if(quest.forWho == forWho):
                result.add(quest)
        return result

