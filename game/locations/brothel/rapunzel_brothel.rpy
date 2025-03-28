define first_r_root = True
define can_go_r = True
define first_time_visit_room_rapunzel = True

label rapunzel_brothel:

    if first_time_visit_room_rapunzel:
        $first_time_visit_room_rapunzel = False
        r "[hero_name], подойди сюда."
        "[r.name] заводит тебя в комнату"
        scene bg brothel_private with dissolve
        show r smile  with dissolve
        mind "Какая приятная комната, только вот выглядит как будто сделана для приватных утех.."
        r "В следующий раз сразу иди сюда, это моя комната, не надо беспокоить другие гостей!"
    else:
        scene bg brothel_private with dissolve
        show r smile  with dissolve
        r "Ты меня искал?"
    jump rapunzel_brothel_menu

label rapunzel_brothel_menu:
    menu:
        "Помоги мне расслабиться" if not first_r_root:
            r "Ах, конечно! Мне самой это нравится!"
            jump rapunzel_root_menu
        "Попросить тренировку":
            r "Ах, ты хочешь улучшить свои навыки? Мне это нравится!"
            call rapunzel_training
            if last_charisma_training_win and first_r_root and my_rapunzel_love >= 50:
                $ first_r_root = False
                r @smile_shy "Ты так много трудишься и так много сделал для меня." with dissolve
                r @smirk "Может я могу помочь тебе расслабиться?" with dissolve
                menu:
                    r "Может я могу помочь тебе расслабиться?"
                    "Определенно можешь":
                        p "Ты точно можешь мне помочь!"
                        show r smile_shy with dissolve
                        r "..."
                        jump rapunzel_root_menu
                    "Ты? Чем?":
                        p "И чем ты можешь мне помочь? Какой мне толк от твоей помощи?"
                        r @neutral "уходи..." with dissolve
                        r annoyed "Я больше не хочу тебя видеть!" with dissolve
                        $can_go_r = False
                        "[r.name] силой выталкивает тебя из своей комнаты и запирает дверь на ключ"
                        $customNotify("Ты больше никогда не встретишь [r.name]")
                        $nextTime()
                        jump brothel
            elif last_charisma_training_win:
                $addChar(["char"], 10)
                r smile_shy "Хорошая работа, [hero_name]!" with dissolve
                $addLove(my_rapunzel, 10)
            else:
                r annoyed "Мог бы хоть постараться!" with dissolve
                $minusLove(my_rapunzel, -2)
            $nextTime()
            jump rapunzel_brothel_menu
        "Спросить про задание" if isNoQuestNow():
            p "У тебя не найдется задания для меня?"
            r "Хм... На самом деле, у меня есть кое-что интересное!"
            call rapunzel_quests
            jump rapunzel_brothel_menu
        "Отказаться от выполнения задания" if isActualQuestOfCharacter("r"):
            p "Я не смогу выполнить это задание."
            r "Ох, ну хорошо, если передумаешь - приходи."
            $ removeQuest()
            jump rapunzel_brothel_menu
        "Уйти":
            p "В другой раз, Рапунцель."
            show r annoyed with dissolve
            r "Ну вот, а я уже придумала, чем тебя занять~"
            r smile "Ладно, не пропадай!" with dissolve
            jump brothel

label rapunzel_root_menu:
    if getLocation() != "brothel":
        r "Пойдем, я знаю, где я смогу помочь тебе расслабиться."
        call tavern_scene
        pause 3.5
        show r smile at right with dissolve
        if not canVisit("tavern"):
            $updateCanVisit("tavern", True)
        r @smile_shy "Мы еще не пришли, идем, за мной!" with dissolve
        "Мы заходим в туалет, открываем потайную дверь и заходим в бордель."

        play sound "audio/door_enter.ogg"
        scene bg brothel_girl1 with dissolve
        play music "audio/brothel_sound.ogg" fadein 2.0 loop
        show r smile at right with dissolve
        
        if not canVisit("brothel"):
            $updateCanVisit("brothel", True)
        
        r @smile_shy "Ну же, идем в мою комнату!" with dissolve
        scene bg brothel_private with dissolve
        show r smile  with dissolve

    menu:
        "Мастурбация" if my_rapunzel_love >= 50:
            call r_root_masturbate
            $nextTime()
            jump brothel
        "Минет" if my_rapunzel_love >= 70:
            call r_root_blowjob  
            $nextTime()
            jump brothel
        "Секс" if my_rapunzel_love >= 80:
            call r_root_fuck  
            $nextTime()
            jump brothel
        "Анал" if my_rapunzel_love >= 90:
            call r_root_anal  
            $nextTime()
            jump brothel
        "Фетиш" if my_rapunzel_love >= 200:
            call r_root_fetish  
            $nextTime()
            jump brothel
        "Вернуться":
            "Ты уходишь восстанавливать силы"
            r @smirk "До встречи~"
            jump brothel

