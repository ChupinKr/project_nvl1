define first_time_quest_eris_black_hole = True

label quest_eris_black_hole_start:
    if first_time_quest_eris_black_hole:
        $first_time_quest_eris_black_hole = False
        $qebh_if_visit_market = False
        mind "Хм, с чего бы мне начать?"
        call find_black_hole_enter
        call magic_dissapear
        call quest_eris_desert_enter
    else:
        call magic_dissapear
    call asoka_root_wake_up
    call quest_eris_desert_asoka_dialog
    call quest_eris_desert_crypt
    if health <= 0:
        call quest_eris_desert_crypt_wake_up
    call quest_eris_black_hole_skelet_king
    call quest_eris_black_hole_end
    
    mind "Надеюсь червоточина здесь больше не возникнет."
    return

label find_black_hole_enter:
    menu:
        "Дождусь вечера" if not isEvening() and not isNight():
            $setTime(2)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Дождусь ночи" if isEvening():
            $setTime(3)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Попытаюсь повторить путь" if current_location != "market":
            $qebh_if_visit_market = True
            call market_scene
            "Ты приходишь на рынок"
            mind "Итак, я на рынке, что дальше?"
        "Вернусь на центральную площадь" if current_location == "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            mind "Ничего не происходит, может я сделал что-то не так?"
            if getTime == 3 and qebh_if_visit_market == True:
                return
        "Попробую встать на место [my_eris.name]" if current_location != "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            if getTime() == 3 and qebh_if_visit_market == True:
                return
            else:
                mind "Ничего не происходит, может я сделал что-то не так?"
        "Сдаться":
            mind "Это сложнее, чем казалось, ладно, попробую в другой раз."
            jump city
    menu:
        "Дождусь вечера" if not isEvening() and not isNight():
            $setTime(2)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Дождусь ночи" if isEvening():
            $setTime(3)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Попытаюсь повторить путь" if current_location != "market":
            $qebh_if_visit_market = True
            call market_scene
            "Ты приходишь на рынок"
            mind "Итак, я на рынке, что дальше?"
        "Вернусь на центральную площадь" if current_location == "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            mind "Ничего не происходит, может я сделал что-то не так?"
            if getTime == 3 and qebh_if_visit_market == True:
                return
        "Попробую встать на место [my_eris.name]" if current_location != "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            if getTime() == 3 and qebh_if_visit_market == True:
                return
            else:
                mind "Ничего не происходит, может я сделал что-то не так?"
        "Сдаться":
            mind "Это сложнее, чем казалось, ладно, попробую в другой раз."
            jump city
    menu:
        "Дождусь вечера" if not isEvening() and not isNight():
            $setTime(2)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Дождусь ночи" if isEvening():
            $setTime(3)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Попытаюсь повторить путь" if current_location != "market":
            $qebh_if_visit_market = True
            call market_scene
            "Ты приходишь на рынок"
            mind "Итак, я на рынке, что дальше?"
        "Вернусь на центральную площадь" if current_location == "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            mind "Ничего не происходит, может я сделал что-то не так?"
            if getTime == 3 and qebh_if_visit_market == True:
                return
        "Попробую встать на место [my_eris.name]" if current_location != "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            if getTime() == 3 and qebh_if_visit_market == True:
                return
            else:
                mind "Ничего не происходит, может я сделал что-то не так?"
        "Сдаться":
            mind "Это сложнее, чем казалось, ладно, попробую в другой раз."
            jump city
    menu:
        "Дождусь вечера" if not isEvening() and not isNight():
            $setTime(2)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Дождусь ночи" if isEvening():
            $setTime(3)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Попытаюсь повторить путь" if current_location != "market":
            $qebh_if_visit_market = True
            call market_scene
            "Ты приходишь на рынок"
            mind "Итак, я на рынке, что дальше?"
        "Вернусь на центральную площадь" if current_location == "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            mind "Ничего не происходит, может я сделал что-то не так?"
            if getTime == 3 and qebh_if_visit_market == True:
                return
        "Попробую встать на место [my_eris.name]" if current_location != "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            if getTime() == 3 and qebh_if_visit_market == True:
                return
            else:
                mind "Ничего не происходит, может я сделал что-то не так?"
        "Сдаться":
            mind "Это сложнее, чем казалось, ладно, попробую в другой раз."
            jump city
    menu:
        "Дождусь вечера" if not isEvening() and not isNight():
            $setTime(2)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечера"
            mind "Итак, вечер наступил, что дальше?"
        "Дождусь ночи" if isEvening():
            $setTime(3)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления ночи."
            mind "Уже ночь, что дальше?"
        "Попытаюсь повторить путь" if current_location != "market":
            $qebh_if_visit_market = True
            call market_scene
            "Ты приходишь на рынок"
            mind "Итак, я на рынке, что дальше?"
        "Вернусь на центральную площадь" if current_location == "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            mind "Ничего не происходит, может я сделал что-то не так?"
            if getTime == 3 and qebh_if_visit_market == True:
                return
        "Попробую встать на место [my_eris.name]" if current_location != "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            if getTime() == 3 and qebh_if_visit_market == True:
                return
            else:
                mind "Ничего не происходит, может я сделал что-то не так?"
        "Сдаться":
            mind "Это сложнее, чем казалось, ладно, попробую в другой раз."
            jump city
    menu:
        "Дождусь вечера" if not isEvening() and not isNight():
            $setTime(2)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Дождусь ночи" if isEvening():
            $setTime(3)
            if current_location == "city":
                call city_scene
            else:
                call market_scene
            "Ты дожидаешься наступления вечер"
            mind "Итак, вечер наступил, что дальше?"
        "Попытаюсь повторить путь" if current_location != "market":
            $qebh_if_visit_market = True
            call market_scene
            "Ты приходишь на рынок"
            mind "Итак, я на рынке, что дальше?"
        "Вернусь на центральную площадь" if current_location == "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            mind "Ничего не происходит, может я сделал что-то не так?"
            if getTime == 3 and qebh_if_visit_market == True:
                return
        "Попробую встать на место [my_eris.name]" if current_location != "market":
            call city_scene
            "Ты встаешь ровно на то место, где стояла [my_eris.name]."
            if getTime() == 3 and qebh_if_visit_market == True:
                return
            else:
                mind "Ничего не происходит, может я сделал что-то не так?"
        "Сдаться":
            mind "Это сложнее, чем казалось, ладно, попробую в другой раз."
            jump city
    mind "Я не могу дальше блуждать, лучше попробую завтра."
    jump city
    return

