# Сюжет:
# 1. ГГ с [my_eris.name] заходят в деревню и находят старейшину деревни(красивая женщина средних лет).
# (от него можно получить информацию о том, что происходит и о слабостях дракона, если припугнуть силой)
# 2. Далее над ГГ и [my_eris.name] пролетает тот самый дракон и приземляется у поля рядом с деревней
# 3. ГГ и [my_eris.name] бегут на поле, находят дракона и начинается бой
# 4. Персонажи успешно справляются с противостоянием дракона, он улетает.
# 5. [my_eris.name] предлагает догнать дракона и убедиться, что он больше никому не навредит.
# 6. ГГ с [my_eris.name] поднимаются на большую гору, на одной из скал находится драконье гнездо, там лежит спит тот самый дракон, охраняя драконьи яйца.
# 7. Дракон проснулся, начинается еще более ожесточенный бой с драконом, Дракон вырубает [my_eris.name] мощным ударом хвостом. ГГ побеждает дракона. ГГ срубает драконий рог.
# 8 Из яйца дракона вылупляется существо, похожее на человека, но с красной кожей и хвостом.
# 9. Выбор: Убить/Пощадить детеныша дракона
# 10. Если пощадили - Знакомство с существом, оно уже может говорить(драконьи дети рождаются сразу очень умными).
# 11. ГГ исцеляет [my_eris.name] с помощью зелья, она приходит в себя.
# 12. Герои возвращаются в гильдию, чтобы сдать квест. Вознаграждение делится пополам.  [my_eris.name] благодарит ГГ за спасение, ведь это второй раз, как он ее спас.
# 13. ГГ возвращается в город.

define dragon_fight_field_first_time = True
define dragon_fight_mountain_first_time = True

label village_quest_eris_dragon_hunting:
    if not dragon_fight_mountain_first_time:
        call dragon_mountain
        call return_village_quest_eris_dragon_hunting
    elif not dragon_fight_field_first_time:
        call dragon_fight_field
        call dragon_mountain
        call return_village_quest_eris_dragon_hunting
    else:
        call village_enter
        call dragon_fight_field
        call dragon_mountain
        call return_village_quest_eris_dragon_hunting
    return

