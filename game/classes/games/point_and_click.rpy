init python:
        import random

        class Bug:
            def __init__(self, id):
                self.id = id
                self.x = random.randint(100, 1600)
                self.y = random.randint(100, 900)
                self.targetX = self.x
                self.targetY = self.y
                self.alive = True  # Флаг, жив ли жук

            def move(self):
                """Обновляет цель движения жука"""
                if self.alive:
                    self.targetX = self.x + random.randint(-200, 200)
                    self.targetY = self.y + random.randint(-200, 200)

                    # Ограничиваем границы движения
                    self.targetX = max(100, min(1600, self.targetX))
                    self.targetY = max(100, min(900, self.targetY))


label bug_hunt: 
    $ score = 0
    $ bug_hunt_winscore = 20
    $ bugs = []  # Список жуков
    $ bug_path = "images/assets/point_and_click/bug.png"
    $ bug_hover_path = "images/assets/point_and_click/bug_hover.png"

    $bugs = [Bug(i) for i in range(20)]

    screen bug_game():
        text "Счет: [score]" xpos 20 ypos 20 size 40 color "#fff"

        for bug in bugs:
            if bug.alive:
                imagebutton:
                    idle bug_path
                    hover bug_hover_path
                    xpos bug.x
                    ypos bug.y
                    action [
                        SetVariable("score", score + 1),
                        Function(setattr, bug, "alive", False)  # Убираем жука
                    ]
                    at move_bug(bug)  # Применяем анимацию движения

    # Анимация хаотичного движения (не сбрасывает позицию)
    transform move_bug(bug):
        ease 1 xpos bug.targetX ypos bug.targetY
        pause 0.1  # Короткая пауза перед следующим движением
        repeat  # Повторяем движение

    window hide
    
    if persistent.lang == "russian":
        if is_cheats:
            menu:
                "У вас включены читы. Пропустить мини-игру?"
                "Играть":
                    pause .01
                "Пропустить":
                    "Успех!"
                    return
    if persistent.lang == "english":
        if is_cheats:
            menu:
                "Cheats are enabled. Skip the mini-game?"
                "Play":
                    pause .01
                "Skip":
                    "Success!"
                    return

    show screen bug_game

    while score < bug_hunt_winscore:
        python:
            for bug in bugs:
                bug.move()  # Обновляем координаты
        $ renpy.pause(0.5)  # Ждем, пока жуки двигаются

    hide screen bug_game
    "Успех!"
    return