label quest_eris_desert_enter:
    call magic_wind_music
    scene bg city_night_bh with dissolve
    p "Получилось! {w} Меня затягивает..."
    menu:
        "Войти в червоточину?"
        "Да":
            "Ты собираешься с мыслями в спускаешься в червоточину."
        "Нет":
            mind "Нет! Я пока не готов, лучше попробую еще раз позже."
            jump city

    call desert_wind_music
    $setTime(0)
    scene bg desert1 at bg_size with flash
    $minusHealth(10)
    if health <= 0:
        "Ты падаешь и теряешь сознание."
        return
    p "Ай! Какого хрена?"
    if not can_find_eris:
        p "Эй! [my_eris.name]! Ты здесь?!"
        p "...{w}..{w}.."
        mind "Похоже ее здесь нет."
    mind "Я в пустыне?"
    mind "Ладно, надо идти, палящее солнце меня не пощадит."

    scene bg desert2 at bg_size with dissolve
    $setTime(1)
    "Ты идешь дальше, солнце и не собирается садиться."
    $minusHealth(7)
    if health <= 0:
        "Ты падаешь и теряешь сознание."
        return
    p "Почему здесь день? Я же заходил ночью."
    if not can_find_eris:
        p "[my_eris.name]! Ну где же ты?"
    mind "Надо экономить силы и идти дальше, надеюсь я скоро найду хоть какое-то поселение."
    if not can_find_eris:
        mind "Или [my_eris.name], где же ты, [my_eris.name]?"

    scene bg desert3 at bg_size with dissolve
    $setTime(2)
    "Ты продвигаешься всё дальше. Благо солнце начинает садиться, но у тебя довольно серьезное обезвоживание."
    $minusHealth(10)
    if health <= 0:
        "Ты падаешь и теряешь сознание."
        return
    if not can_find_eris:
        p "Черт, и как мне её найти? Здесь нет ничего кроме меска и камней!"
        p "[my_eris.name]! Если ты здесь, ответь мне!"
        show eris transparent_smile at mid, transparent with dissolve
        eris "Я здесь, спасибо, что спас меня, [hero_name]~"
        p "[my_eris.name]... Э-это ты?"
        eris transparent_smile "Конечно я, глупенький, я услышала и пришла к тебе~" with dissolve
        eris transparent_shy "Следуй за мной, пойдем в таверну, и сделаем котят~" with dissolve
        mind "Нет, это галлюцинация!{w} Надо сосредоточиться и идти дальше."
        hide eris with dissolve
    else:
        show eris transparent_smile at mid, transparent with dissolve
        eris "[hero_name]~"
        p "[my_eris.name]? Ч-что ты здесь делаешь?"
        eris transparent_smile "Я здесь, чтобы помочь тебе~" with dissolve
        eris transparent_shy "Следуй за мной, пойдем в таверну, и сделаем котят~" with dissolve
        mind "Нет, это галлюцинация!{w} Надо сосредоточиться и идти дальше."
        hide eris with dissolve

    mind "К-кажется я вижу что-то в далеке."
    mind "Это какое-то поселение? {w} Надеюсь мне там помогут."
    scene bg desert_tents at bg_size with dissolve
    mind "Я... я дошел?"
    "Ты падаешь и теряешь сознание."
    return