# ГГ с [my_eris.name] заходят в соседнюю деревушку
label village_enter:
    call village_scene
    "Вы заходите в небольшую фермерскую деревню. Воздух пропитан запахом сена и земли, но что-то не так."
    "Тишина окутывает улицы, и лишь слабый ветер шелестит листвой. Кажется, жители прячутся."

    # Показываем [my_eris.name] слева
    show eris t_neutral at mid with dissolve
    eris "Тихо тут, слишком тихо. В деревнях обычно шумно — люди работают, скот мычит. А тут как будто все вымерло."
    "Ее голос звучит уверенно, но с легкой ноткой раздражения. [my_eris.name] явно не любит, когда что-то идет не по плану."

    p "Скорее всего, это из-за дракона. Люди боятся выходить из домов."
    "Ты оглядываешься, пытаясь заметить хоть какие-то признаки жизни."

    eris t_angry "Хмф! Если они такие трусы, то хорошо, что мы здесь. Дракону не поздоровится." with dissolve
    "[my_eris.name] сжимает кулаки, ее глаза горят решимостью. Она явно готова к бою."

    # Появление Макимы
    
    show eris t_angry at move_left with dissolve
    "В этот момент к вам медленно подходит женщина. Ее шаги легкие, но в каждом движении чувствуется властность."
    show makima sly_smile at mid with dissolve
    makima sly_smile_say "Добро пожаловать в нашу скромную деревню, путники. Я — [makima.name], глава этого места. Что привело вас сюда?" with dissolve
    "Она улыбается, но ее взгляд холодный и проницательный, словно она уже знает ответ."
    show makima smile with dissolve

    p "Мы слышали, что у вас проблема с драконом. Мы решили взять задание и прогнать его."
    
    show eris t_smile with dissolve
    eris "Да, и мы не уйдем, пока не разберемся с этой тварью!"
    "[my_eris.name] говорит громко, почти вызывающе."

    makima sly_smile_say "Дракон, говорите? Да, он действительно беспокоит нас. Но это не простая задача. Вы уверены, что готовы?" with dissolve
    "Ее голос мягкий, но в нем чувствуется скрытая насмешка."
    show makima sly_smile with dissolve

    p "Мы готовы. Но нам нужно больше информации — где он прячется, как нападает, есть ли у него слабости."
    
    makima neutral_say "Информация? Хм… Это не так просто. Я должна убедиться, что вы не просто авантюристы, которые сбегут при первой опасности." with dissolve
    "Она делает паузу, внимательно глядя на тебя, словно оценивая каждую деталь."
    show makima neutral with dissolve

    # [my_eris.name] вмешивается
    eris "Эй, мы не какие-то слабаки! Мы уже сражались вместе, и я доверяю ему!"
    "Голос [my_eris.name] полон уверенности."

    makima sly_smile_say "Как мило. Но доверие твоей подруги меня не убедит. Давай проверим, насколько ты сам понимаешь, с чем столкнешься." with dissolve
    show makima sly_smile with dissolve
    "[makima.name] улыбается, но в ее глазах нет тепла."

    # Вопросы Макимы
    show makima neutral with dissolve
    "Она начинает задавать вопросы, и ты чувствуешь, что от твоих ответов зависит, доверится ли она тебе."

    $ points = 0
    menu:
        "Как ты собираешься подойти к дракону?"
        "Я изучу его повадки и найду слабое место, чтобы нанести точный удар.":
            $ points += 1
            makima smile_say "Интересно. Осторожность — это плюс. Но посмотрим, что дальше." with dissolve
        "Я пойду прямо на него и зарублю, пока он не успел опомниться.":
            makima angry_say "Смело, но глупо. Дракон не даст тебе шанса на такой подвиг." with dissolve
        "Я попробую отвлечь его и заманить в ловушку.":
            $ points += 1
            makima smile_say "Хитро. Мне нравится, когда люди думают наперед." with dissolve

    show makima neutral with dissolve
    menu:
        "Что ты знаешь о драконах?"
        "Они охраняют свои владения и часто имеют уязвимые места, вроде глаз или брюха.":
            $ points += 1
            makima smile_say "Неплохо. Ты явно не новичок в таких делах." with dissolve
        "Это просто большие ящерицы, которые дышат огнем.":
            makima neutral_say "Как примитивно. Ты недооцениваешь своего врага." with dissolve
        "Их можно приручить, если предложить еду.":
            makima angry_say "Забавно, но наивно. Дракон скорее съест тебя, чем твой подкуп." with dissolve

    show makima neutral with dissolve
    hide eris with dissolve
    mind "Похоже [my_eris.name] это надоело."
    menu:
        "Почему ты хочешь помочь нам?"
        "Я не могу оставить людей в беде, если могу что-то сделать.":
            $ points += 1
            makima smile_say "Благородно. Возможно, в тебе есть что-то большее, чем кажется." with dissolve
        "Мне нужна награда, чтобы продолжить свое путешествие.":
            makima neutral_say "Честно, но мелочно. Деньги — слабая мотивация." with dissolve
        "Я просто люблю сражаться с чудовищами.":
            makima angry_say "Твое рвение впечатляет, но оно может тебя погубить." with dissolve

    show makima neutral with dissolve
    menu:
        "Что ты сделаешь, если дракон окажется сильнее, чем ты думаешь?"
        "Я отступлю и найду другой способ победить.":
            $ points += 1
            makima smile_say "Разумно. Гордость не должна мешать выживанию." with dissolve
        "Я буду биться до последнего, даже если погибну.":
            makima angry_say "Отвага или глупость? Скорее второе." with dissolve
        "Я позову [my_eris.name], и мы разберемся вместе.":
            $ points += 1
            makima neutral_say "Командная работа? Интересный подход." with dissolve

    # Проверка результата
    if points >= 4:
        makima smile_say "Хм… Ты удивил меня. Пожалуй, я могу довериться тебе." with dissolve
        show eris t_smile at left with dissolve
        eris t_angry "Эй, что она сказала? Мы идем за драконом?" with dissolve

        show makima smile with dissolve
        "Ее голос становится чуть мягче, но в нем все еще чувствуется контроль."
        makima neutral_say "[my_eris.name], не могла бы ты проверить окрестности? Мне нужно обсудить с твоим другом детали." with dissolve
        show makima smile with dissolve
        
        eris t_angry "Ладно, но не задерживайтесь. Я хочу поскорее найти этого дракона!" with dissolve
        hide eris with dissolve
        "[my_eris.name] уходит проверять окрестности."

        makima "Пойдем со мной. Я расскажу тебе все, что знаю… и, возможно, немного больше."
        "Она берет тебя за руку и ведет в сторону небольшого дома. Ее прикосновение холодное, но в нем есть странная притягательность."
        
        scene bg makima_root_titfuck1 at bg_size with fade
        "Когда вы оказываетесь наедине, [makima.name] вальяжно садится на кресло."
        scene bg makima_root_titfuck1_say at bg_size with dissolve
        makima "Ты доказал свою ценность."
        scene bg makima_root_titfuck1 at bg_size with dissolve
        p "Так ты расскажешь, где его найти или о его слабостях?"
        scene bg makima_root_titfuck1_say at bg_size with dissolve
        makima "Дракон прячется в горах к северу, он нападает по ночам, и его чешуя уязвима под крыльями."
        scene bg makima_root_titfuck1 at bg_size with dissolve
        
        if charisma >= 30:
            "Она делает паузу, ее взгляд становится более интенсивным."
            scene bg makima_root_titfuck1_say at bg_size with dissolve
            makima "А теперь… позволь мне отблагодарить тебя за твою решимость."
            # Здесь начинается сцена минета, но я оставлю это на ваше усмотрение для дальнейшей детализации.
            call makima_titfuck
            scene bg makima_root_titfuck1 at bg_size with long_fade
            "[makima.name] поправляет одежду."
            scene bg makima_root_titfuck1_say at bg_size with dissolve
            makima "Теперь ты знаешь всё, что нужно. Удачи в битве с драконом." with dissolve
            scene bg makima_root_titfuck1 at bg_size with dissolve
            p "Спасибо за ценную информацию."
        else:
            $customNotify("Недостаточно харизмы")
            p "Спасибо, это очень ценная информация."
            scene bg makima_root_titfuck1_say at bg_size with long_fade
            makima smile_say "Теперь ты знаешь всё, что нужно. Удачи в битве с драконом." with dissolve
            scene bg makima_root_titfuck1 at bg_size with dissolve

        call village_scene
        "Ты выходишь из дома и встречаешь [my_eris.name]."
        show eris t_neutral at mid with dissolve
        eris "Ну что, узнал что-нибудь полезное?"
        p "Да, теперь мы знаем, где искать дракона."


    else:
        $customNotify("Вы провалили проверку")
        makima neutral_say "В любом случае этого недостаточно. Я не могу доверить такое задание тому, кто не готов." with dissolve
        show makima neutral with dissolve
        show eris t_angry at left with dissolve
        eris t_angry "Эй, что она сказала? Мы идем за драконом или нет?" with dissolve
        hide makima with dissolve
        p "Пока нет. Мне нужно лучше подготовиться."
        "[my_eris.name] хмурится, но соглашается. Вам придется подготовиться получше и вернуться позднее."
        "Вы с [my_eris.name] покидаете деревню, обдумывая следующий шаг."
        call forest_scene
        show eris t_angry at mid with dissolve
        eris "Ладно, видимо придётся вернуться сюда в другой день."
        "Вы возвращаетесь в город и расходитесь."
        jump city
    
    return

