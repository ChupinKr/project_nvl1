init python:
    if persistent.lang == "russian":
        magic_questions = [
            {
                "text": "Какой магический элемент наиболее непредсказуем?",
                "answers": [
                    {"text": "Огонь. Он приносит как тепло, так и разрушение.", "correct": True},
                    {"text": "Вода. Она подстраивается под любую форму.", "correct": False},
                    {"text": "Тьма. Никто до конца не знает её природы.", "correct": False}
                ]
            },
            {
                "text": "Что важнее для сильного мага?",
                "answers": [
                    {"text": "Сила. Без неё заклинания бесполезны.", "correct": False},
                    {"text": "Контроль. Магия без контроля разрушительна.", "correct": True},
                    {"text": "Наследие. Истинная мощь передаётся по крови.", "correct": False}
                ]
            },
            {
                "text": "Почему маги используют жесты и слова при заклинаниях?",
                "answers": [
                    {"text": "Так магия лучше понимает их намерения.", "correct": True},
                    {"text": "Они просто создают зрелищность.", "correct": False},
                    {"text": "Это осталось от древних традиций.", "correct": False}
                ]
            },
            {
                "text": "Какой самый опасный вид магии?",
                "answers": [
                    {"text": "Некромантия. Она нарушает естественный порядок.", "correct": False},
                    {"text": "Разум. Она способна сломать личность.", "correct": True},
                    {"text": "Пространство. Ошибка в расчётах — и ты потерян.", "correct": False}
                ]
            },
            {
                "text": "Что делает артефакт по-настоящему мощным?",
                "answers": [
                    {"text": "Редкость материалов, из которых он создан.", "correct": False},
                    {"text": "Сила мага, который его зачаровал.", "correct": False},
                    {"text": "История и намерение, заложенные в него.", "correct": True}
                ]
            },
            {
                "text": "Можно ли создать магию из ничего?",
                "answers": [
                    {"text": "Нет, энергия не возникает без источника.", "correct": True},
                    {"text": "Да, если иметь достаточно знаний.", "correct": False},
                    {"text": "Магия сама решает, где появиться.", "correct": False}
                ]
            },
            {
                "text": "Что отличает истинного мага от простого волшебника?",
                "answers": [
                    {"text": "Истинный маг не использует слова, лишь мысли.", "correct": False},
                    {"text": "Истинный маг понимает, когда НЕ использовать магию.", "correct": True},
                    {"text": "Истинный маг рождается с даром, а волшебник учится.", "correct": False}
                ]
            },
            {
                "text": "Какой самый сложный аспект магического ритуала?",
                "answers": [
                    {"text": "Чёткое произнесение заклинаний.", "correct": False},
                    {"text": "Поддержание концентрации на протяжении всего ритуала.", "correct": True},
                    {"text": "Использование редких ингредиентов.", "correct": False}
                ]
            },
            {
                "text": "Что сильнее — магия или воля?",
                "answers": [
                    {"text": "Магия. Даже сильный дух не устоит перед мощными заклятиями.", "correct": False},
                    {"text": "Воля. Истинный маг подчиняет магию своему разуму.", "correct": True},
                    {"text": "Они равны. Магия без воли хаотична, а воля без магии слаба.", "correct": False}
                ]
            },
            {
                "text": "Можно ли превзойти естественные пределы магии?",
                "answers": [
                    {"text": "Да, если нарушить законы мира.", "correct": False},
                    {"text": "Только если найти новый источник силы.", "correct": True},
                    {"text": "Нет, магия подчиняется строгим правилам.", "correct": False}
                ]
            },
            {
                "text": "Какую роль играет эмоция в магии?",
                "answers": [
                    {"text": "Она может усиливать заклинания, но делает их нестабильными.", "correct": True},
                    {"text": "Эмоции мешают магу. Истинный маг хладнокровен.", "correct": False},
                    {"text": "Без эмоций магия просто не работает.", "correct": False}
                ]
            },
            {
                "text": "Почему некоторые маги теряют разум?",
                "answers": [
                    {"text": "Они погружаются слишком глубоко в знания, не предназначенные для смертных.", "correct": True},
                    {"text": "Они используют слишком много энергии разом.", "correct": False},
                    {"text": "Магия вытягивает их жизненную силу.", "correct": False}
                ]
            },
            {
                "text": "Можно ли полностью подавить магию в человеке?",
                "answers": [
                    {"text": "Нет, магия всегда найдёт способ проявиться.", "correct": False},
                    {"text": "Да, с помощью особых печатей или артефактов.", "correct": True},
                    {"text": "Только если уничтожить его источник силы.", "correct": False}
                ]
            },
            {
                "text": "Что произойдёт, если переплести несколько заклинаний одновременно?",
                "answers": [
                    {"text": "Заклинания усилят друг друга.", "correct": False},
                    {"text": "Заклинания могут сплестись в нечто новое... или взорваться.", "correct": True},
                    {"text": "Одно из них просто поглотит другое.", "correct": False}
                ]
            },
            {
                "text": "Как узнать, что магия достигла своего предела?",
                "answers": [
                    {"text": "Когда маг больше не чувствует потока энергии.", "correct": False},
                    {"text": "Когда даже простейшие заклинания становятся нестабильными.", "correct": True},
                    {"text": "Когда тело начинает разрушаться от перегрузки.", "correct": False}
                ]
            }
        ]
    if persistent.lang == "english":
        magic_questions = [
            {
                "text": "Which magical element is the most unpredictable?",
                "answers": [
                    {"text": "Fire. It brings both warmth and destruction.", "correct": True},
                    {"text": "Water. It adapts to any shape.", "correct": False},
                    {"text": "Darkness. No one fully understands its nature.", "correct": False}
                ]
            },
            {
                "text": "What is most important for a powerful mage?",
                "answers": [
                    {"text": "Strength. Without it, spells are useless.", "correct": False},
                    {"text": "Control. Magic without control is destructive.", "correct": True},
                    {"text": "Legacy. True power is passed down through blood.", "correct": False}
                ]
            },
            {
                "text": "Why do mages use gestures and words when casting spells?",
                "answers": [
                    {"text": "So magic better understands their intentions.", "correct": True},
                    {"text": "They’re just putting on a show.", "correct": False},
                    {"text": "It’s a remnant of ancient traditions.", "correct": False}
                ]
            },
            {
                "text": "Which type of magic is the most dangerous?",
                "answers": [
                    {"text": "Necromancy. It disrupts the natural order.", "correct": False},
                    {"text": "Mind. It can break a person’s identity.", "correct": True},
                    {"text": "Space. A miscalculation, and you’re lost.", "correct": False}
                ]
            },
            {
                "text": "What makes an artifact truly powerful?",
                "answers": [
                    {"text": "The rarity of the materials it’s made from.", "correct": False},
                    {"text": "The strength of the mage who enchanted it.", "correct": False},
                    {"text": "The history and intent imbued within it.", "correct": True}
                ]
            },
            {
                "text": "Can magic be created from nothing?",
                "answers": [
                    {"text": "No, energy doesn’t come without a source.", "correct": True},
                    {"text": "Yes, if you have enough knowledge.", "correct": False},
                    {"text": "Magic itself decides where it appears.", "correct": False}
                ]
            },
            {
                "text": "What distinguishes a true mage from a mere wizard?",
                "answers": [
                    {"text": "A true mage uses only thoughts, not words.", "correct": False},
                    {"text": "A true mage knows when NOT to use magic.", "correct": True},
                    {"text": "A true mage is born with the gift, while a wizard learns.", "correct": False}
                ]
            },
            {
                "text": "What is the most challenging aspect of a magical ritual?",
                "answers": [
                    {"text": "Pronouncing spells clearly.", "correct": False},
                    {"text": "Maintaining focus throughout the entire ritual.", "correct": True},
                    {"text": "Using rare ingredients.", "correct": False}
                ]
            },
            {
                "text": "What is stronger—magic or will?",
                "answers": [
                    {"text": "Magic. Even a strong spirit can’t withstand powerful spells.", "correct": False},
                    {"text": "Will. A true mage bends magic to their mind.", "correct": True},
                    {"text": "They’re equal. Magic without will is chaotic, and will without magic is weak.", "correct": False}
                ]
            },
            {
                "text": "Can the natural limits of magic be surpassed?",
                "answers": [
                    {"text": "Yes, if you break the laws of the world.", "correct": False},
                    {"text": "Only if you find a new source of power.", "correct": True},
                    {"text": "No, magic follows strict rules.", "correct": False}
                ]
            },
            {
                "text": "What role do emotions play in magic?",
                "answers": [
                    {"text": "They can amplify spells but make them unstable.", "correct": True},
                    {"text": "Emotions hinder a mage. A true mage is cold-blooded.", "correct": False},
                    {"text": "Without emotions, magic simply doesn’t work.", "correct": False}
                ]
            },
            {
                "text": "Why do some mages lose their minds?",
                "answers": [
                    {"text": "They delve too deep into knowledge not meant for mortals.", "correct": True},
                    {"text": "They use too much energy at once.", "correct": False},
                    {"text": "Magic drains their life force.", "correct": False}
                ]
            },
            {
                "text": "Can magic be completely suppressed in a person?",
                "answers": [
                    {"text": "No, magic will always find a way to manifest.", "correct": False},
                    {"text": "Yes, with special seals or artifacts.", "correct": True},
                    {"text": "Only by destroying their source of power.", "correct": False}
                ]
            },
            {
                "text": "What happens if you weave multiple spells together at once?",
                "answers": [
                    {"text": "The spells will amplify each other.", "correct": False},
                    {"text": "The spells might combine into something new… or explode.", "correct": True},
                    {"text": "One will simply overpower the other.", "correct": False}
                ]
            },
            {
                "text": "How do you know when magic has reached its limit?",
                "answers": [
                    {"text": "When the mage no longer feels the flow of energy.", "correct": False},
                    {"text": "When even the simplest spells become unstable.", "correct": True},
                    {"text": "When the body starts breaking down from overload.", "correct": False}
                ]
            }
        ]



