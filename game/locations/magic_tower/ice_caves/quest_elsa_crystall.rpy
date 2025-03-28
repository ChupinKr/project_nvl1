# Встреча с Эмилией в пещерах
label quest_elsa_crystall_start:
    scene bg magic_tower_enterence at Transform(zoom=1.5)  with fade
    "[e.name] говорила, что надо идти на север... Хорошо."
    "Буквально за Магической башней, на Севере ты увидел расположены обмерзшие пещены"
    p "Скорее всего имено сюда мне и нужно."
    call ice_caves_scene
    "Ты заходишь в ледяные пещеры, и холод пробирает до костей."
    mind "Там проход! Кажется я слышу оттуда какие-то звуки."
    "Ты продвигаешься глубже в пещеры."
    scene bg ice_cave_golem1 at Transform(zoom=1.5)  with fade
    p "!!!!"
    "Перед тобой — ледяной голем."
    mind "Кажется он меня пока не заметил, справлюсь ли я с такой громадиной?.."
    menu:
        "Что мне делать?"
        "Сразиться с Ледяным Големом":
            call start_battle(200, renpy.random.randint(300, 400), "Ледяным Големом", 'scene')
            if last_battle_win:
                p "Фух! Каким-то чудом я его победил.."
                $addChar(["str"], 10)
            else:
                "Мне удалось сбежать, надеюсь он не будет меня преследовать.."
        "Попытаться обойти его":
            "Ты решаешь пройти по стеночке, медленно и аккуратно, в надежде, что Голем тебя не заметит"
            if renpy.random.randint(0, 100) > 80:
                mind "Кажется мне очень повезло"
                "Ты проходишь мимо Голема"
            else:    
                call start_battle(200, renpy.random.randint(300, 400), "Ледяным Големом", 'scene')
                if last_battle_win:
                    p "Фух! Каким-то чудом я его победил.."
                    $addChar(["str"], 10)
                else:
                    "Мне удалось сбежать, надеюсь он не будет меня преследовать.."
        "Отвлечь его и пройти мимо" if intelligence >= 100:
            "Ты берешь камень и кидаешь его в стену"
            mind "Ледяной Голем отвлекся, пора идти."
            "Ты успешно проходишь мимо Голема, пока он ищет источник шума"

    "Ты продвигаешься дальше, в глубь пещеры"
    play music "audio/arctic_wind.ogg" fadein 5.0 loop
    scene bg ice_cave_main at Transform(zoom=1.5)  with fade
    emilia "Кто нибудь! Помогите мне!"
    "Ты слышишь, как кто-то зовет на помощь."
    scene bg emilia_captured at Transform(zoom=1.5)  with fade
    "Ты замечаешь девушку, закованную в цепи."
    emilia "Кто... кто ты? Ты пришёл освободить меня или тоже за кристаллом?"
    p "Я [hero_name]. Ищу 'Кристалл зимнего эха'. А ты как здесь оказалась?"
    emilia "Меня зовут [emilia.name]... Я пыталась заполучить кристалл, чтобы усилить свою магию, но эти големы схватили меня."
    emilia "Они... сильнее, чем я думала. Пожалуйста, помоги мне выбраться!"

    menu:
        "Освободить её без условий":
            call free_emilia
        "Предложить сделку":
            call deal_with_emilia
    return

# Вариант 1: Освободить без условий
label free_emilia:
    call ice_caves_scene
    if strength > 50:
        "Ты подходишь к ней и разбиваешь их ударом или магией."
        "[emilia.name] приводит себя в порядок"
    elif intelligence > 50:
        "Ты подходишь к ней и с помощью магии нагреваешь цепи, они разрушаются."
        "[emilia.name] приводит себя в порядок"
    else:
        $customNotify("Недостаточно силы или интеллекта")
        "Ты пытаешься пытаешься сломать цепи, но у тебя ничего не выходит"
        p "Прости, у меня не вышло, удачи тебе!"
        emilia "Стой! Н-но... Как же я?"
        p "Я верю в тебя! Ты должна сама справиться..."
        "Ты видишь что-то мерцающее в углу пещеры"
        mind "Наверняка это то, что мне нужно"
        "Получен 'Кристалл зимнего эха' и уходишь, пока не пришло еще больше големов"
        return

    show emilia smile with dissolve
    emilia "Спасибо, [hero_name]! Я не думала, что кто-то поможет мне просто так."
    p "Не за что. Кристалл всё ещё здесь?"
    emilia "Да, он там, в глубине. Я покажу тебе."
    "[emilia.name] ведёт тебя к кристаллу, её шаги легки, несмотря на усталость."
    scene bg ice_caves_crystall at Transform(zoom=1.5)  with fade
    show emilia smile at left_bit with dissolve
    # Кристалл сияет в центре пещеры
    emilia "Вот он. Бери, ты его заслужил."
    emilia smile_blush "Ещё раз спасибо... Я даже не знаю, как отблагодарить тебя..." with dissolve
    scene bg emilia_kiss1 at Transform(zoom=1.5)  with fade
    pause .5
    scene bg emilia_kiss2 at Transform(zoom=1.5)  with dissolve
    call hide_dialog
    "Она внезапно наклоняется и мягко целует тебя в щёку, её губы прохладны, но нежны."
    scene bg emilia_kiss3 at Transform(zoom=1.5)  with fade
    call hide_dialog
    scene bg ice_caves_crystall_empty at Transform(zoom=1.5)  with fade
    show emilia smile_blush at left_bit with dissolve
    emilia "Будь осторожен, [hero_name]. Может, мы ещё встретимся."
    "Ты расплавляешь лед и забираешь 'Кристалл зимнего эха'."
    p "Надеюсь на это."
    hide emilia with dissolve
    "[emilia.name] уходит в глубину пещер, а ты возвращаешься."
    return

