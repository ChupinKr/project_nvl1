# Определяем изображения для грязной и чистой посуды

image fresh_dish = "images/assets/cleaner/fresh_dish.png"
image fresh_cup = "images/assets/cleaner/fresh_cup.png"
image fresh_book_blue = "images/assets/cleaner/fresh_book_blue.png"
image fresh_book_red = "images/assets/cleaner/fresh_book_red.png"

# Трансформации для посуды "dish"
transform trans_dish_show():
    "images/assets/cleaner/dirty_dish.png"
# Трансформации для посуды "cup"
transform trans_cup_show():
    "images/assets/cleaner/dirty_cup.png"
# Трансформации для посуды "book red"
transform trans_book_red_show():
    "images/assets/cleaner/dirty_book_red.png"
# Трансформации для посуды "book blue"
transform trans_book_blue_show():
    "images/assets/cleaner/dirty_book_blue.png"
 
transform pulse_zoom:
    zoom 1.0
    linear 0.4 zoom 1.05
    linear 0.4 zoom 1.0
    repeat
 
transform trans_normal_dish():
    trans_dish_show
    0.1
    repeat

transform trans_touch_dish():
    trans_dish_show
    function func_touch_dish
    0.1
    repeat
 
transform trans_normal_cup():
    trans_cup_show
    0.1
    repeat
 
transform trans_touch_cup():
    trans_cup_show
    function func_touch_dish
    0.1
    repeat

transform trans_normal_book_red():
    trans_book_red_show
    0.1
    repeat

transform trans_touch_book_red():
    trans_book_red_show
    function func_touch_dish
    0.1
    repeat
 
transform trans_normal_book_blue():
    trans_book_blue_show
    0.1
    repeat
 
transform trans_touch_book_blue():
    trans_book_blue_show
    function func_touch_dish
    0.1
    repeat
 
init python:
    import math, random
    dish_value_max = 100
 
    # Общие переменные мини-игры
    dish_value = 0
    dish_state = False
    dish_xzoom = 1.0
    dish_traning = False
    mouse_pos = (0,0)
 
    # Время на выполнение очистки (в секундах)
    clean_time = 10.0
    # Переменная для анимации таймера: AnimatedValue(clean_bar, 100, clean_time)
    clean_bar = 100
    # Флаг для предупреждения (смена цвета бара)
    clean_warning = False
 
    # Переменные для выбора посуды:
    # selected_item будет равен "dish" или "cup"
    # selected_fresh_item – соответственно "fresh_dish" или "fresh_cup"
    selected_item = "dish"        # значение по умолчанию
    selected_fresh_item = "fresh_dish"
 
    def clean_go(warning=False):
        global clean_bar, clean_warning
        if warning:
            clean_warning = True
        else:
            # Обнуляем значение, чтобы AnimatedValue анимировало изменение от 0 до 100 за clean_time секунд
            clean_bar = 0
        renpy.restart_interaction()
        
    cleanGo = renpy.curry(clean_go)
 
    def dish_calm():
        global dish_value, dish_traning
        if dish_value > 0 and not dish_traning:
            dish_value -= 1
 
    def func_touch_dish(trans, st, at):
        global dish_value, mouse_pos
        now_mouse = renpy.get_mouse_pos()
        dist = math.sqrt(sum([(a - b)**2 for (a, b) in zip(mouse_pos, now_mouse)]))
        if dist > 15:
            dish_value += 1.5
            mouse_pos = now_mouse
 
screen dishScreen():
    modal True
 
    # Таймеры для отсчёта:
    # 1. Немедленный запуск анимации (сбрасываем значение бара до 0)
    timer 0.01 action cleanGo()
    # 2. По истечении 2/3 времени включаем предупреждение (смена цвета)
    timer clean_time * 0.6666 action cleanGo(True)
    # 3. По истечении полного времени переходим к провалу
    timer clean_time action Jump("clean_fail")
 
    # Таймер-бар, отображающий оставшееся время, располагается в нижней части экрана
    bar:
        align (0.5, 0.9)
        xysize (300, 30)
        value AnimatedValue(clean_bar, 100, clean_time)
        if clean_warning:
            left_bar Solid("#e02")
    
    text ("Натирай посуду!" if whatToWash == "dish" else "Натирай книгу!") xalign 0.5 yalign 0.1 size 70 at pulse_zoom

    default refresh_var = 0
    bar value dish_value range dish_value_max:
        xalign 0.5
        xsize 700
    text "Прогресс: [dish_value]":
        xalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.3
        focus_mask True
        # Исправленные условия для всех возможных значений selected_item:
        idle (
            trans_normal_dish if selected_item == "dish" else 
            trans_normal_cup if selected_item == "cup" else 
            trans_normal_book_red if selected_item == "book_red" else 
            trans_normal_book_blue
        )
        hover (
            trans_touch_dish if selected_item == "dish" else 
            trans_touch_cup if selected_item == "cup" else 
            trans_touch_book_red if selected_item == "book_red" else 
            trans_touch_book_blue
        )
        action SetScreenVariable("refresh_var", refresh_var)
    timer 0.1:
        action SetScreenVariable("refresh_var", refresh_var)
        repeat True
    timer 0.5:
        action dish_calm
        repeat True
    if dish_value >= dish_value_max:
        timer 0.1:
            action Jump("clean_success")
 
label start_clean(whatToWash):
    # Сброс параметров игры
    $ dish_value = 0
    $ clean_bar = 100
    $ clean_warning = False
    # Случайным образом выбираем, с какой посудой будем работать
    if(whatToWash == "dish"):
        $ selected_item = renpy.random.choice(["dish", "cup"])
    if(whatToWash == "books"):
        $ selected_item = renpy.random.choice(["book_blue", "book_red"])
    $ selected_fresh_item = "fresh_" + selected_item
    call screen dishScreen
    return
 
label clean_fail:
    $ last_clean_win = False
    "Вы не справились"
    return
 
label clean_success:
    $ last_clean_win = True
    hide screen dishScreen
    # Показываем соответствующую чистую посуду:
    if selected_item == "dish":
        show fresh_dish:
            xalign 0.5
            yalign 0.3
    elif selected_item == "cup":
        show fresh_cup:
            xalign 0.5
            yalign 0.3
    elif selected_item == "book_red":
        show fresh_book_red:
            xalign 0.5
            yalign 0.3
    elif selected_item == "book_blue":
        show fresh_book_blue:
            xalign 0.5
            yalign 0.3
    pause 1.5
    hide fresh_cup
    hide fresh_dish
    hide fresh_book_red
    hide fresh_book_blue
    return
