
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



image paper = "paper.png"
default notices = []
init python:
    def customNotify(message):
        global notices
        notices.append(message)
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def getQuest(quest):
        global active_quest,notices
        active_quest = quest
        notices.append("Ты принял квест " + str(active_quest.name))
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def removeQuest():
        global active_quest, notices
        notices.append("Ты отказался от квеста " + str(active_quest.name))
        active_quest = no_quest
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
        global money, strength, charisma, mana, notices
        strength += charCount * strength_mod
        charisma += charCount * charisma_mod
        mana += charCount * mana_mod
        notices.append("Сил нет, буквально..")
        notices.append("Будто постарел немного..")
        notices.append("И ты забываешь базовые знания..")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addChar(chars, charCount):
        global strength, charisma, mana, notices
        for char in chars:
            if char == "str":
                strength += charCount * strength_mod
                notices.append("Ты чувствуешь себя сильнее")
            if char == "char":
                charisma += charCount * charisma_mod
                notices.append("Ты чувствуешь себя харизматичнее")
            if char == "mana":
                mana += charCount * mana_mod
                notices.append("Ты чувствуешь себя умнее")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusMoneyPlusChar(minusMoney, chars, charCount):
        global money, strength, charisma, mana, notices
        money -= minusMoney
        for char in chars:
            if char == "str":
                strength += charCount * strength_mod
                notices.append("Ты чувствуешь себя сильнее")
            if char == "char":
                charisma += charCount * charisma_mod
                notices.append("Ты чувствуешь себя харизматичнее")
            if char == "mana":
                mana += charCount * mana_mod
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

    def addLove(who, countLove):
        global m_love, e_love, r_love, ts_love, s_love, nag_love, f_love, h_love,mer_love, mao_love, notices
        if who == "f":
            f_love += countLove
        elif who == "nag":
            nag_love += countLove
        elif who == "mer":
            mer_love += countLove
        elif who == "s":
            s_love += countLove
        elif who == "ts":
            ts_love += countLove
        elif who == "h":
            h_love += countLove
        elif who == "m":
            m_love += countLove
        elif who == "e":
            e_love += countLove
        elif who == "r":
            r_love += countLove
        elif who == "mao":
            mao_love += countLove
        notices.append("Характеристика симпатии ["+ who +".name] увеличилась")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def minusLove(who, countLove):
        global m_love, e_love, r_love, ts_love, s_love, nag_love, f_love, h_love,mer_love, mao_love, notices
        if who == "f":
            f_love -= countLove
        elif who == "nag":
            nag_love -= countLove
        elif who == "mer":
            mer_love -= countLove
        elif who == "s":
            s_love -= countLove
        elif who == "ts":
            ts_love -= countLove
        elif who == "h":
            h_love -= countLove
        elif who == "m":
            m_love -= countLove
        elif who == "e":
            e_love -= countLove
        elif who == "r":
            r_love -= countLove
        elif who == "mao":
            mao_love -= countLove
        notices.append("Характеристика симпатии уменьшилась")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addNPCStr(who, countStr):
        global nag_str,notices
        if who == "nag":
            nag_str += countStr 
        if who == "eris":
            eris_str += countStr
        notices.append("Противник становится серьезнее")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []

    def addLoveAndStr(who, countLove, countStr):
        global nag_str,miku_love,nag_love,notices
        if who == "miku":
            miku_love += countLove
            miku_str += countStr * strength_mod
        if who == "nag":
            nag_love += countLove
            nag_str += countStr * strength_mod
        notices.append("Противник становится серьезнее")
        notices.append("Характеристика симпатии увеличилась")
        renpy.show_screen('notify_plus', notices=notices)
        notices = []