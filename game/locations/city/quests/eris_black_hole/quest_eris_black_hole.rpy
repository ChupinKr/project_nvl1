label quest_eris_black_hole_start:
    "IN PROGRESS"
    
    mind "Надеюсь червоточина здесь больше не возникнет."
    if not can_find_eris:
        mind "Наконец всё вернулось в норму."
        $can_find_eris = True
        $customNotify("Ты можешь найти Эрис на тренировочной площадке.")
    return