label dragon_fight_field:
    $dragon_fight_field_first_time = False
    # Начало сцены: дракон пролетает над героями
    "Внезапно над вами пролетает огромная тень, заслоняя солнце."
    scene bg dragon_fly1 at bg_size with dissolve
    "Вы с [my_eris.name] поднимаете головы и видите дракона, чьи крылья рассекают воздух."
    scene bg dragon_fly2 at bg_size with dissolve
    "С громким рёвом он пролетает над деревней, сотрясая землю."
    scene bg dragon_fly1 at bg_size with dissolve
    eris "Он летит в на север."

    call village_scene
    show eris t_smile at mid with dissolve
    eris "Ну же, идем охотиться на дракона! Он сел в том поле!"
    mind "Не нравится мне эта идея"

    # Герои бегут на поле
    scene bg dragon_angry at bg_size with dissolve
    show eris t_angry at left with dissolve
    eris "Вот он! Пора показать этой твари, кто здесь главный!"
    hide eris with dissolve
    "[my_eris.name] нанесла один удар по шкуре дракона, но он будто ничего не почувствовал."
    show eris t_angry at left with dissolve
    eris "Что это? Я будто ударила сталь!"
    $choice = 0
    menu:
        "Что делать?"
        "Сказать [my_eris.name] разрезать его брюхо":
            p "[my_eris.name]! Разрешь его огромное брюхо!"
            eris "Поняла!"
            hide eris with dissolve
            "[my_eris.name] разгоняется, стараять разрезать его брюхо, но Дракон без проблем отразает атаку и отбрасывает [my_eris.name]."
            scene bg dragon_angry at bg_size with flash
            show eris t_angry_torn at left with dissolve
            eris "Черт, [hero_name]! Не сработало!"
            $choice = 1
            $minusLove(my_eris, 5)
        "Сказать [my_eris.name] бить в голову":
            p "[my_eris.name]! Ударь по голове, должно сработать!"
            eris "Поняла!"
            hide eris with dissolve
            eris "Черт! Не сработало! [hero_name]!"
            "[my_eris.name] прыгает, замахиваясь по его голове, но его шкура не поддается и Дракон отбрасывает [my_eris.name] мощным ударом."
            scene bg dragon_angry at bg_size with flash
            show eris t_angry_torn at left with dissolve
            eris "Черт, [hero_name]! Не сработало!"
            $choice = 2
            $minusLove(my_eris, 5)
        "Сказать [my_eris.name] бить под крылья":
            p "[my_eris.name]! Бей под его крылья, это слабое место!"
            eris "Поняла!"
            hide eris with dissolve
            $addLove(my_eris,5)
            "[my_eris.name] пробегает сбоку от него и наносит сокрушительный удар по его крыльям."
            scene bg dragon_angry_blood at bg_size with flash
            show eris t_smile_torn at left with dissolve
            eris "Хаха! [hero_name]! Это сработало!"
            $choice = 3
            call dragon_fight_field_blood
            return

    p "Держись, [my_eris.name]. Это будет непросто."
    # Начало боя: дракон встречает героев
    scene bg dragon_angry_fire1 at bg_size with dissolve
    show eris t_angry_torn at left with dissolve
    "Дракон поворачивается к вам, его глаза пылают, а из пасти начинает собираться пламя."
    eris "Я отвлеку его! А ты бей, как только появится шанс!"
    p "Договорились!"
    "Эрис бросается вперёд, её меч сверкает на солнце."
    show eris at move_mid with dissolve
    scene bg dragon_angry_fire2 at bg_size with dissolve
    "Дракон выпускает струю огня, но [my_eris.name] ловко уворачивается."
    eris "Ха! Тебе меня не достать!"

    # Бой продолжается: герои ищут слабые места
    scene bg dragon_angry at bg_size_plus with dissolve
    "Пока [my_eris.name] отвлекает дракона, ты обходишь его с фланга и бьешь."
    menu:
        "Куда ударить?"
        "Разрезать его брюхо" if choice != 1:
            "Ты подбегаешь пытаясь разрубить его брюхо, но Дракон сопротивляется."
            call start_battle(10, 100, "Дракон", 'forest')
            "Ты приближаешься и наносишь один мощный удар по голове."
            scene bg dragon_angry_blood at bg_size with flash
            call dragon_fight_field_blood
            return
        "Бить в голову" if choice != 2:
            "Ты подбегаешь пытаясь ударить в голову, но Дракон сопротивляется."
            call start_battle(10, 100, "Дракон", 'forest')
            scene bg dragon_angry_blood at bg_size with flash
            "Ты приближаешься и наносишь один мощный удар по голове."
            call dragon_fight_field_blood
            return
        "Бить под крылья":
            scene bg dragon_angry_blood at bg_size with flash
            "Ты уворачиваешься он всех ударов Дракона и наносишь удар по крыльям."
            eris "Отлично! Ты его достал!"
            call dragon_fight_field_blood
            return
    return

