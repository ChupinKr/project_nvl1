init python:
    class MyCharacter:
        def __init__(
            self, 
            in_name, 
            in_old,
            in_img,
            in_desc,
            in_notice,
            in_short_name
        ):
            self.name = in_name  # Имя
            self.old = in_old  # Картинка
            self.img = in_img  # Картинка
            self.desc = in_desc  # Описание
            self.notice = in_notice  # Совет
            self.short_name = in_short_name  # Совет

    def addNPCStr(charac, countStr):
        current_str = switchStr(charac, countStr)
        if persistent.lang == "russian":
            customNotify(str(charac.name) + " теперь серьезнее")
        if persistent.lang == "english":
            customNotify(str(charac.name) + " became more serious")
        return
    
    def switchStr(charac, countLove):
        global my_freya_str, my_elsa_str, my_nag_str, my_rapunzel_str, my_tsunade_str, my_sakura_str, my_merlin_str
        global my_holo_str, my_miku_str, my_mao_str, my_darkness_str, my_eris_str
        if charac.short_name == "f":
            my_freya_str += countLove
            return my_freya_str
        elif charac.short_name == "e":
            my_elsa_str += countLove
            return my_elsa_str
        elif charac.short_name == "nag":
            my_nag_str += countLove
            return my_nag_str
        elif charac.short_name == "r":
            my_rapunzel_str += countLove
            return my_rapunzel_str
        elif charac.short_name == "ts":
            my_tsunade_str += countLove
            return my_tsunade_str
        elif charac.short_name == "s":
            my_sakura_str += countLove
            return my_sakura_str
        elif charac.short_name == "mer":
            my_merlin_str += countLove
            return my_merlin_str
        elif charac.short_name == "h":
            my_holo_str += countLove
            return my_holo_str
        elif charac.short_name == "m":
            my_miku_str += countLove
            return my_miku_str
        elif charac.short_name == "mao":
            my_mao_str += countLove
            return my_mao_str
        elif charac.short_name == "d":
            my_darkness_str += countLove
            return my_darkness_str
        elif charac.short_name == "eris":
            my_eris_str += countLove
            return my_eris_str
        return

    def minusLove(charac, countMinusLove):
        current_love = switchLove(charac, countMinusLove)
        if persistent.lang == "russian":
            customNotify("Симпатия " + str(charac.name) + " уменьшилась")
        if persistent.lang == "english":
            customNotify(str(charac.name) + "'s sympathy has diminished")
        return

    def addLove(charac, countLove):
        current_love = switchLove(charac, countLove)
        if persistent.lang == "russian":
            customNotify("Симпатия " + str(charac.name) + " возросла")
        if persistent.lang == "english":
            customNotify(str(charac.name) + "'s sympathy has increased")
        return
        
    def switchLove(charac, countLove):
        global my_freya_love, my_elsa_love, my_nag_love, my_rapunzel_love, my_tsunade_love, my_sakura_love, my_merlin_love
        global my_holo_love, my_miku_love, my_mao_love, my_darkness_love, my_eris_love
        if charac.short_name == "f":
            my_freya_love += countLove
            return my_freya_love
        elif charac.short_name == "e":
            my_elsa_love += countLove
            return my_elsa_love
        elif charac.short_name == "nag":
            my_nag_love += countLove
            return my_nag_love
        elif charac.short_name == "r":
            my_rapunzel_love += countLove
            return my_rapunzel_love
        elif charac.short_name == "ts":
            my_tsunade_love += countLove
            return my_tsunade_love
        elif charac.short_name == "s":
            my_sakura_love += countLove
            return my_sakura_love
        elif charac.short_name == "mer":
            my_merlin_love += countLove
            return my_merlin_love
        elif charac.short_name == "h":
            my_holo_love += countLove
            return my_holo_love
        elif charac.short_name == "m":
            my_miku_love += countLove
            return my_miku_love
        elif charac.short_name == "mao":
            my_mao_love += countLove
            return my_mao_love
        elif charac.short_name == "d":
            my_darkness_love += countLove
            return my_darkness_love
        elif charac.short_name == "eris":
            my_eris_love += countLove
            return my_eris_love
        return