label r_root_masturbate:
    "[r.name] садит тебя на свою кровать и скидывает с себя почти всю одежду"
    show r smile_naked  with dissolve
    "Она садится на колени перед тобой, обнажая свою прелестную грудь"
    hide r  with dissolve
    scene bg r_masturbate1 with dissolve
    call hide_dialog
    mind "Чёрт, как мне вообще реагировать на это?"

    scene bg r_masturbate2_1 with dissolve
    call hide_dialog
    mind "[r.name] прикрыла одну грудь."  
    r "Ты ведь всё равно уже видел... Так зачем мне закрываться?"

    scene bg r_masturbate2_2 with dissolve
    call hide_dialog
    mind "Её пальцы неспешно скользят по груди... Она что, дразнит меня?"  
    r "Ммм... Интересно, а если так?"
    p "Ты это делаешь специально, да?"

    scene bg r_masturbate3 with dissolve
    call hide_dialog
    mind "Теперь [r.name] обеими руками трогает свои груди."  
    r "Ты ведь не против, если я немного поиграю сама с собой?"
    p "..."

    scene bg r_masturbate4_test with dissolve
    call hide_dialog
    mind "Она ущипнула сосок и всё еще ухмыляется, ух, как же это заводит."  

    scene bg r_masturbate4_test2 with dissolve
    call hide_dialog
    r "Ах~... А ты так напряжён... Расслабься, просто смотри."
    p "Ты говоришь так, будто это легко."

    scene bg r_masturbate5 with dissolve
    call hide_dialog
    r "Ааах..."
    mind "Как же развратно это выглядит, и как мне оставаться спокойным?"


    scene bg r_masturbate6 with dissolve
    call hide_dialog
    "Удовольствие на лице [r.name] резко сменилось на ухмылку"
    mind "Она хотела убедиться, что я еле держусь? Так это была проверка?"
    r "Тебе ведь нравится? Не скрывай этого."
    p "Думаю, тут уже бесполезно что-то скрывать.."

    scene bg r_masturbate7 with dissolve
    call hide_dialog
    mind "Она явно рада моему ответу."
    r "Ммм... Ещё немного, и я совсем забудусь...Пора подавать главное блюдо~"

    "[r.name] разворачивается и встает на четвереньки..."
    scene bg r_masturbate8 with dissolve
    call hide_dialog
    mind "Теперь четко видно её шикарную фигуру, ах, эти идеально округлые бёдра..."  
    mind "Из одежды на ней лишь эти нежные розовые трусики..."
    r "Тебе интересно, что под ними?"
    p "Ты и так знаешь ответ."

    "Она поднимается чуть наклившись, подставляя круглую попку... И смотрит на меня через плечо."  
    scene bg r_masturbate9_1 with dissolve
    call hide_dialog
    mind "Как мне не сорваться в такой момент?"
    p "Ты ведь нарочно меня провоцируешь, да?"
    
    "[r.name] раздвигает свою попку..."
    scene bg r_masturbate9_2 with dissolve
    call hide_dialog
    mind "Господи, она делает это прямо передо мной."
    mind "Каждое её движение – это вызов, она наслаждается тем, как я реагирую."
    r "Ты же хотел рассмотреть всё получше, да?"
    p "Ты просто играешь со мной."

    "[r.name] наклоняется ещё сильнее, растягивая ягодицы, но трусики всё ещё скрывают самое сокровенное."
    scene bg r_masturbate10 with dissolve
    call hide_dialog
    mind "Чёрт, это выглядит так откровенно... и так возбуждающе."
    r "Немного терпения... Наслаждайся этим моментом."
    p "Как будто у меня есть выбор."

    scene bg r_masturbate11 with dissolve
    call hide_dialog
    mind "Теперь её попка полностью открыта передо мной... а её взгляд — игривый и дерзкий."
    r "Ну же... признайся, ты в восторге?"
    p "Я бы солгал, если бы сказал, что нет."

    scene bg r_masturbate11_2 with dissolve
    call hide_dialog
    mind "[r.name] слегка приспускает трусики... на короткий миг я увидел её анус."
    r "Ой, ты это видел? Какой ты везучий~"
    p "Ты издеваешься?"

    mind "Трусики сползают ещё ниже, и теперь передо мной раскрывается куда более соблазнительный вид."
    scene bg r_masturbate11_3 with dissolve
    call hide_dialog
    mind "Чёрт, у меня перехватывает дыхание."
    r "Теперь тебе видно гораздо больше... Каково это?"
    p "...Невероятно."

    mind "[r.name] медленно тянет ткань вниз, теперь трусики едва держатся на её бёдрах."
    scene bg r_masturbate12 with dissolve
    call hide_dialog
    mind "Это последние мгновения перед тем, как я увижу её полностью обнажённой."
    r "Думаешь, стоит их снять? Или ещё немного подождать?"
    p "Ты прекрасно знаешь, чего я хочу."

    "[r.name] одной рукой оттягивает свою левую ягодицу, открывая мне полный вид."
    scene bg r_masturbate13 with dissolve
    call hide_dialog
    mind "Это уже не просто игра, она даёт мне всё, что у неё есть."
    r "Теперь ты точно увидел всё. Доволен?"
    p "...Я в шоке."

    "Её пальцы скользят по влажной коже, легко касаясь её самого сокровенного места."
    scene bg r_masturbate14 with dissolve
    call hide_dialog
    mind "Я буквально слышу её дыхание, прерывистое и горячее."
    r "Ммм... Знаешь, мне уже не остановиться..."
    p "Ты выглядишь так, будто уже на грани."

    "[r.name] всё глубже погружается в наслаждение, двигаясь всё быстрее."
    scene bg r_masturbate15 with dissolve
    call hide_dialog
    mind "Я не могу оторвать глаз... Это самое откровенное зрелище в моей жизни."
    r "Ааах... Да, смотри... Мне нравится, когда ты смотришь..."
    p "Ты с ума меня сведёшь."

    scene bg r_masturbate16_17 with dissolve
    call hide_dialog
    mind "Её тело содрогается, её лицо полностью отражает экстаз..."
    mind "Чёрт, это так неприлично и так чертовски возбуждающе."
    r "Ааах...! Я чувствую, как всё течёт... Это так хорошо..."
    
    scene bg r_masturbate18 with dissolve
    call hide_dialog
    mind "[r.name] убирает руку, давая мне полюбоваться зрелищем... Её соки стекают по бёдрам."  
    mind "Это чертовски возбуждающе. Она наслаждается каждым мгновением, зная, что я не могу отвести взгляд."  
    r "Смотри... Я ведь такая мокрая..."  
    p "Ты слишком хороша, чтобы не смотреть."  

    if my_rapunzel_love < 70:
        r "Ладно, милыый [hero_name], на сегодня с тебя достаточно~~"
        scene bg brothel_private with dissolve
        show r smile_naked with dissolve
        $customNotify("Недостаточно симпатии [r.name]")
        "Она остановилась на самом интересном, может если она будет мне больше доверять, то я получу еще больше?"
        return

    "Её пальцы тянутся к её анусу... Она собирается..."  
    scene bg r_masturbate19 with dissolve  
    call hide_dialog
    mind "Чёрт, она действительно делает это!"  
    r "Ммм... Это так приятно... Ты ведь не против, если я продолжу?"  

    "Теперь она достаёт игрушку... Неужели она собирается?"
    scene bg r_toy_anal1 with dissolve  
    call hide_dialog
    mind "Я не думал, что увижу нечто подобное... но, чёрт возьми, я рад, что это происходит."  
    r "Ааах... Да... Это даже лучше, чем я ожидала..."  
    p "Ты сводишь меня с ума, [r.name]."   

    "Игрушка медленно погружается еще глубже в её анус, её дыхание становится всё прерывистее." 
    scene bg r_toy_anal2 with dissolve 
    call hide_dialog 
    mind "Она будто на другой планете, полностью погрузившись в наслаждение."  
    r "Ммм... Да... Ещё глубже..."  
    p "Я теряю голову..."  

    if my_rapunzel_love < 90:
        $customNotify("Недостаточно симпатии [r.name]")
        r "Ладно, милыый [hero_name], на сегодня с тебя достаточно~~"
        scene bg brothel_private with dissolve
        show r smile_naked with dissolve
        "Она остановилась на самом интересном, может если она будет мне больше доверять, то я получу еще больше?"
        return

    "[r.name] подзывает тебя к себе, чтобы ты заменил ее игрушку своим членом" 
    scene bg r_dick_anal1 with vpunch 
    call hide_dialog
    r "О даа... Никакая игрушка с этим не сравнится"  
    "Узкий анус [r.name] жадно поглощает твой член" 
    "[r.name] улыбается"

    
    scene bg r_dick_anal2 with dissolve
    pause .2
    scene bg r_dick_anal3 with dissolve
    pause .2
    scene bg r_dick_anal4 with dissolve
    pause .2
    scene bg r_dick_anal3 with dissolve
    pause .2
    scene bg r_dick_anal2 with dissolve
    pause .2
    scene bg r_dick_anal3 with dissolve
    pause .2
    scene bg r_dick_anal4 with dissolve
    pause .1
    scene bg r_dick_anal3 with dissolve
    pause .1
    scene bg r_dick_anal4 with dissolve
    pause .03
    scene bg r_dick_anal3 with dissolve
    pause .03
    scene bg r_dick_anal4 with dissolve
    pause .03
    scene bg r_dick_anal3 with dissolve
    pause .03
    scene bg r_dick_anal4 with dissolve
    pause .03
    scene bg r_dick_anal3 with dissolve
    pause .03
    scene bg r_dick_anal4 with dissolve
    pause .03
    scene bg r_dick_anal3 with dissolve
    pause .03
    scene bg r_dick_anal4 with dissolve
    pause .03
    scene bg r_dick_anal3 with dissolve
    pause .03
    scene bg r_dick_anal4 with dissolve
    pause .03
    scene bg r_dick_anal3 with dissolve
    pause .03
    scene bg r_dick_anal4 with dissolve
    pause .03
    scene bg r_dick_anal3 with dissolve
    pause .03
    scene bg r_dick_anal4 with dissolve
    call hide_dialog

    scene bg r_dick_anal4 with dissolve
    "Глаза [r.name] начинают слезиться, а соки струятся по ее упругим бедрам"
    call hide_dialog
    r "Долбли, добли меня еще сильнее!"

    "Ты почти полностью вставил свой член в ее анус"
    "Тушь течет по лицу [r.name], она больше не может себя контролировать"
    scene bg r_dick_anal5 with dissolve
    call hide_dialog
    r "Еби меня, [hero_name], еще жесче!"
    
    mind "Как я могу ослушаться?"
    scene bg r_dick_anal6 with flash
    call hide_dialog
    "Ты целиком вгоняешь свой член в ее анус"
    r "Аааааааах!!!"
    r "Да! Да! Да! Да! Да!"

    scene bg r_dick_anal7 with flash
    call hide_dialog
    "Ты продолжаешь жестко ебать [r.name], кажется она начала терять сознание"
    
    scene bg r_dick_anal8 with flash
    call hide_dialog
    "[r.name] падает, без сознания, слезы всё еще текут по ее лицу, а задница всё еще приподнята"
    
    "Ты не можешь резко остановиться кончать, поэтому начинаешь кончать на ее прекрасное обнаженное тело"
    p "Аргх.."
    scene bg r_dick_anal9 with flash
    call hide_dialog
    "Сперма попала на тело [r.name] и стекает на простыни"
    
    scene bg r_dick_anal10 with flash
    call hide_dialog
    "Ты кончаешь еще больше, теперь все тело, задница и даже лицо [r.name] облиты твой спермой"
    "На лице [r.name] по прежнему красуется довольная улыбка"

    p "Доброй ночи, [r.name]."
    "Ты желаешь ей доброй ночи и уходишь"

    return


