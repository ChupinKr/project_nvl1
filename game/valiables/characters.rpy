init python:
    class MyCharacter:
        def __init__(
            self, 
            in_name, 
            in_love, 
            in_strength,
            in_img,
            in_desc,
            in_notice,
            in_short_name
        ):

            self.name = in_name  # Имя
            self.love = in_love  # Симпатия
            self.str = in_strength  # Сила
            self.img = in_img  # Картинка
            self.desc = in_desc  # Описание
            self.notice = in_notice  # Совет
            self.short_name = in_short_name  # Совет

        def addNPCStr(self, countStr):
            self.str += countStr
            if persistent.lang == "russian":
                customNotify(str(self.name) + " стала серьезнее")
            if persistent.lang == "english":
                customNotify(str(self.name) + " became more serious")
            return

        def addLove(self, countLove):
            self.love += countLove
            if persistent.lang == "russian":
                customNotify("Симпатия " + str(self.name) + " возросла")
            if persistent.lang == "english":
                customNotify(str(self.name) + "'s sympathy has increased")
            return

        def minusLove(self, countLove):
            self.love -= countLove
            if persistent.lang == "russian":
                customNotify("Симпатия " + str(self.name) + " уменьшилась")
            if persistent.lang == "english":
                customNotify(str(self.name) + "'s sympathy has diminished")
            return

    if persistent.lang == "english":
        my_freya = MyCharacter("Freya", 0, 10000, 
        "images/characters/freya_ch/f smile.png", 
        "The goddess who summoned you to this world, she watches your every move.", 
        "Try to 'do the right thing,' and she’ll reward you. \nJust know that doing the right thing isn’t always the best path.",
        "f"
        )

        my_elsa = MyCharacter("Elsa", 0, 500,
        "images/characters/elsa_ch/new/e smile.png", 
        "A student of a great sorceress. \nHer specialty is ice magic. \nShe’s quite headstrong and sharp-tongued, but if you make an effort to please her, she won’t forget it.",
        "Try to complete her tasks.",
        "e"
        )

        my_nag = MyCharacter("Nagatoro", 0, 100,
        "images/characters/nagatoro_ch/nag grin.png", 
        "Pretty harsh with her words and loves a good fight. \nShe’s spent years honing her martial arts and physique. \nShe enjoys teasing people.",
        "Try to surpass her in strength—note that she only gets stronger.",
        "nag"
        )

        my_rapunzel = MyCharacter("Rapunzel", 0, 20,
        "images/characters/rapunzel_ch/new/r smile.png", 
        "A playful and cheerful girl. \nShe’s quite crude with her language. \nShe seems to be connected to some shady characters.",
        "Train your charisma with her, and you’ll be in for a treat.",
        "r"
        )

        my_tsunade = MyCharacter("Tsunade", 0, 500,
        "images/characters/tsunade_ch/ts smile.png", 
        "A serious woman who works as the chief doctor at the local hospital. \nShe’s the one who’ll heal you, so it’s best to stay on good terms with her.",
        "IN PROGRESS",
        "ts"
        )

        my_sakura = MyCharacter("Sakura", 0, 300,
        "images/characters/sakura_ch/s smile.png", 
        "The assistant to the chief doctor at the local hospital. \nShe can be harsh at times, but she has a very kind heart.",
        "IN PROGRESS",
        "s"
        )

        my_merlin = MyCharacter("Merlin", 0, 0,
        "images/characters/merlin_ch/standart/mer smile.png", 
        "The head of the Magic Tower. \nA great sorceress who seems capable of anything.",
        "Try to get smarter so you can find her whenever you need to.",
        "mer"
        )

        my_holo = MyCharacter("Holo", 0, 30,
        "images/characters/holo_ch/h smile.png", 
        "A wolf-girl. A vendor at one of the stalls in the City Market. \nA very gentle girl with a pleasant personality and a stunning figure.",
        "Help her out at the City Market.",
        "h"
        )

        my_miku = MyCharacter("Miku", 0, 40,
        "images/characters/miku_ch/m smile.png", 
        "A bright girl who runs her own tavern. She serves drinks, so she’s almost always holding a mug of beer.",
        "Help her out at the Tavern.",
        "m"
        )

        my_mao = MyCharacter("Mao Mao", 0, 20,
        "images/characters/maomao_ch/mao smile.png", 
        "A short girl who runs her own brothel. \nShe doesn’t look it, but she’s actually an adult and very clever.",
        "Bring girls to work at her brothel—she’ll pay you well.",
        "mao"
        )

        my_darkness = MyCharacter("Darkness", 0, 300,
        "images/characters/darkness_ch/d smile.png", 
        "A fairly strong girl. \nThe head of the local warriors’ guild. \nShe has masochistic tendencies but keeps them hidden.",
        "Don’t go easy on her.",
        "d"
        )

        my_eris = MyCharacter("Eiris", 0, 150,
        "images/characters/eris_ch/mini/eris t_smile.png", 
        "A girl who sharpens her skills every morning at the Training Grounds. \nShe’s determined to get stronger to catch up to some mage.",
        "Train with her and complete her tasks.",
        "eris"
        )
    elif persistent.lang == "russian":
        my_freya = MyCharacter("Фрея", 0, 10000, 
        "images/characters/freya_ch/f smile.png", 
        "Богиня, призвавшая тебя в этот мир, она следит за каждым твоим действием.", 
        "Постарайся \"поступать правильно\" и она тебя отблагодарит. \nТолько знай, что поступать правильно - не всегда лучший путь.",
        "f"
        )
        my_elsa = MyCharacter("Эльза", 0, 500,
        "images/characters/elsa_ch/new/e smile.png", 
        "Ученица великой волшебницы. \nЕе профиль - ледяная магия. \nОна довольно своевольна и резка, но если постараешься ей услужить - она в долгу не останется.",
        "Постарайся выполнять ее задания.",
        "e"
        )
        my_nag = MyCharacter("Нагаторо", 0, 100,
        "images/characters/nagatoro_ch/nag grin.png", 
        "Довольно резкая в высказываниях и любит подраться. \nОна долго оттачивала боевые искусства и свое тело. \nЛюбит поддразнивать.",
        "Постарайся обогнать ее по силе, заметь, она становится лишь сильнее.",
        "nag"
        )
        my_rapunzel = MyCharacter("Рапунцель", 0, 20,
        "images/characters/rapunzel_ch/new/r smile.png", 
        "Игривая и веселая девушка. \nДовольно пошлая в своих выражениях. \nКажется связана с темными личностями.",
        "Тренируй харизму с ней и будет тебе счастье.",
        "r"
        )
        my_tsunade = MyCharacter("Цунаде", 0, 500,
        "images/characters/tsunade_ch/ts smile.png", 
        "Серьезная дама, работает в местой больнице главным врачом. \nИменно она будет лечить тебя, так что лучше придерживаться с ней хороших отношений.",
        "IN PROGRESS",
        "ts"
        )
        my_sakura = MyCharacter("Сакура", 0, 300,
        "images/characters/sakura_ch/s smile.png", 
        "Помошница главного врача в местной больнице. \nБывает злая, но у нее очень доброе сердце.",
        "IN PROGRESS",
        "s"
        )
        my_merlin = MyCharacter("Мерлин", 0, 0,
        "images/characters/merlin_ch/standart/mer smile.png", 
        "Глава Магической башни. \nВеликая волшебница, способная будто на всё.",
        "Постарайся стать умнее, чтобы в любое время иметь возможность найти ее.",
        "mer"
        )
        my_holo = MyCharacter("Холо", 0, 30,
        "images/characters/holo_ch/h smile.png", 
        "Девушка-волчица. Продавщица в одной из лавок на Городском рынке. \nОчень нежная девушка с приятным характером и шикарной фигурой.",
        "Помогай ей на Городском рынке.",
        'h'
        )
        my_miku = MyCharacter("Мику", 0, 40,
        "images/characters/miku_ch/m smile.png", 
        "Светлая девушка, которая держит свою таверну. Разносит напитки, так что почти все время ходит с кружкой пива в руках.",
        "Помогай ей в Таверне.",
        "m"
        )
        my_mao = MyCharacter("Мао Мао", 0, 20,
        "images/characters/maomao_ch/mao smile.png", 
        "Низкая девушка, заведующая своим Борделем. \nНа вид  и не скажешь, но на деле уже взрослая и очень умная.",
        "Приводи девок работать к ней в Бордель, она хорошо оплатит.",
        "mao"
        )
        my_darkness = MyCharacter("Даркнесс", 0, 300,
        "images/characters/darkness_ch/d smile.png", 
        "Довольно сильная девушка. \nГлава местной гильдии войнов. \nИмеет мазохистские наклонности, но скрывает это.",
        "Не жалей ее.",
        "d"
        )
        my_eris = MyCharacter("Эрис", 0, 150,
        "images/characters/eris_ch/mini/eris t_smile.png", 
        "Девушка, которая каждое утро оттачивает свои навыки на Тренировочной площадке. \nОна стремится стать сильнее, чтобы догнать по силе какого-то мага.",
        "Тренируйся и выполняй ее задания.",
        "eris"
        )


