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
default key_value = 80
default deviation1 = 0
default deviation2 = 0
default deviation3 = 0
default deviation4 = 0
default magic_training_difficult = 15#чем больше, тем проще

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
    key "mouseup_1" action If(tick <= key_value + magic_training_difficult and tick >= key_value - magic_training_difficult, Function(success), Show("failGame"))
    key "K_SPACE" action If(tick <= key_value + magic_training_difficult and tick >= key_value - magic_training_difficult, Function(success), Show("failGame"))

    if casting:
        if tick < 20:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + deviation1), SetScreenVariable("tick", tick - deviation1))
        elif tick < 40:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + deviation2), SetScreenVariable("tick", tick - deviation2))
        elif tick < 60:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + deviation3), SetScreenVariable("tick", tick - deviation3))
        else:
            timer 0.1 repeat True action If(not reversal, SetScreenVariable("tick", tick + deviation4), SetScreenVariable("tick", tick - deviation4))

        if tick >= 88:
            timer 0.1 action SetScreenVariable("reversal", True)
        elif tick < 12:
            timer 0.1 action SetScreenVariable("reversal", False)

        text "Твой счет: " + str(score) size 50 xoffset 10 yoffset 30
        text "Целься в [key_value]%!!" at vibrate size 80 yoffset 100
        #text "tick [tick]" size 80 yoffset 100

        bar:
            align(0.5, 0.6)
            value AnimatedValue(value=tick, range=100, delay=0.1, old_value=None)
            xysize(1000, 50)

## Логика мини-игры.
label start_magic_training(intelligence):
    $ key_value = renpy.random.randint(0, 100)
    $ deviation1 = renpy.random.randint(1, 10)
    $ deviation2 = renpy.random.randint(2, 10)
    $ deviation3 = renpy.random.randint(3, 10)
    $ deviation4 = renpy.random.randint(4, 10)
    $ score = 0  # Сбрасываем очки перед игрой
    $ win_score = 3

    pause .5
    if is_cheats:
        menu:
            "У вас включены читы. Пропустить мини-игру?"
            "Играть":
                pause .01
            "Пропустить":
                $score = win_score
                call end_magic_game
                "Успех!"
                return

    show expression Text("Будь внимателен!") at truecenter as txt
    with dissolve
    pause
    hide txt
    $ casting = True
    call screen reactionGame
    return

## Переход после завершения игры
label end_magic_game:
    hide screen failGame
    hide screen finishGame
    if score >= win_score:
        $ last_reaction_win = True
    return