label quest_eris_desert_asoka_dialog:
    scene bg desert_tent_indoor at bg_size with fade
    show asoka smile at mid with dissolve
    
    p "Где я?"
    asoka smile_say "Ты наконец очнулся. Я уж думала, что кричать придётся до заката." with dissolve
    
    asoka neutral_say "Ты в пустыне, в землях Татуина. Это всё, что тебе нужно знать. {w}Хотя, судя по твоему виду, ты и этого не поймёшь." with dissolve
    show asoka neutral with dissolve

    p "Татуин? Как я сюда попал? Я шёл по пустыне и… потерял сознание."
    asoka angry_say "Ты шёл по пустыне без воды и еды, как полный идиот! {w}Удивительно, что ты вообще жив. Я нашла тебя лежащим лицом в песке и тащила сюда, пока ты не соизволил открыть глаза." with dissolve
    show asoka angry with dissolve

    asoka angry_say "Но знаешь… ты всё равно особенный. Все наши соплеменники, и особенны мужчины..." with dissolve 
    asoka angry_say "Какая-то болезнь… или проклятье. Они падают один за другим, а ты — вот он, стоишь на ногах, хоть и выглядишь как полутруп." with dissolve
    show asoka angry with dissolve

    p "Проклятье? Это… странно. Я не отсюда. Я попал сюда через какую-то червоточину."
    mind "Не думаю, что стоит ей рассказывать о том, что я из другого мира."

    asoka surprised_say "Червоточину? Ты серьёзно?" with dissolve
    asoka smirk_say "Это что, твоя сказка на ночь, чтобы я пожалела тебя?" with dissolve
    show asoka smirk with dissolve
    mind "Конечно она мне не верит..."
    p "Н-но я не..."

    asoka smile_say "Хотя… если ты не врёшь, это многое объясняет. Ты не похож на местных. Да и, судя по всему, слишком упрям, чтобы умереть так просто." with dissolve
    show asoka smile with dissolve

    if can_find_eris:
        p "Я должен вернуться. Можешь помочь мне найти путь обратно?"
        asoka neutral_say "Скажи кто ты и откуда. Может быть я знаю, как помочь тебе вернуться." with dissolve
        p "Меня зовут [hero_name], я из Эльтирании."
        asoka neutral_say "Впервые слышу.{w} Ладно, возможно, я знаю, как помочь тебе. У нас есть старая легенда о разломах в пустыне… может, это и есть твоя червоточина. Но у меня есть условие." with dissolve
        show asoka neutral with dissolve
    else:
        p "Я должен найти [my_eris.name]. Можешь помочь мне найти её?"
        asoka neutral_say "[my_eris.name]? Рыжеволосая женщина человек? Ты случаем не её имеешь ввиду?" with dissolve
        show asoka neutral with dissolve
        p "Да! Это точно она!"
        asoka neutral_say "А ты получается [hero_name]?" with dissolve
        asoka neutral_say "[my_eris.name] сейчас лежит у нас в лазарете. В бреду она бубнила твоё имя. Судя по всему она подверглась проклятью, как и все остальные..." with dissolve
        asoka smile_say "С другой стороны это значит, что ты точно не откажешься." with dissolve
        show asoka smile with dissolve

    asoka smirk_say "Помоги мне снять проклятье с моего племени. Ты — единственный мужчина, который ещё может что-то сделать. " with dissolve
    asoka smirk_say "Если справишься, я не просто помогу в ответ… Я сделаю так, чтобы ты запомнил меня навсегда." with dissolve
    show asoka smirk with dissolve
    
    p "Хорошо, но как я могу помочь?"

    asoka neutral_say "Мы сюда прибыли как раз для изучения проблемы, но сейчас все наши мужчины уже лежат, а оставшиеся женщины за ними ухаживают." with dissolve
    show asoka neutral with dissolve

    p "А зачем вы взяли с собой мужчин, если знали, что все они помирают?"

    asoka angry_say "Мы взяли самых сильных, на которых не влияла никакая болезнь... {w}Пока мы не прибыли сюда." with dissolve
    show asoka neutral with dissolve

    p "И вы поняли, что здесь то самое место, которое может отравлять жизни ваших соплеменников?"

    asoka neutral_say "Да, всё верно. Мы решили, что источником болезни является эта пирамида. Ну или то, что находится внутри." with dissolve
    show asoka neutral with dissolve

    p "И..."

    asoka smile_say "Именно туда мы с тобой и отправимся. {w}Раньше я бы пошла одна, но кто знает, что там, да и ты у меня в долгу." with dissolve
    show asoka neutral with dissolve

    p "Понятно. И когда же мы отправимся?"

    asoka neutral_say "Когда ты полностью излечишь свои травмы. Ты себя давно видел?" with dissolve
    asoka angry_say "Выглядишь так, будто уже умер и воскрес." with dissolve
    show asoka angry with dissolve

    mind "Доля правды в этом есть."

    asoka smile_say "Вот, выпей и готовься. {w}Пустыня не прощает слабаков. И я тоже." with dissolve
    show asoka smile with dissolve
    
    "[asoka.name] протягивает тебе бутыль с подозрительным содержимым."
    menu:
        "[asoka.name] протягивает тебе бутыль с подозрительным содержимым."
        "Выпить":
            p "Ты меня спасла, не вижу причин не доверять тебе."
            asoka smile_say "Хорошо, хорошо, пей до дна." with dissolve
            $addHealth(100)
            p "Что-то мне не хорошо..."
            show asoka smirk with dissolve
            scene bg black_screen at bg_size with vpunch
            if intelligence >= 50:
                call asoka_root_tent_blowjob
            else:
                $customNotify("Необходимо 50 интеллекта")
            "Спустя какое-то время."
            scene bg desert_tent_indoor at bg_size with long_fade
            show asoka neutral_say_cummed at mid with dissolve
            asoka "Наконец пришел в себя? {w}Я дала тебе сильнодействующее лекарство, оно должно было тебя полностью восстановить."
            p "Х-хорошо, а что у тебя на лице?"
            hide asoka with dissolve
            "[asoka.name] вытирает лицо."
            show asoka neutral_say at mid with dissolve
            asoka "Ничего, я просто обедала."
            show asoka neutral with dissolve
        "Отказаться":
            p "Пока я не могу тебе доверять. Не переживай, я и так справлюсь."
            asoka angry_say "Смотри не пожалей о своих словах." with dissolve

    asoka neutral_say "Ладно, думаю мы можем идти." with dissolve
    return

