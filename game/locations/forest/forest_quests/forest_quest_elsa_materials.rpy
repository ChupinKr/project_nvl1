define first_time_forest_quest_elsa_materials = True
define can_find_ent = False

label forest_quest_elsa_materials:
    call dark_forest_scene
    "Я вошёл в густой, таинственный лес, где солнечные лучи пробивались сквозь кроны деревьев."
    "В воздухе витал аромат свежей зелени, а где-то вдали раздавался лёгкий звонкий смех."
    "Я слышал легенды об этом месте, где магия переплетается с реальностью."
    "Мои шаги отозвались эхом в тишине, пока я пробирался сквозь заросли."
    if first_time_forest_quest_elsa_materials:
        "Внезапно, между деревьями, что-то шелохнулось."
        mind "Кажется что-то приближается..."
        show ramiris neutral_flying_dark2 with dissolve
        pause .3
        mind "Э-это дух? Или что это?"
        show ramiris neutral_flying_dark1 with dissolve
        pause .3
        mind "Пожалуйста, пускай оно не будет враждебным.."

        ramiris neutral_flying "Эй, ты кто такой? Что ты тут забыл? Если ты пришёл испортить мой лес, уходи сразу!" with dissolve
        mind "!!!!!"
        ramiris blush_hide_panties_mini "Эй, куда ты смотришь?!" with dissolve
        p "А-а, эмм, никуда!"
        menu:
            "Приветливо поздороваться":
                p "Привет! Я просто исследую местность, наслаждаюсь её красотой."
                ramiris "Ой, исследователь, значит? Ха! Смотри, чтоб тебя не съели местные звери!"
            "Спросить о травах":
                p "Я ищу редкие магические травы. Ты знаешь, где их найти?"
                ramiris "О, может, и знаю... Но почему я должна тебе помогать? Вдруг ты какой-нибудь вредитель?"
        
        ramiris crossed_smile_mini "[ramiris.name] задумчиво скрестила руки на груди и пристально посмотрела на меня." with dissolve
        mind "Она уже забыла о том, что я увидел ее трусики? Какая невнимательная фея.."

        menu:
            "Подойти ближе, чтобы завести разговор":
                p "Я осторожно шагнул вперёд, желая узнать больше о тебе и этом лесу."
                ramiris crossed_smile "Ты чего такой смелый? Думаешь, если ты такой высокий, то можешь просто так запугать меня? Ха! Ничего подобного!" with dissolve
                p "Нет, я просто хочу узнать, кто ты и почему здесь правишь."
                ramiris crossed_grin "Ну-ну, поближе, говоришь? Раз уж ты пришёл, то я тебя не отпущу просто так." with dissolve
            "Переосмыслить свой подход":
                p "Может, я был слишком резок, подойду к ней поближе."
                ramiris crossed_smile "Ой, не стесняйся, герой. Лучше быть прямым, чем скрытным." with dissolve
        
        "[ramiris.name] начала медленно кружиться вокруг меня, её взгляд был полон игривого интереса."
        ramiris "Ты знаешь, что в этом лесу я хозяйка? Если хочешь что-то получить, тебе придётся меня заинтересовать."
        p "Заинтересовать? Как именно?"
        

        ramiris crossed_smirk "У меня есть несколько идей. Ты ведь не против немножко развлечений, правда?" with dissolve
        menu:
            "Сказать, что я не против развлечений":
                p "Я открыт для любых удовольствий и приключений."
                ramiris crossed_surprised "Ой, как смело! Тогда посмотрим, насколько ты готов к настоящим испытаниям." with dissolve
            "Сказать, что я предпочитаю разумное общение":
                p "Я предпочитаю сначала поговорить, узнать друг друга, а потом решать, что дальше."
                ramiris "О, ты такой скучный! Но может, даже умным иногда хочется поиграть."
        "Мы остановились у величественного старого дерева, под которым мир казался иным."
        
        ramiris crossed_smile "Слушай, я тебе помогу. Но сначала... давай узнаем друг друга получше." with dissolve
        p "Что ты имеешь в виду, [ramiris.name]?"
        ramiris "Я хочу понять, насколько ты чувствуешь этот лес, его ритм и пульс. Расскажи, что привело тебя сюда?"
        p "Я всегда искал приключения, что-то, что заставляет сердце биться чаще. И вот я здесь, среди магии и опасностей."
        ramiris "Хмм, слова — это пустяк. Действия говорят громче. Сейчас ты докажешь свою решимость."
        "Она приблизилась, её голос стал тихим и проникновенным."
        ramiris "В глубине этого леса, в месте, которое я называю 'Сердце Леса', спрятаны травы, необходимые для создания истинной магии."
        p "И ты готова помочь мне их найти?"
        ramiris "Помочь? Ха! Я помогу лишь тем, кто докажет свою силу и решимость."
        "Наши взгляды встретились, наполненные обещаниями и вызовом."
        p "Как мне доказать, что я достоин твоей помощи?"
    else:
        ramiris "Давно не виделись, пойдем?"

    ramiris "Сначала ты пройдёшь через испытания. Готов?"
    menu:
        "Согласиться на испытание":
            p "Я готов ко всему. Покажи, что у тебя есть."
            ramiris "Отлично. Мое испытание — Лабиринт Заблудших Мыслей. Там ты столкнёшься со своими страхами и желаниями."
        "Спросить подробнее о испытании":
            p "Как ты будешь меня испытывать?"
            ramiris "Его название - Лабиринт Заблудших Мыслей"
            ramiris "Это место, где каждый шаг — выбор между смелостью и страхом. Ты увидишь свои сокровенные тайны."
            p "Звучит опасно..."
        ramiris "Мы уже на месте!"

    "[ramiris.name] взмахнула крыльями, и лес вокруг начал преображаться, окутываясь мистическим туманом."
    scene bg entrance_labyrinth with fade
    "Мы подошли к входу в лабиринт, окутанному мерцающим дымкой."
    ramiris "Внутри тебя ждут твои страхи и желания. Пройди лабиринт, и, возможно, я помогу тебе."
    "Я сделал глубокий вдох и шагнул в туман, оставив позади обычный мир."
    scene bg labyrinth1 with fade
    "Лабиринт оказался не просто местом, а испытанием духа и тела."
    show screen minds1 with dissolve
    pause .15
    show screen minds5 with dissolve
    pause .5
    hide screen minds1 with dissolve
    pause .15
    hide screen minds5 with dissolve
    p "!!!"
    mind "[ramiris.name] не солгала, внутри моей головы звучали голоса!"
    scene bg labyrinth2 with dissolve
    mind "Я прошёл через узкие коридоры, где каждая тень шептала о моих неудачах."
    show screen minds2 with dissolve
    pause .1
    show screen minds3 with dissolve
    pause .5
    hide screen minds2 with dissolve
    pause .1
    hide screen minds3 with dissolve
    mind "Я шел вперед, а время тянулось бесконечно, и я боролся со своими внутренними демонами."
    scene bg labyrinth3 with dissolve
    mind "Кажется я уже близко..."
    p "Арргх!"
    show screen minds1 with dissolve
    pause .2
    show screen minds4 with dissolve
    pause .5
    hide screen minds1 with dissolve
    pause .2
    hide screen minds4 with dissolve
    if intelligence >= 60:
        $addChar(["str"], 10)
    else:
        $customNotify("Необходимо 60 интеллекта")
        "Ты падаешь в обморок не способный подняться"
        $ nextDay()
        $health = 0
        jump surgency_tsunade_cure

    mind "Наконец, измученный, я вышел из лабиринта, чувствуя, как изменился."
    call dark_forest_scene
    show ramiris smile with dissolve
    "У выхода уже ждала [ramiris.name], её взгляд был холоден, но в нём мелькала искра уважения."
    ramiris "Вот и вышел ты. Лабиринт был жесток, не так ли? Но теперь ты знаешь, на что способен."
    p "Это было невероятно... Каждая минута казалась вечностью, и страх был так осязаем."
    ramiris "Теперь, когда ты доказал свою решимость, перейдём к следующему этапу."
    
    "Мы продолжили путь по лесу, обсуждая всё: от великих битв до тайн природы."
    ramiris "Расскажи, какая была твоя самая смелая битва?"
    mind "Лучше немного приукрашу, не рассказывать же ей, как меня избили бродяги..."
    p "Была битва с ордами чудовищ в руинах древнего замка. Каждая секунда была борьбой за жизнь."
    ramiris "Хм, похоже, ты знаешь, что такое риск. Но здесь испытания совсем иные."
    p "Что именно тебя ожидает здесь?"
    ramiris "Скоро ты встретишь Энта — древнее существо, питающееся страхом и падением природы."
    "Мы шли долго, и ожидание казалось мучительным."

    "Наконец, перед нами появились массивные деревья, за которыми скрывалось нечто зловещее."
    hide ramiris with dissolve
    show ent angry at left_bit with dissolve
    "Передо мной появился Разгневанный энт, покрытый мхом и трещинами, из которых сочился яд."
    ramiris "Вот он. Твоя следующая проверка — победить это существо, чтобы доказать свою силу."
    p "Я готов. Пусть судьба решит, кто из нас окажется сильнее."
    call start_battle(200, 100, 'Разгневанный энт', 'next')
    hide ent with dissolve 
    $customNotify("Теперь ты можешь выследить энта в лесу")
    if last_battle_win:
        "С победой я ощутил, как энергия леса вливается в меня, наполняя новыми силами."
        $ addChar(["str"],10)
        if strength > 100:
            menu:
                "Надругаться":
                    call fuck_ent
                    call dark_forest_scene
                    ramiris smile_blush "Вау, не знала, что с ними можно так обойтись..."
                "Отпустить":
                    "Энт сбегает"
        else:
            $customNotify("Необходимо 100 силы")
        $can_find_ent = True
        show ramiris smile with dissolve
        ramiris smile "Ты действительно справился! Может, ты не такой уж и слабак."
    else:
        show ramiris smile with dissolve
        ramiris smile "Я не могу тебя похвалить, но ты выжил, это уже что-то."
    
    
    
    "После боя мы остановились, чтобы перевести дыхание и осмыслить произошедшее."
    if last_battle_win:
        ramiris "Ты доказал свою силу! Каждое испытание — шаг к истинному себе."
    else:
        ramiris "Ты выжил и это главное! Каждое испытание — шаг к истинному себе."
    p "Что будет дальше, [ramiris.name]? Я готов слушать."
    
    ramiris "Дальше я расскажу, где найти магические травы. Но сперва — немного отдыха."
    "Мы подошли к маленькому ручью, где журчание воды успокаивало душу."
    call ramiris_root_river_dialog
    
    scene bg meadow with fade
    show ramiris smile with dissolve

    if charisma > 70:
        "Мы подошли к старому дереву, под которым спряталась небольшая поляна."
        ramiris blush "Здесь, в тишине, я хочу, чтобы ты полностью открыл своё сердце."with dissolve
        ramiris "Почувствуй ритм природы, позволь душе летать свободно. Здесь, в этом месте, мы становимся одним с лесом."
        "С каждым мгновением наша связь становилась крепче, как будто время остановилось."
        menu:
            ramiris "Мы можем связать наши души здесь, на этой чудесной поляне..." with dissolve
            "Связь с [ramiris.name]":
                call fuck_ramiris
                scene bg meadow with fade
                "Ты возвращаешься к поиску магических материалов"
                "Через некоторое время..."
                "..."
                "....."
                show ramiris smile_naked_cummed with dissolve
                ramiris "Ахх, [hero_name], это было замечательно~" with dissolve
                p "Ты же лежала там, совсем без сил?!"
                ramiris "Я уже в порядке. Только мне нужно привести себя в порядок.."
                hide ramiris with dissolve
                pause 1
                show ramiris smile_cummed with dissolve
                mind "Она не вытерла лицо... Ну ладно, так даже лучше."
            "Не сейчас":
                ramiris "Ты прав, не время отдыхать."
    else:
        $customNotify("Необходимо 70 харизмы")

    ramiris "Впереди ещё один этап. Мы должны собрать необходимые тебе травы."
    ramiris "Вот оно, место, где они растут. Будь осторожен, здесь может быть не так спокойно."
    p "Я готов."
    mind "Каждая капля пота и каждый удар судьбы стоят ее тела. [e.name], я обязательно выполню твое задание."
    "Мы остановились, и [ramiris.name] внимательно осмотрела местность."
    ramiris "Смотри, здесь растут редкие травы, впитавшие магию древних времён. Природа говорит с теми, кто умеет слушать."
    p "[ramiris.name], послушай, возможно глупый вопрос, но как мне понять, что я на верном пути?"
    ramiris "Прислушайся к шёпоту ветра, к ритму падающих листьев. Каждая мелочь здесь — знак, который стоит твоего внимания."
    "Мы провели несколько минут в молчании, погружённые в звуки природы."
    p "Я думаю, я понял. Это не просто сбор трав — это путь к себе."
    p "[ramiris.name]... Спасибо за всё, что ты мне открыла."

    call ramiris_root_kiss
    "[ramiris.name] медленно отступила в тень деревьев."
    "Я остался с новыми знаниями, ощущением неизбежного будущего и вкусом её губ на моих."
    p "Я знал, что этот лес изменит меня навсегда."
    p "Возможно, именно здесь начнётся моя истинная история."
    return

