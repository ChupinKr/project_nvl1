define is_free_dance = True
label rapunzel_brothel_first_visit:
    call tavern_scene
    pause 3.5
    show r smile at right with dissolve
    p "Это место не особо похоже на то, что ты описывала."
    if not canVisit("tavern"):
        $updateCanVisit("tavern", True)
    r @smile_shy "Мы еще не пришли, идем, за мной!" with dissolve
    "Мы заходим в туалет, а там уже открываем потайную дверь"

    play sound "audio/door_enter.ogg"
    scene bg brothel_girl1 at bg_size with dissolve
    play music "audio/brothel_sound.ogg" fadein 2.0 loop
    show r smile at right with dissolve
    
    if not canVisit("brothel"):
        $updateCanVisit("brothel", True)
    "Меня ослепили диковинные для этих мест, фиотеловые огни"
    mind "Это действительно похоже на современный бордель, на что только не идут люди, чтобы повеселиться, магия и тут пригодилась?"
    p "У меня нет слов, это лучшее место, что я видел!"
    mind "Я ведь не был в подобных местах в прошлой жизни.."
    p "Подожди! А это разве законно? Нас не арестуют за посещение таких заведений?"
    r @open_smile "Да расслабься, [hero_name], я тут не раз бывала, как видишь, жива и здорова."
    p "Я вижу, всё выглядит просто потрясающе, но для чего ты меня сюда привела?"
    r @open_smile "Пойдем к Ма... то есть к старшей, обсудим план действий, она должна заметить твой потенциал!"
    p "Какой еще потенциал? Ты все твердишь про него, но я даже не понимаю, о чем ты!"
    "Мне кажется она ненормальная"
    if chosen_blessing.name == available_blessings[2].name:
        "Хотя, возможно, это из-за дара от Богини"
        "Да, наверняка дело в нем, надо будет ее проведать, поблагодарить еще раз, чудесный дар"
    r @open_smile "Хватит задавать глупые вопросы! Вот же она, наша [mao.name]!"
    
    mao @smirk "[r.name], просила же тебя девок приводить, а ты мужика привела, зачем он мне тут?"
    r @smirk "Мне пора идти, [hero_name], увидимся ~"
    hide r with dissolve
    show mao neutral at right_bit with dissolve
    mao "Неужели эта аура исходит от тебя, юноша? Эй, как звать то тебя?"
    p "Меня [hero_name] зовут, меня сюда силой притащила [r.name], я вообще не при делах."
    if hero_name == "master" or hero_name == "daddy":
        mao @open_smile "А имя то говорящее! Подстать ауре!"
    else:
        mao "Для такой сильной ауры имя можно было бы подобрать и получше!"
    mao "Так, [hero_name], смотри какое дело, от нас сейчас ушло довольно много девиц, а работать кому-то надо."
    p "Я"
    p "НЕ"
    p "БУДУ"
    p "ЭТИМ ЗАНИМАТЬСЯ!!!"
    mao @open_smile "Тише, тише, а то нас в таверне услышат. Тебе и не надо, я говорю о том, чтобы приглашать девушек работать у нас." with dissolve
    mao smile "Звучит интереснее, да? А мы тебе монет отсыпем за каждую." with dissolve
    p "А как же стража? Если меня поймают? Или вовсе решат казнить?" with dissolve
    mao smirk "А ты хорошо тогруешься, [hero_name]! Убедил, бонусом посещение моего борделя бесплатно!" with dissolve
    p "ДОГОВОРИЛИСЬ!" 
    $can_invite_brothel = True
    $customNotify("Теперь вы можете приглашать девушек на работу в Бордель")
    mao smile "Понимаю, что дело это не быстрое, особенно для красавиц здешних. Но я верю в тебя!" with dissolve
    mao "Когда поймешь, что у тебя есть шанс пригласить девушку работать у нас - можешь подойти ко мне и я позволю ей войти, иначе девушка никак к нам не попадет."
    mao "Наверняка ты не заметил того бугая на входе, вот с ним лучше не спорить!"
    "Ты оборачиваешься и по спине прибегают мурашки, это явно не один из тех мужиков, которых ты видел ранее"
    "Под 3 метра ростом, кажется, будто он великан"
    mao @open_smile "Хаха! Страшно, да? Грозный охранник, это Корг, полувеликан." with dissolve
    "В этом мире ты раньше не встречал великанов, но теперь у тебя даже пропало желание их когда-либо встречать"
    "Кажется, что при желании он сможет сжать твою голову одной рукой, да так, что она лопнет"
    mao "По условиям договорились, по цене - зависит от дамы, надеюсь на продуктивное сотрудничество!"
    "Вы жмете руку [mao.name]"
    $nextTime()
    jump brothel

label brothel:
    call brothel_scene

    "Вы в борделе, сюда всегда приятно заглянуть!"
    jump brothel_menu

label brothel_menu:
    menu:
        "Подойти к [mao.name]" if can_go_mao:
            jump visit_mao
        "Найти [r.name]" if can_go_r:
            if (isNight() or isEvening()):
                "Ты ее не находишь, стоит поискать ее в лесу"
                $customNotify("[r.name] можно найти в Борделе только вечером или ночью")
            jump rapunzel_brothel
        "Посмотреть танец":
            if not is_free_dance:
                korg "Сначала оплата, танец потом"
                if money >= 10:
                    $minusMoney(10)
                    korg "Можешь проходить."
                    jump brothel_girl_menu
                else:
                    korg "Ты без денег, проваливай!"
                    menu:
                        korg "Ты без денег, проваливай!"
                        "Свалить":
                            "Ты отходишь от [krog.name]"
                            jump brothel
                        "Драться":
                            call start_battle(200, korg_str , krog.name, 'brothel')
                            if last_battle_win:
                                mind "Я победил, но что мне с ним делать дальше?"
                                menu:
                                    "Что мне с ним делать дальше?"
                                    "Унизить":
                                        call fuck_krog
                                        "[krog.name] был прилюдно унижен, все девушки видели это"
                                    "Отпустить":
                                        p "На этот раз я тебя прощаю, но лучше не лезь ко мне, [krog.name]"
                            $nextTime()
                            jump brothel_girl_menu
            else:
                jump brothel_girl_menu
        "Уйти":
            jump tavern

label fuck_krog:
    "IN PROGRESS"
    return
            
label brothel_girl_menu:
    "IN PROGRESS"
    menu:
        "Уйти":
            jump brothel_menu