label quest_eris_desert_crypt:
    #У входа в пирамиду
    call sand_steps_sound
    scene bg desert_pyramid_enterence at bg_size with fade
    "Перед тобой возвышается огромная пирамида."
    mind "Интересно, какие загадки она хранит в себе?"
    show asoka neutral_say at left_bit with dissolve
    asoka "Ты чего в облаках летаешь? Нам нужно исследовать ее и спасти жизни миллионов."
    show asoka neutral with dissolve

    p "А ты уверена, что именно здесь?" 
    asoka neutral_say "Да, наши величайшие умы пришли именно к этому выводу, жаль, что их уже не спасти." with dissolve
    show asoka neutral with dissolve

    p "Но ты вообще понимаешь, что нам нужно искать?"
    asoka smirk_say "Предположительно это что-то должно иметь большое гипнотическое воздействие." with dissolve
    asoka "Думаешь не справишься?"
    show asoka smirk with dissolve

    p "Надеюсь справлюсь..."
    if charisma >= 40:
        mind "Я точно справлюсь, я так много тренировался!"
    else:
        $customNotify("Необходимо 40 харизмы")
        mind "Не уверен, справлюсь ли, я не особо тренировал сопротивление гипнотическому воздействию."
    asoka smile_say "Не сомневайся в себе и всё получится!" with dissolve
    show asoka smile with dissolve

    #Внутри пирамиды
    $quest_eris_desert_crypt_move_right = False
    call sand_steps_sound
    scene bg desert_pyramid_indoor1 at bg_size with long_fade
    "Вы заходите в пирамиру. Факел зажегся как только ты ступил внутрь."
    mind "Подозрительно... Хотя наверно здесь тоже есть магия, нечему удивляться."
    show asoka neutral at left_bit with dissolve
    asoka neutral_say "Развилка, хм, куда пойдем?" with dissolve
    show asoka neutral with dissolve

    p "У меня тот же вопрос. Это ты у нас специалист по пирамидам и явно о болезни ты знаешь больше меня."
    asoka angry_say "А пораскинуть своими мозгами тебе слишком сложно? Сам выбери путь." with dissolve
    show asoka angry with dissolve

    menu:
        "Куда идти?"
        "Налево":
            $quest_eris_desert_crypt_move_right = False
            p "Ладно, идем налево."
        "Направо":
            $quest_eris_desert_crypt_move_right = True
            p "Ладно, идем направо."
    
    asoka neutral_say "Все равно любой из путей может быть верным, нам лишь надо найти что-то с высоким психическим влиянием и уничтожить."
    show asoka neutral with dissolve

    call sand_steps_sound
    if not quest_eris_desert_crypt_move_right:
        scene bg desert_pyramid_indoor2 at bg_size with long_fade
        show asoka neutral at right_mid with dissolve
    else:
        scene bg desert_pyramid_indoor2 at bg_size,flipped with long_fade
        show asoka neutral at left_mid with dissolve

    "Вы отказываетесь в коридоре, ведушим прямо."
    p "Ну что, идем дальше?"
    asoka neutral_say "Да. Разве у нас есть еще какие-то варианты?" with dissolve
    show asoka neutral with dissolve

    call sand_steps_sound
    if not quest_eris_desert_crypt_move_right:
        scene bg desert_pyramid_indoor3 at bg_size with long_fade
        show asoka neutral at right_mid with dissolve
    else:
        scene bg desert_pyramid_indoor3 at bg_size,flipped with long_fade
        show asoka neutral at left_mid with dissolve

    asoka neutral_say "Ещё один идентичный проход, идем быстрее." with dissolve
    show asoka neutral with dissolve
    p "Ладно, ладно, идем."
    "Вы ускоряете шаг"
    
    call sand_steps_sound
    if not quest_eris_desert_crypt_move_right:
        scene bg desert_pyramid_indoor4 at bg_size with fade
        show asoka neutral at right_mid with dissolve
    else:
        scene bg desert_pyramid_indoor4 at bg_size,flipped with fade
        show asoka neutral at left_mid with dissolve

    pause .5
    
    call sand_steps_sound
    if not quest_eris_desert_crypt_move_right:
        scene bg desert_pyramid_indoor2 at bg_size with fade
        show asoka neutral at right_mid with dissolve
    else:
        scene bg desert_pyramid_indoor2 at bg_size,flipped with fade
        show asoka neutral at left_mid with dissolve

    "Проходы похожи один на другой."
    "Ты уже не понимаешь сколько бродишь по этим бесчисленным коридорам."

    pause .5
    
    call sand_steps_sound
    if not quest_eris_desert_crypt_move_right:
        scene bg desert_pyramid_indoor3 at bg_size with fade
        show asoka neutral at right_mid with dissolve
    else:
        scene bg desert_pyramid_indoor3 at bg_size,flipped with fade
        show asoka neutral at left_mid with dissolve

    pause .5

    call sand_steps_sound
    if not quest_eris_desert_crypt_move_right:
        scene bg desert_pyramid_indoor4 at bg_size with fade
        p "Ч-что? Где [asoka.name]? Почему я здесь один?"
        p "Л-ладно, она самостоятельная девочка, догонит."
        if not can_find_eris:
            p "Мне надо торопиться, чтобы найти источник, вылечить всех и вернуться назад с [my_eris.name]."
        else:
            p "Самое главное сейчас уничтожить источник гипнотического излучения, как сказала [asoka.name]."
        "Ты в одиночку идешь дальше."
        mind "Ч-что? [asoka.name]?"
        call asoka_root_suck_another
        scene bg desert_pyramid_indoor4 at bg_size with flash
        "[asoka.name] быстрым движением разрубает нечисть."
        show asoka neutral_say_cummed at left_mid with dissolve
        asoka "Я победила противника."
        show asoka neutral with dissolve
        p "Х-хорошо..."
        asoka surprised "Ах да!" with dissolve
        hide asoka with dissolve
        "[asoka.name] вытирает лицо."
        show asoka neutral_say at left_mid with dissolve
        asoka "Ну что, идем дальше?"
        show asoka neutral with dissolve
        mind "Она думает, что я ничего не заметил?!"
    else:
        scene bg desert_pyramid_indoor4 at bg_size,flipped with fade
        p "[asoka.name]? Ты тут?"
        show asoka neutral at left_mid with dissolve
        asoka neutral_say "Да, конечно я тут, куда я могла подеваться?" with dissolve
        p "М-мне просто показалось..."
        show mummy stand_angry at right_mid with vpunch
        mummy "Гррр!"
        show asoka angry with dissolve
        "Внезапно на тебя нападает мумия."
        call start_battle(90, 120 , mummy.name, 'return_here')
        if not last_battle_win:
            $health = 10
            return
        hide asoka with vpunch
        "В ходе битвы [asoka.name] пострадала, прикрыв тебя от удара."
        "Но [mummy.name] не отступает."
        mummy "Грар!"
        call start_battle(45, 150 , mummy.name, 'return_here')
        if not last_battle_win:
            $health = 10
            return
        show mummy stand_embarrassed at right_mid with dissolve
        mummy "Рррр?.."
        if strength < 60:
            $customNotify("Необходимо 60 силы")
        menu:
            "Что сделать с этой мумией?"
            "Надругаться" if strength >= 60:
                call mummy_root_desert_pussy_fuck
                scene bg desert_pyramid_indoor4 at bg_size,flipped with fade
            "Добить":
                hide mummy with flash
                "Ты хладнокровно избавляешься от нечисти."
            "Отпустить":
                p "Ступай, пускай ты и [mummy.name], но ты женщина, я не могу тебя убить."
                $addLove(my_freya, 10)
                hide mummy with dissolve
                "[mummy.name] уходит."
                p "Как там [asoka.name]? Надо проверить, в порядке ли она!"
                call sand_steps_sound
                "Ты идешь в сторону [asoka.name]."
                show mummy stand_angry at mid with red
                $minusHealth(20)
                p "Чёртова нежить!"
                hide mummy with flash
                "Одним мощным ударом ты уничтожаешь её."
                if health <= 0:
                    "Ты падаешь и теряешь сознание."
                    return
                p "Эта тварь!{w} Ладно, она мертва, теперь окончательно."

        p "Точно, надо узнать, в порядке ли [asoka.name]."
        "Ты немного трясешь ее за плечи и она просыпается."
        show asoka surprised at left_mid with hpunch
        asoka surprised_say "А? Где я?" with dissolve
        show asoka surprised with dissolve
        p "Мы в пустыне, в пирамиде, расследуем некую болезнь, из-за которой умерло всё твоё племя."
        asoka surprised_say "А?" with dissolve
        asoka angry_say "Точно, я вспомнила, идем дальше, чувствую, мы уже близко." with dissolve
        show asoka angry with dissolve
    return

