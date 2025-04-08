define first_time_forest_quest_eris_goblin_hunting = True

label forest_quest_eris_goblin_hunting:
    show eris t_smile with dissolve
    if not first_time_forest_quest_eris_goblin_hunting:
        eris t_angry "Эй, в тот раз мы так ничего и не добились!" with dissolve
        eris "Надеюсь в этот раз ты получще подготовился?"
        p "Да..."
    else:
        eris "Вот теперь-то и убедимся, на что ты действительно способен."
        p "..."
    "Мы заходим в темный лес."
    $first_time_forest_quest_eris_goblin_hunting = False
    # Исследование тёмного леса
    call dark_forest_scene
    show eris t_smile with dissolve
    "Лес вокруг был тёмным и плотным. Высокие деревья нависали, почти не пропуская свет."
    
    show eris t_neutral with dissolve
    eris "Гоблины обычно не уходят далеко от своего логова. Надо искать следы."

    menu:
        "Осмотреть землю":
            p "Посмотрим, есть ли следы."
            "Ты присел и начал внимательно осматривать землю."
            "В грязи виднелись небольшие следы — явно не человеческие."
            eris "Они где-то рядом!"
        
        "Прислушаться":
            p "Тсс... Послушаем."
            "Где-то вдали слышалось хихиканье и хруст веток."
            eris "Гоблины... они любят подкрадываться."

    show goblin5 at right,small,darken with dissolve
    show goblin4 at right_mid,small,darken with dissolve
    "Впереди, среди кустов, мелькнули маленькие тёмные фигуры."
    
    show eris t_smile at move_left with dissolve
    eris "О, наконец-то! Давай проверим, кто из нас справится лучше!"
    show goblin5 at normal_size,normal_brightness with dissolve
    show goblin4 at normal_size,normal_brightness with dissolve
    eris "Ты берешь правого, я левого!"
    hide eris with dissolve
    hide goblin4 with dissolve
    play music "audio/tg_sound.ogg" fadein 2.0 loop
    show goblin5 at move_mid with dissolve
    call start_battle(100, 70, goblin.name, 'forest')
    hide goblin5 with dissolve
    play music "audio/forest_evening_night_music.ogg" fadein 2.0 loop
    
    show eris t_smirk at mid with dissolve
    eris "Пф-ф... Они даже не сопротивляются!"

    #Глубже в лес, новые враги
    scene bg dark_forest2 at bg_size with fade
    show eris t_smirk at mid with dissolve
    "Вы двинулись дальше, пробираясь через темный лес в его глубь."
    
    show eris t_angry at move_left_mid with dissolve
    eris "Что-то не так... здесь слишком тихо."
    
    "Как только она это сказала, кусты резко зашевелились."
    show goblin3 at right_mid with dissolve
    "Из темноты выскочил гоблин!"

    eris t_smirk "Ха! Он всего один! {w} Я сама с ним разберусь!" with dissolve
    hide goblin3 with dissolve
    hide eris with dissolve
    play music "audio/tg_sound.ogg" fadein 2.0 loop
    "Началась схватка [my_eris.name] и [goblin.name]. Ты слышишь звуки ударов."
    mind "[my_eris.name] победит, это всего-лишь один маленький гоблин."
    "Пока есть возможность, ты решил расслабиться и посмотреть на то, как природа на самом деле прекрасна..."
    mind "Этот лес...{w} Наверняка когда-то он был прекрасным местом..."
    mind "Как жаль, что гоблины его разорили, при том их так мало."
    mind "Почему раньше никто не охотился на них?{w} Действительно загадка..."
    play music "audio/forest_evening_night_music.ogg" fadein 5.0 loop
    eris "Ай! [hero_name]! Быстрее!"
    "Ты резко оборачиваешься на крик [my_eris.name]"
    show eris t_angry_torn at left_mid with dissolve
    p "[my_eris.name]! Что случилось?!"
    eris "Еще один гоблин напал сзади и он всё еще где-то здесь!"
    show goblin1 at right_mid with vpunch
    $health -= 10
    $customNotify("Тебя ударили в спину")
    if health <= 0:
        jump battle_loss
    p "Черт! Ну всё, больше не убежишь!"
    call start_battle(90, 120, goblin.name, 'forest')
    hide goblin1 with dissolve
    eris t_smile_torn "Отлично!" with dissolve
    eris t_angry_torn_bares "Ай! Кажется во время своей атаки он задел мою ногу!" with dissolve
    eris "Чертовы гоблины!"
    mind "Мне не стоит расслабляться, в таком состоянии [my_eris.name] не сможет сражаться."
    p "Мы уходим!"
    eris t_smile_torn "Пф... Это ерунда. Он уже за это поплатился." with dissolve
    p "В любом случае вокруг уже никого не осталось, давай я тебе помогу."
    show eris t_angry_torn_bares with dissolve
    "Стиснув зубы, [my_eris.name] приняла помощь и вы постепенно выходите из леса."

    call dark_forest_scene
    eris t_angry_torn "Смотри! Впереди!" with dissolve
    p "Только не это..."
    show hopgoblin1 at mid with dissolve
    hopgoblin "Skrig.. Sgrik.."
    p "Черт.. Это будет не просто."
    
    eris t_angry_torn_bares "Вот дерьмо... {w} Я... Сейчас помогу..." with dissolve
    menu:
        "Приказать [my_eris.name] отступить":
            p "[my_eris.name], отойди! Это моя битва."
            $addLove(my_eris, 10)
            eris "Я не привыкла отсиживаться! Но ладно, будь по-твоему."
            hide eris with dissolve
            call start_battle(200, 150, hopgoblin.name, 'forest')
            hide hopgoblin1 with dissolve
        
        "Сражаться вместе":
            p "Вместе у нас больше шансов!"
            $addLove(my_eris, 7)
            eris "Да!Заходи к нему справа, я отвлеку его!"
            call start_battle(100, 150, hopgoblin.name, 'forest')
            hide hopgoblin1 with dissolve
            
    show eris t_smile_torn at mid with dissolve
    eris "Хаха! Мы победили!"

    call forest_eris_root_kiss

    call dark_forest_scene
    show eris t_smile_torn at left_mid with dissolve
    "Вы слышите, как еще больше гоблинов приходят на запах мертвых сородичей."
    show goblin4 at right,small,darken with dissolve
    pause.5
    show goblin5 at right_mid,small,darken with dissolve
    pause.5
    show goblin3 at right_bit,small,darken with dissolve
    show eris t_angry_torn_bares with dissolve

    p "[my_eris.name], ты ранена. Давай спрячемся в той пещере, и перевяжем твою рану."
    eris "Хорошо, только нам нужно смыть с себя их запах, а то они нас учуят"

    call forest_quest_eris_goblin_hunting_cave

    return 

