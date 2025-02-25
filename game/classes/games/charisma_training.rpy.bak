define last_charisma_training_win = False


## Логика мини-игры.
label start_charisma_training(charisma):
    pause .5
    show expression Text("Будь внимателен!") at truecenter as txt
    with dissolve
    pause
    hide txt

    $ score = 0  # Сбрасываем очки перед игрой
    $ win_score = 3
    
    #TODO исправить
    $score = win_score
    call end_charisma_training

    return

## Переход после завершения игры
label end_charisma_training:
    "IN PROGRESS"
    if score >= win_score:
        $ last_charisma_training_win = True
    return