label dragon_fight_field_blood:
    show eris t_angry_torn at left with dissolve
    "Крылья Дракона отваливаются, он еле держится."

    eris "Ну же, [hero_name]! Завершающий удар!"
    menu:
        "Что делать?"
        "Использовать магию льда" if intelligence > 20:
            "Ледяные копья протыкают чешую ослабевшего Дракона. Он падает."
            $addLove(my_elsa, 10)
        "Использовать боевые искусства" if strength > 50:
            "Ты приближаешься и наносишь несколько сокрушительных ударов. Дракону падает."
            $addLove(my_nag, 5)
            $addLove(my_eris, 5)
        "Ударить изо всех сил":
            scene bg dragon_angry_blood at bg_size_plus with dissolve
            "Ты приближаешься, Дракон явно сильно ослаблен, но упорно сопротивляется."
            call start_battle(10, 150, "Дракон", 'forest')
            "Ты приближаешься и наносишь один мощный удар."
            "Тебе повезло, этого было достаточно. Дракону падает."
    scene bg dragon_dead at bg_size_plus with dissolve
    eris "[hero_name]! Ты убил его!"
    p "Да! Хух..."
    "Ты выдыхаешь, бой наконец завершился."
    eris "Надо отрубить его рог, как доказательство выполнения задания."
    "Ты подбираешься ближе и отрубаешь его рог."
    scene bg dragon_dead_no_horn at bg_size_plus with flash
    scene bg dragon_dead_no_horn at bg_size with dissolve
    "Ты отходишь."
    show eris t_smile_torn at left with dissolve
    eris "Отлично, осталось лишь добраться до гильдии и завершить задание!"

    "Через мгновение вы слышите громкий рев дракона где-то вдали из за гор."
    eris t_angry_torn "Ты слышал это?!" with dissolve
    p "Д-да. Скорее всего слышали все в округе."
    eris "Идем на звук!"
    return


label dragon_fight_field_fail:
    $health = 0
    "Вы проиграли этот бой. Но на вашей стороне Боги. Дракон вас не съел."
    jump battle_loss