label forest_eris_root_kiss(is_preview=False):
    $setSceneUnlockedFlag('seen_forest_eris_root_kiss')
    call forest_scene_music
    scene bg eris_root_kiss1 at bg_size with fade
    call hide_dialog
    "[my_eris.name] приближается к тебе."
    mind "Она? [my_eris.name] целует меня?!"
    scene bg eris_root_kiss2 at bg_size with dissolve
    pause .5
    scene bg eris_root_kiss3 at bg_size with dissolve
    call hide_dialog
    scene bg eris_root_kiss4 at bg_size with pink
    call hide_dialog
    p "А-а-а, спасибо..."
    scene bg eris_root_kiss5 at bg_size with dissolve
    pause 1
    scene bg eris_root_kiss6 at bg_size with dissolve
    call hide_dialog

    eris "Спасибо тебе, [hero_name]. Ты меня спас и заслужил это."
    return

label eris_root_river_situation(is_preview=False):
    $setSceneUnlockedFlag('seen_eris_root_river_situation')
    call river_scene_music
    scene bg eris_root_river1 at bg_size with fade
    mind "Как же прекрасно её тело."
    scene bg eris_root_river2 at bg_size with dissolve
    mind "Каждый изгиб, [my_eris.name], ты меня дразнишь?"
    scene bg eris_root_river3 at bg_size with dissolve
    mind "Черт, она заметила, что я подглядываю за ней?!"
    scene bg eris_root_river4 at bg_size with dissolve
    eris "Хватит пялиться на меня!"
    scene bg eris_root_river5 at bg_size with dissolve
    pause .5
    scene bg eris_root_river6 at bg_size with flash
    return