label quest_eris_desert_crypt_wake_up:
    scene bg desert_pyramid_throne1 at bg_size with fade
    show asoka angry at left_mid with dissolve
    asoka angry_say "Спящая красавица наконец очнулась?" with dissolve
    show asoka angry with dissolve
    p "Я-я..."
    asoka angry_say "Никаких оправданий! Соберись! Впереди трон, а на нем скелет, думаю он то нам и нужен!" with dissolve
    $addHealth(20)
    show asoka angry with dissolve
    return

label quest_eris_black_hole_skelet_king:
    scene bg desert_pyramid_throne1 at bg_size with fade
    show asoka angry at left_mid with dissolve
    asoka angry_say "Эй ты! Мы одолеем тебя!" with dissolve
    show asoka angry with dissolve
    "..."
    "....."
    "Ответа не последовало, скелет не двинулся с места."
    p "Может быть он..."
    show bg desert_pyramid_throne2 at bg_size with dissolve
    call hide_dialog
    p "[asoka.name]! Ты видела? Его голова отвалилась!"
    asoka angry_say "Мы не боимся тебя, тварь! Выходи на честный бой!" with dissolve
    p "[asoka.name]? Ты меня слышишь?"
    "[asoka.name] продолжает кричать на скелет."
    "Ты подходишь к ней."
    asoka angry_say "Чертов скелет! Решил натравить на меня свою нежить?!" with dissolve
    menu:
        "[asoka.name] замахивается на тебя."
        "Защищаться":
            call start_battle(100, 200, asoka.name, 'return_here')
            scene bg desert_pyramid_throne2_2 at bg_size with dissolve
            call hide_dialog
            mind "Это было не просто."
            mind "Так, пока [asoka.name] в отключке надо разобраться."
            "Ты замечаешь, что череп скелета начал истекать кровью."
            p "Проклятый скелет!"
            show bg desert_pyramid_throne3 at bg_size with flash
            call hide_dialog
            "Ты разрушаешь череп, вся кровь и свечение моментально испаряются."
            show asoka surprised with dissolve
            asoka "А?" with dissolve
            mind "Понятно, она была заколдована, видимо то самое гипнотическое воздействие."
        "Заставить её остановиться" if charisma >= 40:
            p "УСПОКОЙСЯ! [asoka.name]!"
            asoka surprised "Ась?" with flash
            p "Ты только что хотела меня убить!"
            asoka neutral_say "Нет. Мы только что зашли." with dissolve
            show asoka neutral with dissolve
            mind "Бесполезно..."
            show bg desert_pyramid_throne2_2 at bg_size with dissolve
            call hide_dialog
            asoka smile_say "Гляди, череп истекает кровью."
            p "И это свечение..."
            hide asoka with dissolve
            show bg desert_pyramid_throne3 at bg_size with flash
            call hide_dialog
            show asoka smile at mid with dissolve
            "Не успеваешь ты договорить, как [asoka.name] ризбивает череп вдребезги, вся кровь и свечение моментально испаряются."
        "Быстро вырубить её" if strength >= 100:
            hide asoka with vpunch
            "Ты быстро наносишь один хороший удар в челюсь. [asoka.name] падает."
            mind "Так, пока [asoka.name] в отключке надо разобраться."
            "Ты замечаешь, что череп скелета начал истекать кровью."
            p "Проклятый скелет!"
            show bg desert_pyramid_throne3 at bg_size with flash
            call hide_dialog
            "Ты походишь и разрушаешь череп, вся кровь и свечение моментально испаряются."
            "[asoka.name] приходит в себя."
            show asoka angry with dissolve
            asoka "Ай.. Как больно..." with dissolve
            show asoka angry with dissolve
            asoka angry_say "Что произошло?" with dissolve
            show asoka angry with dissolve
            mind "Понятно, она была заколдована, видимо то самое гипнотическое воздействие."
        "Разбить череп" if intelligence >= 40:
            hide asoka with dissolve
            show bg desert_pyramid_throne3 at bg_size with flash
            call hide_dialog
            "Ты подбегаешь и разбиваешь череп вдребезги."
            "[asoka.name] приходит в себя."
            show asoka surprised at left_mid with dissolve
            asoka surprised "А? Что?" with dissolve
            p "Ты только что хотела напасть на меня!"
            asoka neutral_say "Нет. Мы только что зашли." with dissolve
            show asoka neutral with dissolve
            mind "Понятно, она была заколдована, видимо то самое гипнотическое воздействие."

    asoka neutral_say "Говори, что произошло!" with dissolve
    show asoka neutral with dissolve
    "Ты рассказваешь ей всё, что только что произошло."
    
    asoka surprised "Правда?" with dissolve
    asoka neutral_say "Получается меня загипнотизировали. Странно, почему на тебя гипноз никак не повлиял?" with dissolve
    show asoka neutral with dissolve
    mind "Думаю надо сказать спасибо Богине."
    p "Не знаю, может я особенный."
    asoka smirk_say "Особенный, да?" with dissolve
    asoka smile_say "Да, ты действительно довольно необычный." with dissolve
    asoka neutral_say "В любом случае я больше не чувствую никакого влияния, думаю наша работа здесь окончена." with dissolve
    show asoka neutral with dissolve
    "Вы выходите из пирамиды без без каких-либо преград."
    return


