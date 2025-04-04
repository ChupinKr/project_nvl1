label chizuru_club_dialog:
    call dance_scene
    "Танец заканчивается, [chizuru.name] спускается со сцены."
    show chizuru d_smirk at mid with dissolve
    chizuru d_smirk_say "Как тебе танец, красавчик?"with dissolve
    show chizuru d_smirk with dissolve
    mind "Что? Она это мне говорит?"
    p "Да, шикарный танец."
    chizuru d_smile_say "Рада, что тебе понравилось." with dissolve
    show chizuru d_smile with dissolve
    p "Так тебе что-то нужно от меня?"
    chizuru d_smirk_say "А ты за словом в карман не лезешь, да?" with dissolve
    chizuru d_smirk_say "Ладно, вижу с тобой не будет так просто." with dissolve
    show chizuru d_smirk with dissolve
    p "Сколько?"
    chizuru d_smile_say "100 монет за мою задницу." with dissolve
    show chizuru d_smile with dissolve
    menu:
        "100 монет за задницу [chizuru.name]"
        "Беру" if money >= 100:
            p "Конечно беру, за такую то попку!"
            $minusMoney(100)
            chizuru d_closed_say "Спасибо за покупку~" with dissolve
            chizuru d_smile_say "Следуй за мной~" with dissolve
            show chizuru d_smile with dissolve
            "Вы отходите от толпы, направляясь к общественному туалету."
            call chizuru_root_toilet_suck
            if strength >= 50:
                menu:
                    "[chizuru.name] уходит"
                    "Схватить":
                        scene bg chizuru_root_toilet_suck9 at bg_size with vpunch
                        chizuru "А?!"
                        scene bg chizuru_root_toilet_suck10_say at bg_size with dissolve
                        chizuru "Ты что себе позволяешь! Отпусти меня!"
                        p "Договор был на твою задницу."
                        scene bg chizuru_root_toilet_suck11 at bg_size with dissolve
                        chizuru "Ммм~ Ненасытный..."
                        call chizuru_root_toilet_own_masturbate
                        call chizuru_root_toilet_vaginal_sex
                    "Ничего":
                        "Ты позволяешь [chizuru.name] уйти."
                        scene bg club_toilet at bg_size with dissolve
            else:
                $customNotify("Необходимо 50 силы")
        "Не пойдет":
            p "Не в этот раз, детка."
            chizuru d_smirk_say "Неплохо тогуешься, ладно, 50 монет." with dissolve
            show chizuru d_smirk with dissolve
            menu:
                "50 монет за задницу [chizuru.name]"
                "Беру" if money >= 50:
                    p "Другое дело, беру!"
                    $minusMoney(50)
                    chizuru d_closed_say "Спасибо за покупку~" with dissolve
                    chizuru d_smile_say "Следуй за мной~" with dissolve
                    show chizuru d_smile with dissolve
                    "Вы отходите от толпы, направляясь к общественному туалету."
                    call chizuru_root_toilet_suck
                    if strength >= 50:
                        menu:
                            "[chizuru.name] уходит"
                            "Схватить":
                                scene bg chizuru_root_toilet_suck9 at bg_size with vpunch
                                chizuru "А?!"
                                scene bg chizuru_root_toilet_suck10_say at bg_size with dissolve
                                chizuru "Ты что себе позволяешь! Отпусти меня!"
                                p "Договор был на твою задницу."
                                scene bg chizuru_root_toilet_suck11 at bg_size with dissolve
                                chizuru "Ммм~ Ненасытный..."
                                call chizuru_root_toilet_own_masturbate
                                call chizuru_root_toilet_vaginal_sex
                            "Ничего":
                                "Ты позволяешь [chizuru.name] уйти."
                                scene bg club_toilet at bg_size with dissolve
                    else:
                        $customNotify("Необходимо 50 силы")
                "Нет":
                    p "Говорю же, не интересует"
                    chizuru d_surprised_say "Впервые у меня такое..." with dissolve
                    p "Впервые кому-то не понравилось твоё тело?"
                    chizuru d_sad_say "Я обслужу тебя бесплатно..." with dissolve
                    show chizuru d_sad with dissolve
                    menu:
                        "Бесплатное обслуживание от [chizuru.name]"
                        "Как пожелаешь":
                            p "Ладно, если ты настаиваешь. {w}Надеюсь оно будет стоить моего времени."
                            chizuru d_smirk_say "Хах, так и знала, никто не может мне отказать." with dissolve
                            chizuru "Следуй за мной~"
                            show chizuru d_smirk with dissolve
                            "Вы отходите от толпы, направляясь к общественному туалету."
                            call chizuru_root_toilet_suck
                            if strength >= 50:
                                menu:
                                    "dD[chizuru.name] уходит"
                                    "Схватить":
                                        scene bg chizuru_root_toilet_suck9 at bg_size with vpunch
                                        chizuru "А?!"
                                        scene bg chizuru_root_toilet_suck10_say at bg_size with dissolve
                                        chizuru "Ты что себе позволяешь! Отпусти меня!"
                                        p "Договор был на твою задницу."
                                        scene bg chizuru_root_toilet_suck11 at bg_size with dissolve
                                        chizuru "Ммм~ Ненасытный..."
                                        call chizuru_root_toilet_own_masturbate
                                        call chizuru_root_toilet_vaginal_sex
                                    "Ничего":
                                        "Ты позволяешь [chizuru.name] уйти."
                                        scene bg club_toilet at bg_size with dissolve
                            else:
                                $customNotify("Необходимо 50 силы")
                        "Нет":
                            p "Ты меня не интересуешь, что непонятного?"
                            chizuru d_cry_say "Да что же со мной не так?!" with dissolve
                            chizuru d_cry_angry_say "Нет! Я прекрасна!{w} Это ты идиот!" with dissolve
                            p "Как скажешь, [chizuru.name]."
                            $minusHealth(5)
                            show chizuru d_cry_angry with flash
                            $customNotify("Ты получил пощечину")
                            $can_find_chizuru = False
                            if health <= 0:
                                jump battle_loss
                            hide chizuru with dissolve
                            "[chizuru.name] ушла."
                            return
                            
    scene bg club_toilet at bg_size with dissolve
    mind "Чтож, мне здесь больше делать нечего."
    call door_enter_sound
    return

