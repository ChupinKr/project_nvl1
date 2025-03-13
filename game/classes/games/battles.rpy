init python:
    import random, math
    health_to_not_escape = 20
    damage_to_enemy = 0
    damage = 0

    # Время на ввод комбинации (в секундах)
    qte_time = 3.0
    # Переменная для анимации бара: при запуске мы будем обнулять её,
    # AnimatedValue(qte_bar, 100, qte_time) анимирует изменение от текущего значения до 100.
    qte_bar = 100
    # Флаг для предупреждения (смена цвета бара)
    qte_warning = False

    def qte_go(warning=False):
        global qte_bar, qte_warning
        if warning:
            qte_warning = True
        else:
            # Обнуляем значение, чтобы AnimatedValue анимировало изменение от 0 до 100 за qte_time секунд
            qte_bar = 0
        renpy.restart_interaction()
        
    QTEGo = renpy.curry(qte_go)

    def generate_qte_sequence():
        #"""Создаёт случайную комбинацию стрелок для ввода."""
        # Пример расчёта количества символов (можно подстроить под свою логику)
        count = math.ceil(enemy_strength / 10) - math.ceil(strength / 20)
        if count < 6:
            count = 6
        if count > 26:
            count = 26
        return "".join(random.choices(["↑", "↓", "←", "→"], k=count))

    def add_qte_input(key):
        #"""Добавляет нажатую клавишу в строку ввода игрока."""
        global qte_input
        if len(qte_input) < len(qte_sequence):
            qte_input += key
            if len(qte_input) == len(qte_sequence):
                renpy.jump("check_qte")

screen battle_hp_bars():
    # Отображение здоровья игрока в левом верхнем углу
    hbox:
        align (0.0, 0.0)
        text "[hero_name]: [health]" size 40 color "#FFFFFF"
    
    # Отображение здоровья противника в правом верхнем углу
    hbox:
        align (1.0, 0.0)
        text "[enemy_name]: [enemy_health]" size 40 color "#FFFFFF"

screen battle_qte():
    modal True

    # Таймеры для отсчёта:
    # 1. Немедленный запуск анимации (сбрасываем значение бара до 0)
    timer 0.01 action QTEGo()
    # 2. По истечении 2/3 времени включаем предупреждение (смена цвета)
    timer qte_time * 0.6666 action QTEGo(True)
    # 3. По истечении полного времени переходим к проверке ввода комбинации
    timer qte_time action Jump("check_qte")

    # Таймер-бар, отображающий оставшееся время, располагается в нижней части экрана
    bar:
        align (0.5, 0.9)
        xysize (300, 30)
        # Анимированное значение от qte_bar до 100 за qte_time секунд
        value AnimatedValue(qte_bar, 100, qte_time)
        # Если включено предупреждение – меняем цвет заполненной части
        if qte_warning:
            left_bar Solid("#e02")
    
    # Центральный блок – последовательность символов и ввод игрока
    vbox:
        align (0.5, 0.5)
        
        # Последовательность символов (комбинация противника)
        hbox spacing 10:
            for symbol in qte_sequence:
                frame:
                    xysize (50, 50)
                    background "#4682B4"
                    text symbol size 40 color "#FFFFFF"
        
        text "" size 30  # Пустой текст для отступа
        
        # Отображение ввода игрока
        hbox spacing 10:
            for i in range(len(qte_sequence)):
                if i < len(qte_input):
                    frame:
                        xysize (50, 50)
                        background "#FFFFFF"
                        text qte_input[i] size 40 color "#4682B4"
                else:
                    frame:
                        xysize (50, 50)
                        background "#FFFFFF"
                        text "" size 40 color "#4682B4"

    # Обработка нажатий клавиш для ввода комбинации
    key "K_UP" action Function(add_qte_input, "↑")
    key "K_DOWN" action Function(add_qte_input, "↓")
    key "K_LEFT" action Function(add_qte_input, "←")
    key "K_RIGHT" action Function(add_qte_input, "→")