label forest_quest_eris_goblin_hunting_cave:
    "Вы тихо уходите и направляетесь к ближайшей речке"
    scene bg river at bg_size with fade
    show eris t_angry_torn with dissolve
    eris "Быстро, смываем с себя запах и уходим!"
    "Вы залезаете в воду."

    call eris_root_river_situation
    $health -= 5
    $customNotify("[my_eris.name] дала тебе хорошую пощечину")
    if health <= 0:
        jump battle_loss
    eris "Ладно, пора идти."
    call steps_sound
    call forest_scene_music
    scene bg river at bg_size with fade
    show eris angry_naked_cover with dissolve
    p "Ты будешь так идти? А если на нас нападут?"
    eris angry_naked_cover_closed_eyes "Да, так и пойду!" with dissolve
    eris angry_naked_cover "Ты же не собираешься отводить от меня взгляд!" with dissolve
    p "..."
    p "А твои вещи я должен нести?!"
    eris angry_naked_cover_closed_eyes "Да, они же мокрые." with dissolve
    eris smile_naked_cover "Или ты хочешь, чтобы я простудилась?" with dissolve
    p "Не хочу...{w} Ладно, идем."
    
    call steps_sound
    call cave_scene_music
    scene bg eris_root_cave0 at bg_size with fade
    play music "audio/cave_music.ogg" fadein 5.0 loop
    "Вы идете заходите в пещеру первым."
    p "Здесь должно быть безопасно..."
    show eris neutral_naked_cover with dissolve
    eris "Черт...{w} Я не думала, что нас так зажмут."
    eris "Pазведи костер, мне холодно."
    scene bg eris_root_cave1 at bg_size with fade
    pause .5
    scene bg eris_root_cave2 at bg_size with fade
    "Ты помогаешь [my_eris.name] сесть. В темноте пещеры свет костра освещает её нежное тело."
    
    scene bg eris_root_cave3 at bg_size with dissolve
    p "Знаешь... Это напоминает мне нашу первую встречу."

    scene bg eris_root_cave3_smile at bg_size with dissolve
    eris "Хах! Ты про тот манекен?"
    "[my_eris.name] вдруг улыбается, забыв на мгновение про усталость и боль."
    
    menu:
        "Пошутить про её силу":
            p "Я тогда всерьёз подумал, что ты решила меня прикончить!"
            scene bg eris_root_cave3_laugh at bg_size with dissolve
            eris "Ну, у тебя была забавная реакция! Я никогда не видела, чтобы кто-то так нелепо уворачивался."
            scene bg eris_root_cave3_smile at bg_size with dissolve
            p "Эй! В том манекене было больше веса, чем во мне!"
            
        "Серьёзно напомнить про тот случай":
            p "Честно, тогда я подумал, что ты ненавидишь новичков."
            scene bg eris_root_cave4 at bg_size with dissolve
            eris "Хех, просто ты оказался в неудачном месте в неудачное время. А ещё у тебя было лицо, которое так и просило пнуть его!"
            scene bg eris_root_cave3_smile at bg_size with dissolve
            p "Спасибо, приятно слышать."
    
    scene bg eris_root_cave3_laugh at bg_size with dissolve
    "Вы оба смеётесь. Смех звучит глухо в каменных стенах, но это даже приятно – напряжение от боя немного уходит."
    
    scene bg eris_root_cave3_say at bg_size with dissolve
    eris "А ты тогда ведь даже не испугался. Ну, почти."
    scene bg eris_root_cave3_smile at bg_size with dissolve
    p "Конечно испугался! Но, думаю, если бы я сразу убежал, ты бы меня ещё сильнее невзлюбила."
    
    scene bg eris_root_cave3_think at bg_size with dissolve
    "[my_eris.name] кивает, задумчиво глядя на стены пещеры."
    
    scene bg eris_root_cave3_think_say at bg_size with dissolve
    eris "А ты ведь изменился с того времени. Теперь я могу рассчитывать на твою поддержку."
    scene bg eris_root_cave3_think at bg_size with dissolve
    p "Так же, как и я на твою."
    
    scene bg eris_root_cave3_smile at bg_size with dissolve
    "Она снова улыбается. Небольшой момент тишины, который вам обоим приятен."

    scene bg eris_root_cave4 at bg_size with dissolve
    eris "Знаешь, [hero_name], я ведь недостаточно тебя отблагодарила..."
    p "Стой. Как же твоя нога?"

    call eris_root_blowjob

    scene bg eris_root_cave23 at bg_size with dissolve
    eris "Гррррр.."
    p "Черт."
    scene bg eris_root_cave24 at bg_size with dissolve
    $health -= 10
    $customNotify("[my_eris.name] зарядила по твоему лицу ногой")
    if health <= 0:
        jump battle_loss
    pause .5
    scene bg eris_root_cave1 at bg_size with flash
    show eris angry_naked_cummed_cover with dissolve
    eris "Будешь думать перед тем, как делать!"
    hide eris with dissolve
    "[my_eris.name] тебя вырубила, ты проспал до утра следующего дня."
    $nextDay()
    scene bg eris_root_cave1 at bg_size with fade
    show eris t_neutral with dissolve
    eris "Проснулся наконец?"
    p "А? Д-да..."
    eris t_smile "Хорошо, пора возвращаться."
    "Снаружи уже виднеется рассвет, вы выходите из пещеры."
    return

