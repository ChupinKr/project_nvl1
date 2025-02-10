image dish = "images/assets/cleaner/dirty_dish.png"
transform trans_dish_show():
    "images/assets/cleaner/dirty_dish.png"
 
transform trans_normal_dish():
    trans_dish_show
    0.1
    repeat
 
transform trans_touch_dish():
    trans_dish_show
    function func_touch_dish
    0.1
    repeat
 
 
init python:
    import math
    dish_value_max = 100
 
 
    dish_value = 0
    dish_state = False
    dish_xzoom = 1.0
    dish_traning = False
    mouse_pos = (0,0)

    # Время на ввод комбинации (в секундах)
    clean_time = 10.0
    # Переменная для анимации бара: при запуске мы будем обнулять её,
    # AnimatedValue(clean_bar, 100, clean_time) анимирует изменение от текущего значения до 100.
    clean_bar = 100
    # Флаг для предупреждения (смена цвета бара)
    clean_warning = False

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
        dist = math.sqrt(sum([(a - b)**2 for (a,b) in zip(mouse_pos,now_mouse)]))
        if dist > 5:
            dish_value += 1.5
            mouse_pos = now_mouse

screen dishScreen():
    modal True

    # Таймеры для отсчёта:
    # 1. Немедленный запуск анимации (сбрасываем значение бара до 0)
    timer 0.01 action cleanGo()
    # 2. По истечении 2/3 времени включаем предупреждение (смена цвета)
    timer clean_time * 0.6666 action cleanGo(True)
    # 3. По истечении полного времени переходим к проверке ввода комбинации
    timer clean_time action Jump("clean_fail")


    # Таймер-бар, отображающий оставшееся время, располагается в нижней части экрана
    bar:
        align (0.5, 0.9)
        xysize (300, 30)
        # Анимированное значение от clean_bar до 100 за clean_time секунд
        value AnimatedValue(clean_bar, 100, clean_time)
        # Если включено предупреждение – меняем цвет заполненной части
        if clean_warning:
            left_bar Solid("#e02")

    default refresh_var = 0
    bar value dish_value range dish_value_max:
        xalign 0.5
        xsize 400
    text "[dish_value]":
        xalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.3
        focus_mask True
        idle trans_normal_dish
        hover trans_touch_dish
        action SetScreenVariable("refresh_var",refresh_var)
    timer 0.1:
        action SetScreenVariable("refresh_var",refresh_var)
        repeat True
    timer 0.5:
        action dish_calm
        repeat True
    if dish_value >= dish_value_max:
        timer 0.1:
            action Jump("clean_success")
 
label start_clean:
    $ dish_value = 0
    $ clean_bar = 100
    $ clean_warning = False
    call screen dishScreen
    return


label clean_fail:
    "Вы не справились"
    return

label clean_success:
    $ addMoney(5)
    "Вы справились и заработали 5 монет!"
    return