define last_magic_knowlenge_win = False

label start_magic_knowlenge_training(character, your_int):
    $ import random
    $ selected_questions = random.sample(magic_questions, 3)
    $ score = 0
    $ win_score = 3  # Количество правильных ответов для победы

    if persistent.lang == "russian":
        if is_cheats:
            menu:
                "У вас включены читы. Пропустить мини-игру?"
                "Играть":
                    pause .01
                "Пропустить":
                    $score = win_score
                    call end_magic_knowlenge(character)
                    return
    if persistent.lang == "english":
        if is_cheats:
            menu:
                "Cheats are enabled. Skip the mini-game?"
                "Play":
                    pause .01
                "Skip":
                    $score = win_score
                    call end_magic_knowlenge(character)
                    return

    # Проходимся по каждому вопросу
    python:
        for question in selected_questions:
            renpy.say(character, question["text"])  # Выводим текст вопроса

            # Создаём меню для ответов
            choices = []
            for answer in question["answers"]:
                choices.append((answer["text"], answer["correct"]))  # Теперь передаём кортежи

            # Ожидание ответа игрока
            result = renpy.display_menu(choices)

            # Проверяем, был ли ответ правильным
            if result:
                score += 1

    call end_charisma_training(character)
    return


label end_magic_knowlenge(character):
    if score >= win_score:
        $ last_magic_knowlenge_win = True
        "Ты ответил правильно на все вопросы!"
    else:
        $ last_magic_knowlenge_win = False
        "Похоже, тебе ещё стоит потренироваться..."

    return