# Вариант 2: Предложить сделку
label deal_with_emilia:
    p "Я могу тебя освободить, но за услугу."
    emilia "Услугу? У меня нет ничего ценного здесь..."
    p "Твоё тело — вполне достаточно. Отдайся мне прямо сейчас, и только потом я разобью цепи."
    scene bg emilia_captured_blush at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Эмилия краснеет, её голос дрожит, повязка на глазах делает её ещё более растерянной."
    emilia "Ты... серьёзно? Я даже не вижу тебя... Но если это твоё условие, я соглашусь."
    emilia "Только обещай, что освободишь меня после. Это мой выбор."
    p "Обещаю. Но сначала ты."

    "Ты срываешь с неё остатки одежды."
    scene bg emilia_sex_chains1 at Transform(zoom=1.5) with fade
    call hide_dialog
    emilia "П-подожди... мы так не договаривались!"
    p "Я освобожу тебя, как только закончу. Ты же хочешь свободы?"
    emilia "Ладно... ты обещал..."
    # Эмилия в цепях, её одежда частично спущена, руки подняты и скованы над головой
    "Цепи звенят, удерживая её руки. [emilia.name] дрожит, её дыхание учащается."
    emilia "Я... сделаю это. Только будь нежен, прошу."
    p "..."

    scene bg emilia_sex_chains2 at Transform(zoom=1.5) with fade
    call hide_dialog
    # Ты расстёгиваешь свою одежду, её ноги слегка раздвинуты, насколько позволяют цепи
    "[emilia.name] наклоняется вперёд, насколько позволяют цепи, пока ты расстёгиваешь штаны. Её тело напрягается."
    p "Ты выглядишь потрясающе, даже в цепях."
    emilia "Не говори так... мне неловко..."

    scene bg emilia_sex_chains2_1 at Transform(zoom=1.5) with fade
    call hide_dialog

    scene bg emilia_sex_chains2_2 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Ты прижимаешь её к холодной земле, кладя свой член на её ягодицы."

    scene bg emilia_sex_chains2_3 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    emilia "Ч-что это? Это... твой член? Он такой горячий..."
    p "Скоро узнаешь."

    scene bg emilia_sex_chains3 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    # Ты входишь в неё, её тело прижато к ледяной стене, цепи звенят от движений
    "Ты водишь головкой члена по её киске. [emilia.name] тихо вздыхает, её голос дрожит."
    emilia "Ах... это... холод и тепло смешиваются..."

    scene bg emilia_sex_chains4 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    # Движения продолжаются, её лицо выражает смесь смущения и удовольствия
    "Ты резко входишь в неё, и [emilia.name] вскрикивает, цепи звенят от её движения."
    emilia "П-пожалуйста... быстрее... я хочу, чтобы ты закончил..."

    scene bg emilia_sex_chains4_1 at Transform(zoom=1.5) with dissolve  
    pause .5
    scene bg emilia_sex_chains4_2 at Transform(zoom=1.5) with dissolve  
    pause .5
    scene bg emilia_sex_chains4_3 at Transform(zoom=1.5) with dissolve  
    pause .3
    scene bg emilia_sex_chains4_2 at Transform(zoom=1.5) with dissolve 
    pause .3
    scene bg emilia_sex_chains4_1 at Transform(zoom=1.5) with dissolve 
    pause .2
    scene bg emilia_sex_chains4_2 at Transform(zoom=1.5) with dissolve 
    pause .2
    scene bg emilia_sex_chains4_3 at Transform(zoom=1.5) with dissolve  
    pause .2
    scene bg emilia_sex_chains4_2 at Transform(zoom=1.5) with dissolve 
    pause .2
    scene bg emilia_sex_chains4_1 at Transform(zoom=1.5) with dissolve  
    pause .1
    scene bg emilia_sex_chains4_2 at Transform(zoom=1.5) with dissolve 
    pause .1
    scene bg emilia_sex_chains4_3 at Transform(zoom=1.5) with flash  
    call hide_dialog

    scene bg emilia_sex_chains5_cum1 at Transform(zoom=1.5) with flash  
    call hide_dialog
    "Ты достигаешь предела, и поток спермы вырывается внутрь неё. [emilia.name] издаёт громкий стон."
    
    scene bg emilia_sex_chains5_cum2 at Transform(zoom=1.5) with flash  
    pause .5
    scene bg emilia_sex_chains5_cum3 at Transform(zoom=1.5) with flash  
    emilia "Ааааах!"

    p "Ещё чуть-чуть."
    scene bg emilia_sex_chains5_cum4 at Transform(zoom=1.5) with flash  
    "Ты выпускаешь ещё один мощный заряд спермы в её киску."
    
    scene bg emilia_sex_chains6_cum1 at Transform(zoom=1.5) with dissolve  
    "Сперма стекает ручьями по её бёдрам, а её лицо выражает экстаз."

    scene bg emilia_sex_chains6_cum2 at Transform(zoom=1.5) with dissolve  
    "Ты вытаскиваешь член, и последние капли спермы падают на её спину."

    scene bg emilia_sex_chains_after at Transform(zoom=1.5) with fade
    emilia "Ты закончил? Теперь освободи меня, как обещал!"

    menu:
        "Освободить [emilia.name]":
            $addLove(my_freya, 10)
            call ice_caves_scene
            if strength > 50:
                "Ты подходишь к ней и одним сильным ударом разбиваешь ледяные цепи."
                "[emilia.name] потирает запястья, приводя себя в порядок."
            elif intelligence > 50:
                "Ты подходишь к ней и, сосредоточившись, используешь магию тепла, чтобы расплавить цепи."
                "[emilia.name] потирает запястья, приводя себя в порядок."
            else:
                $customNotify("Недостаточно силы или интеллекта")
                "Ты пытаешься сломать цепи, но они слишком крепкие для тебя."
                p "Прости, Эмилия, у меня не получается. Желаю удачи!"
                emilia "Стой! Но... как же я останусь здесь?"
                p "Я верю в тебя. Ты сильная, справишься сама..."
                "В углу пещеры ты замечаешь мерцающий свет."
                scene bg ice_caves_crystall at Transform(zoom=1.5) with fade
                mind "Кажется, это то, что мне нужно."
                "Получен 'Кристалл зимнего эха'."
                scene bg ice_caves_crystall_empty at Transform(zoom=1.5) with fade
                "Ты быстро уходишь, пока големы не вернулись."
                return
            show emilia angry with dissolve
            emilia "Кристалл там, в той пещере. Забирай его."
            scene bg ice_caves_crystall at Transform(zoom=1.5) with fade
            "Ты идёшь к кристаллу и берёшь его в руки."
            scene bg ice_caves_crystall_empty at Transform(zoom=1.5) with fade
            show emilia angry at left_bit with dissolve
            emilia "Ты... оказался не таким, как я думала. Но всё же спасибо, что освободил."
            p "До встречи, Эмилия."
            "Она кивает, бросив на тебя хмурый взгляд, и уходит в глубину пещер, пока ты отправляешься в город."

        "Я солгал":
            p "Знаешь, я верю в тебя. Ты сможешь выбраться сама."
            scene bg emilia_sex_chains_after2 at Transform(zoom=1.5) with fade
            emilia "С-стой! Ты же... я только что сделала всё, что ты просил!"
            "Ты замечаешь мерцающий свет в углу пещеры."
            emilia "Нет, пожалуйста, не оставляй меня!"
            scene bg ice_caves_crystall at Transform(zoom=1.5) with fade
            mind "Кажется, это то, что мне нужно."
            "Получен 'Кристалл зимнего эха'."
            scene bg ice_caves_crystall_empty at Transform(zoom=1.5) with fade
            "Ты разворачиваешься и уходишь, пока не появились новые големы."
    return

# Награда от Эльзы
label quest_elsa_crystall_reward:
    call elsa_masturbate_scene
    return
