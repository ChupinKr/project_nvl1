define damage_to_enemy = 0
define base_enemy_health = 100
define health_to_not_escape = 20

init python:
    import random
    import math

    def generate_qte_sequence():
        """Создаёт случайную комбинацию стрелок для ввода."""
        count = math.ceil(enemy_strength / 10 - strength / 10)
        if count < 4:
            count = 4
        return "".join(random.choices(["↑", "↓", "←", "→"], k=count))

    def add_qte_input(key):
        """Добавляет нажатую клавишу в строку ввода игрока."""
        global qte_input
        if len(qte_input) < len(qte_sequence):
            qte_input += key

screen battle_qte():
    modal True
    timer 3.0 action Jump("check_qte")  # Время на ввод комбинации

    # Отображение здоровья игрока в левом верхнем углу
    hbox:
        align (0.0, 0.0)  # Позиционируем в левом верхнем углу
        text "[hero_name]: [health]" size 40 color "#FFFFFF"  # Отображаем текущие очки здоровья игрока

    # Отображение здоровья противника в правом верхнем углу
    hbox:
        align (1.0, 0.0)  # Позиционируем в правом верхнем углу
        text "[enemy_name]: [enemy_health]" size 40 color "#FFFFFF"  # Отображаем здоровье противника

    # Центральный vbox, в котором будет основная последовательность символов и ввод игрока
    vbox:
        align (0.5, 0.5)

        # Текст с рамкой для последовательности (противник)
        hbox spacing 10:  # Добавляем расстояние между рамками
            for symbol in qte_sequence:
                frame:
                    xysize (50, 50)  # Размер рамки
                    background "#4682B4"  # Цвет рамки (цвет текста противника)
                    text symbol size 40 color "#FFFFFF"  # Цвет текста внутри рамки (белый)

        # Добавляем расстояние между контейнерами
        text "" size 30  # Пустой текст для создания промежутка

        # Текст с рамкой для ввода игрока
        hbox spacing 10:  # Добавляем расстояние между рамками
            for i in range(len(qte_sequence)):  # Делаем столько контейнеров, сколько символов в последовательности
                if i < len(qte_input):  # Если символ был введен, показываем его
                    frame:
                        xysize (50, 50)  # Размер рамки
                        background "#FFFFFF"  # Цвет рамки (белый)
                        text qte_input[i] size 40 color "#4682B4"  # Цвет текста внутри рамки (цвет противника)
                else:  # Если символ еще не был введен
                    frame:
                        xysize (50, 50)  # Размер рамки
                        background "#FFFFFF"  # Цвет рамки (белый)
                        text "" size 40 color "#4682B4"  # Пустой текст

    # Клавиши для ввода
    key "K_UP" action Function(add_qte_input, "↑")
    key "K_DOWN" action Function(add_qte_input, "↓")
    key "K_LEFT" action Function(add_qte_input, "←")
    key "K_RIGHT" action Function(add_qte_input, "→")

label start_battle:
    $ qte_sequence = generate_qte_sequence()  # Генерируем случайную последовательность
    $ qte_input = ""  # Обнуляем ввод игрока
    $ enemy_health = base_enemy_health  # Устанавливаем здоровье противника на 100
    call screen battle_qte
    return

label check_qte:
    $ qte_input = qte_input.strip()  # Убираем лишние пробелы, если они есть
    if qte_input == qte_sequence:  # Сравниваем без лишних пробелов
        jump qte_success
    else:
        jump qte_fail

label qte_success:
    # Уменьшаем здоровье противника случайным количеством
    $ damage_to_enemy = random.randint(strength, strength*2)  # Случайный урон от 10 до 100
    $ enemy_health -= damage_to_enemy  # Уменьшаем здоровье противника
    # Проверка на победу
    if enemy_health <= 0:
        jump battle_win
    else:
        # Генерируем новую последовательность и очищаем ввод игрока
        $ qte_sequence = generate_qte_sequence()
        $ qte_input = ""
        jump continue_battle

label qte_fail:
    # Уменьшаем здоровье игрока на случайный урон
    $ damage = random.randint(enemy_strength, enemy_strength*2)  # Случайный урон для игрока (например, от 10 до 30)
    $ health -= damage  # Уменьшаем здоровье игрока

    # Проверка на поражение игрока
    if health <= 0:
        $ health = 0
        jump battle_loss
    else:
        # Генерируем новую последовательность и очищаем ввод игрока
        $ qte_sequence = generate_qte_sequence()
        $ qte_input = ""
        jump continue_battle

label continue_battle:
    if damage_to_enemy > 0:
        "Вы наносите противнику [damage_to_enemy], показатель здоровья противника [enemy_health]"
    else:
        "Противник нанес вам урон [damage], ваш показатель здоровья [health]"
    $ damage_to_enemy = 0
    menu:
        "Продолжить бой":
            call screen battle_qte  # Продолжаем бой
        "Попытаться сбежать":
            jump battle_escape  # Бегство из боя

label battle_win:
    "Вы наносите противнику [damage_to_enemy], показатель здоровья противника [enemy_health]"
    "Противник побежден!"
    $ last_battle_win = True
    jump after_win_battle

label battle_loss:
    "Противник нанес вам урон [damage], ваш показатель здоровья [health]"
    "Ты проиграл бой, возможно стоило улучшить свои навыки перед тем, как вступать в бой с серьезным противником"
    $ last_battle_win = False
    $ death_count += 1
    jump surgency_tsunade_cure

label battle_escape:
    "Ты пытаешься сбежать из боя"
    $ last_battle_win = False
    if strength / 2 * random.randint(1, 10) > enemy_strength:
        "Тебе повезло, ты убежал и даже почти не чувствуешь боли"
        if health < health_to_not_escape:
            "О нет, адреналин прошел"
            "Ты не чувствуешь ничего кроме боли"
            jump surgency_tsunade_cure
        else:
            "Тебе больно, но это терпимо, может само пройдет"
            "(Не пройдет, иди к врачу)"
            jump escape_battle
    else:
        "Противник такого уровня тебя не отпустит, ты пропустил удар"
        jump qte_fail

label after_win_battle:
    if battle_location == "ruined_temple":
        if enemy_name == es.name:
            jump battle_win_ruined_temple_nagatoro
        elif enemy_name == r.name:
            jump battle_win_ruined_temple_rapunzel
        elif enemy_name == e.name:
            jump battle_win_ruined_temple_elsa
    elif battle_location == "magic_tower":
        if enemy_name == es.name:
            jump battle_win_magic_tower_nagatoro
        elif enemy_name == r.name:
            jump battle_win_magic_tower_rapunzel
        elif enemy_name == e.name:
            jump battle_win_magic_tower_elsa
    elif battle_location == "training_ground":
        jump battle_win_training_ground
    elif battle_location == "bar":
        jump battle_win_bar
    elif battle_location == "tavenr":
        jump battle_win_tavenr
    else: 
        "Залупа какая-то, не нашел куда тебя пристроить, пора умирать, напиши мне, этой баг по ходу"
        return

label escape_battle:
    if battle_location == "ruined_temple":
        jump ruined_temple
    elif battle_location == "magic_tower":
        jump magic_tower
    elif battle_location == "training_ground":
        jump training_ground
    elif battle_location == "bar":
        jump bar
    elif battle_location == "tavenr":
        jump tavenr
    else: 
        "Залупа какая-то, не нашел куда тебя пристроить, пора умирать, напиши мне, этой баг по ходу"
        return