label eris_root_blowjob(is_preview=False):
    $setSceneUnlockedFlag('seen_eris_root_blowjob')
    if not is_preview:
        $eris_first_time_root = False
    scene bg eris_root_cave5 at bg_size with dissolve
    "[my_eris.name] прижимаеться к твоей промежности."
    scene bg eris_root_cave6 at bg_size with dissolve
    eris "Я же должна отпратить своему спасителю..."
    scene bg eris_root_cave7 at bg_size with dissolve
    pause .5
    scene bg eris_root_cave8 at bg_size with dissolve
    eris "И как ты его только в штанах мог удержать?{w} Ладно, я постараюсь..."
    scene bg eris_root_cave9 at bg_size with dissolve
    pause .5
    scene bg eris_root_cave10 at bg_size with dissolve
    eris "Мнф?"
    p "Ах, да, продолжай."
    scene bg eris_root_cave11 at bg_size with dissolve
    pause .5
    scene bg eris_root_cave12 at bg_size with dissolve
    "[my_eris.name] берет головку твого члена целиком в рот и начинает двигаться"
    scene bg eris_root_cave13 at bg_size with dissolve
    pause .5
    scene bg eris_root_cave14 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave13 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave14 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave13 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave14 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave13 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave14 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave13 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave14 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave13 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave14 at bg_size with dissolve
    p "Ах... Можешь взять его поглубже?"
    eris "Мнннф."
    
    scene bg eris_root_cave15 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave15 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave17 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave15 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave17 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave15 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave17 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave15 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave17 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave15 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave17 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave15 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave16 at bg_size with dissolve
    pause .1
    scene bg eris_root_cave17 at bg_size with flash

    p "[my_eris.name], я..."
    scene bg eris_root_cave18 at bg_size with flash
    pause .3
    scene bg eris_root_cave19 at bg_size with flash
    pause .3
    scene bg eris_root_cave20 at bg_size with flash
    eris "Мммнфф!"
    scene bg eris_root_cave21 at bg_size with dissolve
    pause .3
    scene bg eris_root_cave22 at bg_size with dissolve
    eris "Аааах!"
    "[my_eris.name] жадно глотает воздух."
    return