label r_root_blowjob:
    "[r.name] полностью разделась и посадила меня на кровать"
    show r smile_naked with fade
    r "[hero_name], Чего ты ждешь? Можешь тоже снимаешь штаны?"
    "Она встает на четвереньки и приближается к твоим ногам, само зрелище тебя уже неплохо завело"
    hide r with fade
    scene bg r_pre_1 with dissolve
    call hide_dialog
    "[r.name] снимает с тебя штаны и перед ее лицом оказывается твой огромный член"
    scene bg r_holding_look_dick_surprised2 with dissolve
    call hide_dialog
    r "О боже, вблизи он еще больше!"
    r "И что мне делать с этим?!"
    "[r.name] все ще изумленная твоим размером примеряет свой ротик к твоему члену"
    scene bg r_look_dick_surprised1 with dissolve
    call hide_dialog
    mind "Это будет не просто, но я верю в [r.name]"
    p "Не переживай, ты справишься."

    scene bg r_close_to_dick with dissolve
    "[r.name] собирается с мыслями, ей нужен был лишь малый толчок, она начинает поглаживать твой член смотря тебе в глаза"
    call hide_dialog
    p "Ухх, умничка."

    scene bg r_lick_look_viewer with dissolve
    call hide_dialog
    "Она открывает свой ротик и тянется языком к твоему члену"

    scene bg r_lick2_look_viewer with dissolve
    call hide_dialog
    "[r.name] облизывает головку твоего члена, проверяя твою реакцию"
    r "[hero_name], тебе нравится?"
    p "Уф, это очень приятно, продолжай."

    scene bg r_suck_1 with dissolve
    call hide_dialog
    "Наконец она берет головку члена в свой теплый ротик"
    p "Мммм.."
    "Она водит языком по уздечке и улыбается, видя твою реакцию"
    "Ты наслаждаешься происходящим"
    
    scene bg r_suck_2_ahegao with dissolve
    call hide_dialog
    "[r.name] старается сразу взять как можно больше твоего члена в рот, ее глаза закатывается"
    mind "Кажется у нее не очень много опыта, видимо это для нее перебор"

    scene bg r_suck_3_look_dick with dissolve
    call hide_dialog
    "[r.name] сосредоточенно двигается по головке у нее во рту с каждым движением все сильнее водя языком"
    p "А-ах, да, даа.."

    scene bg r_suck_4_ahegao with dissolve
    call hide_dialog
    "Это слишком большой размер для [r.name], она еле справляется с головкой"
    "Но ее упорство и характер не позволят ей сдаться"

    scene bg r_suck_5_neutral with dissolve
    call hide_dialog
    "[r.name] с силой пропускает кончик головки в свое горло"
    r "Мммффф"

    scene bg r_suck_6 with dissolve
    call hide_dialog
    "Щеки [r.name] наливаются румянцем, кажется ей становится тяжело дышать в таком положении"
    
    scene bg r_suck_7 with dissolve
    call hide_dialog
    "Ее глаза начинают слезиться, но оно не выпускает твоего члена изо рта"
    
    scene bg r_suck_8 with dissolve
    call hide_dialog
    "[r.name] двигается губами вдоль головки твоего члена, постепенно привыкая к нехватке воздуха"
    "Тушь начинает стекать по ее розовым от румянца щекам, тебя это заводит еще сильнее, твой член твердеет"
    p "Уффф"
    r "Ммммфф!"

    scene bg r_suck_9 with dissolve
    call hide_dialog
    "[r.name] понимает, что всё делает правильно и старается взять твой член еще глубже в горло, ведь она не заглотила даже половину твоего члена"
    
    scene bg r_suck_10 with dissolve
    call hide_dialog
    "Ее глаза начинают закрываться.."
    
    scene bg r_suck_11 with dissolve
    call hide_dialog
    "Не выпуская твоего члена, она переводит дыхание и продолжает упорно сосать"
    "Ты выпускаешь \"немного\" предспермы"
    "[r.name] состредоточенно старается всё проглотить"

    scene bg r_suck_12 with dissolve
    call hide_dialog
    "С каждым ее движением ты заводишься все сильнее"
    "Твой член начинает пульсировать всё сильнее, а движения [r.name] ускоряются"
    
    scene bg r_suck_13 with dissolve
    call hide_dialog
    mind "Я уже так близок?! Так быстро?"
    "Ты выпускаешь поток спермы в горло [r.name]"
    
    scene bg r_suck_14 with dissolve
    call hide_dialog
    p "Аааах, [r.name]."
    r "Ммм.. Ммффф.."
    "[r.name] справляется и проглатывает всё до капли"
    mind "Но это была лишь первая порция"
    
    scene bg r_suck_15 with dissolve
    call hide_dialog
    p "А-а-ааа!"
    r "Мммррррффффф!!!"

    scene bg r_suck_16 with dissolve
    call hide_dialog
    "[r.name] старается отстраниться от члена, но ты ей этого не позволишь, ты встаешь, хватаешь ее шелковистые волосы и притягиваешь почти на всю длину члена"
    
    scene bg r_suck_17 with dissolve
    call hide_dialog
    "[r.name] умоляющим взглядом просит тебя остановиться, но ты даже не думаешь об этом"
    
    if strength < 30:
        $customNotify("Недостаточно силы")
        "Ты не смог удержать ее голову"
        scene bg brothel_private with dissolve
        show r naked_cummed_annoyed with dissolve
        r "Урод!"
        $minusLove(my_rapunzel, -10)
        "[r.name] расстроенная уходит"
        return

    scene bg r_suck_18 with dissolve
    call hide_dialog
    "Сперма сочится из ее ротика, стекая по горлу на ее красивую грудь"
    "[r.name] с силой сопротивляется"
    "Она закрыла глаза, сопротивляясь изо всех сил, но ты оказался сильнее"
    

    scene bg r_suck_19 with dissolve
    call hide_dialog
    "[r.name] вновь смотрит на тебя умоляющими глазами"
    mind "Наверняка она так просит меня не останавливаться и долбить ее жесче(ахаха)"
    p "Получай, сука!"

    "..."
    "..."
    "..."
    scene bg r_suck_20 with dissolve
    call hide_dialog
    "Выпустив всё до конца ты ослабеваешь хватку и [r.name] постепенно отстраняется от твоего члена"
    
    scene bg r_suck_21 with dissolve
    call hide_dialog
    "Всё лицо [r.name] испачкано спермой, слезами и тушью"
    "Она жадно старается сосать даже сейчас, самостоятельно двигаясь по члену"
    
    scene bg r_suck_22 with dissolve
    call hide_dialog
    "Ее груди уже полностью покрыты твоей спермой"
    
    scene bg r_suck_23 with dissolve
    call hide_dialog
    "[r.name] вопросительно смотрит на тебя, убеждаясь в том, что тебе понравилось"
    p "Да, ты отлично постаралась, [r.name]"

    scene bg r_suck_24 with dissolve
    call hide_dialog
    r "Мммффф"
    mind "Думаю это был вздох облегчения"
    
    scene bg r_suck_25 with dissolve
    call hide_dialog
    "Теперь у нее во рту головка члена, она обсасывает ее, не желая отпускать"
    r "Мммммффф, мммм"
    "[r.name] старается почистить ее язычком, доставляя тебе еще больше удовольствия"

    scene bg r_suck_26 with dissolve
    call hide_dialog
    "Наконец она может расслабиться, она в последний раз проводит языком по головке твоего члена, а из ее рта вытекает немного спермы"
    
    scene bg r_suck_27 with dissolve
    call hide_dialog
    "Она держит твой член в руках и смотрит тебе в глаза, не понимая, что ей думать, злиться на тебя за такую жестокость?"
    
    scene bg r_suck_28 with dissolve
    call hide_dialog
    "[r.name] понимает, что это не важно, главное то, что она справилась на отлично"
    
    scene bg r_suck_29 with dissolve
    call hide_dialog
    "Она прикрывает глаза тянется к твоему члену губами, разве ей не достаточно того, что только чт опроизошло?"
    
    scene bg r_suck_30 with dissolve
    call hide_dialog
    "Это был поцелуй полный чувств к твоему члену"
    
    scene bg r_suck_31 with dissolve
    call hide_dialog
    r "Не ты один наслаждался происходящим~~"
    
    p "Рад, что тебе понравилось, [r.name]."
    scene bg r_suck_28 with dissolve
    call hide_dialog
    "Вы еще какое то время смотрите друг на друга"
    "!!!!!"
    mao "Эй, [r.name], где ты там? Пора за работу!" with vpunch
    r "Ты слышал ее, мне пора, до встречи~"

    scene bg r_suck_31 with dissolve
    call hide_dialog
    "[r.name] на последок еще раз целует твой член и поднимается"
    scene bg brothel_private with dissolve
    show r smile_naked_cummed with dissolve
    r "После такого ты обязан навещать меня чаще~"
    p "Конечно!"

    return