define my_freya_love = 0
define my_freya_str = 10000
define my_freya = None
define my_elsa_love = 0
define my_elsa_str = 10
define my_elsa = None
define my_nag_love = 0
define my_nag_str = 100
define my_nag = None
define my_rapunzel_love = 0
define my_rapunzel_str = 20
define my_rapunzel = None
define my_tsunade_love = 0
define my_tsunade_str = 500
define my_tsunade = None
define my_sakura_love = 0
define my_sakura_str = 300
define my_sakura = None
define my_merlin_love = 0
define my_merlin_str = 20
define my_merlin = None
define my_holo_love = 0
define my_holo_str = 30
define my_holo = None
define my_miku_love = 0
define my_miku_str = 40
define my_miku = None
define my_mao_love = 0
define my_mao_str = 20
define my_mao = None
define my_darkness_love = 0
define my_darkness_str = 200
define my_darkness = None
define my_eris_love = 0
define my_eris_str = 150
define my_eris = None

init: #TODO сделать отдельные переменные для силы и 
    if persistent.lang == "english":
        $my_freya = MyCharacter("Freya", "~10000",
        "images/characters/freya_ch/f smile.png", 
        "The goddess who summoned you to this world, she watches your every move.", 
        "Try to 'do the right thing,' and she’ll reward you. \nJust know that doing the right thing isn’t always the best path.",
        "f"
        )
        $my_elsa = MyCharacter("Elsa", "23",
        "images/characters/elsa_ch/new/e smile.png", 
        "A student of a great sorceress. \nHer specialty is ice magic. \nShe’s quite headstrong and sharp-tongued, but if you make an effort to please her, she won’t forget it.",
        "Try to complete her tasks.",
        "e"
        )
        $my_nag = MyCharacter("Nagatoro", "21",
        "images/characters/nagatoro_ch/nag grin.png", 
        "Pretty harsh with her words and loves a good fight. \nShe’s spent years honing her martial arts and physique. \nShe enjoys teasing people.",
        "Try to surpass her in strength—note that she only gets stronger.",
        "nag"
        )
        $my_rapunzel = MyCharacter("Rapunzel", "22",
        "images/characters/rapunzel_ch/new/r smile.png", 
        "A playful and cheerful girl. \nShe’s quite crude with her language. \nShe seems to be connected to some shady characters.",
        "Train your charisma with her, and you’ll be in for a treat.",
        "r"
        )
        $my_tsunade = MyCharacter("Tsunade", "74",
        "images/characters/tsunade_ch/ts smile.png", 
        "A serious woman who works as the chief doctor at the local hospital. \nShe’s the one who’ll heal you, so it’s best to stay on good terms with her.",
        "IN PROGRESS",
        "ts"
        )
        $my_sakura = MyCharacter("Sakura", "27",
        "images/characters/sakura_ch/s smile.png", 
        "The assistant to the chief doctor at the local hospital. \nShe can be harsh at times, but she has a very kind heart.",
        "IN PROGRESS",
        "s"
        )
        $my_merlin = MyCharacter("Merlin", "3649",
        "images/characters/merlin_ch/standart/mer smile.png", 
        "The head of the Magic Tower. \nA great sorceress who seems capable of anything.",
        "Try to get smarter so you can find her whenever you need to.",
        "mer"
        )
        $my_holo = MyCharacter("Holo", "874",
        "images/characters/holo_ch/h smile.png", 
        "A wolf-girl. A vendor at one of the stalls in the City Market. \nA very gentle girl with a pleasant personality and a stunning figure.",
        "Help her out at the City Market.",
        "h"
        )
        $my_miku = MyCharacter("Miku", "25",
        "images/characters/miku_ch/m smile.png", 
        "A bright girl who runs her own tavern. She serves drinks, so she’s almost always holding a mug of beer.",
        "Help her out at the Tavern.",
        "m"
        )
        $my_mao = MyCharacter("Mao Mao", "21",
        "images/characters/maomao_ch/mao smile.png", 
        "A short girl who runs her own brothel. \nShe doesn’t look it, but she’s actually an adult and very clever.",
        "Bring girls to work at her brothel—she’ll pay you well.",
        "mao"
        )
        $my_darkness = MyCharacter("Darkness", "22",
        "images/characters/darkness_ch/d smile.png", 
        "A fairly strong girl. \nThe head of the local warriors’ guild. \nShe has masochistic tendencies but keeps them hidden.",
        "Don’t go easy on her.",
        "d"
        )
        $my_eris = MyCharacter("Eiris", "19",
        "images/characters/eris_ch/min/training_outfit/eris t_smile.png", 
        "A girl who sharpens her skills every morning at the Training Grounds. \nShe’s determined to get stronger to catch up to some mage.",
        "Train with her and complete her tasks.",
        "eris"
        )
    elif persistent.lang == "russian":
        $my_freya = MyCharacter("Фрея", "~10000",
        "images/characters/freya_ch/f smile.png", 
        "Богиня, призвавшая тебя в этот мир, она следит за каждым твоим действием.", 
        "Постарайся \"поступать правильно\" и она тебя отблагодарит. \nТолько знай, что поступать правильно - не всегда лучший путь.",
        "f"
        )
        $my_elsa = MyCharacter("Эльза", "23",
        "images/characters/elsa_ch/new/e smile.png", 
        "Ученица великой волшебницы. \nЕе профиль - ледяная магия. \nОна довольно своевольна и резка, но если постараешься ей услужить - она в долгу не останется.",
        "Постарайся выполнять ее задания.",
        "e"
        )
        $my_nag = MyCharacter("Нагаторо", "21",
        "images/characters/nagatoro_ch/nag grin.png", 
        "Довольно резкая в высказываниях и любит подраться. \nОна долго оттачивала боевые искусства и свое тело. \nЛюбит поддразнивать.",
        "Постарайся обогнать ее по силе, заметь, она становится лишь сильнее.",
        "nag"
        )
        $my_rapunzel = MyCharacter("Рапунцель", "22",
        "images/characters/rapunzel_ch/new/r smile.png", 
        "Игривая и веселая девушка. \nДовольно пошлая в своих выражениях. \nКажется связана с темными личностями.",
        "Тренируй харизму с ней и будет тебе счастье.",
        "r"
        )
        $my_tsunade = MyCharacter("Цунаде", "74",
        "images/characters/tsunade_ch/ts smile.png", 
        "Серьезная дама, работает в местой больнице главным врачом. \nИменно она будет лечить тебя, так что лучше придерживаться с ней хороших отношений.",
        "IN PROGRESS",
        "ts"
        )
        $my_sakura = MyCharacter("Сакура", "27",
        "images/characters/sakura_ch/s smile.png", 
        "Помошница главного врача в местной больнице. \nБывает злая, но у нее очень доброе сердце.",
        "IN PROGRESS",
        "s"
        )
        $my_merlin = MyCharacter("Мерлин", "3649",
        "images/characters/merlin_ch/standart/mer smile.png", 
        "Глава Магической башни. \nВеликая волшебница, способная будто на всё.",
        "Постарайся стать умнее, чтобы в любое время иметь возможность найти ее.",
        "mer"
        )
        $my_holo = MyCharacter("Холо", "874",
        "images/characters/holo_ch/h smile.png", 
        "Девушка-волчица. Продавщица в одной из лавок на Городском рынке. \nОчень нежная девушка с приятным характером и шикарной фигурой.",
        "Помогай ей на Городском рынке.",
        'h'
        )
        $my_miku = MyCharacter("Мику", "25",
        "images/characters/miku_ch/m smile.png", 
        "Светлая девушка, которая держит свою таверну. Разносит напитки, так что почти все время ходит с кружкой пива в руках.",
        "Помогай ей в Таверне.",
        "m"
        )
        $my_mao = MyCharacter("Мао Мао", "21",
        "images/characters/maomao_ch/mao smile.png", 
        "Низкая девушка, заведующая своим Борделем. \nНа вид  и не скажешь, но на деле уже взрослая и очень умная.",
        "Приводи девок работать к ней в Бордель, она хорошо оплатит.",
        "mao"
        )
        $my_darkness = MyCharacter("Даркнесс", "22",
        "images/characters/darkness_ch/d smile.png", 
        "Довольно сильная девушка. \nГлава местной гильдии войнов. \nИмеет мазохистские наклонности, но скрывает это.",
        "Не жалей ее.",
        "d"
        )
        $my_eris = MyCharacter("Эрис", "19",
        "images/characters/eris_ch/mini/training_outfit/eris t_smile.png", 
        "Девушка, которая каждое утро оттачивает свои навыки на Тренировочной площадке. \nОна стремится стать сильнее, чтобы догнать по силе какого-то мага.",
        "Тренируйся и выполняй ее задания.",
        "eris"
        )

