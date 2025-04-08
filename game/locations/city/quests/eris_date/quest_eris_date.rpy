define can_find_chizuru = True
define first_time_find_blond = True

# Начало квеста
label quest_eris_date_start:
    # Время вечер, вы договорились встретиться в центральной развилке города и погулять
    mind "Видимо, [my_eris.name] опаздывает, или я пришел раньше?{w} Она всегда такая — либо мчится сломя голову, либо заставляет всех ждать."
    mind "Не важно, подожду её немного. "
    "Какое-то время спустя..."
    if not isEvening():
        $setTime(2)
        call city_scene
    show eris smile with dissolve
    eris "Эй, [hero_name]! Ты что, уже тут торчишь? Небось весь день ждал, да?"
    p "Привет, [my_eris.name]! Нет, только пришёл.{w} Вау! Ты выглядишь просто потрясающе!"
    eris smile_blush "Да? Ну... спасибо, наверное." with dissolve
    eris smirk_blush "А ты выглядишь как обычно — не то чтобы это плохо, но мог бы и постараться!" with dissolve
    p "Эй, я старался! Это мой лучший плащ!"
    eris laugh "Плащ? Ха, да он будто с прошлогоднего задания весь в пыли!" with dissolve
    eris smile_blush "Ладно, прощаю. Так куда ты меня тащишь?" with dissolve
    p "Думал прогуляться по рынку. Там фестиваль, еда, всякое разное."
    eris smile "Вот это уже интересно! Чего стоим? Пошли!" with dissolve
    
    # Переход к прогулке по рынку
    
    call market_walk
    call dance_scene_start
    call wallet_theft
    call going_home
    if not isQuestCompleted(quest_eris_date):
        call black_hole_event
    call going_currently_home
    return

# Сцена 1: Прогулка по рынку
label market_walk:
    call market_scene 
    "Мы добрались до рынка. Шум толпы, запахи специй и звон металла от кузниц сразу ударили в нос."
    show eris smile with dissolve
    eris "Ты только посмотри, [hero_name]! Вон там мечи висят — острые, как мой! А вон там щит — жаль, тяжеловат, а то бы я его примерила."
    p "Ты и так как ходячий арсенал. Может, для разнообразия попробуем что-то не острое?"
    eris "Что ты имеешь в виду? Еду, что ли?"
    p "Ага, вон там жарят фрукты в меду. Пахнет здорово, давай попробуем."
    eris annoyed "Фрукты в меду? Серьёзно? Я что, ребёнок, чтобы жевать сладкое?" with dissolve
    p "Хмм, ладно, может хочешь жареную сосиску?"
    eris neutral "Её можно." with dissolve

    if money >= 10:
        $minusMoney(10)
        call eris_root_sausage
        "[my_eris.name] быстро доела сосиску."
        call market_scene
        show eris smirk_blush with dissolve
        p "Сосиска была очень вкусная, что ты ее так обсасывала?"
        show eris annoyed with dissolve
        eris "Заткнись, [hero_name]! {w}Я просто проверяла, не отрава ли это!!"
        p "Ага, конечно..."
    else:
        p "Эм, прости, у меня с собой нет денег."
        eris annoyed "Серьезно? Ты пошел на свидание без денег?!" with dissolve
        p "Ты назвала это свиданием?"
        eris embarassed_blush "Н-нет, тебе показалось..." with dissolve

    "Вы идете дальше по оживленному вечернему рынку."
    # Переход к танцам
    return

