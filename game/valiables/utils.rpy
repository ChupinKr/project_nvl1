
# Переходы
define dis5 = Dissolve(.5)
define dis25 = Dissolve(.25)
define flash = Fade(0.1, 0.0, 1.0, color="#FFFFFF")

# сторонние переменные
define enemy_name = "Противник"
define enemy_strength = 0
define battle_location = 0
define last_battle_win = None
define last_clean_win = None

#положения
transform left_bit:
    xalign 0.25
    yalign 1.5
transform left_mid:
    xalign 0.1
    yalign 1.5
transform left:
    xalign 0.0
    yalign 1.5
transform right_bit:
    xalign 0.75
    yalign 1.5
transform right_mid:
    xalign 0.9
    yalign 1.5
transform right:
    xalign 1.0
    yalign 1.5
transform mid:
    xalign 0.5
    yalign 1.5

# положения сфер
transform mid_left:
    xalign 0.2
    yalign 0.5
transform mid_right:
    xalign 0.8
    yalign 0.5
transform mid_mid:
    xalign 0.5
    yalign 0.5