init:
    # Инициализация персонажей с соответствующими цветами имен
    
    if persistent.lang == "english":
        define r = Character("Rapunzel", color="#FFBA00", image='r', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])   # Золотистый (блондинка)
        define e = Character("Elsa", color="#87CEFA", image='e', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])   # Светло-голубой (платиновая блондинка)
        define nag = Character("Nagatoro", color="#964B00", image='nag', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])   
        define god = Character("God", color="#B38DF9", image='f', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define f = Character("Freya", color="#B38DF9", image='f', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define ts = Character("Tsunade", color="#FFD700", image='ts', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define s = Character("Sakura", color="#FFC0CB", image='s', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define mer = Character("Merlin", color="#800080", image='mer', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define h = Character("Holo", color="#ff8c00", image='h', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define m = Character('Innkeeper', color="#00ffff", image='m', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define mao = Character('Mao Mao', color="#006400", image='mao', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define d = Character('Darkness', color="#c0c0c0", image='d', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define eris = Character('Eiris', color="#ff5555", image='eris', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define makima = Character("Makima", color="#ffaa00", image='makima', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])  # Макима из "Человека-бензопилы"
        define chizuru = Character("Сhizuru", color="#ffaa00", image='chizuru', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])  # Чизуру из "Девушки на час"
        define guy1 = Character('Guy', color="#ffaaaa", image='guy1', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define asoka = Character("Ahsoka", color="#FFA500", image="asoka", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])
        
        # Some guys
        define old_woman = Character('Old woman', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define guy2 = Character('Guy 2', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define guy3 = Character('Guy 3', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define sg = Character('Muddy guy', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])  #shady guy

        define goblin = Character('Goblin', color="#66cc33", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define hopgoblin = Character('Hop-goblin', color="#66cc33", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define korg = Character('Korg', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define korg_str = 300

        #quest fuckable enemies
        define ent = Character('Ent Girl', color="#013220", image='ent', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define woblin = Character('Goblin-woman', color="#66cc33", image='woblin', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define wragon = Character('Dragoness', color="#ff0000", image='wragon', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define mummy = Character('Mummy', color="#ff0000", image='mummy', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        
        #quest persns
        define emilia = Character("Emilia", color="#dda0dd", image='emilia', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define ramiris = Character('Ramiris', color="#FFBA00", image='ramiris', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define onna = Character("Onna", color="#FAD7A0", image='onna', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 

    elif persistent.lang == "russian":
        define r = Character("Рапунцель", color="#FFBA00", image='r', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])   # Золотистый (блондинка)
        define e = Character("Эльза", color="#87CEFA", image='e', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])   # Светло-голубой (платиновая блондинка)
        define nag = Character("Нагаторо", color="#964B00", image='nag', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])   
        define god = Character("Богиня", color="#B38DF9", image='f', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define f = Character("Фрея", color="#B38DF9", image='f', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define ts = Character("Цунаде", color="#FFD700", image='ts', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define s = Character("Сакура", color="#FFC0CB", image='s', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define mer = Character("Мерлин", color="#800080", image='mer', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define h = Character("Холо", color="#ff8c00", image='h', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define m = Character('Тавернщица', color="#00ffff", image='m', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define mao = Character('Мао Мао', color="#006400", image='mao', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define d = Character('Даркнесс', color="#c0c0c0", image='d', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define eris = Character('Эрис', color="#ff5555", image='eris', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define makima = Character("Макима", color="#ffaa00", image='makima', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])  # Макима из "Человека-бензопилы"
        define chizuru = Character("Чизуру", color="#ffaa00", image='chizuru', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])  # Чизуру из "Девушки на час"
        define guy1 = Character('Парень', color="#ffaaaa", image='guy1', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define asoka = Character("Асока", color="#FFA500", image="asoka", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])
        
        # Some guys
        define old_woman = Character('Старая щенщина', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define guy2 = Character('Парень 2', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define guy3 = Character('Парень 3', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define sg = Character('Мутный тип', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))])  #shady guy

        define goblin = Character('Гоблин', color="#66cc33", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define hopgoblin = Character('Хоп-гоблин', color="#66cc33", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define korg = Character('Корг', color="#ffaaaa", who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define korg_str = 300

        #quest fuckable enemies
        define woblin = Character('Женщина-гоблин', color="#66cc33", image='woblin', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define ent = Character('Девушка Энт', color="#013220", image='ent', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define wragon = Character('Драконица', color="#ff0000", image='wragon', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define mummy = Character('Мумия', color="#ff0000", image='mummy', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        

        #quest persns
        define emilia = Character("Эмилия", color="#dda0dd", image='emilia', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define ramiris = Character('Рамирис', color="#FFBA00", image='ramiris', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
        define onna = Character("Онна", color="#FAD7A0", image='onna', who_outlines=[(1, "#FFFFFF", absolute(0), absolute(0))]) 