label chizuru_root_dance:
    scene bg chizuru_root_dance0 at bg_size with fade
    "Ты подходи к сцене и видишь чарующую девушку и ее шикарный танец с шестом."

    scene bg chizuru_root_dance1 at bg_size with dissolve
    pause.5
    scene bg chizuru_root_dance2 at bg_size with dissolve
    pause.5
    scene bg chizuru_root_dance3 at bg_size with dissolve
    pause.5
    scene bg chizuru_root_dance2 at bg_size with dissolve
    mind "Мне кажется, или она смотрит на меня?"
    guy1 "Зажигай, [chizuru.name]!"

    scene bg chizuru_root_dance3 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance2 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance3 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance2 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance3 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance2 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance3 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance2 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance3 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance2 at bg_size with dissolve
    pause.2
    scene bg chizuru_root_dance3 at bg_size with dissolve
    mind "Как же эта [chizuru.name] горяча..."
    
    scene bg chizuru_root_dance4 at bg_size with dissolve
    pause.3
    scene bg chizuru_root_dance5 at bg_size with dissolve
    chizuru "Ах..."
    
    scene bg chizuru_root_dance5_2 at bg_size with dissolve
    pause.3
    scene bg chizuru_root_dance6 at bg_size with dissolve
    pause.5
    scene bg chizuru_root_dance7 at bg_size with dissolve
    chizuru "Хааа... аах."

    scene bg chizuru_root_dance8 at bg_size with dissolve
    pause .3
    
    return