# Сцена 2: Танцы у костра
label dance_scene_start:
    call dance_scene_music
    eris smile "О, [hero_name], слышишь?" with dissolve
    p "Да, кажется там проходит какая-то тусовка."
    if canVisit("brothel"):
        mend "Знакомая музыка...{w} Наверняка [my_mao.name] и [my_rapunzel.name] постарались."
    call steps_sound
    "Вы подходите ближе"
    call dance_scene
    show eris neutral at left with dissolve
    "На площади все танцуют. Трубы и электронная музыка задавали ритм, люди танцевали в светах ярких огней, смех и музыка наполняли воздух."
    mind "Магия это удивительно..."
    show eris annoyed with dissolve
    eris "Это что, они тут все пляшут? Выглядит как куча дурней, которые не знают, куда деть энергию!"
    p "Ну, это весело. Давай попробуем, [my_eris.name]? Потанцуем?"
    show eris smile at move_left_out with dissolve
    if intelligence >= 30 and can_find_chizuru:
        menu:
            "Ты заметил, что [my_eris.name] уходит"
            "Пойти за [my_eris.name]":
                "Ты решил последовать за [my_eris.name]"
            "Насладиться шоу":
                "Ты решил остаться и досмотреть шоу и подходишь ближе к танцовщицам."
                call chizuru_root_dance
                if charisma >= 30:
                    scene bg chizuru_root_dance8_say at bg_size with dissolve
                    pause 1
                    call chizuru_club_dialog
                else:
                    $customNotify("Необходимо 30 харизмы")
                    "[chizuru.name] встает и уходит."
                    mind "Больше здесь не на что гладеть."
                    call door_enter_sound
                call dance_scene
                mind "Так, я сильно отвлекся, надо найти [my_eris.name], мы всё же на свидании"

    else:
        $customNotify("Необходимо 30 интеллекта")
    mind "Ты быстро находишь [my_eris.name]."
    show eris neutral at left with dissolve
    p "Эй, [my_eris.name], не убегай, может хотя бы попробуем станцевать?"
    eris annoyed "Танцевать? Я?! Да ты шутишь! Я лучше мечом помашу, чем тут ноги топтать!" with dissolve
    p "А если я скажу, что это как бой, только без оружия? Надо ловкость показать."
    eris smirk "Хм... Ловкость, говоришь? Ну, это уже звучит не так глупо. " with dissolve
    extend annoyed "Но если я увижу, что ты пялишься, как идиот, я тебе врежу!" with dissolve
    p "Договорились. Давай, бери меня за руку."
    show eris smirk_blush with dissolve
    eris "Только попробуй что-то выкинуть, [hero_name]. " 
    extend embarassed_blush "Я тебе не какая-нибудь принцесса на балу!" with dissolve
    "Я протянул руку, и она неохотно её взяла. Мы начали двигаться под музыку."
    
    call eris_root_date_dance

    call dance_scene
    $nextTime()
    show eris laugh at mid with dissolve
    eris "Ахаха, ты видел как я шмякнулась?"
    p "Хах, да, тебе не больно?"
    eris smile_blush "Конечно нет, за кого ты меня принимаешь?" with dissolve
    return

