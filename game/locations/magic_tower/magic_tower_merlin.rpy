define first_mer_root = True
define can_go_mer = True
# Поиск Мерлин (шанс зависит от intelligence)
label find_merlin:
    call magic_tower_scene

    "Я отправился на поиски Мерлин. Она не любит, когда её беспокоят, но, возможно, мне повезёт."

    $ find_chance = intelligence  # Чем выше intelligence, тем выше шанс
    $ roll = renpy.random.randint(1, 100)

    if roll <= find_chance and can_go_mer:
        scene bg magic_library1 with fade
        show mer smirk at center with dissolve
        mer "Ты меня нашёл. Вопрос в том, зачем."
        jump merlin_menu
    else:
        $customNotify("Недостаточно интеллекта")
        "Я бродил по башне, но так и не смог её найти. Видимо, она очень занята."
        "Интересно, что еще инетересного можно найти в башне"
        $nextTime()
        jump magic_tower_hub

label merlin_menu:
    menu:
        "Попросить урок":
            jump mer_teach
        "Приватные уроки" if not first_mer_root:
            call mer_root_menu
            jump merlin_menu
        "Попросить квест":
            show mer neutral with dissolve
            mer "Если хочешь задание – у меня всегда есть кое-что... рискованное."
            "Мерлин хитро улыбнулась и начала рассказывать про квест."
            call merlin_quests
            jump merlin_menu
        "Отказаться от задания" if isActualQuestOfCharacter("mer"):
            p "Я не смогу выполнить это задание."
            mer @smirk "Ожидаемо..."
            $ removeQuest()
            jump merlin_menu
        "Уйти":
            "Я решил не рисковать и оставить Мерлин в покое."
            jump magic_tower_hub

label merlin_quests:
    "IN PROGRESS"
    return

label mer_teach:
    show mer surprised with dissolve
    mer "Ты действительно хочешь учиться? Ну что ж, посмотрим, как долго ты продержишься."
    "Мерлин начала объяснять сложные магические принципы, и мой мозг начал плавиться."
    mer neutral "Итак, ты всё понял? Сможешь повторить то, что я рассказала?"
    call merlin_training
    return
    