label chizuru_root_toilet_suck:
    call brothel_bass_sound
    scene bg club_toilet at bg_size with dissolve
    show chizuru d_smirk at mid with dissolve
    chizuru d_smirk_say "Мы на месте~" with dissolve
    show chizuru d_smirk with dissolve

    scene bg chizuru_root_toilet_suck0 at bg_size with dissolve
    pause .4
    scene bg chizuru_root_toilet_suck1 at bg_size with dissolve
    call hide_dialog
    "[chizuru.name] садится на колени перед тобой."
    
    scene bg chizuru_root_toilet_suck1_say at bg_size with dissolve
    chizuru "Ну что, достанешь свою игрушку?"
    scene bg chizuru_root_toilet_suck1 at bg_size with dissolve
    call hide_dialog
    p "Сначала сбрось лишнюю одежду."

    scene bg chizuru_root_toilet_suck2 at bg_size with dissolve
    pause .4
    scene bg chizuru_root_toilet_suck3 at bg_size with dissolve
    pause .4
    scene bg chizuru_root_toilet_suck3_2 at bg_size with dissolve
    call hide_dialog
    "[chizuru.name] скидывает топ"
    
    scene bg chizuru_root_toilet_suck3_2_say at bg_size with dissolve
    chizuru "Тебе так нравится моя грудь?"

    scene bg chizuru_root_toilet_suck3_2 at bg_size with dissolve
    mind "Как же она заводит..{w} Ладно, пора достать \"кракена\"."

    scene bg chizuru_root_toilet_suck4 at bg_size with vpunch
    pause .3
    scene bg chizuru_root_toilet_suck4_2 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_suck4_3_say at bg_size with dissolve
    call hide_dialog
    chizuru "Именно на такой размер я и рассчитывала~"
    
    scene bg chizuru_root_toilet_suck4_3 at bg_size with dissolve
    p "Может приступишь уже?"
    
    scene bg chizuru_root_toilet_suck5 at bg_size with dissolve
    call hide_dialog
    "[chizuru.name] хватает твой толстый член обеими руками и начинает дрочить."

    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_suck5_5 at bg_size with dissolve

    chizuru "Моя техника тебя не впечатлила?"
    p "Ах... Т-ты была очень близка..."

    scene bg chizuru_root_toilet_suck5_4 at bg_size with dissolve
    call hide_dialog
    "Судя по всему [chizuru.name] рада это слышать."
    
    scene bg chizuru_root_toilet_suck5_5 at bg_size with dissolve
    pause .4
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_suck5_2 at bg_size with flash
    p "Аргх!"

    scene bg chizuru_root_toilet_suck6 at bg_size with flash
    chizuru "Мммм~"

    scene bg chizuru_root_toilet_suck6_2 at bg_size with flash
    call hide_dialog

    scene bg chizuru_root_toilet_suck6_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_suck6_3_say at bg_size with dissolve
    chizuru "Вижу тебе действительно понравилось~"
    
    scene bg chizuru_root_toilet_suck6_3 at bg_size with dissolve
    p "Потрясающая техника..."
    
    scene bg chizuru_root_toilet_suck7 at bg_size with fade
    call hide_dialog
    "[chizuru.name] поднимается"

    scene bg chizuru_root_toilet_suck8_say at bg_size with dissolve
    call hide_dialog
    chizuru "Спасибо за покупку."

    scene bg chizuru_root_toilet_suck8 at bg_size with dissolve
    return

