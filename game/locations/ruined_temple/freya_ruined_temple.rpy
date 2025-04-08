define is_show_stat = False

label talk_to_freya:
    call haven_scene
    pause 1.0
    $ outfit_chance = renpy.random.randint(1,100)
    if outfit_chance > 90 and my_freya_love >= 50:
        show f smile_shy_naked_hold with dissolve
        f "Дорогой, ты так неожиданно зашел, я как раз переодевалась, чем я могу помочь тебе?"
    elif outfit_chance > 70 and my_freya_love >= 40:
        show f smile_shy_hold_swimsuit with dissolve
        f "[hero_name], тебя не учили стучаться? Хотя ничего страшного, это всего-лишь плавательный костюм."
        f "Кстати как тебе?"
        menu:
            "Тебе идет":
                p "Тебе очень идет!"
                $addLove(my_freya, 5)
            "Прикройся":
                p "Что за стыд, могла бы прикрыться"
                f "Ах так?"
                if my_freya_love >= 70:
                    f "Может быть так тебе больше понравится?"
                    show f smile_shy_naked_hold with dissolve
                    menu:
                        "Так лучше":
                            p "Так определенно лучше!"
                            $addLove(my_freya, 10)
                            f "Так и знала~"
                        "Нет":
                            p "Господи, ты меня не слышала?!"
                            f "Хам!"
                            $minusLove(my_freya,-10)
                            show f little_sad with dissolve
                else:
                    "Больше такого не увидишь!"
                    $minusLove(my_freya,-10)
                    show f little_sad with dissolve
    elif outfit_chance > 60 and my_freya_love >= 30:
        show f smile_shy_hold with dissolve      
    else:
        show f smile with dissolve
        f "Ты выглядишь растерянным, милый~"  
        f "Но не волнуйся, у тебя есть выбор. Я не могу подсказывать слишком явно… но могу дать намёк."
    
    jump talk_to_freya_menu

label talk_to_freya_menu:
    menu:
        "Помоги мне" if not is_show_stat:
            f "Дорогой, я понимаю, всё это очень сложно, но я верю в тебя!"
            f "Я не могу вмешиваться в дела смертных, пойми."
            f "Хотя кажется я знаю, что тебе может помочь.."
            show screen stat
            $ is_show_stat = True
            f "Я вручаю тебе магические письмена, в них будет написана вся важная для тебя информация."
            f "А также всё, что с тобой происходит.."
            f "Но не переживай, я не буду в них заглядывать."
            "Кнопка для просмотра текущей информации отображаются в правом верхнем углу"
            jump talk_to_freya_menu
        "Помоги мне" if my_freya_love >= 50:
            p "Я так устал, помоги мне расстабиться, ты же богиня."
            f "Дорогой, я вижу ты отлично потрудился."
            jump freya_root_menu
        "Спросить про город":
            f "Город — это место, где ты найдёшь защиту и, возможно, союзников."  
            f "Но не думай, что там всё будет легко. Иногда за безопасность приходится платить…"
            jump talk_to_freya_menu
        "Спросить про лес чудовищ":
            f "Этот лес опасен. Без подготовки ты долго не проживёшь. Но… там можно найти редкие ресурсы и секреты."
            jump talk_to_freya_menu
        "Спросить про девушек, которых встретил":
            f "О, любопытный~? Каждая из них может стать твоим проводником в этом мире… или чем-то большим~"  
            f "Но не забывай: твои поступки влияют на то, как они тебя воспринимают."
            jump talk_to_freya_menu
        "Закончить разговор":
            f "Ты всегда можешь обратиться ко мне, но твоя судьба зависит от тебя."
            f "До встречи!"
            jump ruined_temple

label freya_root_menu:
    menu:
        "Мастурбация" if my_freya_love >= 50:
            call freya_root_masturbate
            jump freya_root_menu
        "Грудями" if my_freya_love >= 60:
            call freya_root_titfuck
            jump freya_root_menu
        "Минет" if my_freya_love >= 70:
            call freya_root_blowjob
            jump freya_root_menu
        "Секс" if my_freya_love >= 80:
            call freya_root_fuck
            jump freya_root_menu
        "Анал" if my_freya_love >= 90:
            call freya_root_anal
            jump freya_root_menu
        "Фетиш" if my_freya_love >= 200:
            call freya_root_fetish
            jump freya_root_menu
        "Вернуться":
            jump talk_to_freya_menu

