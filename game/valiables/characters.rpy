init python:
    class MyCharacter:
        def __init__(
            self, 
            in_name, 
            in_love, 
            in_strength,
            in_img,
            in_desc,
            in_notice
        ):

            self.name = in_name  # Имя
            self.love = in_love  # Симпатия
            self.str = in_strength  # Сила
            self.img = in_img  # Картинка
            self.desc = in_desc  # Описание
            self.notice = in_notice  # Совет

        
    my_freya = MyCharacter("Фрея", 0, 10000, 
    "images/characters/freya_ch/f smile.png", 
    "Богиня, призвавшая тебя в этот мир, она следит за каждым твоим действием.", 
    "Постарайся \"поступать правильно\" и она тебя отблагодарит. \nТолько знай, что поступать правильно - не всегда лучший путь."
    )
    my_elsa = MyCharacter("Эльза", 0, 500,
    "images/characters/elsa_ch/new/e smile.png", 
    "Ученица великой волшебницы. \nЕе профиль - ледяная магия. \nОна довольно своевольна и резка, но если постараешься ей услужить - она в долгу не останется.",
    "Постарайся выполнять ее задания."
    )
    my_nag = MyCharacter("Нагаторо", 0, 100,
    "images/characters/nagatoro_ch/nag grin.png", 
    "Довольно резкая в высказываниях и любит подраться. \nОна долго оттачивала боевые искусства и свое тело. \nЛюбит поддразнивать.",
    "Постарайся обогнать ее по силе, заметь, она становится лишь сильнее."
    )
    my_rapunzel = MyCharacter("Рапунцель", 0, 20,
    "images/characters/rapunzel_ch/new/r smile.png", 
    "Игривая и веселая девушка. \nДовольно пошлая в своих выражениях. \nКажется связана с темными личностями.",
    "Тренируй харизму с ней и будет тебе счастье."
    )
    my_tsunade = MyCharacter("Цунаде", 0, 500,
    "images/characters/tsunade_ch/ts smile.png", 
    "Серьезная дама, работает в местой больнице главным врачом. \nИменно она будет лечить тебя, так что лучше придерживаться с ней хороших отношений.",
    "IN PROGRESS"
    )
    my_sakura = MyCharacter("Сакура", 0, 300,
    "images/characters/sakura_ch/s smile.png", 
    "Помошница главного врача в местной больнице. \nБывает злая, но у нее очень доброе сердце.",
    "IN PROGRESS"
    )
    my_merlin = MyCharacter("Мерлин", 0, 0,
    "images/characters/merlin_ch/standart/mer smile.png", 
    "Глава Магической башни. \nВеликая волшебница, способная будто на всё.",
    "Постарайся стать умнее, чтобы в любое время иметь возможность найти ее."
    )
    my_holo = MyCharacter("Холо", 0, 30,
    "images/characters/holo_ch/h smile.png", 
    "Девушка-волчица. Продавщица в одной из лавок на Городском рынке. \nОчень нежная девушка с приятным характером и шикарной фигурой.",
    "Помогай ей на Городском рынке."
    )
    my_miku = MyCharacter("Мику", 0, 40,
    "images/characters/miku_ch/m smile.png", 
    "Светлая девушка, которая держит свою таверну. Разносит напитки, так что почти все время ходит с кружкой пива в руках.",
    "Помогай ей в Таверне."
    )
    my_mao = MyCharacter("Мао Мао", 0, 20,
    "images/characters/maomao_ch/mao smile.png", 
    "Низкая девушка, заведующая своим Борделем. \nНа вид  и не скажешь, но на деле уже взрослая и очень умная.",
    "Приводи девок работать к ней в Бордель, она хорошо оплатит."
    )
    my_darkness = MyCharacter("Даркнесс", 0, 300,
    "images/characters/darkness_ch/d smile.png", 
    "Довольно сильная девушка. \nГлава местной гильдии войнов. \nИмеет мазохистские наклонности, но скрывает это.",
    "Не жалей ее."
    )
    my_eris = MyCharacter("Эрис", 0, 150,
    "images/characters/eris_ch/mini/eris t_smile.png", 
    "Девушка, которая каждое утро оттачивает свои навыки на Тренировочной площадке. \nОна стремится стать сильнее, чтобы догнать по силе какого-то мага.",
    "Тренируйся и выполняй ее задания."
    )

init:
    # Инициализация персонажей с соответствующими цветами имен
    define r = Character("Рапунцель", color="#FFBA00", image='r')  # Золотистый (блондинка)
    define my_rapunzel.love = 0
    define e = Character("Эльза", color="#87CEFA", image='e')  # Светло-голубой (платиновая блондинка)
    define my_elsa.love = 0
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
    define guy1 = Character('Парень 1', color="#ffaaaa")
    define guy2 = Character('Парень 2', color="#ffaaaa")
    define guy3 = Character('Парень 3', color="#ffaaaa")
    define sg = Character('Мутный тип', color="#ffaaaa") #shady guy

    
    define korg = Character('Корг', color="#ffaaaa")
    define korg_str = 300
    #quest persns
    define ent = Character('Девушка Энт', color="#013220", image='ent')
    define emilia = Character("Эмилия", color="#dda0dd", image='emilia')
    define ramiris = Character('Рамирис', color="#FFBA00", image='ramiris')