label dragon_mountain:
    scene bg mountain at bg_size with fade
    "Вы оборачиваетесь в сторону ближайшей горы, чтобы понять, откуда исходил этот протяжный рёв."
    scene bg mountain_roar at bg_size with vpunch
    "WRAAAAaaaaaR!"
    show eris t_smile_torn at mid with dissolve
    eris "Ты слышал? Мы обязаны добить оставшегося дракона!"
    p "[my_eris.name], твоя одежда..."
    hide eris with dissolve
    scene bg mountain at bg_size with dissolve
    eris "Чёрт! Я совсем забыла!"
    "[my_eris.name] переодевается. Опыт не прошел бесследно, она начала брать запасную одежду на задания."
    p "...{w}..{w}.."
    show eris t_angry at mid with dissolve
    eris "Мог бы и раньше сказать!"
    p "Ладно, идём уже."

    scene bg forest_path1 at bg_size with fade
    call steps_sound
    show eris t_neutral at mid with dissolve
    "Вы идете по лесной тропе в сторону горы."
    eris t_angry "Ты всегда такой молчаливый перед боем, или это я тебя так раздражаю?" with dissolve
    p "Просто думаю о том, как лучше подойти к дракону. Он не будет лёгким противником."
    eris t_smile "Ха! Да мы его вдвоём точно одолеем! Мы же только что одного такого одолели." with dissolve
    p "Да, но этот дракон может быть намного опаснее."
    eris t_angry "Ну и что? С каждой битвой я становлюсь сильнее! И ты тоже, надеюсь." with dissolve
    p "Конечно, но всё равно нужно быть осторожными. Драконы — не шутка."
    
    show bg forest_path2 at bg_size with dissolve
    call steps_sound
    eris t_neutral "Ладно, ладно, я поняла. Но ты слишком серьёзный. Расслабься немного!" with dissolve
    p "Расслаблюсь, когда мы победим."
    eris t_angry "Хмф! Ты всегда такой зануда." with dissolve
    "Она улыбается, подталкивая тебя локтем."
    eris t_smirk_blush "Кстати, спасибо, что не стал пялиться, когда я переодевалась." with dissolve
    p "Я... э-э... просто не хотел тебя смущать."
    eris t_angry "Ага, конечно. Ты просто боялся, что я тебя ударю." with dissolve
    p "Может быть."
    show eris t_smile at mid with dissolve
    "Вы оба улыбаетесь, и напряжение немного спадает."

    show bg forest_path3 at bg_size with dissolve
    call steps_sound
    eris t_smile "Ладно, давай придумаем план. Как ты думаешь, с чего начать?" with dissolve
    p "Сначала нужно найти его логово. Потом оценить его силу и найти слабые места."
    eris t_smirk "Или просто ворваться и зарубить его!" with dissolve
    p "Ты всегда такая импульсивная."
    eris t_smile "А ты всегда такой осторожный. Но именно поэтому мы хорошая команда." with dissolve
    p "Да, ты права."
    "Вы продолжаете идти."
    
    scene bg forest_mountain_path at bg_size with fade
    "Ты решаешь обернуться и осмотреться вокруг."
    mind "Какой прекрасный вид. Я никогда бы такого не увидел в прошлом мире."
    show eris t_smile at left_mid with dissolve
    eris "Не зевай, мы почти пришли."
    p "Ты права."

    scene bg dragon_cave_enterence at bg_size with fade
    call steps_sound
    show eris t_neutral at left with dissolve
    eris "Наконец дошли, заходим?"

    show wragon angry at mid with vpunch
    hide eris
    "Из ниоткуда вылетает [wragon.name] и с одного удара откидывает [my_eris.name]."
    scene bg eris_mountain_unconscious at bg_size with fade
    "Ты смотришь на [my_eris.name], она лежит без сознания."
    wragon "Гррр..."
    
    scene bg dragon_cave_enterence at bg_size with fade
    show wragon angry at mid with dissolve
    wragon "Гррр... Люди! Это вы убили моего мужа?!"
    menu:
        wragon "Гррр... Люди! Это вы убили моего мужа?!"
        "Солгать":
            p "Твоего мужа? Нет! Мы лишь странники, которые оказались здесь случайно."
        "Сказать правду":
            p "Да, это мы, но я тебе не проигаю!"
            wragon "Твоя дерзость станет твоей погибелью!"
            call start_battle(200, 3000, wragon.name, 'forest')
            "Перед смертью [wragon.name] что-то говорит на неизвестно тебе языке."
            hide wragon with dissolve
            wragon "Moriantur omnes et omnia...{w} Totus post mortem belli dea moriatur mundus."
            call dragon_fight_mountain_fail
        "Попытаться убежать":
            wragon "Я не дам тебе так просто уйти!"
            "Она быстро нагоняет тебя и пронзает твоё тело своей рукой."
            call dragon_fight_mountain_fail

    $ points = 0
    wragon "В любом случае, ты осмелился явиться сюда. Я задам тебе четыре вопроса. Отвечай мудро, и, возможно, ты сохранишь свою жизнь."

    # Вопрос 1
    wragon "Почему ты пришёл в моё логово? Чего ты ищешь?"
    menu:
        "Я искал сокровища.":
            wragon angry "Жадность — плохой советчик." with dissolve
            "Как только она договорила - твой желудок был проткнут ее рукой."
            call dragon_fight_mountain_fail
        "Я хотел доказать свою силу.":
            wragon neutral "Глупая бравада." with dissolve
        "Я искал приключений и знаний.":
            $ points += 1
            wragon smile "Любопытство — достойная цель." with dissolve

    # Вопрос 2
    wragon "Что ты думаешь о драконах?"
    menu:
        "Они злобные монстры, которых нужно истреблять.":
            wragon angry "Ты предвзят и глуп." with dissolve
            "Как только она договорила - твой желудок был проткнут ее рукой."
            call dragon_fight_mountain_fail
        "Они величественные существа, достойные уважения.":
            $ points += 1
            wragon smile "Ты умеешь видеть суть." with dissolve
        "Я не знаю, я впервые вижу дракона.":
            wragon neutral "Незнание — не оправдание." with dissolve

    # Вопрос 3
    wragon "Если бы ты мог выбрать, что бы ты сделал с моим сокровищем?"
    menu:
        "Забрал бы всё себе.":
            wragon angry "Ты вор и предатель." with dissolve
            "Как только она договорила - твой желудок был проткнут ее рукой."
            call dragon_fight_mountain_fail
        "Оставил бы его тебе, ведь оно твоё.":
            $ points += 1
            wragon smile "Ты уважаешь чужое." with dissolve
        "Забрал бы и раздал поселенцам из своей деревни.":
            wragon neutral "Щедрость, это похвально, но это всё еще кража." with dissolve

    # Вопрос 4
    wragon "Что ты ценишь больше всего?"
    menu:
        "Силу и власть.":
            wragon neutral "Это путь к одиночеству." with dissolve
        "Дружбу и верность.":
            $ points += 1
            wragon smile_say "Ты мудр для человека." with dissolve
        "Богатство и славу.":
            wragon neutral "Пустые ценности." with dissolve

    # Итог
    if points > 3:
        wragon smile_say "Ты удивил меня, человек. Ты не только умён, но и честен. Я оставлю тебя в живых." with dissolve
        wragon smile_closed "Знаешь, человек, между нами не столь большая разница." with dissolve
        p "Д-да?"
        mind "Что происходит?!"
        wragon horny_say "Да, я в этом убеждена. Ты мыслишь прямо как дракон." with dissolve
        show wragon horny with dissolve
        mind "Кажется она очень честная и справедливая."
        p "Тогда как ты объяснишь то, что моя подруга [my_eris.name] сейчас лежит без сознания?"
        wragon ashamed "Д-да, возможно я слегка перегнула палку..." with dissolve
        p "Слегка? Да она без сознания и возможно уже мертва!"
        wragon "Я била не в полную силу, она должна быть в порядке."
        wragon horny_say "Кажется я понимаю, к чему ты клонишь~" with dissolve
        show wragon horny with dissolve
        menu:
            wragon "Как я могу загладить свою вину?"
            "Дай мне своё тело":
                p "Отдайся мне."
                if charisma > 30:
                    wragon horny "Ты не пожалеешь~" with dissolve
                    call wragon_root_fuck
                    scene bg dragon_cave_enterence at bg_size with fade
                    show wragon horny_cummed_say at mid with dissolve
                    wragon "Не забудь про свою подругу, путешественник." with dissolve
                else:
                    $customNotify("Недостаточно харизмы")
                    wragon angry "Ну уж нет, знай своё место. {w}Убирайся прочь, пока я не передумала!" with dissolve
                    wragon "И про подругу не забудь."
                call heal_eris_by_yourself
                return
            "Вылечи [my_eris.name]":
                wragon horny_say "Как благородно с твоей стороны, ты в перую очередь заботишься о друзьях." with dissolve
                $addLove(my_freya,10)
                wragon "Она не нуждается в серьезном лечении. Сам лечи её."
                show wragon horny with dissolve
                mind "Чёрт, эта [wragon.name] бесполезна."
                call heal_eris_by_yourself
                return
            "Ничем":
                p "Мне ничего от тебя не нужно, просто не трогай нас."
                call heal_eris_by_yourself
                return
    elif points > 2:
        wragon neutral "Но в итоге ты меня не убедил. Уходи, пока я не передумала." with dissolve
        call heal_eris_by_yourself
        return
    else:
        wragon angry "Твои ответы неубедительны. {w} Я чувствую, это ты убил моего мужа!" with dissolve
        call dragon_fight_mountain_fail
    return

