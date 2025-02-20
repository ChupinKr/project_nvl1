define is_free_dance = True
label rapunzel_brothel_first_visit:
    scene bg tavern with fade
    pause 3.5
    show r smile at right with dis5
    p "Это место не особо похоже на то, что ты описывала."
    $updateCanVisit("tavern", True)
    r @smile_shy "Мы еще не пришли, идем, за мной!"
    "Мы заходим в туалет, а там уже открываем потайную дверь"
    
    scene bg brothel_girl1 with dis5
    show r smile at right with dis5
    $updateCanVisit("brothel", True)
    "Меня ослепили диковинные для этих мест, фиотеловые огни"
    "Это действительно похоже на современный бордель, на что только не идут люди, чтобы повеселиться, магия и тут пригодилась"
    p "У меня нет слов, это лучшее место в этом городе!"
    p "Подойжди! А это разве законно? Нас не арестуют за посещение таких заведений?"
    r @open_smile "Да расслабься, [hero_name], я тут не раз бывала, как видишь, жива и свободна"
    p "Я вижу, всё выглядит просто потрясающе, но для чего ты меня сюда привела?"
    r @open_smile "Пойдем к Мам... то есть к старшей, обсудим план действий, она должна заметить твой потенциал!"
    p "Какой еще потенциал? Ты все твердишь про него, но я даже не понимаю, о чем ты!"
    "Мне кажется она ненормальная"
    if chosen_blessing.name == available_blessings[2].name:
        "Хотя, возможно, это из-за дара от Богини"
        "Да, наверняка дело в нем, надо будет ее проведать, поблагодарить еще раз, чудесный дар"
    r @open_smile "Хватит задавать глупые вопросы! Вот же она, наша [mao.name]!"
    
    mao @smirk "[r.name], просила же тебя девок приводить, а ты мужика привела, зачем он мне тут?"
    r @smirk "Мне пора идти, [hero_name], увидимся ~"
    hide r with dis5
    show mao neutral at right_bit with dis5
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
    mao @open_smile "Тише, тише, а то нас в баре услышат. Тебе и не надо, я говорю о том, чтобы приглашать девушек работать у нас."
    mao smile "Звучит интереснее, да? А мы тебе монет отсыпем за каждую."
    p "А как же стража? Если меня поймают? Или вовсе решат казнить?"
    mao smirk "А ты хорошо тогруешься, [hero_name]! Убедил, бонусом посещение моего борделя бесплатно!"
    p "ДОГОВОРИЛИСЬ!" 
    $can_invite_brothel = True
    $customNotify("Теперь вы можете приглашать девушек на работу в Бордель")
    mao smile "Понимаю, что дело это не быстрое, особенно для красавиц здешних. Но я верю в тебя!"
    mao "Когда поймешь, что у тебя есть шанс пригласить девушку работать у нас - можешь подойти ко мне и я позволю ей войти, иначе девушка никак к нам не попадет."
    mao "Наверняка ты не заметил того бугая на входе, вот с ним лучше не спорить!"
    "Ты оборачиваешься и по спине прибегают мурашки, это явно не один из тех мужиков, которых ты видел ранее"
    "Под 3 метра ростом, кажется, будто он великан"
    mao @open_smile "Хаха! Страшно, да? Грозный охранник, это Корг, полувеликан."
    "В этом мире ты раньше не встречал великанов, но теперь у тебя даже пропало желание их когда-либо встречать"
    "Кажется, что при желании он сможет сжать твою голову в одной рукой, да так, что она лопнет"
    mao "По условиям договорились, по цене - зависит от дамы, надеюсь на продуктивное сотрудничество!"
    "Вы жмете руку [mao.name]"
    jump brothel

label brothel:
    $ girl = renpy.random.randint(1, 100)
    if girl < 20:
        scene bg brothel_girl1 with fade
    if girl >= 20 and girl < 40:
        scene bg brothel_girl2 with fade
    if girl >= 40 and girl < 60:
        scene bg brothel_girl3 with fade
    if girl >= 60 and girl < 80:
        scene bg brothel_girl4 with fade
    if girl >= 80 and girl < 100:
        scene bg brothel_girl5 with fade

    "Вы в борделе, сюда всегда приятно заглянуть!"
    jump brothel_menu

label brothel_menu:
    menu:
        "Подойти к [mao.name]" if can_go_mao:
            jump visit_mao
        "Найти [r.name]" if can_go_r:
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
                        "Свалить":
                            "Ты отходишь от [krog.name]"
                            jump brothel
                        "Драться":
                            call start_battle(200, korg_str , krog.name, 'brothel')
                            if last_battle_win:
                                mind "Я победил, но что мне с ним делать дальше?"
                                menu:
                                    "Унизить":
                                        call fuck_krog
                                        "[krog.name] был прилюдно унижен, все девушки видели это"
                                        jump brothel_girl_menu
                                    "Отпустить":
                                        p "На этот раз я тебя прощаю, но лучше не лезь ко мне, [krog.name]"
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