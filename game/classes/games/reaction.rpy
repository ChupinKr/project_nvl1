init python:
    score = 0
    win_score = 0
    last_reaction_win = False  # Переменная для запоминания результата

    def success():
        global score, last_reaction_win
        score += 1
        if score >= 3:
            last_reaction_win = True
            renpy.hide_screen("reactionGame")
            renpy.show_screen("finishGame")

default casting = False

## Анимация тряски текста.
transform vibrate:
    pos(0.5, 0.4) anchor(0.5, 0.5) rotate 0
    linear 0.1 rotate 5
    linear 0.1 rotate 0
    linear 0.1 rotate -5
    linear 0.1 rotate 0
    repeat

screen failGame:
    on "show" action Hide("reactionGame"), SetVariable("casting", False), SetVariable("last_reaction_win", False)
    text "Провал.." size 100 align(0.5, 0.5)
    dismiss action Hide("failGame"), Jump("end_magic_game")  # Автоматический выход

screen finishGame:
    on "show" action Hide("reactionGame"), SetVariable("casting", False)
    text "Успех!" size 100 align(0.5, 0.5)
    if score >= 3:
        timer 1.0 action Jump("end_magic_game")  # Задержка перед выходом

screen reactionGame:
    modal True
    default tick = 0
    default reversal = False
    key "mouseup_1" action If(tick >= 80, Function(success), Show("failGame"))
    key "K_SPACE" action If(tick >= 80, Function(success), Show("failGame"))

    if casting:
        if tick < 20:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + 3), SetScreenVariable("tick", tick - 3))
        elif tick < 40:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + 6), SetScreenVariable("tick", tick - 6))
        elif tick < 60:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + 16), SetScreenVariable("tick", tick - 16))
        else:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + 20), SetScreenVariable("tick", tick - 20))

        if tick >= 95:
            timer 0.1 action SetScreenVariable("reversal", True)
        elif tick < 5:
            timer 0.1 action SetScreenVariable("reversal", False)

        text "Твой счет: " + str(score) size 50 xoffset 10 yoffset 30
        text "Жми SPACE" at vibrate size 100
        text "На 80%!!" at vibrate size 80 yoffset 100

        bar:
            align(0.5, 0.6)
            value AnimatedValue(value=tick, range=100, delay=0.1, old_value=None)
            xysize(1000, 50)

## Логика мини-игры.
label magic_training(mana):
    $ score = 0  # Сбрасываем очки перед игрой
    $ win_score = 3
    $ casting = True
    e "Сконцентрируйся, представь перед собой сферу, очень горячую."
    e "Вообрази, с какой силой ее надо оттолкнуть, чтобы попасть в мишень, будь сосредоточен."
    e "Теперь, когда ты понимаешь, что нужной энергии как раз достаточно - стреляй."
    call screen reactionGame
    return

## Переход после завершения игры
label end_magic_game:
    hide screen failGame
    hide screen finishGame
    if score >= win_score:
        $ last_reaction_win = True
    return