label merlin_training:
    call start_magic_knowlenge_training(mer, intelligence)
    if last_magic_knowlenge_win:
        p "Да, без проблем расскажу"
        if intelligence >= 60:
            "Ты слово в слово пересказываешь всё, что рассказала [mer.name], она чувствует, что время было потрачено не зря и проникается к тебе уважением."
            mer @surprised "Удивительно, а ты не безнадежен!"
            $addChar(["intelligence"],10)
            $addLove(my_merlin, 10)
            if first_mer_root and my_merlin_love >= 50:
                mer smile "Не хочешь пройти дополнительный курс? Этот курс сильно укрепит твои знания!"
                menu:
                    mer "Хочешь пройти дополнительный курс?"
                    "Конечно!":
                        p "Само собой, я хочу изучить еще больше!"
                        mer smirk "Тогда следуй за мной."
                        jump mer_root
                    "Не сейчас":
                        p "Сейчас я занят, может чуть позже?"
                        mer annoyed "Раз посмел прийти в магическую башню - у тебя не должно оставаться приоритетов выше изучения магии!"
                        "Внезапно ты перемещаешься в центральную развилку магической башни, она даже не дала тебе оправдаться"
                        play sound "audio/magic_dissapear.ogg"
                        jump magic_tower_hub
            else:
                "Урок закончился и ты очутился в середине развилки магической башни"
                play sound "audio/magic_dissapear.ogg"
                jump magic_tower_hub
        else:
            $customNotify("Необходимо 60 интеллекта")
            "Ты попытался рассказать всё именно так, как говорила [mer.name], но у тебя не вышло"
            $minusLove(my_merlin,-2)
            "[mer.name] выглядит раздраженной"
            "Хорошо, что хоть что-то ты запомнил"
            $addChar(["intelligence"],3)
            mer @sigh "Большего от тебя и не ожидала, всё, я занята, уходи!"
            "Внезапно ты перемещаешься в центральную развилку магической башни, она даже не дала тебе оправдаться"
            play sound "audio/magic_dissapear.ogg"
            jump magic_tower_hub
    else:
        if intelligence >= 50:
            p "Я не понял пару моментов, но в остальном ты мне раскрыла глаза!"
            "[mer.name] рассказывает тебе ту часть, которую сразу у тебя не удалось понять"
            $addLove(my_merlin, 7)
            mer smile "По глазам вижу, теперь то ты всё понял"
            p "Да, спасибо, что разъяснила!"
            $addChar(["intelligence"],5)
            mer "Если вновь появятся вопросы - можешь найти меня и я постараюсь помочь."
            p "Хорошо, еще я бы хотел..."
            "Не успев договорить, ты перемещаешься в центральную развилку магической башни"
            play sound "audio/magic_dissapear.ogg"
            jump magic_tower_hub
        else:
            $customNotify("Необходимо 50 интеллекта")
            p "Я не понял пару моментов, но в остальном ты мне раскрыла глаза!"
            "[mer.name] еще пару часов объясняла тебе структуры магических элементов и разжевывала основны магического сотворения"
            "И даже так ты ничего не понял"
            "Возможно стоит сначала повысить свой интелект.."
            "[mer.name] выглядит раздраженной"
            $minusLove(my_merlin,-3)
            "Жаль, что ты ничего не запомнил"
            mer @sigh "Больше я не собираюсь тратить на тебя свое время!"
            "Внезапно ты перемещаешься в центральную развилку магической башни, она даже не дала тебе оправдаться"
            play sound "audio/magic_dissapear.ogg"
            jump magic_tower_hub
    jump magic_tower_hub
    return

label mer_root:
    scene bg magic_library1 with fade
    show mer smirk at center with dissolve
    mer smirk "Самое время дать тебе приватные уроки."
    if first_mer_root:
        $first_mer_root = False
        mer "Возможно ты не знал, но магические силы можно передавать, ими можно делиться."
        p "Что? Это потрясающе, но как? Я прочитал достаточно и нигде об этом не было ни слова!"
        mer @smile "Да, это мое личное исследование. Но до практики я еще не доходила."
        mer @smirk "Будешь моим испытуемым?"
        menu:
            mer "Будешь моим испытуемым?"
            "Конечно":
                p "Конечно, я пожертвую телом ради науки!"
                mer smile "Это именно то, что я ожидала услышать."
                $addLove(my_merlin, 5)
                jump mer_root_menu
            "Откажусь":
                p "Откажусь, мне не нравится эта идея."
                $ can_go_mer = False
                mer @annoyed "То есть ты мне не доверяешь? Будь по твоему!"
                "Внезапно ты перемещаешься в центральную развилку магической башни, она даже не дала тебе оправдаться"
                $customNotify("Ты больше никогда не встретишь [mer.name]")
                play sound "audio/magic_dissapear.ogg"
                jump magic_tower_hub
    else:
        jump mer_root_menu

label mer_root_menu:
    menu:
        "Мастурбация" if my_merlin_love >= 50:
            call mer_root_masturbate
            jump mer_root_menu
        "Грудями" if my_merlin_love >= 60:
            call mer_root_titfuck
            jump mer_root_menu
        "Минет" if my_merlin_love >= 70:
            call mer_root_blowjob
            jump mer_root_menu
        "Секс" if my_merlin_love >= 80:
            call mer_root_fuck
            jump mer_root_menu
        "Анал" if my_merlin_love >= 90:
            call mer_root_anal
            jump mer_root_menu
        "Фетиш" if my_merlin_love >= 200:
            call mer_root_fetish
            jump mer_root_menu
        "Вернуться":
            mer @smirk "До встречи~"
            play sound "audio/magic_dissapear.ogg"
            jump magic_tower_hub

