init python:
    class GirlQuest:
        def __init__(self, whatToDo, forWho, forWhoShort, repeatable, 
        location, countObj, 
        character_says,
        req_love=0, req_str=0, req_intelligence=0,req_char=0,
        reward_money=0, reward_character=0, 
        str_bonus=0, intelligence_bonus=0, char_bonus=0):
            if self:
                if forWho:
                    self.name = whatToDo + " для " + forWho  # Название квеста
                else:
                    self.name = whatToDo 
            else:
                self.name = "None"
            self.whatToDo = whatToDo  # Что сделать
            self.forWho = forWho  # Для кого делаем
            self.forWhoShort = forWhoShort  # Для кого делаем
            self.repeatable = repeatable  # Повторяемый

            self.location = location  # Локация
            self.countObj = countObj  # Количество

            self.req_love = req_love  # Требуемая привязанность персонажа
            self.req_str = req_str  # Требуемая сила
            self.req_intelligence = req_intelligence  # Требуемая мана
            self.req_char = req_char  # Требуемая харизма

            self.reward_money = reward_money  # Награда в деньгах
            self.reward_character = reward_character  # Награда в отношении

            self.str_bonus = str_bonus  # Награда в стате силы
            self.intelligence_bonus = intelligence_bonus  # Награда в стате магии
            self.char_bonus = char_bonus  # Награда в стате харизмы

    
    no_quest = GirlQuest(whatToDo="Найди чем заняться", forWho="", forWhoShort="p", repeatable=True,
    location="Где хочешь", countObj=0, 
    character_says=["Займись уже чем-нибудь"],
    req_love=0, req_str=0, req_intelligence=0, req_char=0, 
    reward_money=0, reward_character=0, 
    str_bonus=0, intelligence_bonus=0, char_bonus=0
    )

    #elsa quests
    quest_elsa_materials = GirlQuest(whatToDo="Собрать материалы", forWho="Эльза", forWhoShort="e", repeatable=True,
    location="Лесная чаща", countObj=10, 
    character_says=["Хорошо, мне нужно несколько редких трав и минералов."
        ,"Ты можешь найти их в этих лесах."],
    req_love=0, req_str=10, req_intelligence=40, req_char=0, 
    reward_money=10, reward_character=10, 
    str_bonus=0, intelligence_bonus=5, char_bonus=0
    )
    quest_elsa_test = GirlQuest(whatToDo="Протестировать работу зелья", forWho="Эльза", forWhoShort="e", repeatable=True,
    location="Разрушенный храм", countObj=3, 
    character_says=["Я вижу, что ты довольно крепкий, если у тебя все еще хватает ума заходить в этот лес."
        ,"Твоё тело мне пригодится~"],
    req_love=30, req_str=0, req_intelligence=20, req_char=0, 
    reward_money=10, reward_character=5, 
    str_bonus=0, intelligence_bonus=5, char_bonus=0
    )

    #rapunzel quests
    quest_rapunzel_mashrooms = GirlQuest(whatToDo="Собрать грибы", forWho="Рапунцель", forWhoShort="r", repeatable=True,
    location="Травянистая поляна", countObj=10, 
    character_says=["Есть такие грибы... Они обладают уникальными свойствами."
        ,"Если ты их найдешь, я буду просто в восторге!"],
    req_love=0, req_str=0, req_intelligence=5, req_char=0, 
    reward_money=10, reward_character=10, 
    str_bonus=0, intelligence_bonus=0, char_bonus=3
    )
    quest_rapunzel_women = GirlQuest(whatToDo="Пригласить дам на подмену", forWho="Рапунцель", forWhoShort="r", repeatable=True,
    location="Темный переулок", countObj=3, 
    character_says=["О, это занятие мне по душе! Нам нужно больше красивых и опытных девушек."
        ,"Если приведешь мне парочку, я тебя щедро отблагодарю~"],
    req_love=0, req_str=0, req_intelligence=0, req_char=10, 
    reward_money=15, reward_character=10, 
    str_bonus=0, intelligence_bonus=0, char_bonus=10
    )
    
    #nagatoro quests
    quest_nagatoro_goblins = GirlQuest(whatToDo="Убить гоблинов", forWho="Нагаторо", forWhoShort="nag", repeatable=True,
    location="Лесная чаща", countObj=5, 
    character_says=["Гоблины не такие уж и слабые."
        ,"Ты уверен, что справишься?"],
    req_love=0, req_str=5, req_intelligence=0, req_char=0, 
    reward_money=15, reward_character=10, 
    str_bonus=2, intelligence_bonus=0, char_bonus=0
    )
    quest_nagatoro_forest = GirlQuest(whatToDo="Зачистить лес", forWho="Нагаторо", forWhoShort="nag", repeatable=True,
    location="Лес монстров", countObj=5, 
    character_says=["Хороший выбор. Там полно опасных существ, будь осторожен."],
    req_love=0, req_str=10, req_intelligence=0, req_char=0, 
    reward_money=25, reward_character=10, 
    str_bonus=4, intelligence_bonus=0, char_bonus=0
    )
    quest_nagatoro_bandits = GirlQuest(whatToDo="Убить бандитов", forWho="Нагаторо", forWhoShort="nag", repeatable=True,
    location="Темный переулок", countObj=3, 
    character_says=["Банда действительно угрожает путникам."
        ,"Это задание стоит того, чтобы им заняться."],
    req_love=0, req_str=20, req_intelligence=0, req_char=0, 
    reward_money=35, reward_character=10, 
    str_bonus=6, intelligence_bonus=0, char_bonus=0
    )

    #tsunade quests
    quest_tsunade_poison_tooth = GirlQuest(whatToDo="Достать клык", forWho="Тсунаде", forWhoShort="ts", repeatable=True,
    location="Лесная чаща", countObj=5, 
    character_says=["Эту змею можно найти в лесу, она крайне ядовита"
        ,"Ты уверен, что справишься?"],
    req_love=0, req_str=20, req_intelligence=0, req_char=0, 
    reward_money=15, reward_character=10, 
    str_bonus=5, intelligence_bonus=0, char_bonus=0
    )

    #sakura quests
    quest_sakura_materials = GirlQuest(whatToDo="Собрать травы", forWho="Сакура", forWhoShort="s", repeatable=True,
    location="Лесная чаща", countObj=5, 
    character_says=["Травы ты сможешь найти без проблем"
        ,"Но там водятся чудовища, будь осторожен"],
    req_love=0, req_str=10, req_intelligence=0, req_char=0, 
    reward_money=15, reward_character=10, 
    str_bonus=0, intelligence_bonus=5, char_bonus=0
    )

    #Проверить, что у тебя нет задания
    def isNoQuestNow():
        result = False
        #renpy.watch(str(quest.req_str))
        #renpy.watch(str(strength))
        if active_quest.name == no_quest.name:
            result = True
        return result

    #проверить, что ты подходишь для задания
    def isAbleQuest(quest, love):
        result = True
        #renpy.watch(str(quest.req_str))
        #renpy.watch(str(strength))
        if quest.req_love > love:
            result = False
        if quest.req_str > strength:
            result = False
        if quest.req_intelligence > intelligence:
            result = False
        if quest.req_char > charisma:
            result = False
        if not quest.repeatable:
            result = False
        #renpy.watch(str(result))
        return result

    #вычисляет принят ли квест этого персонажа сейчас
    def isActualQuestOfCharacter(who):
        result = False
        if who == "ts":
            targetQuests = [quest_tsunade_poison_tooth]
        if who == "s":
            targetQuests = [quest_sakura_materials]
        if who == "r":
            targetQuests = [quest_rapunzel_mashrooms,quest_rapunzel_women]
        if who == "e":
            targetQuests = [quest_elsa_materials, quest_elsa_test]
        if who == "nag":
            targetQuests = [quest_nagatoro_bandits, quest_nagatoro_forest, quest_nagatoro_goblins]
        if who == "mer":
            targetQuests = []
        if who == "d":
            targetQuests = []
        if who == "h":
            targetQuests = []
        if who == "m":
            targetQuests = []
        if who == "eris":
            targetQuests = []
        if any(active_quest.name in q.name for q in targetQuests):
            result = True
        return result

    def completeQuest(quest):
        addMoney(active_quest.reward_money)
        addLove(active_quest.forWhoShort, active_quest.reward_character)
        addChar(["str"], active_quest.str_bonus)
        addChar(["char"], active_quest.char_bonus)
        addChar(["intelligence"], active_quest.intelligence_bonus)
        removeQuest(False)
        quest.repeatable = False
        return True

    def getQuest(quest):
        global active_quest,notices
        active_quest = quest
        notices.append("Ты принял квест " + str(active_quest.name))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def removeQuest(inform = True):
        global active_quest, notices
        active_quest = no_quest
        if inform:
            notices.append("Ты отказался от квеста " + str(active_quest.name))
            renpy.show_screen('notify_plus', notices=notices)
            notices = []