label ramiris_root_kiss(is_preview=False):
    scene bg ramiris_kiss1 at bg_size with fade
    "[ramiris.name] посмотрела на меня с теплотой, её глаза отражали свет луны. Её щеки слегка порозовели."
    ramiris "Спасибо тебе, [hero_name], за то, что поверил в магию этого леса."
    "Она сделала шаг ближе, её пальцы легко коснулись моей руки."

    scene bg ramiris_kiss2 at bg_size with dissolve
    "В следующую секунду её губы мягко накрыли мои."
    "Поцелуй был тёплым, наполненным нежностью и скрытой силой."
    "В этот миг весь лес замер, словно сама природа благословляла этот момент."

    scene bg ramiris_kiss1 at bg_size with dissolve
    "Когда она отстранилась, её глаза сияли, а на губах играла загадочная улыбка."
    
    scene bg meadow at bg_size with fade
    show ramiris blush with dissolve
    ramiris "Теперь иди и исполни свою судьбу!"
    return


label ramiris_root_river_dialog(is_preview=False):
    scene bg ramiris_river1 at bg_size with fade
    ramiris "Знаешь, [hero_name], природа умеет лечить даже самые раненые сердца."
    "[ramiris.name] села на мягкую траву, пригласив меня разделить с ней этот миг."
    p "Расскажи, как ты стала хозяйкой этого леса? Какая цена была заплачена за твою силу?"
    scene bg ramiris_river3 at bg_size with dissolve
    ramiris "О, это длинная история, полная кровавых битв и потерь. Но, может, я расскажу тебе немного..."
    scene bg ramiris_river2 at bg_size with dissolve
    "Она задумалась, её взгляд стал тёплым, но с оттенком грусти."
    scene bg ramiris_river3 at bg_size with dissolve
    ramiris "Когда-то я была простой феей, как и многие. Но судьба распорядилась иначе..."
    "[ramiris.name] начала рассказывать свою историю, словно ветер шёпотом передавал древние тайны."
    scene bg ramiris_river4 at bg_size with dissolve
    ramiris "Я родилась здесь, в этом лесу, и природа дала мне силу защищать его."
    scene bg ramiris_river1 at bg_size with dissolve
    p "Значит, ты приняла решение стать его хранительницей?"
    scene bg ramiris_river3 at bg_size with dissolve
    ramiris "Не столько выбор, сколько судьба. Каждая победа и поражение сделали меня тем, кто я есть."
    scene bg ramiris_river1 at bg_size with dissolve
    "Её голос затих, и тишина окутала нас, наполненная воспоминаниями."
    p "Я чувствую, что за каждым твоим словом скрыта боль, но и огромная сила."
    scene bg ramiris_river4 at bg_size with dissolve
    ramiris "Боль и страсть — неразделимы. Они делают нас живыми, если мы умеем с ними обращаться."
    scene bg ramiris_river1 at bg_size with dissolve
    "Мы молчали некоторое время, слушая шум ручья и шелест листвы."
    p "Что для тебя значит любовь, [ramiris.name]?"
    scene bg ramiris_river3 at bg_size with dissolve
    ramiris "Любовь — это огонь, который согревает в холодные ночи, но может обжечь, если им не управлять."
    scene bg ramiris_river1 at bg_size with dissolve
    p "Я никогда не чувствовал такой страсти. С тобой я готов рискнуть всем."
    scene bg ramiris_river3 at bg_size with dissolve
    ramiris "Ты умеешь находить слова... Возможно, ты станешь для меня этим светом."
    scene bg ramiris_river1 at bg_size with dissolve
    "Наши взгляды встретились, и в них мелькнула искра взаимопонимания и ожидания."
    p "Кажется, наше приключение становится чем-то большим, чем просто поиск трав."
    scene bg ramiris_river4 at bg_size with dissolve
    ramiris "Помни, всё имеет свою цену. Каждая радость и каждая боль — часть пути."
    return