init:
    # Инициализация персонажей с соответствующими цветами имен
    
    if persistent.lang == "english":
        define r = Character("Rapunzel", color="#FFBA00", image='r')  # Золотистый (блондинка)
        define e = Character("Elsa", color="#87CEFA", image='e')  # Светло-голубой (платиновая блондинка)
        define nag = Character("Nagatoro", color="#964B00", image='nag')  
        define god = Character("God", color="#B38DF9", image='f')
        define f = Character("Freya", color="#B38DF9", image='f')
        define ts = Character("Tsunade", color="#FFD700", image='ts')
        define s = Character("Sakura", color="#FFC0CB", image='s')
        define mer = Character("Merlin", color="#800080", image='mer')
        define h = Character("Holo", color="#ff8c00", image='h')
        define m = Character('Innkeeper', color="#00ffff", image='m')
        define mao = Character('Mao Mao', color="#006400", image='mao')
        define d = Character('Darkness', color="#c0c0c0", image='d')
        define eris = Character('Eiris', color="#7B1113", image='eris')
        ## Some guys
        define old_woman = Character('Old woman', color="#ffaaaa")
        define guy1 = Character('Guy 1', color="#ffaaaa")
        define guy2 = Character('Guy 2', color="#ffaaaa")
        define guy3 = Character('Guy 3', color="#ffaaaa")
        define sg = Character('Muddy guy', color="#ffaaaa") #shady guy

        define goblin = Character('Goblin', color="#66cc33")
        define hopgoblin = Character('Hop-goblin', color="#66cc33")
        define korg = Character('Korg', color="#ffaaaa")
        define korg_str = 300

        #quest fuckable enemies
        define ent = Character('Ent Girl', color="#013220", image='ent')
        define woblin = Character('Goblin-woman', color="#66cc33", image='woblin')

        #quest persns
        define emilia = Character("Emilia", color="#dda0dd", image='emilia')
        define ramiris = Character('Ramiris', color="#FFBA00", image='ramiris')
        define onna = Character("Onna", color="#FAD7A0", who_outlines=[(2, "#5D4037")], image='onna')

    elif persistent.lang == "russian":
        define r = Character("Рапунцель", color="#FFBA00", image='r')  # Золотистый (блондинка)
        define e = Character("Эльза", color="#87CEFA", image='e')  # Светло-голубой (платиновая блондинка)
        define nag = Character("Нагаторо", color="#964B00", image='nag')  
        define god = Character("Богиня", color="#B38DF9", image='f')
        define f = Character("Фрея", color="#B38DF9", image='f')
        define ts = Character("Цунаде", color="#FFD700", image='ts')
        define s = Character("Сакура", color="#FFC0CB", image='s')
        define mer = Character("Мерлин", color="#800080", image='mer')
        define h = Character("Холо", color="#ff8c00", image='h')
        define m = Character('Тавернщица', color="#00ffff", image='m')
        define mao = Character('Мао Мао', color="#006400", image='mao')
        define d = Character('Даркнесс', color="#c0c0c0", image='d')
        define eris = Character('Эрис', color="#7B1113", image='eris')
        ## Some guys
        define old_woman = Character('Старая щенщина', color="#ffaaaa")
        define guy1 = Character('Парень 1', color="#ffaaaa")
        define guy2 = Character('Парень 2', color="#ffaaaa")
        define guy3 = Character('Парень 3', color="#ffaaaa")
        define sg = Character('Мутный тип', color="#ffaaaa") #shady guy

        define goblin = Character('Гоблин', color="#66cc33")
        define hopgoblin = Character('Хоп-гоблин', color="#66cc33")
        define korg = Character('Корг', color="#ffaaaa")
        define korg_str = 300

        #quest fuckable enemies
        define woblin = Character('Женщина-гоблин', color="#66cc33", image='woblin')
        define ent = Character('Девушка Энт', color="#013220", image='ent')
        
        #quest persns
        define emilia = Character("Эмилия", color="#dda0dd", image='emilia')
        define ramiris = Character('Рамирис', color="#FFBA00", image='ramiris')
        define onna = Character("Онна", color="#FAD7A0", who_outlines=[(2, "#5D4037")], image='onna')
