init python:
    if persistent.lang == "russian":
        charisma_questions = [
            {
                "text": "Ты часто бросаешь такие взгляды? Или мне стоит почувствовать себя особенной?",
                "answers": [
                    {"text": "Особенной? Нет... Ты вне всех категорий.", "correct": True},
                    {"text": "Я смотрю так только на тех, кто заслуживает большего.", "correct": False},
                    {"text": "А ты хочешь быть единственной?", "correct": False}
                ]
            },
            {
                "text": "Какой комплимент мне действительно запомнится?",
                "answers": [
                    {"text": "Тот, который никто никогда тебе не говорил.", "correct": False},
                    {"text": "Тот, который прозвучит искренне, а не ради эффекта.", "correct": True},
                    {"text": "Тот, который ты сама хочешь услышать.", "correct": False}
                ]
            },
            {
                "text": "Представь, что ты можешь сказать мне только одно слово. Какое оно будет?",
                "answers": [
                    {"text": "Тайна.", "correct": False},
                    {"text": "Желание.", "correct": False},
                    {"text": "Останься.", "correct": True}
                ]
            },
            {
                "text": "Как ты понимаешь, что по-настоящему нравишься женщине?",
                "answers": [
                    {"text": "Когда она не боится показать ревность.", "correct": False},
                    {"text": "Когда она начинает хотеть нравиться мне.", "correct": True},
                    {"text": "Когда она даёт мне полную свободу.", "correct": False}
                ]
            },
            {
                "text": "Ты согласен с тем, что любовь — это битва, где один всегда проигрывает?",
                "answers": [
                    {"text": "Да, но лучший воин знает, когда стоит сдаться.", "correct": False},
                    {"text": "Нет, любовь — это союз, а не война.", "correct": True},
                    {"text": "В любви побеждает тот, кто меньше любит.", "correct": False}
                ]
            },
            {
                "text": "Какой самый большой риск в отношениях?",
                "answers": [
                    {"text": "Открыться, зная, что можешь быть отвергнут.", "correct": False},
                    {"text": "Потерять себя, пытаясь угодить другому.", "correct": False},
                    {"text": "Поверить в иллюзию, а не в человека.", "correct": True}
                ]
            },
            {
                "text": "Что важнее — запомниться или быть понятным?",
                "answers": [
                    {"text": "Запомниться. Память важнее смысла.", "correct": False},
                    {"text": "И то, и другое. Без смысла тебя забудут, без эмоций — не воспримут.", "correct": False},
                    {"text": "Быть понятным. Только тогда ты останешься в чьей-то памяти.", "correct": True}
                ]
            },
            {
                "text": "Что делает слова по-настоящему убедительными?",
                "answers": [
                    {"text": "Когда в них есть страсть и огонь.", "correct": False},
                    {"text": "Когда они звучат таинственно.", "correct": False},
                    {"text": "Когда они соответствуют поступкам.", "correct": True}
                ]
            },
            {
                "text": "Что сложнее: соблазнить или удержать?",
                "answers": [
                    {"text": "Соблазнить. Искры не всегда разгораются в пламя.", "correct": False},
                    {"text": "Удержать. Желание мимолётно, а привязанность требует усилий.", "correct": True},
                    {"text": "Оба варианта одинаково сложны, но лишь если играешь по правилам.", "correct": False}
                ]
            },
            {
                "text": "Как ты относишься к тем, кто играет в любовь?",
                "answers": [
                    {"text": "Если это красиво, почему бы и нет?", "correct": False},
                    {"text": "Игра — это часть охоты, а охота — суть соблазна.", "correct": False},
                    {"text": "Тот, кто играет, боится настоящих чувств.", "correct": True},
                ]
            },
            {
                "text": "Если бы я попросила тебя назвать самое соблазнительное качество, что бы ты выбрал?",
                "answers": [
                    {"text": "Красота, конечно.", "correct": False},
                    {"text": "Тайна, которую хочется разгадать.", "correct": False},
                    {"text": "Уверенность в сочетании с лёгким вызовом.", "correct": True}
                ]
            },
            {
                "text": "Какая фраза лучше всего описывает идеальную встречу?",
                "answers": [
                    {"text": "Когда она заканчивается позже, чем вы оба планировали.", "correct": False},
                    {"text": "Когда уходя, ты не знаешь, кто из вас кого соблазнил.", "correct": True},
                    {"text": "Когда после неё хочется написать первым.", "correct": False}
                ]
            },
            {
                "text": "Ты веришь в любовь с первого взгляда?",
                "answers": [
                    {"text": "Конечно, если она достаточно сильная.", "correct": False},
                    {"text": "Да, если это взгляд в глаза, а не в декольте.", "correct": False},
                    {"text": "Я верю в интерес с первого взгляда. А любовь — это выбор.", "correct": True}
                ]
            },
            {
                "text": "Какая эмоция заставляет нас влюбляться?",
                "answers": [
                    {"text": "Комфорт. Когда с человеком легко, любовь неизбежна.", "correct": False},
                    {"text": "Страсть. Если её нет, то и влюблённость невозможна.", "correct": False},
                    {"text": "Неуверенность. Волнение перед неизвестностью делает чувства ярче.", "correct": True},
                ]
            },
            {
                "text": "Какой момент важнее — первый поцелуй или первое 'Я люблю тебя'?",
                "answers": [
                    {"text": "Первое признание. Оно создаёт связь между душами.", "correct": False},
                    {"text": "Первый поцелуй. Он говорит больше, чем слова.", "correct": True},
                    {"text": "Ни один из них, если они были без искренности.", "correct": False}
                ]
            }
        ]
    if persistent.lang == "english":
        charisma_questions = [
            {
                "text": "Do you often give looks like that? Or should I feel special?",
                "answers": [
                    {"text": "Special? No... You’re beyond all categories.", "correct": True},
                    {"text": "I only look like that at those who deserve more.", "correct": False},
                    {"text": "And do you want to be the only one?", "correct": False}
                ]
            },
            {
                "text": "What compliment would I really remember?",
                "answers": [
                    {"text": "One that no one has ever told you before.", "correct": False},
                    {"text": "One that sounds sincere, not just for effect.", "correct": True},
                    {"text": "One that you yourself want to hear.", "correct": False}
                ]
            },
            {
                "text": "Imagine you can only say one word to me. What would it be?",
                "answers": [
                    {"text": "Mystery.", "correct": False},
                    {"text": "Desire.", "correct": False},
                    {"text": "Stay.", "correct": True}
                ]
            },
            {
                "text": "How do you know a woman truly likes you?",
                "answers": [
                    {"text": "When she’s not afraid to show jealousy.", "correct": False},
                    {"text": "When she starts wanting to please me.", "correct": True},
                    {"text": "When she gives me complete freedom.", "correct": False}
                ]
            },
            {
                "text": "Do you agree that love is a battle where one always loses?",
                "answers": [
                    {"text": "Yes, but the best warrior knows when to surrender.", "correct": False},
                    {"text": "No, love is an alliance, not a war.", "correct": True},
                    {"text": "In love, the one who loves less wins.", "correct": False}
                ]
            },
            {
                "text": "What’s the biggest risk in a relationship?",
                "answers": [
                    {"text": "Opening up, knowing you might be rejected.", "correct": False},
                    {"text": "Losing yourself while trying to please the other.", "correct": False},
                    {"text": "Believing in an illusion instead of the person.", "correct": True}
                ]
            },
            {
                "text": "What’s more important — to be remembered or to be understood?",
                "answers": [
                    {"text": "To be remembered. Memory matters more than meaning.", "correct": False},
                    {"text": "Both. Without meaning, you’ll be forgotten; without emotion, you won’t be felt.", "correct": False},
                    {"text": "To be understood. Only then will you stay in someone’s memory.", "correct": True}
                ]
            },
            {
                "text": "What makes words truly convincing?",
                "answers": [
                    {"text": "When they carry passion and fire.", "correct": False},
                    {"text": "When they sound mysterious.", "correct": False},
                    {"text": "When they match your actions.", "correct": True}
                ]
            },
            {
                "text": "What’s harder: to seduce or to keep?",
                "answers": [
                    {"text": "To seduce. Sparks don’t always turn into flames.", "correct": False},
                    {"text": "To keep. Desire is fleeting, but attachment takes effort.", "correct": True},
                    {"text": "Both are equally hard, but only if you play by the rules.", "correct": False}
                ]
            },
            {
                "text": "How do you feel about those who play at love?",
                "answers": [
                    {"text": "If it’s done beautifully, why not?", "correct": False},
                    {"text": "A game is part of the hunt, and the hunt is the essence of seduction.", "correct": False},
                    {"text": "Those who play are afraid of real feelings.", "correct": True}
                ]
            },
            {
                "text": "If I asked you to name the most seductive quality, what would you choose?",
                "answers": [
                    {"text": "Beauty, of course.", "correct": False},
                    {"text": "A mystery you want to unravel.", "correct": False},
                    {"text": "Confidence paired with a subtle challenge.", "correct": True}
                ]
            },
            {
                "text": "Which phrase best describes the perfect encounter?",
                "answers": [
                    {"text": "When it ends later than either of you planned.", "correct": False},
                    {"text": "When you leave unsure who seduced whom.", "correct": True},
                    {"text": "When afterward, you want to text first.", "correct": False}
                ]
            },
            {
                "text": "Do you believe in love at first sight?",
                "answers": [
                    {"text": "Of course, if it’s strong enough.", "correct": False},
                    {"text": "Yes, if it’s a look in the eyes, not at the neckline.", "correct": False},
                    {"text": "I believe in interest at first sight. Love is a choice.", "correct": True}
                ]
            },
            {
                "text": "What emotion makes us fall in love?",
                "answers": [
                    {"text": "Comfort. When it’s easy with someone, love is inevitable.", "correct": False},
                    {"text": "Passion. Without it, infatuation is impossible.", "correct": False},
                    {"text": "Uncertainty. The thrill of the unknown makes feelings stronger.", "correct": True}
                ]
            },
            {
                "text": "Which moment matters more — the first kiss or the first 'I love you'?",
                "answers": [
                    {"text": "The first confession. It builds a bond between souls.", "correct": False},
                    {"text": "The first kiss. It says more than words.", "correct": True},
                    {"text": "Neither, if they lack sincerity.", "correct": False}
                ]
            }
        ]


define last_charisma_training_win = False

label start_charisma_training(character, your_charisma):
    $ import random
    $ selected_questions = random.sample(charisma_questions, 3)
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
                    call end_charisma_training(character)
                    return
    if persistent.lang == "english":
        if is_cheats:
            menu:
                "Cheats are enabled. Skip the mini-game?"
                "Play":
                    pause .01
                "Skip":
                    $score = win_score
                    call end_charisma_training(character)
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

    if score >= win_score:
        $ last_charisma_training_win = True

    call end_charisma_training(character)
    return


label end_charisma_training(character):
    if score >= win_score:
        $ last_charisma_training_win = True
        "Ты ответил правильно на все вопросы!"
    else:
        $ last_charisma_training_win = False
        "Похоже, тебе ещё стоит потренироваться..."

    return