label dragon_fight_mountain_fail:
    scene bg black_screen at bg_size with dissolve
    "Ты мертв."
    $health = 0
    "Но это же просто игра, повтори попытку."
    jump battle_loss

label heal_eris_by_yourself(is_preview=False):
    $setSceneUnlockedFlag('seen_heal_eris_by_yourself')
    scene bg eris_mountain_unconscious at bg_size with fade
    p "Мне нужно как-то поднять [my_eris.name] на ноги. И чем быстрее, тем лучше."
    menu:
        "Как исцелить [my_eris.name]?"
        "Магией":
            if intelligence < 30 and not is_preview:
                $customNotify("Недостаточно интеллекта")
                p "Ффф... Мнн! {w}Ха..."
                "Ты стараешься изо всех сил, но ничего не происходит."
                call heal_eris_by_yourself
                return
            mind "Кажется я помню одно заклинание."
            "Ты закрываешь глаза и произносишь заклинание, которое удалось выучить."
            p "O mirabilia naturae, aperi alas tuas"
            scene bg eris_mountain_unconscious_fireflies_1 at bg_size with dissolve
            p "Et divino lumine prolem largire"
            scene bg eris_mountain_unconscious_fireflies_2 at bg_size with dissolve
            p "Ut omnes vitae pulchritudines noverit."
            scene bg eris_mountain_unconscious_fireflies_3 at bg_size with dissolve
            p "[my_eris.name]! Слава богу, ты жива!"
            scene bg eris_mountain_unconscious_fireflies_4 at bg_size with dissolve
            "[my_eris.name] в шоке от происходящего смотрит на тебя."
            eris "А? [hero_name]?"
            scene bg eris_mountain_unconscious_fireflies_5 at bg_size with dissolve
            "Магические существа начинают растворяться в воздухе."
            eris "Так ты и магией владеешь?"
            p "Совсем немного..."
            if not is_preview:
                $addLove(my_eris,5)
            scene bg eris_mountain_unconscious_fireflies_6 at bg_size with dissolve
            "[my_eris.name] поднимается целая и невредимая, будто ничего и не было."
            eris "Шутишь? Ты удивительный человек, [hero_name]!"
            scene bg forest_mountain_path at bg_size with fade
            show eris t_smile at mid with dissolve
            
        "Подручными средствами":
            "Ты достаешь флягу с водой и выливаешь всё на [my_eris.name]."
            scene bg eris_mountain_unconscious_wet_1 at bg_size with flash
            p "Ну же! Это ведь просто слабый ушиб, ты ведь жива!"
            scene bg eris_mountain_surprised_wet_1 at bg_size with dissolve
            "[my_eris.name] резко раскрыла глаза."
            scene bg eris_mountain_unconscious_wet_2 at bg_size with dissolve
            "Она в шоке от происходящего смотрит на тебя."
            eris "А? [hero_name]? Почему я мокрая?"
            if not is_preview:
                $minusLove(my_eris, 5)
            scene bg eris_mountain_angry_wet_1 at bg_size with dissolve
            p "Слава богу, [my_eris.name]... Ты..."
            scene bg eris_mountain_angry_wet_2 at bg_size with dissolve
            mind "Чёрт. Кажется она недовольна."
            eris "Гррр..."
            scene bg eris_mountain_angry_wet_3 at bg_size with dissolve
            pause .7
            scene bg forest_mountain_path at bg_size with flash
            if not is_preview:
                $health -= 10
            $customNotify("[my_eris.name] довольно сильно ударила тебя")
            if health <= 0:
                jump battle_loss
            show eris t_angry at mid with dissolve

    p "[my_eris.name], в любом случае, нам нужно быстро уходить!"
    mind "Эта [wragon.name]... Я не могу предугадать её ход мыслей. Она слишком опасна."
    eris t_surprised "Что? О чем ты?" with dissolve
    p "Расскажу по дороге."
    return