label quest_eris_black_hole_end:
    call sand_steps_sound
    scene bg desert_pyramid_enterence at bg_size with fade
    show asoka neutral at left_bit with dissolve
    asoka neutral_say "Надеюсь это помогло, если так, то все уже должны очнуться и поправляться." with dissolve
    p "..."

    call sand_steps_sound
    scene bg desert_tents at bg_size with dissolve
    show asoka smile at left_bit with dissolve
    "[asoka.name] заметила, что её друзья и соплеменники начали приходить в себя."
    asoka smile_say "У нас получилось! Мы сделали это!" with dissolve
    asoka smile_say "Иди в палатку, я позже догоню, мне нужно всем рассказать." with dissolve
    hide asoka with dissolve
    "Ты идешь в палатку."

    scene bg desert_tent_indoor at bg_size with fade
    if not can_find_eris:
        show eris smile_blush at mid with dissolve
        eris "[hero_name]... Я так переживала... Мне рассказали, что ты ушел в проклятую пирамиду."
        eris laugh "Я так рада, что с тобой всё хорошо!" with dissolve
        show eris smile with dissolve
        p "Да, теперь всё хорошо. Отдыхай, тебе нужны силы."
        eris smile_blush "Да." with dissolve
        hide eris with dissolve
        mind "Надо же, [my_eris.name] никогда бы не согласилась идти отдыхать... Видимо она действительно без сил."
    "Ты решил сесть и наконец перевести дух."
    "..."
    "....."
    "......."
    asoka "Эй, [hero_name]!"
    mind "Спокойствие длилось недолго."
    "Ты выходишь из палатки."

    call sand_steps_sound
    scene bg desert_tents at bg_size with dissolve
    show asoka neutral at mid with dissolve
    asoka neutral_say "Как мы и договаривались, я выведу тебя отсюда, и мы постараемся сделать так, чтобы этот портал больше не открывался." with dissolve
    asoka smirk_say "Ну разве что исключительно для тебя~" with dissolve
    asoka smile_say "Кстати ты не забыл, что ещё я тебе обещала?" with dissolve
    show asoka smirk with dissolve
    menu:
        asoka "Ты не забыл, что ещё я тебе обещала?"
        "Что запомню тебя?":
            asoka smirk_say "Верно, [hero_name]. Следуй за мной." with dissolve
            show asoka smirk with dissolve
            call sand_steps_sound
            "[asoka.name] заводит тебя в одну из палаток."
            call asoka_root_tent_vaginal_fuck
            "Вы выходите из палатки."
            scene bg desert_tents at bg_size with dissolve
            mind "[asoka.name] приводит себя в порядок, надо её дождаться."
            show asoka smirk at mid with dissolve
            asoka smile_say "На этом всё, [hero_name]. Надеюсь ты остался доволен." with dissolve
            show asoka smile with dissolve
            p "Еще как доволен. Я точно этого не забуду."
        "Отдашь мне свою сочную задницу?":
            asoka angry_say "Ты охренел? Ничего я такого не обещала!" with dissolve
            show asoka angry with dissolve
            mind "Ой.."
            p "Эм, ладно..."
        "Нет, не помню":
            asoka smile_say "Ожидаемо, много чего произошло." with dissolve
            show asoka smile with dissolve
            p "А что ты мне обещала?"
            asoka smile_say "Да ничего, проехали, собирайся, [hero_name]." with dissolve
            show asoka smile with dissolve

    show asoka neutral_say at mid with dissolve
    if can_find_eris:
        asoka "Теперь мы можем отправить тебя домой."
    else:
        asoka "Теперь мы можем отправить вас с [my_eris.name] домой."
    show asoka neutral with dissolve
    p "Что? Уже? Как вы это сделаете?"
    mind "Я не хочу вдруг оказаться посреди океана или что-то в этом роде."
    asoka smile_say "Наши величайшие умы уже давно изучили эту технологию, я лишь подняла архивы." with dissolve
    
    if can_find_eris:
        asoka smirk_say "Просто стой на месте, мы тебя телепортируем и заблокируем обратный доступ для всех." with dissolve
    else:
        asoka smirk_say "Просто стойте на месте, мы вас телепортируем и заблокируем обратный доступ для всех." with dissolve
    
    asoka smirk_say "Конечно кроме тебя, [hero_name]~" with dissolve
    show asoka smirk with dissolve
    p "Прощай, [asoka.name]."
    asoka smile_say "До встречи, [hero_name]." with dissolve
    show asoka smile with dissolve
    hide asoka with dissolve
    
    if not can_find_eris:
        mind "Стоп, а как же..."
        show eris annoyed at left_bit with dissolve
        eris "Эй, ты про меня не забыл?"
        p "Конечно не забыл, и ты не забудь, что с тебя еще за свидание причитается."
        eris embarassed_blush "Я-я помню..." with dissolve

    return
