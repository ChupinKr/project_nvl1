
# Переходы
define dis25 = Dissolve(.25)
define flash = Fade(0.1, 0.0, 1.0, color="#FFFFFF")
define pink = Fade(0.1, 0.0, 1.0, color="#FFC0CB")
define red = Fade(0.1, 0.0, 1.0, color="#FF0000")
define long_fade = Fade(0.5, 1.2, 0.5)

# сторонние переменные
define enemy_name = "Противник"
define enemy_strength = 0
define battle_location = 0
define last_battle_win = None
define last_clean_win = None

#яркость
transform darken:
    matrixcolor BrightnessMatrix(-0.75)
transform darken_bit:
    matrixcolor BrightnessMatrix(-0.25)
transform normal_brightness:
    matrixcolor BrightnessMatrix(0)

#размер
transform small:
    zoom 0.75
transform smaller:
    zoom 0.7
transform normal_size:
    zoom 1
transform bg_size:
    zoom 1.5
transform bg_size_plus:
    zoom 2

#перещемещение
transform move_left_mid:
    linear 1.0 left_mid  # Плавно перемещает персонажа в исходную позицию за 2 секунды

#перещемещение
transform move_left:
    linear 1.0 left  # Плавно перемещает персонажа в исходную позицию за 2 секунды

#перещемещение
transform move_left_out:
    linear 1 left_out  # Плавно перемещает персонажа в исходную позицию за 2 секунды

#перещемещение
transform move_right_out:
    linear 1 right_out  # Плавно перемещает персонажа в исходную позицию за 2 секунды

#перещемещение
transform move_right_bit:
    linear 1.0 right_bit  # Плавно перемещает персонажа в исходную позицию за 2 секунды

#перещемещение
transform move_mid:
    linear 1.0 mid  # Плавно перемещает персонажа в исходную позицию за 2 секунды

#слегка прозрачный
transform transparent:
    alpha 0.8

#отразить по горизонтали
transform flipped:
    xzoom -1

#положения
transform left_out:
    xalign -0.5
    yalign 1.2
transform left_bit:
    xalign 0.4
    yalign 1.2
transform left_mid:
    xalign 0.25
    yalign 1.2
transform left:
    xalign 0.0
    yalign 1.2
transform mid:
    xalign 0.5
    yalign 1.2
transform right_out:
    xalign 1.5
    yalign 1.2
transform right_bit:
    xalign 0.6
    yalign 1.2
transform right_mid:
    xalign 0.75
    yalign 1.2
transform right_mid2:
    xalign 0.85
    yalign 1.2
transform right:
    xalign 1.0
    yalign 1.2

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

label hide_dialog:
    window hide
    pause 5.0
    return

