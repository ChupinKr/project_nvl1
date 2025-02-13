init python:
    import random
    import datetime

# Определение области попадания
define reaction_area_x = 400
define reaction_area_y = 300
define reaction_area_radius = 200

label start_reaction:

    # Визуальный элемент с белой линией
    image reaction_line = "reaction_line.png"

    # Переменная для хранения флага реакции игрока
    $ reaction_success = False

    # Метка для сцены проверки реакции
    label reaction_check:

        # Отображение изображения линии
        scene bg reaction_line

        # Ожидание реакции игрока
        pause 2.0

        # Проверка попадания в область реакции
        $ mouse_x, mouse_y = renpy.mouse.x, renpy.mouse.y
        $ distance = ((mouse_x - reaction_area_x) ** 2 + (mouse_y - reaction_area_y) ** 2) ** 0.5

        if distance <= reaction_area_radius:
            $ reaction_success = True

    if reaction_success:
        "Вы попали в белую линию! Вы выиграли!"
    else:
        "Вы не попали в белую линию! Вы проиграли!"