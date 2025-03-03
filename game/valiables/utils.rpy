
# Переходы
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
    yalign 1.2
transform left_mid:
    xalign 0.1
    yalign 1.2
transform left:
    xalign 0.0
    yalign 1.2
transform right_bit:
    xalign 0.75
    yalign 1.2
transform right_mid:
    xalign 0.9
    yalign 1.2
transform right:
    xalign 1.0
    yalign 1.2
transform mid:
    xalign 0.5
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
    def customNotify(message):
        global notices
        notices.append(message)
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addMoney(plusMoney=0):
        global money,notices
        money += plusMoney
        notices.append("Ты получил " + str(plusMoney) + " монет")
        notices.append("У тебя " + str(money) + " монет")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusMoney(minusMoney=0):
        global money,notices
        money -= minusMoney
        notices.append("Ты потерял " + str(minusMoney) + " монет")
        notices.append("У тебя " + str(money) + " монет")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def buyItem(item):
        global money,gg_items,notices
        money -= item.price
        gg_items.append(item)
        notices.append("Ты потерял " + str(item.price) + " монет")
        notices.append("У тебя " + str(money) + " монет")
        notices.append("Ты купил " + str(item.name))
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
        notices.append("Сил нет, буквально..")
        notices.append("Будто постарел немного..")
        notices.append("Тебе очень плохо..")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addChar(chars, charCount):
        global strength, charisma, intelligence, notices
        for char in chars:
            if char == "str":
                strength += charCount * strength_mod
                notices.append("Ты чувствуешь себя сильнее")
            if char == "char":
                charisma += charCount * charisma_mod
                notices.append("Ты чувствуешь себя харизматичнее")
            if char == "intelligence":
                intelligence += charCount * intelligence_mod
                notices.append("Ты чувствуешь себя умнее")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusMoneyPlusChar(minusMoney, chars, charCount):
        global money, strength, charisma, intelligence, notices
        money -= minusMoney
        for char in chars:
            if char == "str":
                strength += charCount * strength_mod
                notices.append("Ты чувствуешь себя сильнее")
            if char == "char":
                charisma += charCount * charisma_mod
                notices.append("Ты чувствуешь себя харизматичнее")
            if char == "intelligence":
                intelligence += charCount * intelligence_mod
                notices.append("Ты чувствуешь себя умнее")
        if minusMoney > 0:
            notices.append("Ты потерял " + str(minusMoney) + " монет")
            notices.append("У тебя " + str(money) + " монет")
        if len(notices) < 1:
            notices.append("Ты чувствуешь себя везучим")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addHealth(counHealth):
        global health,notices
        health += counHealth
        if(health > 100):
            health = 100
        if counHealth > 10:
            notices.append("Ты чувствуешь себя намного лучше")
        else:
            notices.append("Ты чувствуешь себя чуть лучше")
        notices.append("Текущий показатель здоровья: " + str(health))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusHealth(counHealth):
        global health,notices
        health -= counHealth
        if(health < 0):
            health = 0
        notices.append("Текущий показатель здоровья: " + str(health))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addLove(who, countLove):
        
        global notices
        if who == "f":
            my_freya.love += countLove
        elif who == "nag":
            my_nag.love += countLove
        elif who == "mer":
            my_merlin.love += countLove
        elif who == "s":
            my_sakura.love += countLove
        elif who == "ts":
            my_tsunade.love += countLove
        elif who == "h":
            my_holo.love += countLove
        elif who == "m":
            my_miku.love += countLove
        elif who == "e":
            my_elsa.love += countLove
        elif who == "r":
            my_rapunzel.love += countLove
        elif who == "mao":
            my_mao.love += countLove
        elif who == "d":
            my_darkness.love += countLove
        elif who == "eris":
            my_eris.love += countLove
        notices.append("Характеристика симпатии ["+ who +".name] увеличилась")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusLove(who, countLove):
        global notices
        if who == "f":
            my_freya.love -= countLove
        elif who == "nag":
            my_nag.love -= countLove
        elif who == "mer":
            my_merlin.love -= countLove
        elif who == "s":
            my_sakura.love -= countLove
        elif who == "ts":
            my_tsunade.love -= countLove
        elif who == "h":
            my_holo.love -= countLove
        elif who == "m":
            my_miku.love -= countLove
        elif who == "e":
            my_elsa.love -= countLove
        elif who == "r":
            my_rapunzel.love -= countLove
        elif who == "mao":
            my_mao.love -= countLove
        elif who == "eris":
            my_eris.love -= countLove
        elif who == "d":
            my_darkness.love -= countLove
        notices.append("Характеристика симпатии уменьшилась")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addNPCStr(who, countStr):
        global notices
        if who == "nag":
            my_nag.str += countStr 
        if who == "eris":
            my_eris.str += countStr
        if who == "d":
            my_darkness.str += countStr
        notices.append("Противник становится серьезнее")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addLoveAndStr(who, countLove, countStr):
        global strength,notices
        if who == "nag":
            my_nag.love += countLove
        strength += countStr * strength_mod
        notices.append("Ты стал сильнее")
        notices.append("Характеристика симпатии увеличилась")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def nextTime():
        global day,time,notices
        if time == "Утро":
            time = "День"
        elif time == "День":
            time = "Вечер"
        elif time == "Вечер":
            time = "Ночь"
        elif time == "Ночь":
            time = "Утро"
            day += 1
            if canVisit("room") and day > while_room:
                updateCanVisit("room", False)
                renpy.jump("room_sleep")
            elif canVisit("room"):
                renpy.jump("room_sleep")
            else:
                renpy.jump("city_overnight_stay")

    def nextDay():
        global day,time,notices
        day += 1
        time = "Утро"
        if day > while_room:
            updateCanVisit("room", False)
        notices.append("Наступил следующий день")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []




    def isNight():
        global time,notices
        if time == "Ночь":
            return True
        else:
            return False

    def isEvening():
        global time,notices
        if time == "Вечер":
            return True
        else:
            return False

    def isDay():
        global time,notices
        if time == "День":
            return True
        else:
            return False

    def isMorning():
        global time
        if time == "Утро":
            return True
        else:
            return False