# Сцена 3: Потерянный кошелёк
label wallet_theft:
    $my_wallet = money
    $minusMoney(my_wallet)
    "В тебя врезается какой-то парень." with vpunch
    p "... {w}Ох. {w}Кажется он украл мой кошелек..."
    eris annoyed "Это тот парень? {w}Может ты его выронил во время танца?" with dissolve
    if my_wallet <= 9:
        $customNotify("Необходимо 10 монет")
        p "Не проблема, у меня там все равно почти не было денег."
        eris laugh "Ахаха, [hero_name], как можно было пойти на свидание почти без денег?" with dissolve
        eris smirk_blush "Но не переживай, в моей комнате тебе не нужно будет ни за что расплачиваться~"with dissolve
        return
    p "Не может быть, во время танца я бы заметил, там было немало денег, надо его найти!"
    eris "Какой наглец посмел?! Где он, покажи мне этого гада!"
    p "Вон там, убегает! Маленький, в капюшоне!"
    eris "Бежим, [hero_name]! Сейчас я ему устрою!"
    call market_scene
    "Мы рванули через рынок. [my_eris.name] мчалась впереди, расталкивая людей."
    eris "Эй, ты, крыса! Стой, или я тебе ноги переломаю!"
    call black_alley_scene
    show guy1 neutral_shadow at darken_bit,left_mid with dissolve
    "[guy1.name] остановился."
    guy1 "Что вам нужно от меня?"
    if first_time_find_blond:
        show eris annoyed at right_mid with dissolve
        eris "Вот мы тебя и догнали, верни кошелек!"
        guy1 "С чего бы? Я честно заработал деньги и ношу в своем кошельке."
        eris smirk "А зачем тогда ты от нас убегал?!" with dissolve
        guy1 "Это моя обычная вечерняя пробежка."
        show eris smirk with dissolve
        p "Почему ты побежал в этот темный переулок? Обычно все бегают по паркам."
        show eris annoyed with dissolve
        guy1 "Мне просто захотелось пробежаться по округе, здесь очень красиво ночью."
        eris smirk "А почему ты бегаешь в такой плотной черной одежде? Тебе не жарко?" with dissolve
        guy1 "Что за допрос? Я не собираюсь отвечать!"
        eris annoyed "[hero_name], это он украл твой кошелек?" with dissolve
        $first_time_find_blond = False
        menu:
            eris "Это он украл твой кошелек?" 
            "Да, это был он":
                p "Да, это точно был он!"
                show guy1 angry at normal_brightness with dissolve
                if persistent.lang == "russian":
                    $guy1.name = "Девушка"
                if persistent.lang == "english":
                    $guy1.name = "Girl"

                guy1 "Слыш пацан! Ты ничего не попутал?!" 
                mind "Что? Это девушка?!"
                show eris annoyed at move_mid with dissolve
                hide guy1 with vpunch
                "Девушка очень быстро получает удар от [my_eris.name] и падает без сознания."
                eris laugh "Я разобралась." with dissolve
                "[my_eris.name] осматриваеn её карманы и находит твой кошелек."
                eris smile "Вот твой кошелек." with dissolve
                $addMoney(my_wallet)
                p "С-спасибо..."
                mind "Иногда она меня пугает..."
                eris smile "Ну что, пойдем? " with dissolve
                eris smirk_blush "У нас есть еще дела~" with dissolve
                p "Идем конечно!"
                call market_scene
                show eris smile_blush at mid with dissolve

            "Нет, я ошибся":
                p "Кажется я ошибся."
                show guy1 smile at normal_brightness with dissolve
                if persistent.lang == "russian":
                    $guy1.name = "Девушка"
                if persistent.lang == "english":
                    $guy1.name = "Girl"
                mind "Что? Это девушка?!"
                guy1 "Слышала его? Отстань от меня!"
                eris annoyed "Сама виновата, нечего бегать по ночам!" with dissolve
                hide eris with dissolve
                p "Эй, [my_eris.name], куда ты?"
                show guy1 smile at move_mid with dissolve
                guy1 smirk "На самом деле это я украла твой кошелек." with dissolve
                p "Да, я знаю, забудь, он твой."
                guy1 surprised "А? Ты не понял? Я украла твои деньги." with dissolve
                p "Да, я понял, просто не хотел, чтобы [my_eris.name] тебя избила."
                guy1 smirk "Благородный поступок, ты получается рыцарь? Или герой?" with dissolve
                $addLove(my_freya, 10)
                p "Я просто поступил так, как посчитал нужным."
                call guy1_black_alley_root
                call black_alley_scene
                "Так, надо скорее разыскать [my_eris.name]. Кажется она ушла в сторону рынка."
                call market_scene
                show eris annoyed at mid with dissolve
                eris "И почему мне пришлось тебя так долго ждать?!"
                p "П-прости, я просто объяснял той девушке, что не стоит бегать по ночам, да еще и в такой одежде..."
                eris smile_blush "Ну ладно, надеюсь ты не забыл про наши планы~" with dissolve
    else:
        show guy1 angry at normal_brightness with dissolve
        p "Опять ты?!"
        eris surprised "Что? Опять?" with dissolve
        eris annoyed "[hero_name], ты недостаточно доходчиво ей объяснил в тот раз?" with dissolve
        show guy1 smile with dissolve
        p "Н-нет, все нормально, можешь идти, [my_eris.name], я тебя догоню."
        guy1 smirk "Ты же не поднимешь руку на беззащитную женщину?" with dissolve
        call guy1_black_alley_root
        call black_alley_scene
        "Так, надо скорее разыскать [my_eris.name]. Кажется она ушла в сторону рынка."
        call market_scene
        show eris annoyed at mid with dissolve
        eris "И почему мне пришлось тебя так долго ждать?!"
        p "П-прости, я просто объяснял, что воровать нельзя."
        eris smile_blush "Ну ладно, надеюсь ты не забыл про наши планы~" with dissolve
    
    return

