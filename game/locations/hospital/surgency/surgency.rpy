
default first_time_surgency = True  

label surgency_tsunade_cure:
    $ bring = []
    call surgency_scene


    show ts neutral with dissolve

    if first_time_surgency and health == 0:
        "Ты медленно приходишь в себя, чувствуя резкую боль во всём теле."
        "Белый потолок, запах медикаментов… Похоже, ты в операционной."
        ts "Очнулся, наконец? Не люблю возиться с пациентами, которые валяются тут днями."
        if money < 10:
            ts "Вижу у тебя небольшие проблемы с золотом."
            ts "Повезло тебе, в первый раз я тебя подлатала бесплатно."
        else:
            ts @smile "С тебя 10 монет за срочную операцию"with dissolve
            $minusMoney(10)
            pause 3.5
        $addHealth(100)
        "Ты ощущаешь, как раны затягиваются, тело наполняется силой… но остаётся слабость."
        $first_time_surgency = False
    elif first_time_surgency:
        if not canVisit("hospital"):
            $ updateCanVisit("hospital", True)
        ts "Идти можешь, и пришёл ко мне, разве тебе нужно лечение? Или у тебя есть ко мне дело?"
        $first_time_surgency = False
    elif health == 0:
        if money >= 10:
            ts "Опять ты? Уже не первый раз на моём операционном столе."  
            ts "С тебя {color=#FFD700}10 монет{/color}. Надеюсь, ты не разорился?"
            $minusMoney(10)
            pause 3.5
            $addHealth(100)
            "Ты ощущаешь, как раны затягиваются, тело наполняется силой… но остаётся слабость."
        else:
            ts angry "Так не пойдет, дорогой, надо и честь знать." with dissolve
            ts "Думаю в этот раз вместо магических кристаллов - энергию мы будем брать прямо из тебя, потерпи, это будет незабываемо!"
            $minusAllChar(5)
            "Ты условно умер, но [ts.name] пожалела тебя"
            $defeat_count +=1
            pause 3.5
            $addHealth(100)
    jump surgency_tsunade_menu

label surgency_tsunade_menu: 
    $ bring = []
    menu:
        set bring
        "Вылечи меня" if health < 100:
            ts "А деньги то у тебя на это есть?"
            menu:
                "Да, [ts.name], вылечите меня поскорее" if money > 10:
                    $minusMoney(10)
                    pause 3.5
                    $addHealth(100)
                "Нет, но я надеялся, что вы мне поможете даром":
                    p "Нет, но я верю, что такая молодая красавица как вы, [ts.name], не сможет оставить юношу умирать"
                    if my_tsunade.love > 20 and charisma > 20:
                        ts "Каков наглец, ладно, но это в последний раз."
                        $addHealth(100)
                        pause 3.5
                        $minusLove("ts", 5)
                        jump surgency_tsunade_menu
                    else:
                        ts "Опять приполз без денег? Так не пойдет, дорогой, надо и честь знать."
                        jump surgency_tsunade_menu
            jump surgency_tsunade_menu
        "Спросить, где ты" if not canVisit("surgency"):
            ts "Ты в лечебнице. Здесь поднимают на ноги таких, как ты — тех, кто не умеет держать меч или уклоняться от ударов."
            $ updateCanVisit("surgency", True)
            jump surgency_tsunade_menu
        "Поинтересоваться, как заработать денег" if not canVisit("tavern"):
            ts "Ох, ты хочешь расплачиваться честно? Что ж, это похвально."
            ts "Вижу ты в этих краях раньше не бывал, так что расскажу"
            ts "В таверне всегда нужны помощники. Помоешь посуду — получишь монеты."
            "[ts.name] рассказывает, как попасть в Таверну"
            $ updateCanVisit("tavern", True)
            jump surgency_tsunade_menu
        "Спросить про задания" if isNoQuestNow():
            p "У вас есть какие-нибудь задания для меня, чтобы я мог честно расплачиваться за лечение?"
            call surgency_tsunade_quests
            jump surgency_tsunade_menu
        "Отказаться от выполнения задания" if isActualQuestOfCharacter("ts"):
            p "Я не смогу выполнить это задание."
            ts "Ох, ну хорошо, если передумаешь - приходи."
            $ removeQuest()
            jump surgency_tsunade_menu
        "Поблагодарить и уйти":
            ts smile "Хоть кто-то умеет говорить «спасибо». Постарайся больше не попадать ко мне." with dissolve
            if not canVisit("hospital"):
                $ updateCanVisit("hospital", True)
            jump city

label surgency_tsunade_quests:
    show ts neutral with dissolve
    ts "Задания? Хм... У меня есть кое-что для тебя."
    menu:
        # "Охота за редким ингредиентом" if not isQuestCompleted(quest_tsunade_poison_tooth):
        #         ts "Мне нужен редкий алхимический ингредиент — клык ядовитой змеи. Можно достать его в глубине леса."
        #         ts "Принеси его, и я заплачу тебе."
        #         if isAbleQuest(quest_tsunade_poison_tooth, 0):
        #             menu:
        #                 "Квест: Охота за редким ингредиентом"
        #                 "Принять квест":
        #                     ts "Отлично, спасибо, буду ждать тебя, желательно в целости."
        #                     $ getQuest(quest_tsunade_poison_tooth)
        #                 "Не принимать квест":
        #                     ts @angry "Ну, значит, не так уж и нуждаешься в деньгах." with dissolve
        #         else:
        #             ts "Хотя подожди, я передумала, вижу, ты слишком слаб для этой работы, возвращайся, когда поднаберешься сил."
        "Отказаться":
            ts "Ну, значит, не так уж и нуждаешься в деньгах."
    return