label chizuru_root_toilet_own_masturbate:
    scene bg chizuru_root_toilet_own_masturbate0 at bg_size with dissolve
    pause .5
    scene bg chizuru_root_toilet_own_masturbate0_2 at bg_size with dissolve
    call hide_dialog
    chizuru "Хих~"
    
    scene bg chizuru_root_toilet_own_masturbate0_3 at bg_size with dissolve
    call hide_dialog
    "[chizuru.name] сильно оттягивает свои стринги."
    
    scene bg chizuru_root_toilet_own_masturbate0_4 at bg_size with vpunch
    call hide_dialog
    "*Щелчок*"
    "Стринги [chizuru.name] лопнули от натяжения."
    
    scene bg chizuru_root_toilet_own_masturbate1 at bg_size with dissolve
    call hide_dialog
    "Она прижалась киской к твоему напряженному члену."
    
    scene bg chizuru_root_toilet_own_masturbate1_2 at bg_size with dissolve
    pause .2
    scene bg chizuru_root_toilet_own_masturbate1_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate1_4 at bg_size with vpunch
    call hide_dialog
    
    scene bg chizuru_root_toilet_own_masturbate2_1 at bg_size with dissolve
    call hide_dialog
    chizuru "Мнх..."
    
    scene bg chizuru_root_toilet_own_masturbate2_2 at bg_size with dissolve
    pause .5
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .5
    scene bg chizuru_root_toilet_own_masturbate2_4 at bg_size with dissolve
    pause .5
    scene bg chizuru_root_toilet_own_masturbate2_2 at bg_size with dissolve
    pause .5
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .5
    scene bg chizuru_root_toilet_own_masturbate2_4 at bg_size with dissolve
    pause .5
    scene bg chizuru_root_toilet_own_masturbate2_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_4 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_4 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_4 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_4 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_own_masturbate2_3 at bg_size with dissolve
    pause .2
    scene bg chizuru_root_toilet_own_masturbate3_1 at bg_size with flash
    pause .35
    scene bg chizuru_root_toilet_own_masturbate3_2 at bg_size with flash
    call hide_dialog
    chizuru "Ааааах~~"

    scene bg chizuru_root_toilet_own_masturbate3_3_say at bg_size with dissolve
    call hide_dialog
    chizuru "Ах..."

    scene bg chizuru_root_toilet_own_masturbate3_3 at bg_size with dissolve
    call hide_dialog
    return

label chizuru_root_toilet_vaginal_sex:
    p "Самое время для главного блюда."
    scene bg chizuru_root_toilet_vaginal_sex0 at bg_size with vpunch
    pause .5
    scene bg chizuru_root_toilet_vaginal_sex0_1 at bg_size with dissolve
    call hide_dialog
    chizuru "Т-ты!"
    "Ты начинаешь двигаться, проникая всё глубже в её киску."

    scene bg chizuru_root_toilet_vaginal_sex1 at bg_size with fade
    pause .3
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_vaginal_sex1_3 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_vaginal_sex1 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .3
    scene bg chizuru_root_toilet_vaginal_sex1_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_3 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .1
    scene bg chizuru_root_toilet_vaginal_sex1 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_vaginal_sex1_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_vaginal_sex1 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_vaginal_sex1_3 at bg_size with dissolve
    pause .05
    scene bg chizuru_root_toilet_vaginal_sex1_2 at bg_size with flash
    pause .2
    scene bg chizuru_root_toilet_vaginal_sex2 at bg_size with flash
    call hide_dialog
    chizuru "А-аааах!"

    scene bg chizuru_root_toilet_vaginal_sex3 at bg_size with flash
    call hide_dialog
    "Ты продолжаешь наполнять [chizuru.name]."
    p "Прими всё!"

    scene bg chizuru_root_toilet_vaginal_sex4 at bg_size with flash
    call hide_dialog
    chizuru "А-аааа!"

    scene bg chizuru_root_toilet_vaginal_sex5 at bg_size with vpunch
    call hide_dialog
    "[chizuru.name] падает на пол обессиленная не в состоянии ничего сказать."

    scene bg chizuru_root_toilet_vaginal_sex6 at bg_size with flash
    call hide_dialog
    "Ты выпускаешь последнюю порцию спермы на ее уставшее тело."
    chizuru "Аа... ааах~"
    p "До встречи, [chizuru.name]."
    "Ты надеваешь штаны и уходишь"
    return