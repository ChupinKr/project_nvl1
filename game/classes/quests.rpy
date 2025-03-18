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
                    if persistent.lang == "russian":
                        self.name = whatToDo + " для " + forWho  # Название квеста
                    if persistent.lang == "english":
                        self.name = whatToDo + " for " + forWho  # Название квеста
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
        
        def setUnrepeatable(self):
            self.repeatable = False
            return

    if persistent.lang == "russian":
        no_quest = GirlQuest(whatToDo="Найди чем заняться", forWho="", forWhoShort="p", 
        repeatable=True,
        location="Надо поискать", countObj=0, 
        character_says=["Займись уже чем-нибудь"],
        req_love=0, req_str=0, req_intelligence=0, req_char=0, 
        reward_money=0, reward_character=0, 
        str_bonus=0, intelligence_bonus=0, char_bonus=0
        )

        #elsa quests
        quest_elsa_materials = GirlQuest(whatToDo="Собрать материалы", forWho="Эльза", forWhoShort="e", 
        repeatable=True,
        location="Лесная чаща", countObj=10, 
        character_says=["Хорошо, мне нужно несколько редких трав и минералов."
            ,"Ты можешь найти их в этих лесах."],
        req_love=0, req_str=10, req_intelligence=40, req_char=0, 
        reward_money=10, reward_character=10, 
        str_bonus=0, intelligence_bonus=5, char_bonus=0
        )
        quest_elsa_crystall = GirlQuest(whatToDo="Добыть Кристалл зимнего эха", forWho="Эльза", forWhoShort="e", 
        repeatable=True,
        location="Ледяные пещеры", countObj=1, 
        character_says=["Я вижу, что ты довольно крепкий, если у тебя все еще хватает ума идти в эти пещеры."
            ,"Твоё тело мне пригодится~"],
        req_love=40, req_str=20, req_intelligence=50, req_char=0, 
        reward_money=50, reward_character=20, 
        str_bonus=0, intelligence_bonus=15, char_bonus=0
        )

        #rapunzel quests
        quest_rapunzel_mashrooms = GirlQuest(whatToDo="Собрать грибы", forWho="Рапунцель", forWhoShort="r", 
        repeatable=True,
        location="Травянистая поляна", countObj=10, 
        character_says=["Есть такие грибы... Они обладают уникальными свойствами."
            ,"Если ты их найдешь, я буду просто в восторге!"],
        req_love=0, req_str=0, req_intelligence=5, req_char=0, 
        reward_money=10, reward_character=10, 
        str_bonus=0, intelligence_bonus=0, char_bonus=3
        )
        quest_rapunzel_women = GirlQuest(whatToDo="Пригласить дам на подмену", forWho="Рапунцель", forWhoShort="r", 
        repeatable=True,
        location="Темный переулок", countObj=3, 
        character_says=["О, это занятие мне по душе! Нам нужно больше красивых и опытных девушек."
            ,"Если приведешь мне парочку, я тебя щедро отблагодарю~"],
        req_love=0, req_str=0, req_intelligence=0, req_char=10, 
        reward_money=15, reward_character=10, 
        str_bonus=0, intelligence_bonus=0, char_bonus=10
        )
        
        #nagatoro quests
        quest_nagatoro_goblins = GirlQuest(whatToDo="Убить гоблинов", forWho="Нагаторо", forWhoShort="nag", 
        repeatable=True,
        location="Лесная чаща", countObj=5, 
        character_says=["Гоблины не такие уж и слабые."
            ,"Ты уверен, что справишься?"],
        req_love=0, req_str=5, req_intelligence=0, req_char=0, 
        reward_money=15, reward_character=10, 
        str_bonus=2, intelligence_bonus=0, char_bonus=0
        )
        quest_nagatoro_forest = GirlQuest(whatToDo="Зачистить лес", forWho="Нагаторо", forWhoShort="nag", 
        repeatable=True,
        location="Лес монстров", countObj=5, 
        character_says=["Хороший выбор. Там полно опасных существ, будь осторожен."],
        req_love=0, req_str=10, req_intelligence=0, req_char=0, 
        reward_money=25, reward_character=10, 
        str_bonus=4, intelligence_bonus=0, char_bonus=0
        )
        quest_nagatoro_bandits = GirlQuest(whatToDo="Убить бандитов", forWho="Нагаторо", forWhoShort="nag", 
        repeatable=True,
        location="Темный переулок", countObj=3, 
        character_says=["Банда действительно угрожает путникам."
            ,"Это задание стоит того, чтобы им заняться."],
        req_love=0, req_str=20, req_intelligence=0, req_char=0, 
        reward_money=35, reward_character=10, 
        str_bonus=6, intelligence_bonus=0, char_bonus=0
        )

        #Eris quests
        quest_eris_goblin_hunting = GirlQuest(
            whatToDo="Охота на гоблинов",
            forWho="Эрис",
            forWhoShort="eris",
            repeatable=True,
            location="Лесная чаща",
            countObj=10,  # Убить 5 гоблинов
            character_says=[
                "Гоблины — мелочь, но их слишком много. Пора их проредить!",
                "Бери меч и пошли, я начну!"
            ],
            req_love=20,  # Требуется минимальная симпатия Эрис
            req_str=20,   # Нужно немного силы для боя
            req_intelligence=0,  # Интеллект не нужен
            req_char=0,   # Харизма не требуется
            reward_money=15,      # Скромная награда
            reward_character=10,  # +10 к любви Эрис
            str_bonus=5,          # Бонус к силе за победу
            intelligence_bonus=0, # Нет бонуса к интеллекту
            char_bonus=0          # Нет бонуса к харизме
        )
        quest_eris_dragon_hunting = GirlQuest(
            whatToDo="Выгнать дракона",
            forWho="Эрис",
            forWhoShort="eris",
            repeatable=False,  # Дракон — редкий противник
            location="Пещера",
            countObj=1,  # Один дракон
            character_says=[
                "Дракон? Отлично, я давно хотела зарубить что-то большое!",
                "Покажи, на что способен, или не мешай мне!"
            ],
            req_love=30,  # Нужно больше доверия Эрис
            req_str=40,   # Дракон требует серьёзной силы
            req_intelligence=10,  # Нужно немного смекалки для тактики
            req_char=0,   # Харизма не важна
            reward_money=50,      # Хорошая награда за сложность
            reward_character=15,  # +15 к любви Эрис
            str_bonus=10,          # Бонус к силе за победу
            intelligence_bonus=0, # Нет бонуса к интеллекту
            char_bonus=0          # Нет бонуса к харизме
        )
        quest_eris_date = GirlQuest(
            whatToDo="Свидание",
            forWho="Эрис",
            forWhoShort="eris",
            repeatable=True,  # Можно повторять для укрепления отношений
            location="Город",
            countObj=0,  # Нет конкретных объектов, просто провести время
            character_says=[
                "Свидание? Ты шутишь? Хотя... давай попробуем!",
                "Только не думай, что я буду скучать. Удиви меня!"
            ],
            req_love=50,  # Нужно больше любви для романтики
            req_str=0,    # Сила не требуется
            req_intelligence=0,  
            req_char=20,  # Харизма важна для успеха
            reward_money=0,       # Нет денег, это не про заработок
            reward_character=20,  # +20 к любви Эрис при успехе
            str_bonus=0,          # Нет бонуса к силе
            intelligence_bonus=1, # Небольшой бонус к интеллекту
            char_bonus=2          # Бонус к харизме за удачное свидание
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

        #проверить, что ты подходишь для задания
        def isAbleQuest(quest, love):
            global notices
            result = True
            #renpy.watch(str(quest.req_str))
            #renpy.watch(str(strength))
            if not quest.repeatable:
                return False
            if quest.req_love > love:
                notices.append("Недостаточно симпатии")
                result = False
            if quest.req_str > strength:
                notices.append("Недостаточно силы")
                result = False
            if quest.req_intelligence > intelligence:
                notices.append("Недостаточно интеллекта")
                result = False
            if quest.req_char > charisma:
                notices.append("Недостаточно харизмы")
                result = False
            #renpy.watch(str(result))
            if notices:
                renpy.show_screen('notify_plus', notices=notices)
            notices = []
            return result
    if persistent.lang == "english":
        no_quest = GirlQuest(whatToDo="Find something to do", forWho="", forWhoShort="p", repeatable=True,
            location="You need to look around", countObj=0, 
            character_says=["Get busy with something already"],
            req_love=0, req_str=0, req_intelligence=0, req_char=0, 
            reward_money=0, reward_character=0, 
            str_bonus=0, intelligence_bonus=0, char_bonus=0
            )

        # Elsa quests
        quest_elsa_materials = GirlQuest(whatToDo="Gather materials", forWho="Elsa", forWhoShort="e", repeatable=True,
            location="Forest Thicket", countObj=10, 
            character_says=["Good, I need some rare herbs and minerals."
                ,"You can find them in these forests."],
            req_love=0, req_str=10, req_intelligence=40, req_char=0, 
            reward_money=10, reward_character=10, 
            str_bonus=0, intelligence_bonus=5, char_bonus=0
            )
        quest_elsa_crystall = GirlQuest(whatToDo="Obtain a Winter Echo Crystal", forWho="Elsa", forWhoShort="e", repeatable=True,
            location="Icy Caves", countObj=1, 
            character_says=["I see you’re pretty sturdy if you still have the wits to head into those caves."
                ,"Your body will come in handy~"],
            req_love=40, req_str=20, req_intelligence=50, req_char=0, 
            reward_money=50, reward_character=20, 
            str_bonus=0, intelligence_bonus=15, char_bonus=0
            )

        # Rapunzel quests
        quest_rapunzel_mashrooms = GirlQuest(whatToDo="Gather mushrooms", forWho="Rapunzel", forWhoShort="r", repeatable=True,
            location="Grassy Clearing", countObj=10, 
            character_says=["There are these mushrooms… They have unique properties."
                ,"If you find them, I’ll be absolutely thrilled!"],
            req_love=0, req_str=0, req_intelligence=5, req_char=0, 
            reward_money=10, reward_character=10, 
            str_bonus=0, intelligence_bonus=0, char_bonus=3
            )
        quest_rapunzel_women = GirlQuest(whatToDo="Recruit ladies for backup", forWho="Rapunzel", forWhoShort="r", repeatable=True,
            location="Dark Alley", countObj=3, 
            character_says=["Oh, this job’s right up my alley! We need more pretty, experienced girls."
                ,"If you bring me a couple, I’ll reward you handsomely~"],
            req_love=0, req_str=0, req_intelligence=0, req_char=10, 
            reward_money=15, reward_character=10, 
            str_bonus=0, intelligence_bonus=0, char_bonus=10
            )

        # Nagatoro quests
        quest_nagatoro_goblins = GirlQuest(whatToDo="Kill goblins", forWho="Nagatoro", forWhoShort="nag", repeatable=True,
            location="Forest Thicket", countObj=5, 
            character_says=["Goblins aren’t as weak as they seem."
                ,"Are you sure you can handle it?"],
            req_love=0, req_str=5, req_intelligence=0, req_char=0, 
            reward_money=15, reward_character=10, 
            str_bonus=2, intelligence_bonus=0, char_bonus=0
            )
        quest_nagatoro_forest = GirlQuest(whatToDo="Clear the forest", forWho="Nagatoro", forWhoShort="nag", repeatable=True,
            location="Monster Forest", countObj=5, 
            character_says=["Good choice. It’s full of dangerous creatures, so be careful."],
            req_love=0, req_str=10, req_intelligence=0, req_char=0, 
            reward_money=25, reward_character=10, 
            str_bonus=4, intelligence_bonus=0, char_bonus=0
            )
        quest_nagatoro_bandits = GirlQuest(whatToDo="Kill bandits", forWho="Nagatoro", forWhoShort="nag", repeatable=True,
            location="Dark Alley", countObj=3, 
            character_says=["That gang’s really a threat to travelers."
                ,"This task is worth taking on."],
            req_love=0, req_str=20, req_intelligence=0, req_char=0, 
            reward_money=35, reward_character=10, 
            str_bonus=6, intelligence_bonus=0, char_bonus=0
            )

        # Eris quests
        quest_eris_goblin_hunting = GirlQuest(
            whatToDo="Goblin hunting",
            forWho="Eris",
            forWhoShort="eris",
            repeatable=True,
            location="Forest Thicket",
            countObj=10,  # Kill 10 goblins
            character_says=[
                "Goblins are small fry, but there are too many of them. Time to thin them out!",
                "Grab a sword and let’s go—I’ll start!"
            ],
            req_love=20,  # Requires some affection from Eris
            req_str=20,   # Needs some strength for combat
            req_intelligence=0,  # Intelligence not required
            req_char=0,   # Charisma not needed
            reward_money=15,      # Modest reward
            reward_character=10,  # +10 to Eris’s affection
            str_bonus=5,          # Strength bonus for victory
            intelligence_bonus=0, # No intelligence bonus
            char_bonus=0          # No charisma bonus
        )
        quest_eris_dragon_hunting = GirlQuest(
            whatToDo="Drive out a dragon",
            forWho="Eris",
            forWhoShort="eris",
            repeatable=False,  # Dragons are rare foes
            location="Cave",
            countObj=1,  # One dragon
            character_says=[
                "A dragon? Perfect, I’ve been itching to take down something big!",
                "Show me what you’ve got, or stay out of my way!"
            ],
            req_love=30,  # Requires more trust from Eris
            req_str=40,   # A dragon demands serious strength
            req_intelligence=10,  # Needs some cunning for tactics
            req_char=0,   # Charisma doesn’t matter
            reward_money=50,      # Good reward for the challenge
            reward_character=15,  # +15 to Eris’s affection
            str_bonus=10,         # Strength bonus for victory
            intelligence_bonus=0, # No intelligence bonus
            char_bonus=0          # No charisma bonus
        )
        quest_eris_date = GirlQuest(
            whatToDo="Date",
            forWho="Eris",
            forWhoShort="eris",
            repeatable=True,  # Can be repeated to strengthen the relationship
            location="City",
            countObj=0,  # No specific objects, just spend time together
            character_says=[
                "A date? Are you kidding? Well… let’s give it a shot!",
                "Don’t think I’ll be bored. Surprise me!"
            ],
            req_love=50,  # Needs more affection for romance
            req_str=0,    # Strength not required
            req_intelligence=0,  
            req_char=20,  # Charisma is key to success
            reward_money=0,       # No money, it’s not about profit
            reward_character=20,  # +20 to Eris’s affection if successful
            str_bonus=0,          # No strength bonus
            intelligence_bonus=1, # Small intelligence bonus
            char_bonus=2          # Charisma bonus for a successful date
        )

        # Tsunade quests
        quest_tsunade_poison_tooth = GirlQuest(whatToDo="Obtain a fang", forWho="Tsunade", forWhoShort="ts", repeatable=True,
            location="Forest Thicket", countObj=5, 
            character_says=["You can find that snake in the forest—it’s highly venomous."
                ,"Are you sure you can handle it?"],
            req_love=0, req_str=20, req_intelligence=0, req_char=0, 
            reward_money=15, reward_character=10, 
            str_bonus=5, intelligence_bonus=0, char_bonus=0
            )

        # Sakura quests
        quest_sakura_materials = GirlQuest(whatToDo="Gather herbs", forWho="Sakura", forWhoShort="s", repeatable=True,
            location="Forest Thicket", countObj=5, 
            character_says=["You should be able to find the herbs without trouble."
                ,"But there are monsters out there, so be careful."],
            req_love=0, req_str=10, req_intelligence=0, req_char=0, 
            reward_money=15, reward_character=10, 
            str_bonus=0, intelligence_bonus=5, char_bonus=0
            )

        # Check if you qualify for the quest
        def isAbleQuest(quest, love):
            global notices
            result = True
            #renpy.watch(str(quest.req_str))
            #renpy.watch(str(strength))
            if not quest.repeatable:
                return False
            if quest.req_love > love:
                notices.append("Not enough affection")
                result = False
            if quest.req_str > strength:
                notices.append("Not enough strength")
                result = False
            if quest.req_intelligence > intelligence:
                notices.append("Not enough intelligence")
                result = False
            if quest.req_char > charisma:
                notices.append("Not enough charisma")
                result = False
            #renpy.watch(str(result))
            if notices:
                renpy.show_screen('notify_plus', notices=notices)
            notices = []
            return result

    #Проверить, что у тебя нет задания
    def isNoQuestNow():
        result = False
        #renpy.watch(str(quest.req_str))
        #renpy.watch(str(strength))
        if active_quest.name == no_quest.name:
            result = True
        return result

    def getQuestListByWho(who):
        result = []
        if who == "ts":
            result = [quest_tsunade_poison_tooth]
        if who == "s":
            result = [quest_sakura_materials]
        if who == "r":
            result = [quest_rapunzel_mashrooms,quest_rapunzel_women]
        if who == "e":
            result = [quest_elsa_materials, quest_elsa_crystall]
        if who == "nag":
            result = [quest_nagatoro_bandits, quest_nagatoro_forest, quest_nagatoro_goblins]
        if who == "mer":
            result = []
        if who == "d":
            result = []
        if who == "h":
            result = []
        if who == "m":
            result = []
        if who == "eris":
            result = [quest_eris_goblin_hunting, quest_eris_dragon_hunting, quest_eris_date]
        return result
        
    #вычисляет принят ли квест этого персонажа сейчас
    def isActualQuestOfCharacter(who):
        result = False
        targetQuests = getQuestListByWho(who)
        if any(active_quest.name in q.name for q in targetQuests):
            result = True
        return result

    def completeQuest(quest, character):
        addMoney(active_quest.reward_money)
        character.addLove(active_quest.reward_character)
        addChar(["str"], active_quest.str_bonus)
        addChar(["char"], active_quest.char_bonus)
        addChar(["intelligence"], active_quest.intelligence_bonus)
        removeQuest(False)
        quest.setUnrepeatable()
        return True

    def isQuestCompleted(quest):
        if quest.repeatable == False:
            return True
        else:
            return False

    def isAnyQuestComplete(character):
        targetQuests = getQuestListByWho(character.short_name)
        if any(q.repeatable == False for q in targetQuests):
            return True
        else:
            return False

    def getQuest(quest):
        global active_quest,notices
        active_quest = quest
        if persistent.lang == "russian":
            notices.append("Ты принял квест " + str(active_quest.name))
        if persistent.lang == "english":
            notices.append("You accepted quest " + str(active_quest.name))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def removeQuest(inform = True):
        global active_quest, notices
        active_quest = no_quest
        if inform:
            if persistent.lang == "russian":
                notices.append("Ты отказался от квеста " + str(active_quest.name))
            if persistent.lang == "english":
                notices.append("You refused quest " + str(active_quest.name))
            renpy.show_screen('notify_plus', notices=notices)
            notices = []