label return_village_quest_eris_dragon_hunting:
    p "Уходим, здесь нам не справиться"
    scene bg forest_path3 at bg_size with fade
    call steps_sound
    show eris t_angry at mid with dissolve
    "Ты тянешь [my_eris.name] за руку, быстро возвращаясь в сторону деревни."
    eris "Стой! Объясни, что произошло?"
    p "Нас одолели. Нам чудом удалось спастись."
    eris t_neutral "Что там было?" with dissolve
    p "Это было очень опасно. Нас могли убить!{w} Квест выполнен, ну же, идем, нужно рассказать жителям деревни."
    eris t_angry "Ты встретил того дракона?" with dissolve
    p "Да, именно он тебя и вырубил."
    eris t_neutral "То есть ты меня спас?" with dissolve
    show bg forest_path2 at bg_size with dissolve
    call steps_sound
    p "Да. Я не мог бросить тебя."
    $addLove(my_eris,10)
    eris t_embarrassed_blush "С-спасибо тебе, [hero_name]..." with dissolve
    p "..."
    hide eris with dissolve
    "Какое-то время вы идете молча."
    show bg forest_path3 at bg_size with dissolve
    call steps_sound
    pause 1
    show bg forest_path2 at bg_size with dissolve
    call steps_sound
    pause 1
    show bg forest_path1 at bg_size with dissolve
    call steps_sound
    pause 1
    show eris t_smile at left with dissolve
    eris t_smile "Смотри! Мы почти дошли!" with dissolve
    if not isNight():
        $setTime(3)
        $customNotify("Наступила ночь")

    p "Отлично! Правда деревня по прежнему выглядит подозрительно."
    call village_scene
    show eris t_smile at left with dissolve
    show makima sly_smile at right_bit with dissolve
    "У входа в деревню вас встречает [makima.name]."
    makima sly_smile_say "[hero_name], [my_eris.name], рада вас видеть в здравии." with dissolve
    show makima smile with dissolve
    p "Мы выполнили задание, вот рог."
    makima smile_say "Я в вас не сомневалась. {w}Конечно же я сообщу в гильдию о вашем подвиге." with dissolve
    show makima smile with dissolve
    eris t_neutral "А что на счет награды?" with dissolve
    makima sly_smile_say "Награду вам выдадут в гильдии.{w} Думаю информация как раз успеет дойти к тому времени, как вы вернетесь." with dissolve
    show makima smile with dissolve
    p "Ты не предупредила о том, что дракон не один!"
    makima angry_say "Так вы нашли второго..." with dissolve
    makima neutral "..." with dissolve
    makima neutral_say "В любом случае, вы выжили. Поздравляю." with dissolve
    show makima neutral with dissolve
    eris t_angry "Так ты знала о опасности, но не сказала?!" with dissolve
    makima angry_say "Вам не следовало туда идти." with dissolve
    show makima neutral with dissolve
    eris t_angry "Почему ты скрыла от нас что-то настолько важное?!" with dissolve
    makima angry_say "Повторю. Вам не следовало туда идти." with dissolve
    makima neutral_say "Думаю мы закончили, удачного пути до города." with dissolve
    hide makima with dissolve
    "[makima.name] уходит."
    eris t_angry "Вот же стерва! Как так можно?! Мы могли умереть!" with dissolve
    p "У этой деревни есть свои секреты...{w} Идём, нам нужен отдых."
    return

label makima_titfuck(is_preview=False):
    $setSceneUnlockedFlag('seen_makima_titfuck')
    scene bg makima_root_titfuck2 at bg_size with fade
    "[makima.name] поднимает свою рубашку и открывает тебе вид на ее шикарную грудь."
    p "*сглатывает*"
    if not is_preview:
        menu:
            makima "Герой, который спасет нас от дракона, желаешь получить дополнительную мотивацию?"
            "Да":
                p "Конечно!"
            "Нет":
                p "Я и без неё управлюсь."
                makima "Будь по твоему"
                return
    scene bg makima_root_titfuck3 at bg_size with fade
    "[makima.name] встает из за стола, пиджак сползает по ее плечам и падает на пол, оголяя её плечи и грудь."
    scene bg makima_root_titfuck4 at bg_size with fade
    makima "Ну же, покажи, что у тебя есть."

    scene bg makima_root_titfuck5_1 at bg_size with fade
    pause .3
    scene bg makima_root_titfuck5_2 at bg_size with dissolve
    call hide_dialog
    makima "Мой любимый размер~"

    scene bg makima_root_titfuck6_1 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck6_2 at bg_size with dissolve
    call hide_dialog
    makima "Герой, ты же спасешь деревню от дракона?"
    p "К-конечно, обязательно..."

    scene bg makima_root_titfuck7 at bg_size with dissolve
    call hide_dialog
    "[makima.name] сильнее сжамает твой член своей грудью."
    p "Ухх"

    scene bg makima_root_titfuck8_1 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck8_3 at bg_size with dissolve
    p "А-ах.. а?{w} Ты остановилась?"
    makima "Думаю эта техника тебе понравится еще больше~"

    scene bg makima_root_titfuck9_1 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck9_3 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck9_1 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck9_1_3 at bg_size with dissolve
    pause .3
    scene bg makima_root_titfuck9_1 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_3 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_1_3 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_1 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_3 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_1_3 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .2
    scene bg makima_root_titfuck9_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_1_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_1_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_2 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_1_3 at bg_size with dissolve
    pause .1
    scene bg makima_root_titfuck9_2 at bg_size with flash
    pause .5
    scene bg makima_root_titfuck9_3 at bg_size with flash
    p "Аргх!"

    scene bg makima_root_titfuck10 at bg_size with flash
    call hide_dialog
    "Мощная струя спермы выстреливает на лицо [makima.name]."

    scene bg makima_root_titfuck11 at bg_size with dissolve
    pause .5
    scene bg makima_root_titfuck12 at bg_size with flash
    call hide_dialog
    "[makima.name] резким движением перекрывает поток спермы."
    makima "*глотает*"

    scene bg makima_root_titfuck13 at bg_size with dissolve
    call hide_dialog
    makima "Мммм~"

    scene bg makima_root_titfuck14 at bg_size with dissolve
    call hide_dialog
    p "*выдыхает*"
    makima "Вижу я смогла тебя удовлетворить, Герой."

    return