label fuck_ent(is_preview=False):
    "Разгневанный энт встает, пускай уже без части брони, но лишь злее"
    show ent prenaked with dissolve
    if not is_preview:
        call start_battle(170, 250, 'Разгневанный энт', 'next')
    if last_battle_win or is_preview:
        show ent naked with dissolve
        ent "Что? Что ты собираешься со мной сделать?"
        p "Оооо, сейчас узнаешь."

        scene ent_fuck1 at bg_size with dissolve
        call hide_dialog
        "Ты опрокидываешь ее на землю, срывая остатки веток с ее головы и тела"
        ent "А-ааааах!"
        
        scene ent_fuck2 at bg_size with dissolve
        call hide_dialog
        mind "Она не сопротивляется.."
        ent "Ах! Ах! Ах!"
        
        scene ent_fuck3 at bg_size with dissolve
        pause .5
        scene ent_fuck2 at bg_size with dissolve
        pause .3
        scene ent_fuck3 at bg_size with dissolve
        pause .3
        scene ent_fuck2 at bg_size with dissolve
        pause .1
        scene ent_fuck3 at bg_size with dissolve
        pause .1
        scene ent_fuck2 at bg_size with dissolve
        pause .1
        scene ent_fuck3 at bg_size with flash
        pause .4
        scene ent_fuck4_1 at bg_size with flash
        call hide_dialog
        p "Аааргх!"

        scene ent_fuck4_2 at bg_size with flash
        call hide_dialog
        ent "Ааааааах~~"
        p "Мы не закончили!"
        
        scene ent_fuck5 at bg_size with flash
        pause .3
        scene ent_fuck4_2 at bg_size with flash
        pause .3
        scene ent_fuck5 at bg_size with flash
        pause .1
        scene ent_fuck4_2 at bg_size with flash
        pause .1
        scene ent_fuck5 at bg_size with flash
        pause .1
        scene ent_fuck4_2 at bg_size with flash
        pause .1
        scene ent_fuck5 at bg_size with flash
        call hide_dialog

        ent "А-аааах~~"
        
        scene ent_fuck6 at bg_size with dissolve
        call hide_dialog
        "Из ее киски сочится сперма"
        
        scene ent_fuck7 at bg_size with dissolve
        call hide_dialog
        "[ent.name] частично покрыта спермой. Ты поднимаешься и тянешься к ее личику"
        
        scene ent_cumming1 at bg_size with dissolve
        call hide_dialog
        p "Твое личико тоже можно удобрить"

        scene ent_cumming2 at bg_size with flash
        pause .4
        scene ent_cumming3 at bg_size with flash
        pause .5
        scene ent_cumming4 at bg_size with flash
        pause .3
        scene ent_cumming4 at bg_size with flash
        call hide_dialog

        scene ent_go1 at bg_size with dissolve
        call hide_dialog
        p "Прощай, теперь это мой лес."

        scene ent_go2 at bg_size with dissolve
        call hide_dialog
        "[ent.name] с тоской смотрит на тебя"

        scene ent_go3 at bg_size with dissolve
        call hide_dialog
        "Она будет ждать тебя..."
    return