label freya_root_masturbate(is_preview=False):
    $setSceneUnlockedFlag('seen_freya_root_masturbate')
    hide f
    "Вы каким-то образом появляетесь у тебя в комнате"
    scene bg room at bg_size with dissolve
    "[f.name] не теряя времени опускается на колени, а одежда на вас пропадает"
    "Вот она магия Богини? Поражает воображение.."

    scene frey_masturbate_1 at bg_size with dissolve
    call hide_dialog
    f "О, дорогой [hero_name], как ты с таким вообще можешь ходить?"
    "[f.name] разглядывает твой член как младенец, которому подарили любимую игрушку"
    f "М-можно я его поглажу?"
    p "Богине можно всё и даже больше."
    f "Спасибо~"

    scene frey_masturbate_2 at bg_size with dissolve
    call hide_dialog
    f "Я не могу его даже обхватить, как ты мог прятать от меня такое сокровище?"
    "[f.name] не может скрыть улыбку, она наслаждается происходящим"
    "Движения продолжаются с усиленным темпом"
    p "Господи, то есть, моя Богиня..Пожалуйста..Н-не останавливайся."
    "Пульсации члена усилились"

    scene frey_masturbate_2_1 at bg_size with dissolve
    call hide_dialog
    "Ты уже готов выплеснуть весь свой стресс, полученный в новом мире"
    "[f.name], кажется, уже готова принять всё до последней капли"
    "Ты видишь ее вожделение в глазах, она жаждет этого как можно скорее"
    "Это было последней каплей, всё произошло быстрее, чем ты думал"
    "Самое время покрыть спермой прекрасную Богиню"

    scene frey_masturbate_3_1 at bg_size with dissolve
    call hide_dialog
    "Твое семя начинает выходить из члена, сильная струя, которая вот вот покроет всё ее тело"
    "[f.name] не ожидала, но ждала этого с нетерпением"
    "Румянец вновь проступил на её лице"
    
    scene frey_masturbate_3_1_blush at bg_size with flash
    call hide_dialog
    f "Ох, [hero_name], о таком надо предупреждать~"

    scene frey_masturbate_3_2 at bg_size with flash
    call hide_dialog
    "[f.name] старается поймать всё до последней капли"

    scene frey_masturbate_3_3 at bg_size with dissolve
    call hide_dialog
    "Ротик богини открылся, она не упустит такое лакомство"
    "[f.name] старается получить всё угощение"
    "Но неминуемо сперма попадает на ее лицо и челку"
    
    scene frey_masturbate_3_4 at bg_size with dissolve
    call hide_dialog
    "Лицо богини уже частично покрыто спермой, но ты не собираешься останавливаться"
    p "Ах, [f.name], не закрывай ротик."
    "Твой член пульсирует, ты выпускаешь еще порцию"
    f "Аааааам"

    scene frey_masturbate_3_5 at bg_size with flash
    call hide_dialog
    f "Ммм, еще?"
    "Ты и не собирался останавливаться, и дальше поливаешь личико богини спермой"
    "Из твоего члена выходит еще больше густой спермы, покрывая всё тело богини"
    "Она вздрагивает от каждой пульсации твоего члена"
    f "Ах, больше, больше!"
    p "А-ах, как прикажешь, [f.name]."
    "Ты извергаешь еще одну огромную порцию спермы прямо на ее лицо"
    "Сперма течет по ее сочным розовым губам прямо на огромные груди и капает на пол"
    f "А-ах"
    "[f.name] наслаждается теплым мужским семенем, стекающим по ее телу"
    "Поток спермы наконец ослабевает"
    "Ты заканчиваешь обильное семяизвержение"

    scene frey_masturbate_3_6 at bg_size with dissolve
    call hide_dialog
    "[f.name] облизывает губы, судя по ее выражению лица она очень довольна"
    f "Видишь, я вся теперь покрыта твоей спермой!"
    p "Я-я..."
    f "И мне очень понравилось~~"
    f "Заглядывай почаще и не забудь меня угостить~"
    "[f.name] поднимается, с ног до головы покрытая твоим семенем"
    
    call room_scene
    show f smile_shy_naked_hold_cummed with dissolve
    if is_preview:
        return
    call hide_dialog
    f "Пожалуй мне пора возвращаться, буду ждать нашей новой встречи~"
    hide f with dissolve
    "[f.name] исчезает, а ты садишься на кровать с облегчением и чувством выполненого долга"
    jump room


label freya_root_titfuck:
    "IN PROGRESS"
    jump freya_root_menu

label freya_root_blowjob:
    "IN PROGRESS"
    jump freya_root_menu

label freya_root_fuck:
    "IN PROGRESS"
    jump freya_root_menu

label freya_root_anal:
    "IN PROGRESS"
    jump freya_root_menu

label freya_root_fetish:
    "IN PROGRESS"
    jump freya_root_menu