label wragon_root_fuck(is_preview=False):
    $setSceneUnlockedFlag('seen_wragon_root_fuck')
    scene bg wragon_anal1 at bg_size with fade
    "[wragon.name] заводит тебя в пещеру."
    "Ты видишь множество комнат, но больше всего твое внимание привлекает [wragon.name] и её сочная задница."
    wragon "Нравится моя пещера?"
    p "Д-да, здесь довольно уютно..."

    scene bg wragon_anal2 at bg_size with dissolve
    call hide_dialog
    wragon "Эта пещерка тебе понравится еще больше~"
    p "*сглатывает*"

    scene bg wragon_anal3 at bg_size with dissolve
    call hide_dialog
    "[wragon.name] наклоняется, открывая тебе вид на ее округлую попку."
    p "Стой! Ты же говорила о том, что у тебя есть муж? Вдруг он узнгает и накажет меня."

    scene bg wragon_anal3_2 at bg_size with dissolve
    call hide_dialog
    wragon "Хаха, не посмеет. Он со мной даже рядом не стоит."

    scene bg wragon_anal3 at bg_size with dissolve
    call hide_dialog
    wragon "Думаю даже ты можешь его одолеть~"

    scene bg wragon_anal4_1 at bg_size with fade
    pause .5
    scene bg wragon_anal4_2 at bg_size with dissolve
    call hide_dialog
    wragon "Так что не тяни время, я уже вне терпения~"
    "Ты быстро стягиваешь штаны и вонзаешь свой член в ее тугую попку."

    scene bg wragon_anal6 at bg_size with flash
    call hide_dialog
    wragon "Ах! Ты решил выбрать эту дырочку?"

    scene bg wragon_anal5 at bg_size with dissolve
    pause .5
    scene bg wragon_anal6 at bg_size with dissolve
    pause .5
    scene bg wragon_anal5 at bg_size with dissolve
    pause .5
    scene bg wragon_anal6 at bg_size with dissolve
    pause .1
    scene bg wragon_anal5 at bg_size with dissolve
    pause .1
    scene bg wragon_anal6 at bg_size with dissolve
    pause .1
    scene bg wragon_anal5 at bg_size with dissolve
    pause .1
    scene bg wragon_anal5 at bg_size with dissolve
    pause .1
    scene bg wragon_anal6 at bg_size with dissolve
    pause .1
    scene bg wragon_anal5 at bg_size with dissolve
    wragon "Стой!"

    scene bg wragon_anal4_2 at bg_size with fade
    call hide_dialog
    wragon "Стой, я не хочу терять твоё семя. Воспользуйся моей киской~"
    
    scene bg wragon_vaginal1 at bg_size with fade
    call hide_dialog
    wragon "Ах! Как же приятно~"
    "[wragon.name] седлает твой член и начинает двигаться."
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .5
    scene bg wragon_vaginal3 at bg_size with dissolve
    pause .5
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .5
    scene bg wragon_vaginal1 at bg_size with dissolve
    pause .5
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .5
    scene bg wragon_vaginal3 at bg_size with dissolve
    pause .5
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .5
    scene bg wragon_vaginal1 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal3 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal1 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal3 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal1 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal3 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal1 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal3 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal1 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal2 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal3 at bg_size with dissolve
    call hide_dialog
    wragon "Ах! Ах! Ах! Не останавливайся!"

    scene bg wragon_vaginal4 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal7 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .2
    scene bg wragon_vaginal4 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal7 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal4 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal7 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal4 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal7 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal4 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal7 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal4 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal7 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal4 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal5 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal6 at bg_size with dissolve
    pause .1
    scene bg wragon_vaginal7 at bg_size with flash
    call hide_dialog
    wragon "Аааах!"

    scene bg wragon_vaginal8 at bg_size with flash
    call hide_dialog
    p "Аргх!"

    scene bg wragon_vaginal9 at bg_size with flash
    call hide_dialog
    wragon "Даааа-ах~"

    scene bg wragon_vaginal10 at bg_size with dissolve
    pause .3
    scene bg wragon_vaginal10_say at bg_size with dissolve
    call hide_dialog
    wragon "Ты оказался лучше, чем я думала~"

    scene bg wragon_vaginal10 at bg_size with dissolve
    call hide_dialog
    p "Ты на это и рассчитывала изначально?"

    scene bg wragon_vaginal10_say at bg_size with dissolve
    call hide_dialog
    wragon "Изначально я рассчитывала убить тебя.{w} А теперь, думаю, у нас будет чудесное потомство."
    
    scene bg wragon_vaginal10 at bg_size with dissolve
    call hide_dialog
    mind "Как же она меня пугает."
    
    scene bg wragon_vaginal10_say at bg_size with dissolve
    wragon "Ты хорошо постарался, смертный, можешь идти."
    "Ты выходишь из пещеры."
    return