label eris_root_sausage(is_preview=False):
    $setSceneUnlockedFlag('seen_eris_root_sausage')
    scene bg eris_root_sousage0 at bg_size with fade
    call hide_dialog
    p "[my_eris.name] выглядит очень довольной."

    scene bg eris_root_sousage1_say at bg_size with dissolve
    eris "Спасибо, [hero_name]!"

    scene bg eris_root_sousage1 at bg_size with dissolve
    p "Пожалуйста, угощайся"

    scene bg eris_root_sousage2 at bg_size with dissolve
    "[my_eris.name] начала посасывать сосиску."

    scene bg eris_root_sousage3 at bg_size with dissolve
    pause .3
    scene bg eris_root_sousage3_2 at bg_size with dissolve
    pause .3
    scene bg eris_root_sousage3 at bg_size with dissolve
    pause .3
    scene bg eris_root_sousage3_2 at bg_size with dissolve
    pause .3
    scene bg eris_root_sousage3 at bg_size with dissolve
    pause .3
    scene bg eris_root_sousage3_2 at bg_size with dissolve
    eris "Мм?"

    scene bg eris_root_sousage4 at bg_size with dissolve
    eris "Фы фево?"
    p "Впервые вижу, чтобы кто-то так ел сосиску..."

    scene bg eris_root_sousage4_2 at bg_size with dissolve
    "Лицо [my_eris.name] наливается румянцем."

    scene bg eris_root_sousage5 at bg_size with dissolve
    pause .5
    scene bg eris_root_sousage6 at bg_size with dissolve
    "Она берет сосиску в зубы и откусывает."

    scene bg eris_root_sousage6_say at bg_size with dissolve
    eris "Может пойдем уже?"
    scene bg eris_root_sousage6 at bg_size with dissolve
    return


label eris_root_date_dance(is_preview=False):
    $setSceneUnlockedFlag('seen_eris_root_date_dance')
    scene bg eris_root_date_dance0 at bg_size with fade
    if not is_preview:
        call start_battle(10, 10, my_eris.name, 'city', False)
    scene bg eris_root_date_dance1 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance2 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance0 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance1 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance2 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance0 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance1 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance2 at bg_size with dissolve
    call hide_dialog
    eris "Ну же, поспевай!"
    if not is_preview:
        call start_battle(10, 10, my_eris.name, 'city', False)
    scene bg eris_root_date_dance3 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance4 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance4 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance3 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance4 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance4 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance3 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance4 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance3 at bg_size with dissolve
    call hide_dialog
    mind "Кажется она вообще не замечает, как сильно развевается её платье."
    eris "Давай же, танцуй со мной, [hero_name]."
    if not is_preview:
        call start_battle(10, 10, my_eris.name, 'city', False)
    scene bg eris_root_date_dance6 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance7 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance6 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance7 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance6 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance7 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance6 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance7 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance7 at bg_size with dissolve
    pause .3
    scene bg eris_root_date_dance5 at bg_size with dissolve
    call hide_dialog
    "[my_eris.name] какое-то время продолжала танцевать, не замечая тебя."
    
    scene bg eris_root_date_dance_fall at bg_size with vpunch
    "Внезапно [my_eris.name] споткнулась и упала."
    eris "..."
    "Ты подходишь и подаешь ей руку."

    scene bg eris_root_date_dance_fall2 at bg_size with dissolve
    eris "Спасибо, [hero_name]!"
    return

label eris_root_tea(is_preview=False):
    $setSceneUnlockedFlag('seen_eris_root_tea')
    if not is_preview:
        $eris_first_time_root = False
    scene bg eris_root_tea0 at bg_size with fade
    call hide_dialog
    eris "[hero_name], я принесла чай~"

    scene bg eris_root_tea1 at bg_size with dissolve
    call hide_dialog
    p "Оу, [my_eris.name], спасибо."
    "Не в силах удержать себя, ты тянешься к [my_eris.name], а она пытается дать тебе горячую чашку чая."

    scene bg eris_root_tea2 at bg_size with vpunch
    call hide_dialog
    eris "Ах, [hero_name]! Ты в порядке?"
    p "Ты пролила немного чая на меня."

    scene bg eris_root_tea3 at bg_size with fade
    call hide_dialog
    eris "А-аа, прости."

    scene bg eris_root_tea4 at bg_size with dissolve
    call hide_dialog
    mind "Никогда не видел [my_eris.name] такой смущенной."
    "[my_eris.name] снимает с тебя брюки, чтобы проверить, какие ожоги ты получил."

    scene bg eris_root_tea5 at bg_size with dissolve
    call hide_dialog
    "Она снимает с тебя штаны."
    p "Такие движения любого возбудят..."

    scene bg eris_root_tea5_2 at bg_size with dissolve
    call hide_dialog
    eris "Т-так ты в порядке?"
    p "Да, все хорошо, как видишь."

    scene bg eris_root_tea6 at bg_size with dissolve
    pause .4
    scene bg eris_root_tea6_2 at bg_size with dissolve
    call hide_dialog
    "[my_eris.name] садится у твоего члена и начинает нежно его ласкать."
    p "Как будто ты его впервые видишь..."
    eris "..."

    scene bg eris_root_tea7_1 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea7_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea7_3 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea7_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea7_3 at bg_size with dissolve
    call hide_dialog
    p "Арх!"

    scene bg eris_root_tea8 at bg_size with dissolve
    call hide_dialog
    eris "Ммм..."

    scene bg eris_root_tea9 at bg_size with vpunch
    call hide_dialog
    "Ты резким движением опрокидываешь [my_eris.name] на спину."

    scene bg eris_root_tea9 at bg_size with dissolve
    call hide_dialog
    eris "Т-только будеть нежен..."

    scene bg eris_root_tea10_1 at bg_size with vpunch
    call hide_dialog
    eris "Ах!"

    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .2
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_3 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_1 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_2 at bg_size with dissolve
    pause .1
    scene bg eris_root_tea10_3 at bg_size with flash
    eris "А-ааах!"

    scene bg eris_root_tea11 at bg_size with flash
    p "Аргх!"

    scene bg eris_root_tea12 at bg_size with flash
    pause .5
    scene bg eris_root_tea13 at bg_size with flash
    call hide_dialog

    scene bg eris_root_tea14 at bg_size with fade
    call hide_dialog
    eris "А-а-ах... Е-еще..."

    mind "Кажется [my_eris.name] не понимает, что происходит, мне стоит идти."
    p "Еще увидимся, [my_eris.name]."
    eris "А-ааах..."

    return