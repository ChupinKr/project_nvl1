init python:
    class GirlQuest:
        def __init__(self, whatToDo, forWho, repeatable, 
        location, countObj, 
        character_says,
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

    
    #elsa quests
    quest_elsa_materials = GirlQuest(whatToDo="Собрать материалы", forWho="Эльза", repeatable=True,
    location="Лесная чаща", countObj=10, 
    character_says=["Хорошо, мне нужно несколько редких трав и минералов."
        ,"Ты можешь найти их в этих лесах."],
    req_character=0, req_str=0, req_mana=0, req_char=0, 
    reward_money=10, reward_character=10, 
    str_bonus=0, mana_bonus=2, char_bonus=0
    )
    quest_elsa_test = GirlQuest(whatToDo="Протестировать работу зелья", forWho="Эльза", repeatable=True,
    location="Разрушенный храм", countObj=3, 
    character_says=["Я вижу, что ты довольно крепкий, если у тебя все еще хватает ума заходить в этот лес."
        ,"Твоё тело мне пригодится~"],
    req_character=0, req_str=0, req_mana=0, req_char=0, 
    reward_money=10, reward_character=5, 
    str_bonus=0, mana_bonus=5, char_bonus=0
    )

    #rapunzel quests
    quest_rapunzel_mashrooms = GirlQuest(whatToDo="Собрать грибы", forWho="Рапунцель", repeatable=True,
    location="Травянистая поляна", countObj=10, 
    character_says=["Есть такие грибы... Они обладают уникальными свойствами."
        ,"Если ты их найдешь, я буду просто в восторге!"],
    req_character=0, req_str=0, req_mana=0, req_char=0, 
    reward_money=10, reward_character=10, 
    str_bonus=0, mana_bonus=0, char_bonus=3
    )
    quest_rapunzel_women = GirlQuest(whatToDo="Пригласить дам", forWho="Рапунцель", repeatable=True,
    location="Темный переулок", countObj=3, 
    character_says=["О, это занятие мне по душе! Нам нужно больше красивых и опытных девушек."
        ,"Если приведешь мне парочку, я тебя щедро отблагодарю~"],
    req_character=0, req_str=0, req_mana=0, req_char=0, 
    reward_money=15, reward_character=10, 
    str_bonus=0, mana_bonus=0, char_bonus=10
    )
    
    #nagatoro quests
    quest_nagatoro_goblins = GirlQuest(whatToDo="Убить гоблинов", forWho="[nag.name]", repeatable=True,
    location="Лесная чаща", countObj=5, 
    character_says=["Гоблины не такие уж и слабые."
        ,"Ты уверен, что справишься?"],
    req_character=0, req_str=0, req_mana=0, req_char=0, 
    reward_money=15, reward_character=10, 
    str_bonus=2, mana_bonus=0, char_bonus=0
    )
    quest_nagatoro_forest = GirlQuest(whatToDo="Зачистить лес", forWho="[nag.name]", repeatable=True,
    location="Лес монстров", countObj=5, 
    character_says=["Хороший выбор. Там полно опасных существ, будь осторожен."],
    req_character=0, req_str=0, req_mana=0, req_char=0, 
    reward_money=25, reward_character=10, 
    str_bonus=4, mana_bonus=0, char_bonus=0
    )
    quest_nagatoro_bandits = GirlQuest(whatToDo="Убить бандитов", forWho="[nag.name]", repeatable=True,
    location="Темный переулок", countObj=3, 
    character_says=["Банда действительно угрожает путникам."
        ,"Это задание стоит того, чтобы им заняться."],
    req_character=0, req_str=0, req_mana=0, req_char=0, 
    reward_money=35, reward_character=10, 
    str_bonus=6, mana_bonus=0, char_bonus=0
    )

    def getAbleQuestsFor(forWho):
        result = []
        for quest in allQuests:
            if(quest.forWho == forWho):
                result.add(quest)
        return result

