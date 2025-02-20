define mao_first_root = True
define mao_first_visit = True
define can_go_mao = True

label visit_mao:
    scene bg brothel_private2 with dissolve
    show mao neutral at right_bit with fade
    if mao_first_visit:
        mind "Вау, а комната [mao.name] очень даже просторная и выглядит довольно благородно."
        mind "Все же не просто так она тут главная"
        mao "Добро пожаловать, [hero_name], чувствуй себя как дома."
        $mao_first_visit = False
    else:
        mao smile "О, [hero_name], удалось найти девушку для нас?"
    jump visit_mao_menu
            
label visit_mao_menu:
    menu:
        "Оплата" if not mao_first_root:
            hide mao with fade
            pause .5
            show mao open_clothes_shy at right_bit with fade
            mao "Всякая работа должна быть оплачена~"
            jump mao_root_menu
        "Повысить оплату за девушку" if mao_love >= 50 and mao_first_root:
            p "Я хочу, чтобы ты платила мне больше за каждую приведенную девушку."
            mao @annoyed "Знаешь, [hero_name], у нас не так уж много посетителей, а для тебя посещение вовсе басплатно.."
            mao @smirk "Кажется я кое-что придумала, ты же видишь, в каком заведении мы находимся."
            hide mao with fade
            mao "И уже должен понимать, кем я прихожусь для девочек."
            show mao panties at right_bit with fade
            mao "Может я могу с тобой расплатиться не монетами, а как-то иначе?"
            menu:
                "Согласен!":
                    p "Это отличная идея! Я же верно тебя понимаю?"
                    mao no_panties "Да, [hero_name], ты верно меня понимаешь~"
                    "Господи, благочестивая [f.name], о таком я и мечтать не смел!"
                    $mao_first_root = False
                    jump brothen_mao_root_menu
                "Так не пойдет":
                    p "Не понимаю о чем ты, плати мне деньгами, хватит увиливать!"
                    mao annoyed "Ах так, отлично, можешь вообще никого не приводить, но и бесплатных танцев тебе не видать!"
                    $is_free_dance = False
                    $customNotify("Танцы в борделе теперь платные")
                    mao @annoyed "Отвратительный мужчинка! Убирайся, тебе больше здесь не рады!"
                    $can_go_mao = False
                    $customNotify("Ты больше никогда не увидишь [mao.name]")
                    "[mao.name] тебя пинками выгнала из своей комнаты"
                    jump brothel
        "Как искать девушку?" if not invited_girl:
            p "А как выбрать девушку? И как ее пригласить?"
            mao @smile_shy "Сначала ты должен добиться ее расположения."
            mao @smile_shy "Дальше продвинуться в отношениях, ведь далеко не каждая девушка согласится работать в борделе."
            mao @open_smile "А потом верить в свои силы и сговорчивость девушки."
            jump visit_mao_menu
        "Да, нашел" if invited_girl:
            p "Это [invited_girl.name], мы с ней довольно близки и она согласилась."
            mao @smile_closed "Неплохо, очень неплохо."
            mao @smile "Пригласишь ее сейчас к нам?"
            menu:
                "Да":
                    "Ты приводишь [invited_girl.name] в Бордель"
                    invited_girl @smile "Привет, меня зовут [invited_girl.name] и я готова работать у вас~"
                    $addChar(["char"], 10)
                    mao @open_smile "Прекрасная кандидатка!"
                    $addLove("mao", 10)
                    mao @smile "Хорошая работа, [hero_name], можешь идти, а мы пока обсудим детали."
                    mao @smile "Ах да, [hero_name], вот твоя оплата."
                    $addMoney(20)
                    jump brothel
                "Позже":
                    p "Чуть позже приведу."
                    mao @annoyed "Зачем с этим тянуть?"
                    jump visit_mao_menu
        "Уйти":
            jump brothel

label brothen_mao_root_menu:
    menu:
        "Мастурбация" if mao_love >= 50:
            call mao_root_masturbate
            jump brothel
        "Грудями" if mao_love >= 60:
            call mao_root_titfuck
            jump brothel
        "Минет" if mao_love >= 70:
            call mao_root_blowjob
            jump brothel
        "Секс" if mao_love >= 80:
            call mao_root_fuck
            jump brothel
        "Анал" if mao_love >= 90:
            call mao_root_anal
            jump brothel
        "Фетиш" if mao_love >= 200:
            call mao_root_fetish
            jump brothel
        "Вернуться":
            "Ты уходишь восстанавливать силы"
            r @smirk "До встречи~"
            jump brothel