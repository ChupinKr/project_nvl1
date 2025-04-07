
$ active_quest = no_quest
define hero_name = "Player"
init:
    if persistent.lang == 'russian':
        $ hero_name = "Игрок"
    else:
        $ hero_name = "Player"
define p = Character(hero_name, color="#FFFFFF")
define mind = Character(hero_name + " mind", color="#FFFFFF")

label start:

    if persistent.lang == "russian":
        $setTime(0) #Всего 4 времени (Утро, День, Вечер, Ночь)
    if persistent.lang == "english":
        $setTime(0) #Всего 4 времени (Утро, День, Вечер, Ночь)

    scene bg haven_bright3
    play music "audio/haven.ogg" fadein 5.0 loop
    "Ты был человеком, обыкновенным, может, даже скучным, но с тобой случилось нечто, что лишило тебя жизни."
    "И вот теперь ты оказался в новом, незнакомом месте. Ты не чувствуешь боли, но осознаёшь, что ушёл."
    "Оставил этот мир, оставил свои прошлые заботы. Но где ты сейчас?"
    "Вокруг всё сверкало ярким светом, пронизывающим пространство."
    
    scene bg haven_bright2 with dissolve
    pause .3
    "Со временем тебя окутывала тишина и лёгкость."
    "Как будто ты оказался в самом центре вселенной, в месте, где нет ни времени, ни смерти."
    
    scene bg haven_bright1 with dissolve
    pause .3
    "Ты знал, что это не рай, но и не ад. Это было что-то другое. Что-то странное и волнующее."

    scene bg haven with dissolve
    pause .3
    "И вот, прямо перед тобой, в этом прекрасном зале, появилась она."
    "Высокая, с белыми волосами, с изысканным платьем, которое словно плавно парило в воздухе."

    show f smile with dissolve
    "Она была совершенством, живым воплощением красоты и изящества, не оставляющим равнодушным никого."

    god "Добро пожаловать, дорогой."
    "Её голос был лёгким и тёплым, как мягкий ветерок, ласкающий кожу."
    
    god "Ты оказался в месте, где пересекаются судьбы. Но, не волнуйся, ты не попал в рай."
    god "Здесь, между мирами, я, [f.name], решаю, кто будет перерождён."

    show f closed_smile with dissolve
    "Ты стоял в удивлении, не зная, что сказать. Но она не торопилась, наблюдала за тобой с лёгкой улыбкой на губах."
    
    show f smile with dissolve
    f "Прежде всего, мне нужно узнать, как тебя зовут?"

    # Запрос имени главного героя
    if persistent.lang == "russian":
        $ hero_name = renpy.input("Как тебя зовут?")
        $ hero_name = hero_name.strip() or "Безымянный"
    if persistent.lang == "english":
        $ hero_name = renpy.input("Whats your name?")
        $ hero_name = hero_name.strip() or "Nameless"

    # Создание персонажа с подставленным именем
    $p = Character("[hero_name]", color="#FFFFFF") # Главный герой с именем, выбранным игроком
    if persistent.lang == "russian":
        $mind = Character("Мысли [hero_name]", color="#FFFFFF")  # Мысли ГГ
    if persistent.lang == "english":
        $mind = Character("[hero_name] mind", color="#FFFFFF")  # Мысли ГГ

    p "Меня зовут [hero_name]."  # Главный герой говорит своё имя

    show f smile_shy_hold with dissolve
    f "Я призвала тебя из твоего мира, [hero_name], потому что мне нужна поддержка."  
    f "Я заметила твои \"достоинства\" невооружённым глазом, поверь, я знаю, что не ошиблась~"  

    show f smile with dissolve
    f "Итак, тебе нужно изменить этот мир... Ведь... Он просто угасает..."  
    f "Мне нужен именно ты!"  
    f closed_smile "Возможно, ты станешь великим, даже более великим, чем сам король Эльтираниии~" with dissolve
    f smile "О, ты не знаешь? Это страна, в которой ты переродишься. Очень интересное место, поверь мне~" with dissolve

    f "Ах, но я не могу рассказать тебе всё сразу…"  
    f @smile "Поэтому я призвала тебя~" with dissolve

    p "Что? Но я не..."
    
    show f closed_smile with dissolve
    f "Да, да, да, ты очень польщен и благодарен за такую возможность, я всё понимаю."  
    f "Пускай я и Богиня любви, но я не оставлю тебя одного и дам тебе один Дар."  

    mind "Что вообще происходит?!"

    f "А теперь, [hero_name], ты стоишь перед серьёзнейшим выбором в твоей новой жизни."

    call f_get_info
    jump start_ask_god