label mer_root_blowjob:
    scene bg magic_library1 with fade
    show mer holding_breast with fade
    call hide_dialog
    mer "[hero_name], давай сегодня попрбуем кое-что интересное~"
    mer "Тебе нравится моя грудь?"
    menu:
        mer "Тебе нравится моя грудь?"
        "Да, очень":
            p "У тебя чудесная грудь"
            mer smile_holding_breast "Правильный ответ~" with dissolve
        "Нет":
            p "Если честно, не очень, мне нравятся груди поменьше, можешь магией их уменьшить?"
            mer "Нет! Убирайся!" 
            $ can_go_mer = False 
            "Внезапно ты перемещаешься в центральную развилку магической башни, она даже не дала тебе оправдаться"
            $customNotify("Ты больше никогда не встретишь [mer.name]")
            jump magic_tower_hub
    show mer neutral_knee with fade
    call hide_dialog
    "[mer.name] встает на колени, наконец ты можешь хорошо рассмотреть ее широкие беда"
    mer "Ну чего же ты ждешь?"
    mer smile_knee "Раздевайся, или хочешь, чтобы я тебя раздела?" with dissolve
    "Ты снимаешь с себя одежду не отрывая глаз от [mer.name]"
    "[mer.name] же смотрит на то, что скрывалось у тебя в штанах"
    "Ее красивые огромные груди, они всегда были такими большими? Или она подколдовала?"
    "Ты задумался, кажется ты видел заклинание увеличения частей тела? Возможно ли его использовать отдельно на груди? [mer.name] хотела сделать занятие еще приятнее? Вдруг это всё очередной тест, а всё вокруг - магия иллюзий?"
    scene bg mer_suck1 with fade
    call hide_dialog
    p "!!!!!" 
    "Пока ты размышлял [mer.name] обхватила головку твоего члена свими мягкими губами" with vpunch
    p "А-а-ах, [mer.name]."
    "[mer.name] смотрит на тебя, ласково обсасывая головку твоего члена"
    "Ты придерживаешь свой член, чтобы она не выпускала его из ротка"
    "Ты чувствуешь, что [mer.name] полностью взяла головку твоего члена и убираешь руку"
    scene bg mer_suck2 with dissolve
    call hide_dialog
    "У нее такой пронзительный взгляд, возможно она оценивает взором твою магическую энергию?"
    "Нет, выглядит скорее как желание убедиться в том, что она всё делает правильно"
    "Ты видишь, что [mer.name] старается высосать все соки из твоего члена"
    "Соки и слюна сочатся и капают изо рта на пол"
    "[mer.name] явно не хочет, чтобы это быстро закончилось, она берет твой член в руку и немного отдаляется не ослабевая хватку"
    scene bg mer_suck2_5 with dissolve
    call hide_dialog
    p "Уххх, а ты в этом хороша"
    mer "Я фнаю~"
    "Она продолжает жадно обсасывать головку твоего члена, не планируя ослабевать хватку и все также смотрит тебе в глаза"
    "Ты возбуждаешься еще сильнее, [mer.name] каким-то образом это чувствует и двигается вперед по члену"
    scene bg mer_suck3 with dissolve
    call hide_dialog
    "Соков становится всё больше"
    "[mer.name] продолжает обсасывать твой член"
    scene bg mer_suck2 with dissolve
    pause .2
    scene bg mer_suck4 with dissolve
    pause .2
    scene bg mer_suck2 with dissolve
    pause .2
    scene bg mer_suck4 with dissolve
    pause .2
    scene bg mer_suck2 with dissolve
    pause .1
    scene bg mer_suck4 with dissolve
    pause .1
    scene bg mer_suck2 with dissolve
    pause .1
    scene bg mer_suck4 with dissolve
    pause .1
    scene bg mer_suck2 with dissolve
    pause .05
    scene bg mer_suck4 with dissolve
    pause .05
    scene bg mer_suck2 with dissolve
    pause .05
    scene bg mer_suck4 with dissolve
    pause .05
    scene bg mer_suck2 with dissolve
    pause .05
    scene bg mer_suck4 with dissolve
    pause .05
    scene bg mer_suck2 with dissolve
    pause .03
    scene bg mer_suck4 with dissolve
    pause .03
    scene bg mer_suck2 with dissolve
    pause .03
    scene bg mer_suck4 with dissolve
    pause .03
    scene bg mer_suck2 with dissolve
    pause .03
    scene bg mer_suck4 with dissolve
    pause .03
    scene bg mer_suck2 with dissolve
    pause .3
    scene bg mer_suck1 with dissolve
    call hide_dialog
    "Она слегка отдаляется, но что-то тебе подсказывает, что это необходимо"
    "!!!!!"
    scene bg mer_suck5 with dissolve
    call hide_dialog
    p "А-ах, глубокий минет? Обожаю опытных женщин!" with vpunch
    mer "Фаааа"
    "[mer.name] заглотила твой член почти целиком, нужна еще лишь пара усилий"
    "И она их делает"
    scene bg mer_suck6 with dissolve
    call hide_dialog
    "Это лучший глубокий минет в твоей жизни, твой член напрягается еще сильнее"

    scene bg mer_suck5 with dissolve
    pause .2
    scene bg mer_suck6 with dissolve
    pause .2
    scene bg mer_suck5 with dissolve
    pause .2
    scene bg mer_suck6 with dissolve
    pause .2
    scene bg mer_suck5 with dissolve
    pause .1
    scene bg mer_suck6 with dissolve
    pause .1
    scene bg mer_suck5 with dissolve
    pause .1
    scene bg mer_suck6 with dissolve
    pause .1
    scene bg mer_suck5 with dissolve
    pause .05
    scene bg mer_suck6 with dissolve
    pause .05
    scene bg mer_suck5 with dissolve
    pause .05
    scene bg mer_suck6 with dissolve
    pause .05
    scene bg mer_suck5 with dissolve
    pause .05
    scene bg mer_suck6 with dissolve
    pause .05
    scene bg mer_suck5 with dissolve
    pause .03
    scene bg mer_suck6 with dissolve
    pause .03
    scene bg mer_suck5 with dissolve
    pause .03
    scene bg mer_suck6 with dissolve
    pause .03
    scene bg mer_suck5 with dissolve
    pause .03
    scene bg mer_suck6 with dissolve
    pause .03
    scene bg mer_suck5 with dissolve
    call hide_dialog

    p "А-а-ааааах"
    mer "Ммммфффф!"
    "Твой член проникает еще глубже в ее глотку, ты начинаешь кончать"
    scene bg mer_suck_cum1 with flash
    call hide_dialog
    "[mer.name] из всех сил старается не выпускать твой член из горла"
    "Она проглатывает всё, старается не упустить ни капли, но что-то все же вырывается из ее ротика"
    "Ты продолжаешь кончать, [mer.name] этого не ожидала"
    scene bg mer_suck_cum2 with flash
    call hide_dialog
    "Ее глаза начинают закатываться от удовольствия"
    "[mer.name] больше не в состоянии удерживать твой член в глотке, мощная струя спермы выталкивает его"
    scene bg mer_suck_cum3 with flash
    call hide_dialog
    "Сперма начинается сочиться все сильнее из ее горла, которым она все еще пытается удержать твой член"
    "[mer.name] старается изо всех сил, у нее начинают проступать слезы"
    scene bg mer_suck_cum4 with flash
    call hide_dialog
    "Тушь потекла, но она все еще делает всё возможное, чтобы удержать этот безумный член в своем узкомгорле"
    "Она сама для себя решила принять всё, что ты ей дашь, но такого огромного количества спермы она не ожидала"
    "Это только сильнее тебя возбуждает и ты кончаешь с еще большей силой"
    scene bg mer_suck_cum5 with flash
    call hide_dialog
    "Слезы текут по ее щекам, смешавшись с тушью, вся помада размазалась, но это именно то выражение лица, которое ты и хотел видеть"
    p "Получай, сука!"
    mer "Мммммррффффффф!!!"
    p "Не понимаю тебя, принимай глубже, шлюха!"
    "Она больше не подает признаков разумности, твой член полностью заполонил ее голову, единственное, о чем она может думать - о твоем члене"
    "Ты видишь, она старается, но она итак на грани своих возможностей"
    "Наконец ты превзошел ожидания [mer.name], хоть и не в магии"
    scene bg mer_suck_cum6 with flash
    call hide_dialog
    "[mer.name] не смогла полностью удержать этот бешеный поток спермы"
    "Часть спермы попала на ее лицо, смешиваясь со слезами и тушью, и забрызгала ее шикарную грудь"
    scene bg mer_suck_cum7 with dissolve
    call hide_dialog
    "[mer.name] медленно отсраняется от твоего члена, но все еще глотает столько спермы, сколько возможно"
    
    scene bg mer_suck_cum8 with dissolve
    call hide_dialog
    "Поток спермы постепенно ослабевает, она начинает приходить в сознание"
    "Она вернулась к головке, своими нежными губками она отсасывает остатки"
    "Поняв, что извержение наконец закончилось, [mer.name] нежно облизывает головку"

    scene bg mer_suck_cum9 with dissolve
    call hide_dialog
    "Всё вокруг уже покрыто густой теплой спермой, с лица [mer.name] капает сперма прямо на груди и с них на пол"
    "[mer.name], не скрывая радости, смотрит на тебя, полизывая член"
    "Ты видишь, что она собой очень довольна, скорее всего это самый большой член в ее жизни"
    
    scene bg mer_suck_cum10 with dissolve
    call hide_dialog
    "Коснувшись чувствительной части головки - [mer.name] заставлять тебя испустить последнюю порцию"
    "[mer.name] смотрит на твой член с вожделением и старается поймать последнюю струю спермы языком"
    "И успешно с этим справляется, гордо сглатывая"

    scene bg mer_suck_cum11 with dissolve
    call hide_dialog
    "Наконец поняв, что твой член успокоился, [mer.name] вновь переводит свой взгляд на тебя"
    "Она смотрит на тебя с неподдельной улыбкой, понимая, что справилась, это был ее личный экзамен, который она сдала на отлично"
    mer "Никогда не смогу привыкнуть к твоему члену~"
    p "Как ты мне сама же говорила - опыт приходит с практикой."

    scene bg mer_suck_cum_closed1eye with dissolve
    call hide_dialog
    "[mer.name] подмигивает тебе"
    p "Повторим еще?"

    scene bg mer_suck_cum_closed_eyes with dissolve
    call hide_dialog
    "[mer.name], полностью покрытая спермой, одобрительно закрывает глаза и чуть наклоняет голову, еще сильнее прижимаясь к твоему члену"
    mer "Однократные исследования не приводят к результату, [hero_name]."
    p "Я учту это."

    scene bg mer_suck_cum11 with dissolve
    call hide_dialog
    "[mer.name] открывает глаза и чуть отстраняется, понимая, что тестирование закончено и надо зафиксировать результаты"
    mer "На этом закончим, [hero_name]."
    p "Буду рад повторить испытания."
    mer "Ты знаешь, где меня найти."
    "Внезапно ты перемещаешься в центральную развилку магической башни, полностью одетый и чистый, с чувством выполненного долга"
    jump magic_tower_hub


label mer_root_masturbate:
    "IN PROGRESS"
    jump mer_root_menu
label mer_root_titfuck:
    "IN PROGRESS"
    jump mer_root_menu
label mer_root_fuck:
    "IN PROGRESS"
    jump mer_root_menu
label mer_root_anal:
    "IN PROGRESS"
    jump mer_root_menu
label mer_root_fetish:
    "IN PROGRESS"
    jump mer_root_menu