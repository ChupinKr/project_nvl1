init:
    # Инициализация переменных
    $ hero_name = ""
    $ chosen_blessing = None  # Хранит выбранное благословение
    $ health = 100  # Здоровье

    $ money = 0  # Харизма
    $ charisma = 0  # Харизма
    $ strength = 0  # Сила
    $ mana = 0  # Объем маны

    # День и время
    $ day = 0 # после вечера должно идти утро след дня
    $ time = 0 #Всего 3 времени (0 - раннее утро, 1 - день, 2 - вечер)

    #Текущий квест
    $ active_quest = None

    # Массив доступных для главного героя заклинаний
    $ available_spells = []

    #Количество смертей
    $ death_count = 0

    #Доступы
    $ can_visit_home = False
    $ can_visit_bar = False
    $ can_visit_tavern = False
    $ can_visit_guild = False
    $ can_visit_magic_tower = False
    $ can_visit_library = False
    $ can_visit_training_ground = False
    $ can_visit_hospital = False
    $ can_visit_black_market = False
    $ can_visit_forest = True
    $ can_visit_ruined_temple = True
    $ can_visit_monster_forest = True


default notices = []
init python:
    def addMoney(plusMoney=0):
        global money,notices
        money += plusMoney
        notices.append("Ты получил " + str(plusMoney) + " золота")
        notices.append("У тебя " + str(money) + " золота")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

screen notify_plus(notices):

    zorder 100
    style_prefix "notify"

    for dd, i in enumerate(notices):
        frame at notify_plus_appear(dd*3.5):
            text i

    timer 4.25+(dd*3.5) action Hide('notify_plus')

transform notify_plus_appear(dd=0):
    on show:
        yoffset dd*7
        alpha 0 xanchor 1.0 xpos 0.0
        pause dd
        linear .25 alpha 1.0 xalign 0.0
        pause 3.25
        linear .5 alpha 0.0

screen buttons:
    vbox:
        xalign 0.99
        yalign 0.01
        imagebutton:
            xalign 0.99
            yalign 0.05
            idle "gui/button/home.png"
            hover "gui/button/home_hover.png"
            action Jump("city")
        imagebutton:
            xalign 0.99
            yalign 0.05
            idle "gui/button/city.png"
            hover "gui/button/city_hover.png"
            action Show("city")
        imagebutton:
            xalign 0.99
            yalign 0.05
            idle "gui/button/stat.png"
            hover "gui/button/stat_hover.png"
            action Show("info_panel")