label fuck_ramiris(is_preview=False):
    scene bg forest_day with fade
    show ramiris smile with dissolve
    ramiris "Терпение, [hero_name]. Сначала мне нужно убедиться, что ты достоин моего внимания."
    
    scene bg ramiris_undress1 at bg_size with fade
    call hide_dialog
    "[ramiris.name] грациозно взмахивает крыльями и взлетает, паря над землёй."
    "Её волосы струятся по ветру, словно танцуя в солнечных лучах."
    ramiris "Смотри внимательно, смертный~"

    scene bg ramiris_undress2 at bg_size with fade
    call hide_dialog
    "Она пролетает мимо, и вокруг тебя начинают падать части её одежды. [ramiris.name] игриво приподнимает юбку, дразняще показывая свои трусики."
    p "Ты... что задумала?"
    ramiris "Разве не ясно? Я хочу, чтобы ты остался со мной..."

    scene bg ramiris_undress3 at bg_size with fade
    call hide_dialog
    "[ramiris.name] делает ещё один круг, останавливается перед тобой и ловким движением демонстрирует, что трусиков на ней уже нет."
    "Твоё сердце колотится в груди, пока она продолжает соблазнительный танец раздевания."

    scene bg ramiris_undress4 at bg_size with fade
    call hide_dialog
    "Наконец она сбрасывает платье полностью, и её крылья мерцают в лучах солнца, подчёркивая изящество обнажённого тела."
    ramiris "Ну, как тебе? Нравится?"
    p "Ты... просто невероятна."
    ramiris "Тогда подойди ко мне ближе, мой милый смертный. Я жажду тебя."

    scene bg ramiris_undress5 at bg_size with fade
    call hide_dialog
    "[ramiris.name] мягко опускается на траву, маняще глядя на тебя и приглашая присоединиться."
    ramiris "Как тебе такой вид, [hero_name]?"
    "Её зов слишком силён, чтобы сопротивляться, и ты опускаешься к ней."

    scene bg ramiris_sex1 at bg_size with fade
    call hide_dialog
    "Ты наклоняешься над ней, а [ramiris.name] смотрит на тебя с предвкушением."
    ramiris "Ну же, покажи мне, на что ты способен!"

    scene bg ramiris_sex2 at bg_size with fade
    call hide_dialog
    "Ты достаёшь свой член — он уже твёрдый и готовый."
    ramiris "Ах... это что, уже?!"

    scene bg ramiris_sex3_0 at bg_size with dissolve
    call hide_dialog
    "[ramiris.name] раздвигает ноги и прижимается к твоему огромному члену, её дыхание учащается."
    ramiris "Ох, боги... он такой большой..."

    scene bg ramiris_sex3_1 at bg_size with dissolve
    call hide_dialog
    p "Не бойся, просто погладь его своими маленькими ручками, прижмись поближе."

    scene bg ramiris_sex3_2 at bg_size with dissolve
    call hide_dialog
    "[ramiris.name] послушно обхватывает твой член обеими руками, её пальцы дрожат от волнения."

    scene bg ramiris_sex4 at bg_size with dissolve
    call hide_dialog
    ramiris "Тебе... нравится это?"
    
    scene bg ramiris_sex5 at bg_size with dissolve
    call hide_dialog
    p "О да, это потрясающе!"

    scene bg ramiris_sex6 at bg_size with dissolve
    call hide_dialog
    "[ramiris.name] слегка улыбается, в её глазах мелькает озорная искорка, словно она задумала нечто большее."

    scene bg ramiris_sex7 at bg_size with dissolve
    call hide_dialog
    "Она наклоняется ближе, прижимаясь лицом к твоему члену, её дыхание обжигает кожу."
    ramiris "А что, если я попробую вот так?.."
    
    scene bg ramiris_sex8 at bg_size with dissolve
    call hide_dialog
    "[ramiris.name] начинает медленно облизывать твой член, её язычок скользит по поверхности."

    scene bg ramiris_sex9 at bg_size with dissolve
    call hide_dialog
    ramiris "Ммм... вкусно..."

    scene bg ramiris_sex8 at bg_size with dissolve
    pause .3
    scene bg ramiris_sex9 at bg_size with dissolve
    pause .3
    scene bg ramiris_sex8 at bg_size with dissolve
    pause .2
    scene bg ramiris_sex9 at bg_size with dissolve
    pause .2
    scene bg ramiris_sex8 at bg_size with dissolve
    pause .1
    scene bg ramiris_sex9 at bg_size with dissolve
    call hide_dialog

    scene bg ramiris_sex10 at bg_size with flash
    call hide_dialog
    "Не выдержав её ласк, ты выпускаешь небольшую струйку спермы."
    
    scene bg ramiris_sex11 at bg_size with dissolve
    call hide_dialog
    ramiris "Чтооо? Ты уже? Это всё?!"

    scene bg ramiris_sex12 at bg_size with dissolve
    call hide_dialog
    "[ramiris.name] не сдаётся: она проводит руками вдоль твоего ствола, и он снова становится твёрдым."
    ramiris "Ого, тебе правда так нравится, [hero_name]?"
    
    scene bg ramiris_sex13 at bg_size with dissolve
    call hide_dialog
    ramiris "Он всё ещё стоит... и что мне теперь с ним делать?"
    
    scene bg ramiris_sex14 at bg_size with dissolve
    call hide_dialog
    p "У меня есть одна мысль..."
    ramiris "Ох, что ты задумал?!"

    scene bg ramiris_sex15_0 at bg_size with dissolve
    call hide_dialog
    "Ты прижимаешь [ramiris.name] к своему члену, её маленькое тело дрожит от твоих движений."
    "Ты начинаешь использовать её тело, скользя вдоль него."

    scene bg ramiris_sex15_1 at bg_size with dissolve
    call hide_dialog
    p "[ramiris.name]... ты такая узкая и горячая."
    ramiris "Давай... не останавливайся, прошу!"
    pause .3
    scene bg ramiris_sex15_2 at bg_size with dissolve
    pause .3
    scene bg ramiris_sex15_1 at bg_size with dissolve
    pause .3
    scene bg ramiris_sex15_2 at bg_size with dissolve
    pause .3
    scene bg ramiris_sex15_1 at bg_size with dissolve
    pause .2
    scene bg ramiris_sex15_2 at bg_size with dissolve
    pause .2
    scene bg ramiris_sex15_1 at bg_size with dissolve
    pause .2
    scene bg ramiris_sex15_2 at bg_size with dissolve
    pause .1
    scene bg ramiris_sex15_1 at bg_size with dissolve
    pause .1
    scene bg ramiris_sex15_2 at bg_size with dissolve
    call hide_dialog

    scene bg ramiris_sex16_1 at bg_size with flash
    pause .5
    scene bg ramiris_sex16_2 at bg_size with flash
    pause .5
    scene bg ramiris_sex16_3 at bg_size with flash
    call hide_dialog
    ramiris "А-а-ааах!"
    "[ramiris.name] дрожит всем телом, достигая оргазма от твоих движений."

    p "Теперь ты точно готова."
    scene bg ramiris_sex17 at bg_size with dissolve
    call hide_dialog
    "Ты с силой входишь в её узкую киску, заполняя её целиком."

    scene bg ramiris_sex17_1 at bg_size with dissolve
    pause .3
    scene bg ramiris_sex17_2 at bg_size with dissolve
    pause .3
    scene bg ramiris_sex17_1 at bg_size with dissolve
    pause .2
    scene bg ramiris_sex17_2 at bg_size with dissolve
    pause .2
    scene bg ramiris_sex17_1 at bg_size with dissolve
    pause .1
    scene bg ramiris_sex17_2 at bg_size with dissolve
    call hide_dialog

    scene bg ramiris_sex17_cum1 at bg_size with flash
    pause .5
    scene bg ramiris_sex17_cum2 at bg_size with flash
    pause .5
    scene bg ramiris_sex17_cum3 at bg_size with flash
    pause .5
    scene bg ramiris_sex17_cum4 at bg_size with flash
    call hide_dialog
    p "Аааргх!"
    "Ты извергаешь поток спермы, заполняя её до краёв. Она вытекает из всех щелей, стекая по её телу."
    
    scene bg ramiris_go0 at bg_size with fade
    call hide_dialog
    "Ты бережно опускаешь её на землю — [ramiris.name] лежит, полностью покрытая твоей спермой."
    
    scene bg ramiris_go1 at bg_size with dissolve
    call hide_dialog
    "Она приходит в себя, пытаясь что-то сказать сквозь усталость."
    ramiris "М-мглф... ф-ф..."
    
    scene bg ramiris_go2 at bg_size with dissolve
    call hide_dialog
    "[ramiris.name] слабо шевелится, пытаясь подняться, но силы покинули её."
    
    scene bg ramiris_go3 at bg_size with dissolve
    call hide_dialog
    p "До встречи, [ramiris.name]. Мы ещё увидимся!"
    "Ты разворачиваешься и уходишь, оставляя её на поляне."
    "[ramiris.name] смотрит тебе вслед, зная, что будет ждать твоего возвращения."

    return