# Сцена 4: Возвращение домой
label going_home:
    call city_scene
    "Мы шли домой к [my_eris.name] по тёмным улицам. Фонари мигали, а день оставил после себя приятную усталость."
    show eris smile at mid with dissolve
    eris "Знаешь, [hero_name], я думала, это будет скучно, но ты меня удивил. Неплохой день!"
    p "Рад, что тебе понравилось. С тобой всегда весело, [my_eris.name]."
    eris smile_blush "Ну, не всегда. Ты иногда такой зануда, особенно с этой твоей осторожностью." with dissolve
    p "А ты слишком безбашенная. Мы идеально уравновешиваем друг друга."
    show eris smirk with dissolve
    eris "Идеально, говоришь? Не зазнавайся! Но... да, было круто. Может, ещё раз сходим. Если ты не облажаешься, конечно."
    p "С таким условием я точно постараюсь."
    eris smirk_blush "Вот и постарайся, а то я быстро найду, чем тебя заменить!" with dissolve
    show eris laugh at mid with dissolve
    "Она засмеялась, и я заметил, как её улыбка стала чуть мягче."
    mind "Кажется, нас ждёт бурная ночь... или хотя бы хороший отдых после такого дня."
    
    return

# Сцена 5: Чёрная дыра
label black_hole_event:
    call magic_wind_music
    scene bg city_night_bh at bg_size with fade
    show eris annoyed at mid with dissolve
    "Но вдруг воздух задрожал. Перед нами возникла чёрная дыра, и неведомая сила начала затягивать [my_eris.name] внутрь."
    eris "[hero_name]! Что за дьявольщина? Ты опять что-то натворил?!"
    p "Я тут ни при чём! Держись, я тебя вытащу!"
    show eris annoyed at smaller with dissolve
    eris "Постарайся, или я тебя потом из могилы достану!"
    "Я схватил её за руку, чувствуя, как она выскальзывает."
    p "[my_eris.name], не сдавайся! Я тебя не отпущу!"
    eris "Тяни сильнее!"
    # Выбор игрока
    menu:
        "Держать изо всех сил":
            call hold_eris
        "Отпустить [my_eris.name]":
            call let_go_eris
    return

# Вариант 1: Держать [my_eris.name]
label hold_eris:
    "Я напряг все силы, вцепившись в её руку. Чёрная дыра гудела, но я не сдавался."
    p "[my_eris.name], держись за меня! Я не дам тебе пропасть!"
    show eris annoyed at smaller with dissolve
    eris "Давай, тяни!"
    scene bg city_night at bg_size with flash
    show eris smirk_blush at mid,normal_size  with dissolve
    "Мои мышцы горели, но я продолжал бороться. Наконец, дыра сжалась и исчезла с хлопком."
    "[my_eris.name] упала мне на руки, тяжело дыша."
    eris smile_blush "Фух... Ладно, ты молодец. Но не думай, что я теперь тебе обязана или что-то такое!" with dissolve
    p "Да я и не надеялся. Главное, ты цела."
    eris annoyed "Цела, цела... Но что это вообще было? Если это твои шуточки, я тебя прикончу!" with dissolve
    p "Клянусь, я не знаю! Может, завтра разберёмся?"
    eris smirk "Завтра? Ха, ладно. Но ты мне должен объяснение!" with dissolve
    "Мы побрели домой. Что-то подсказывало, что это только начало."
    return

# Вариант 2: Отпустить [my_eris.name]
label let_go_eris:
    "Мои руки задрожали и ослабели. [my_eris.name] выскользнула и исчезла в чёрной дыре."
    hide eris with dissolve
    eris "[hero_name]!"
    scene bg city_night at bg_size with flash
    "Её голос оборвался. Дыра закрылась, оставив меня одного."
    p "[my_eris.name]! Нет!"
    mind "Я не смог её удержать. Она пропала... навсегда?"
    $can_find_eris = False
    $customNotify("Ты больше не увидишь [my_eris.name]")
    mind "Что-то мне подсказывает, что я больше ее не увижу..."
    $completeQuest(quest_eris_date, my_eris, False)
    mind "Нет, надо исследовать эту червоточину!"
    $getQuest(quest_eris_black_hole)
    jump city
    return

label going_currently_home:
    call tavern_scene
    show eris smirk_blush at mid with dissolve
    eris "Зайдешь выпить чаю?"
    p "Это был тяжелый день, надо отдохнуть, чашка чая не повредит."
    call door_enter_sound
    scene bg eris_room at bg_size with fade
    "Вы поднимаететесь и заходите в комнату [my_eris.name]"
    show eris smirk_blush at mid with dissolve
    eris "Подожди минутку, я подготовлюсь"
    hide eris with dissolve
    mind "...{w}..{w}.."
    show eris transparent_shy at mid with dissolve
    pause .4
    call eris_root_tea
    return


    