label start_battle(enemy_hp, enemy_str, name, loc):
    $ damage_to_enemy = 0
    $ damage = 0
    $ enemy_health = enemy_hp  # Устанавливаем здоровье противника
    $ enemy_strength = enemy_str  # Устанавливаем здоровье противника
    $ battle_location = loc
    $ enemy_name = name
    $ qte_time = 3.0 + (0.03 * strength)
    $ qte_bar = 100
    $ enemy_strength += 5 # с течением боя противник становится сильнее(чтобы не затягивать бои)
    $ qte_sequence = generate_qte_sequence()  # Генерируем случайную последовательность
    $ qte_input = ""  # Обнуляем ввод игрока
    $ qte_warning = False
    pause .5
    
    if is_cheats:
        menu:
            "У вас включены читы. Пропустить мини-игру?"
            "Играть":
                pause .01
            "Пропустить":
                call battle_win
                return

    show expression Text("Сейчас начнется битва, приготовься!") at truecenter as txt
    with dissolve
    pause
    hide txt
    show screen battle_hp_bars
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
    $ damage_to_enemy = random.randint(math.ceil(strength / 2), math.ceil(strength * 1.5))  # Случайный урон
    $ damage_to_enemy = damage_to_enemy
    if damage_to_enemy < 10:
        $ damage_to_enemy = 10
    $ enemy_health -= damage_to_enemy   # Уменьшаем здоровье противника
    # Проверка на победу
    if enemy_health <= 0:
        hide screen battle_hp_bars
        jump battle_win
    else:
        # Генерируем новую последовательность и очищаем ввод игрока
        $ damage_to_enemy = 0
        $ damage = 0
        $ qte_sequence = generate_qte_sequence()
        $ qte_input = ""
        # Сброс таймера: возвращаем значение qte_bar в 100 и сбрасываем предупреждение
        $ qte_bar = 100
        $ qte_warning = False
        call screen battle_qte  # Продолжаем бой

label qte_fail:
    # Уменьшаем здоровье игрока на случайный урон
    $ damage = random.randint(math.ceil(enemy_strength / 2), math.ceil(enemy_strength * 1.5))  # Случайный урон для игрока (например, от 10 до 30)
    $ damage = damage - (strength * 2)
    if damage < 10:
        $ damage = 10
    $ health -= damage # Уменьшаем здоровье игрока

    # Проверка на поражение игрока
    if health <= 0:
        $ health = 0
        hide screen battle_hp_bars
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
            # Сброс таймера: возвращаем значение qte_bar в 100 и сбрасываем предупреждение
            $ qte_bar = 100
            $ qte_warning = False
            call screen battle_qte  # Продолжаем бой
        "Попытаться сбежать":
            jump battle_escape  # Бегство из боя

label battle_win:
    "Вы наносите противнику [damage_to_enemy], показатель здоровья противника [enemy_health]"
    "Противник побежден!"
    $ last_battle_win = True
    $ strength += 2 * strength_mod
    return

label battle_loss:
    "Противник нанес вам урон [damage], ваш показатель здоровья [health]"
    "Ты проиграл бой, возможно стоило улучшить свои навыки перед тем, как вступать в бой с серьезным противником"
    $ last_battle_win = False
    "Ты падаешь без сознания"
    $ nextDay()
    jump surgency_tsunade_cure
    return

label battle_escape:
    "Ты пытаешься сбежать из боя"
    $ last_battle_win = False
    if strength / 2 * random.randint(1, 10) > enemy_strength:
        "Тебе повезло, ты убежал и даже почти не чувствуешь боли"
        if health < health_to_not_escape:
            mind "О нет, адреналин прошел"
            "Ты не чувствуешь ничего кроме боли, от боли ты падаешь в обморок"
            $ nextDay()
            jump surgency_tsunade_cure
        else:
            "Тебе больно, но это терпимо, само пройдет"
            jump escape_battle
    else:
        "Противник такого уровня тебя не отпустит, ты пропустил удар"
        jump qte_fail

label escape_battle:
    hide screen battle_hp_bars
    "Ухх, было близко, хорошо, что успел убежать"
    if battle_location == "ruined_temple":
        jump ruined_temple
    elif battle_location == "magic_tower":
        jump magic_tower_alone
    elif battle_location == "training_ground":
        jump training_ground
    elif battle_location == "bar":
        jump bar
    elif battle_location == "tavern":
        jump tavern
    elif battle_location == "market":
        jump market
    elif battle_location == "forest":
        jump forest
    elif battle_location == "brothel":
        jump brothel
    else: 
        return