label r_root_fuck:
    show r smile with dissolve
    r "Ой, [hero_name], я так хотела тебе кое-что показать~ *хихикает*"
    p "И что же ты придумала на этот раз?"
    
    scene bg r_fuck1 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[r.name] забирается к тебе на кровать."
    r "А ты разве сам не догадываешься, что это может быть?~"
    
    scene bg r_fuck2 at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[r.name] наклоняется еще сильнее, ее платье задрается, открывая тебе вид на ее попку."
    r "Нет никаких мыслей?"
    p "!"
    
    scene bg r_play_pussy at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[r.name] плюхается на кровать, раздвигает ножки и неуверенно трогает свою киску, глядя на тебя с любопытством."
    r "Я видела, как это делают... Смотри, я умею! *хихикает* Ой, а вдруг это слишком?"
    p "Ты сама начала, давай дальше."
    
    scene bg r_blowjob_start at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Она подползает к тебе, смотрит на твой член большими глазами и осторожно берёт его в рот, но тут же отдёргивается."
    r "Ой, он такой большой! Это что, туда надо? *сосёт чуть-чуть* Мне страшно, но... прикольно!"
    p "Не бойся, ты справишься."
    
    scene bg r_ass_tease at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "[r.name] встаёт, поворачивается попкой и медленно спускает трусики, подглядывая за тобой через плечо."
    r "Смотри, какая я смелая! Хочешь потрогать? Только... не сильно, хорошо? *хихикает*"
    
    scene bg r_vaginal_start at Transform(zoom=1.5) with vpunch
    call hide_dialog
    "Ты хватаешь её за бёдра и врываешься в её киску. [r.name] вскрикивает, её маленькое тело дрожит от испуга."
    r "Ой-ой! [hero_name], это что?! Оно такое... большое! Мне страшно! *хнычет* Но... делай ещё!"
    
    scene bg r_vaginal_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg r_vaginal_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg r_vaginal_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg r_vaginal_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_vaginal_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_vaginal_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_vaginal_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_vaginal_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg r_vaginal_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg r_vaginal_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg r_vaginal_3 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Она пищит и хнычет, но её глаза блестят от восторга, волосы колышутся в такт твоим движениям."
    r "Ой, это... как в моих фантазиях! Но... оно такое тёплое и страшное!"
    
    scene bg r_vaginal_climax at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты кончаешь внутрь неё, и [r.name] взвизгивает, её лицо краснеет от удивления и страха."
    r "Ай! Что это было?! Оно... течёт внутри! Ой, [hero_name], это так странно! *хихикает*"
    
    scene bg r_anal_start at Transform(zoom=1.5) with vpunch
    call hide_dialog
    "Ты переворачиваешь её и врываешься в её попку. [r.name] кричит, её ручки хватаются за волосы."
    r "Ой-ой-ой! Это куда?! [hero_name], оно туда не влезет! Я боюсь! *шмыгает носом*"
    
    scene bg r_anal_1 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg r_anal_2 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg r_anal_3 at Transform(zoom=1.5) with dissolve
    pause .2
    scene bg r_anal_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_anal_1 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_anal_2 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_anal_3 at Transform(zoom=1.5) with dissolve
    pause .1
    scene bg r_anal_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg r_anal_3 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg r_anal_2 at Transform(zoom=1.5) with dissolve
    pause .03
    scene bg r_anal_3 at Transform(zoom=1.5) with flash
    call hide_dialog
    "Она дрожит и хнычет, но её голос дрожит от смеси страха и наивного удовольствия."
    r "Ой... оно такое... тугое! Мне страшно, но... как интересно!"
    
    scene bg r_anal_climax at Transform(zoom=1.5) with flash
    call hide_dialog
    "Ты кончаешь в её попку, и [r.name] вскрикивает, её тело содрогается, она едва держится на ногах."
    
    scene bg r_after at Transform(zoom=1.5) with dissolve
    call hide_dialog
    "Ты вытаскиваешь член, и [r.name] падает на пол, её длинные волосы разметались вокруг, из неё вытекает сперма. Она тяжело дышит, глядя на тебя большими глазами."
    r "Ой... [hero_name]... Это было... как в сказке, но... я так испугалась! *хнычет* И мне понравилось..."
    p "Отдыхай, маленькая."
    
    call hide_dialog
    "Ты встаёшь и уходишь, оставляя [r.name] лежать без сил, с её наивной улыбкой и дрожащими руками."
    $nextTime()
    jump brothel

label r_root_anal:
    "IN PROGRESS"
    return

label r_root_fetish:
    "IN PROGRESS"
    return
