init python:
    import renpy.exports as renpy
    import random

    def update_energy():
        global energy, running, stable_zone

        while running:
            if renpy.get_mouse_pressed()[0]:  # Если зажата левая кнопка
                energy = min(energy + energy_gain, max_energy)
            else:
                energy = max(energy - energy_loss, min_energy)

            # Двигаем зону стабильности вверх или вниз случайным образом
            shift = random.choice([-1, 1]) * stable_shift_speed
            new_lower = max(10, min(80, stable_zone[0] + shift))
            new_upper = min(90, max(20, stable_zone[1] + shift))

            stable_zone = [new_lower, new_upper]

            renpy.restart_interaction()
            renpy.pause(0.1)
label magic_training_gmmm:
    scene bg room

    if persistent.lang == "russian":
        if is_cheats:
            menu:
                "У вас включены читы. Пропустить мини-игру?"
                "Играть":
                    pause .01
                "Пропустить":
                    "Ты успешно контролировал магию!"
                    return
    if persistent.lang == "english":
        if is_cheats:
            menu:
                "Cheats are enabled. Skip the mini-game?"
                "Play":
                    pause .01
                "Skip":
                    "You have successfully controlled magic!"
                    return

    $ energy = 0  # Начальный уровень энергии
    $ min_energy = 0
    $ max_energy = 100
    $ stable_zone = [40, 60]  # Начальная зона стабильности
    $ energy_loss = 0.5  # Насколько быстро падает энергия
    $ energy_gain = 1.5  # Насколько быстро растёт энергия при нажатии
    $ running = True
    $ stable_shift_speed = 0.3  # Скорость изменения зоны стабильности

    screen magic_game():
        frame:
            xalign 0.5
            yalign 0.5
            background "#444"
            xsize 20
            ysize 200

            bar:
                xalign 0.5
                yalign 1.0
                value energy
                range max_energy
                xsize 20
                ysize 200
                thumb "gui/bar/thumb.png"

        text "Энергия: [energy]%":
            xalign 0.5
            yalign 0.8

        text "Зона стабильности: [stable_zone[0]] - [stable_zone[1]]%" color "#00f":
            xalign 0.5
            yalign 0.9

        if energy < stable_zone[0]:
            text "Слишком слабо!" color "#f00" xalign 0.5 yalign 0.1
        elif energy > stable_zone[1]:
            text "Перегрузка!" color "#f00" xalign 0.5 yalign 0.1
        else:
            text "Стабильность!" color "#0f0" xalign 0.5 yalign 0.1

    python:
        renpy.start_predict("magic_game")
        renpy.invoke_in_thread(update_energy)

    show screen magic_game

    $ renpy.pause(10.0)  # Время тренировки

    $ running = False  # Остановка обновления энергии
    hide screen magic_game

    if stable_zone[0] <= energy <= stable_zone[1]:
        "Ты успешно контролировал магию!"
    else:
        "Магическая энергия вышла из-под контроля..."

    return