image paper = "paper.png"
default notices = []
init python:
    def setLang(new_lang):
        global time
        persistent.lang = new_lang
        lang = persistent.lang
        renpy.change_language(persistent.lang)
        renpy.utter_restart()

    def cheatsOn():
        global is_cheats
        is_cheats = True
    def cheatsOff():
        global is_cheats
        is_cheats = False

    def customNotify(message):
        global notices
        notices.append(message)
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def setLocation(location):
        global current_location
        current_location = location

    def getLocation():
        global current_location
        return current_location

    def addMoney(plusMoney=0):
        global money, notices
        money += plusMoney
        if persistent.lang == "russian":
            notices.append("Ты получил " + str(plusMoney) + " монет")
            notices.append("У тебя " + str(money) + " монет")
        if persistent.lang == "english":
            notices.append("You got " + str(plusMoney) + " coins")
            notices.append("You have " + str(money) + " coins")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusMoney(minusMoney=0):
        global money,notices
        money -= minusMoney
        if persistent.lang == "russian":
            notices.append("Ты потерял " + str(minusMoney) + " монет")
            notices.append("У тебя " + str(money) + " монет")
        if persistent.lang == "english":
            notices.append("You lost " + str(minusMoney) + " coins")
            notices.append("You have " + str(money) + " coins")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def buyItem(item):
        global money,gg_items,notices
        money -= item.price
        gg_items.append(item)
        if persistent.lang == "russian":
            notices.append("Ты потерял " + str(item.price) + " монет")
            notices.append("У тебя " + str(money) + " монет")
            notices.append("Ты купил " + str(item.name))
        if persistent.lang == "english":
            notices.append("You lost " + str(item.price) + " coins")
            notices.append("You have " + str(money) + " coins")
            notices.append("You bought " + str(item.name))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusAllChar(count):
        global money, strength, charisma, intelligence, notices
        strength -= count
        charisma -= count
        intelligence -= count
        if strength < 0:
            strength = 0
        if charisma < 0:
            charisma = 0
        if intelligence < 0:
            intelligence = 0
        if persistent.lang == "russian":
            notices.append("Сил нет, буквально..")
            notices.append("Будто постарел немного..")
            notices.append("Тебе очень плохо..")
        if persistent.lang == "english":
            notices.append("I'm literally exhausted..")
            notices.append("Like I've aged a bit..")
            notices.append("You feel really bad..")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addChar(chars, charCount):
        global strength, charisma, intelligence, notices
        for char in chars:
            if char == "str":
                strength += charCount * strength_mod
                if persistent.lang == "russian":
                    notices.append("Ты чувствуешь себя сильнее")
                if persistent.lang == "english":
                    notices.append("You feel stronger")
                    
            if char == "char":
                charisma += charCount * charisma_mod
                if persistent.lang == "russian":
                    notices.append("Ты чувствуешь себя харизматичнее")
                if persistent.lang == "english":
                    notices.append("You feel more charismatic")

            if char == "intelligence":
                intelligence += charCount * intelligence_mod
                if persistent.lang == "russian":
                    notices.append("Ты чувствуешь себя умнее")
                if persistent.lang == "english":
                    notices.append("You feel smarter")
                
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusMoneyPlusChar(minusMoney, chars, charCount):
        global money, strength, charisma, intelligence, notices
        money -= minusMoney
        for char in chars:
            if char == "str":
                strength += charCount * strength_mod
                if persistent.lang == "russian":
                    notices.append("Ты чувствуешь себя сильнее")
                if persistent.lang == "english":
                    notices.append("You feel stronger")
            if char == "char":
                charisma += charCount * charisma_mod
                if persistent.lang == "russian":
                    notices.append("Ты чувствуешь себя харизматичнее")
                if persistent.lang == "english":
                    notices.append("You feel more charismatic")
            if char == "intelligence":
                intelligence += charCount * intelligence_mod
                if persistent.lang == "russian":
                    notices.append("Ты чувствуешь себя умнее")
                if persistent.lang == "english":
                    notices.append("You feel smarter")
        if minusMoney > 0:
            if persistent.lang == "russian":
                notices.append("Ты потерял " + str(minusMoney) + " монет")
                notices.append("У тебя " + str(money) + " монет")
            if persistent.lang == "english":
                notices.append("You lost " + str(minusMoney) + " coins")
                notices.append("You have " + str(money) + " coins")
        if len(notices) < 1:
            if persistent.lang == "russian":
                notices.append("Ты чувствуешь себя везучим")
            if persistent.lang == "english":
                notices.append("You feel lucky")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addHealth(countHealth):
        global health,notices
        health = 0
        health += countHealth
        if(health > 100):
            health = 100
        if countHealth > 10:
            if persistent.lang == "russian":
                notices.append("Ты чувствуешь себя намного лучше")
            if persistent.lang == "english":
                notices.append("You feel much better")
        else:
            if persistent.lang == "russian":
                notices.append("Ты чувствуешь себя чуть лучше")
            if persistent.lang == "english":
                notices.append("You feel a little better")
        if persistent.lang == "russian":
            notices.append("Текущий показатель здоровья: " + str(health))
        if persistent.lang == "english":
            notices.append("Current health: " + str(health))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusHealth(countHealth):
        global health,notices
        health -= countHealth
        if(health < 0):
            health = 0
        if persistent.lang == "russian":
            notices.append("Текущий показатель здоровья: " + str(health))
        if persistent.lang == "english":
            notices.append("Current health: " + str(health))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addLoveAndStr(who, countLove, countStr):
        global strength,notices
        if who == "nag":
            my_nag_love += countLove
        strength += countStr * strength_mod
        if persistent.lang == "russian":
            notices.append("Ты стал сильнее")
            notices.append("Характеристика симпатии увеличилась")
        if persistent.lang == "english":
            notices.append("You've become stronger")
            notices.append("The sympathy characteristic has increased")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def nextTime():
        global day,time,notices
        if persistent.lang == "russian":
            if time == "Утро" or time == "Morning":
                time = "День"
            elif time == "День" or time == "Day":
                time = "Вечер"
            elif time == "Вечер" or time == "Evening":
                time = "Ночь"
            elif time == "Ночь" or time == "Night":
                if canVisit("room") and day > while_room:
                    updateCanVisit("room", False)
                    renpy.jump("room_sleep")
                elif canVisit("room"):
                    renpy.jump("room_sleep")
                else:
                    renpy.jump("city_overnight_stay")
        if persistent.lang == "english":
            if time == "Утро" or time == "Morning":
                time = "Day"
            elif time == "День" or time == "Day":
                time = "Evening"
            elif time == "Вечер" or time == "Evening":
                time = "Night"
            elif time == "Ночь" or time == "Night":
                if canVisit("room") and day > while_room:
                    updateCanVisit("room", False)
                    renpy.jump("room_sleep")
                elif canVisit("room"):
                    renpy.jump("room_sleep")
                else:
                    renpy.jump("city_overnight_stay")


    def setTime(time_num):  #0,1,2,3 - morning, day, evening, night
        global time
        if persistent.lang == "russian":
            if time_num == 0:
                time = "Утро"
            if time_num == 1:
                time = "День"
            if time_num == 2:
                time = "Вечер"
            if time_num == 3:
                time = "Ночь"
        if persistent.lang == "english":
            if time_num == 0:
                time = "Morning"
            if time_num == 1:
                time = "Day"
            if time_num == 2:
                time = "Evening"
            if time_num == 3:
                time = "Night"

    def getTime():  #0,1,2,3 - morning, day, evening, night
        if persistent.lang == "russian":
            if time == "Утро" or time == "Morning":
                return 0
            elif time == "День" or time == "Day":
                return 1
            elif time == "Вечер" or time == "Evening":
                return 2
            elif time == "Ночь" or time == "Night":
                return 3


    def nextDay():
        global day,time,notices
        day += 1
        if persistent.lang == "russian":
            time = "Утро"
        if persistent.lang == "english":
            time = "Morning"
        if day > while_room:
            updateCanVisit("room", False)
        if persistent.lang == "russian":
            notices.append("Наступил следующий день")
        if persistent.lang == "english":
            notices.append("The next day has arrived")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []




    def isNight():
        global time,notices
        if persistent.lang == "russian":
            return time == "Ночь"
        if persistent.lang == "english":
            return time == "Night"

    def isEvening():
        global time,notices
        if persistent.lang == "russian":
            return time == "Вечер"
        if persistent.lang == "english":
            return time == "Evening"

    def isDay():
        global time,notices
        if persistent.lang == "russian":
            return time == "День"
        if persistent.lang == "english":
            return time == "Day"

    def isMorning():
        global time
        if persistent.lang == "russian":
            return time == "Утро"
        if persistent.lang == "english":
            return time == "Morning"