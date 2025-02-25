define first_time_nagatoro_dodjo = True

label nagatoro_dodjo:
    scene bg nagatoro_dodjo with fade
    show nag grin with dissolve
    nag "Мы пришли, с чего начнем?"
    jump nagatoro_dodjo_menu

label nagatoro_dodjo_first_time:
    scene bg nagatoro_dodjo with fade
    show nag grin with dissolve
    p "Надо же, традиционный Японский стиль."
    nag @happy "Это же додзё, само собой так и никак иначе."
    nag "Итак, мы на месте, будем тренироваться по плану."
    nag "Первым будет спортивное позирование, я буду показывать строение различных мышц, а ты будешь оценивать мое состояние."
    nag "Это будет полезно для твоего понимания идеального мышечного развития тела."
    p "Действительно! В этом есть смысл."
    nag @happy "Так и я о том же! Это базовая тренировка в спортивных программах прогрессивных стран."
    nag "Ну что, готов?"
    menu:
        "Сдержанно кивнуть.":
            p "Да, конечно."
            nag @grin "Хм, какой ты серьёзный. Давай посмотрим, надолго ли тебя хватит."
        
        "С подозрением прищуриться.":
            p "Ты точно про спорт говоришь?"
            nag @normal_shy "Ч-что за намёки? Это тренировка!"
            p "Ага, тренировка. Конечно..."
            nag @happy "Вот именно! И никаких подозрений!"
        
        "Показать заинтересованность.":
            p "Звучит интересно! Показывай!"
            nag @grin "Вот это настрой! Тогда начинаем!"
    call nagatoro_root_show from _call_nagatoro_root_show
    scene bg nagatoro_dodjo with fade
    show nag normal_shy_battle6 with dissolve
    nag "На этом пока закончим, найди меня в лесу, и мы продолжим наши занятия!"
    nag "Можешь идти."
    "Ошеломленный ты уходишь, надеясь на развитие ваших тренировок"
    jump city
    

label nagatoro_dodjo_menu:
    menu:
        "Спортивное позирование" if nag_love >= 50: 
            call nagatoro_root_show from _call_nagatoro_root_show_1
            $nextTime()
            jump nagatoro_dodjo
        "Растираение грудными мыщцами" if nag_love >= 60: 
            call nagatoro_root_titfuck from _call_nagatoro_root_titfuck
            $nextTime()
            jump nagatoro_dodjo
        "Развитие лицевых мышц" if nag_love >= 70: 
            call nagatoro_root_blowjob from _call_nagatoro_root_blowjob
            $nextTime()
            jump nagatoro_dodjo
        "Тренировка мышц таза" if nag_love >= 80: 
            call nagatoro_root_fuck from _call_nagatoro_root_fuck
            $nextTime()
            jump nagatoro_dodjo
        "Стимулирование анальной проходимости" if nag_love >= 90: 
            call nagatoro_root_anal from _call_nagatoro_root_anal
            $nextTime()
            jump nagatoro_dodjo
        "Тренировка с доп. условиями" if nag_love >= 90: 
            call nagatoro_root_fetish from _call_nagatoro_root_fetish
            $nextTime()
            jump nagatoro_dodjo
        "Не хочу тренироваться": 
            p "Продолжим позже, сейчас у меня есть более важные дела."
            nag "Как скажешь."
            "Ты уходишь"
            jump city

label nagatoro_root_show:
    hide nag with fade 
    scene bg nag_show0 with dissolve
    "[nag.name] в спортивном костюме села напротив тебя"
    nag "Итак, [hero_name], я знаю, что ты готов, просто, мне нужно время, чтобы собраться."
    p "Начинай, я буду внимательно смотреть и запоминать позы."
    scene bg nag_show1 with dissolve
    nag "Я уже начала, а ты и не заметил, видишь, это поза лотоса."
    p "Так это все знают, покажи что-нибудь новое."
    scene bg nag_show1_2 with dissolve
    "[nag.name] немного расчачивает бедра в позе лотоса"
    p "Что ты делаешь?"
    nag "Это часть разминки, я растягиваюсь, нельзя позировать без растяжки!"
    scene bg nag_show1_3 with dissolve
    pause .3
    scene bg nag_show2 with dissolve
    "[nag.name] подняла ноги и на мгновение тебе удалось увидеть очертания ее киски через трусики"
    nag "Эй, я тут! На что это ты там смотрел?"
    p "Э-э-э, ни на что!"
    nag "Сейчас я покажу упражнение для пресса"
    scene bg nag_show2_1 with dissolve
    pause .3
    scene bg nag_show2 with dissolve
    pause .3
    scene bg nag_show2_1 with dissolve
    pause .3
    scene bg nag_show2 with dissolve
    pause .3
    scene bg nag_show2_1 with dissolve
    pause .3
    scene bg nag_show2 with dissolve
    nag "Примерно так."
    p "Никогда не знал о таком"
    mind "Как же эротично это выглядит, кажется я видел киску [nag.name] сквозь трусики, не могла же она просто так ничего не надеть кейроги? Она опять меня дразнит!"
    scene bg nag_show3 with dissolve
    p "!!!!!"
    nag "А-ах, да, видишь, благодаря тренировкам я довольно гибкая~"
    mind "Ух, какая она гибкая. Пожалуйста не меняй позу, пожалуйста не меняй позу!"
    nag "Эээй, ты чего так уставился?"
    scene bg nag_show3_1 with dissolve
    nag "Таким образом я растягиваю мышцы спины, на самом деле очень полезное упражнение!"
    "Ты одобрительно киваешь"

    scene bg nag_show3_2 with dissolve
    nag "И вот на что я способна благодаря ежедневным тренировкам, учись, [hero_name]."
    p "Удивительно!"
    mind "Удивительно, что я просто сижу и смотрю"

    scene bg nag_show4 with dissolve
    "[nag.name] села на колени, выпрямив грудь"
    nag "Ты ошибаешься, если думаешь, что у меня только растяжка хорошая!"
    p "Да? В чем же ты еще хорошая?"

    scene bg nag_show1_3 with dissolve
    nag "Во всем, например, у меня очень сильные руки."
    p "В руках я не сомневаюсь, пару раз на себе почувствовал."
    nag "Ха ха, свои грудные мышцы я тоже развивала."

    scene bg nag_show4 with dissolve
    p "Да? Что-то не видно!"
    scene bg nag_show5 with dissolve
    "[nag.name] снимает с себя топ и выставляет грудь вперед"
    p "Чт-т-т-т-ооооооо?!!!!!"
    nag "Ну так ты посмотри поближе!"
    p "А я м-м-могу п-п-потрогать?"
    nag "Ахахах, конечно нет!"
    scene bg nag_show6 with dissolve
    nag "Но ты можешь смотреть и восхищаться."
    p "Д-да, [nag.name], ты действительно потрясающая."
    p "Кхм, то есть, т-твоя фигура, т-твое физическое состояние! Оно потрясающее!"
    scene bg nag_show7 with dissolve
    nag "Правда? Смотришь только на фигуру?"
    p "Н-нееет, что ты!"
    scene bg nag_show8 with dissolve
    "[nag.name] приподнимает свою грудь"
    nag "А я считаю, что сейчас ты должен смотреть только на мою фигуру!"
    mind "Господи, что с ней? Что здесь со всеми? Откуда столько похоти в ее взгляде?"
    scene bg nag_show9_1 with dissolve
    nag "Хотя грудь и правда не самая сильная моя сторона."
    nag "Ладно, думаю этого достаточно."
    p "Ч-что? Это всё?"

    if nag_love < 55:
        $customNotify("Недостаточно симпатии")
        nag "Да, с тебя хватит, давай займемся обычными тренировками, а то что-то ты расслабился сильно."
        mind "Опять спарринг, а мне так нравилось. Наверняка если я постараюсь завоевать ее доверие - она покажет еще больше!"
        "Вы встаете, [nag.name] одевается"
        return

    nag "Нет, мы только начали, [hero_name]."
    scene bg nag_show9_2 with dissolve
    nag "Я хотела сказать, что помимо груди больше всего я вкладывала сил именно в бедренные вышцы."
    mind "О да, я мечтал об этом, каждый спарринг, каждый партер были не зря!"
    nag "Что молчишь? Неужели результаты моих тренировок настолько поражают?"
    p "Д-дааа, [nag.name], ты точно не зря старалась!"
    scene bg nag_show9_3 with dissolve
    mind "Кажется еще чуть чуть и я буду на небесах, у нее просто охуенная задница."
    nag "Ты не видел даже половины моих способностей, а я уже поразительная. Ха ха, старайся больше, [hero_name]!"
    p "Дааа, охуенная зад..."
    nag "Повтори ка?! Что ты сказал?"
    p "Я сказал... Очень привлекательная фигура!"
    scene bg nag_show9_4 with dissolve
    nag "Я так и услышала~"
    pause .3
    nag "А теперь я покажу тебе упражнение из йоги. Именно так я занимаюсь обычно."
    scene bg nag_show9_5 with dissolve
    mind "Идеальная округлая задница, кажется я вижу очертания ее ануса"
    nag "Ты как-то неправильно сидишь, сядь вот туда! Наверняка же не понимаешь, как делать эти упражнения."
    scene bg nag_show10 with dissolve
    mind "Я пересел с другого края, чтобы еще лучше видеть ее округлые части."
    nag "Эй, я же сказала сесть по другому!"
    p "Но я уже сел тут и мне всё понятно."
    nag "Ну тогда ладно~"
    scene bg nag_show11 with dissolve
    mind "[nag.name] слегка наклонилась, не думаю, что это упражнение, она точно не хотела просто показать свои прелести мне?"
    nag "Не витай в облаках, а то заставлю повторять за мной!"
    scene bg nag_show12 with dissolve
    p "!!!!!"
    mind "Я отчетливо вижу ее анус через трусики, да и она вся покраснела"
    nag "Эй, хватит пялиться, у нас тренировка, это упражнение, смотри!"
    scene bg nag_show13 with dissolve
    mind "Как же она гнется, это просто нечто"
    nag "Видишь, как важны ежедневные тренировки! Моя гибкость тебя поразила?"
    p "Да, не то слово!"
    scene bg nag_show14 with dissolve
    nag "Хочешь потрогать? Она такая мягкая и при этом упругая~"
    p "Чт-т-тооо?"
    nag "Хаха, да шучу я!"

    if nag_love < 60:
        $customNotify("Недостаточно симпатии")
        nag "Всё, на этом закончим, пора идти заниматься еще и твоими тренировками."
        mind "Опять спарринг, а мне так нравилось. Наверняка если я постараюсь завоевать ее доверие - она покажет еще больше!"
        "Вы встаете, [nag.name] одевается"
        return
    
    scene bg nag_show15 with dissolve
    nag "Мне кажется ты меня уже достаточно хорошо знаешь~"
    p "Т-точно, тебе же не нравятся одежда, смущающая движение."
    nag "В точку, [hero_name]."

    scene bg nag_show16 with dissolve
    "[nag.name] стягивает с себя трусики обнажая свою попку"
    p "[nag.name], ты отлично поработала над своей фигурой!"
    nag "Да? Посмотри на это!"

    scene bg nag_show17 with dissolve
    p "!!!!!"
    nag "Да, я тренировала сфинктер!!!"
    nag "Я не просто так показываю тебе всё это!"
    nag "Сам смотри!"

    scene bg nag_show18 with dissolve
    p "Ты проделала огромную работу! У тебя отличное тело!"
    nag "Дааа? Скажи еще что еще тебе во мне нравится, [hero_name]? Нууу же."

    scene bg nag_show19 with dissolve
    mind "Она считает, что я не замечаю того, что она чуть присела и начала мастурбировать? Она думает, что если я ношу очки, то я слепой?!"
    p "Мне н-нравится то, что ты ставишь и д-добиваешься своих целей!"
    scene bg nag_show20_2 with dissolve
    nag "Ииии?"
    p "Т-твое упорство приносит п-плоды!"
    scene bg nag_show20_3 with dissolve
    nag "Ааааах, дааааа!"
    "Ты не можешь сделать вид, что ничего не заметил"
    
    if nag_love < 70:
        $customNotify("Недостаточно симпатии")
        "Но [nag.name] может"
        scene bg nag_show19 with dissolve
        nag "Кхм... Ааах, как же я устала!"
        nag "Давай на этом закончим, пора заняться твоими тренировками."
        mind "Опять спарринг, а мне так нравилось. Наверняка если я постараюсь завоевать ее доверие - она покажет еще больше!"
        "Вы встаете, [nag.name] одевается"
        return

    nag "Ты же всё видел, да, [hero_name]?"
    p "Чт-т-тооо? Неееет, конечно нет!"
    scene bg nag_show20_4 with dissolve
    nag "А теперь? Смотри, наслаждайся!"
    "[nag.name] повенулась с тебе спиной и показала весь поток соков из ее киски"
    nag "Знаешь, что я сейчас хочу сделать?"
    "Ты сидишь и не понимаешь, что она от тебя ждет"
    
    scene bg nag_show21 with dissolve
    "[nag.name] вставляет пальчики в свой тугой анус"
    mind "Так вот, что она имела ввиду под тренировкам."
    nag "Аааах, [hero_name], смотри, не отводи вгляда!"
    "Даже если бы она просила не смотреть, у тебя бы не вышло. Ты даже не мограешь"

    scene bg nag_show22 with dissolve
    "Глаза [nag.name] закатываются от наслаждения, да и ты сам тоже уже готов взять ее прямо сейчас"
    nag "Аааах, [hero_name], смотри, смотри, это всё для тебя!"

    scene bg nag_show23 with dissolve
    "[nag.name] приподняла попку, чтобы показать тебе результат"
    "Ты видишь, как соки стекают по ее нежным бедрам и киске, от этого заводишься всё сильнее"
    
    scene bg nag_show24 with dissolve
    nag "Как тебе шоу? Понравилось же?"

    if nag_love < 90:
        $customNotify("Недостаточно симпатии")
        p "У меня нет слов!"
        scene bg nagatoro_dodjo with fade
        show nag grin_battle6 with dissolve
        nag "Ты должен был сказать, что мои достижения тебя вдохновили на большие тренировки!"
        nag "Я дала тебе столько мотивации, хаха, самое время тренировать тебя!"
        return
        
    "Ты не можешь сдержаться и набрасываешься на [nag.name]"
    nag "Ах, [hero_name], что на тебя нашло?!"
    p "Я не могу себя контролировать, прими это!"
    scene bg nag_show_anal1 with dissolve
    pause .3
    scene bg nag_show_anal2 with dissolve
    pause .3
    scene bg nag_show_anal3 with dissolve
    pause .3
    scene bg nag_show_anal4 with dissolve
    pause .3
    scene bg nag_show_anal5 with dissolve
    pause .3
    scene bg nag_show_anal4 with dissolve
    pause .3
    scene bg nag_show_anal3 with dissolve
    pause .3
    scene bg nag_show_anal4 with dissolve
    pause .3
    scene bg nag_show_anal3 with dissolve
    pause .3
    scene bg nag_show_anal4 with dissolve
    pause .3
    scene bg nag_show_anal5 with dissolve

    nag "Ааааааах, [hero_name]!"
    p "Прими это, сука!"

    scene bg nag_show_anal5_cum0 with flash
    
    nag "А-а-ааааах"
    scene bg nag_show_anal_cum1 with dissolve
    pause .5
    scene bg nag_show_anal_cum2 with dissolve
    pause .5
    scene bg nag_show_anal_cum3 with flash
    pause .2
    scene bg nag_show_anal_cum3 with flash
    pause .2
    scene bg nag_show_anal_cum3 with flash
    pause .7
    scene bg nag_show_anal_cum4 with flash
    pause .2
    scene bg nag_show_anal_cum4 with flash
    pause .2
    scene bg nag_show_anal_cum4 with flash

    p "Еще увидимся."
    "Ты одеваешься и уходишь"

    jump city

label nagatoro_root_titfuck:
    nag @grin "Уже не терпится, да?"
    hide nag grin with dissolve
    "[nag.name] вышла из комнаты"
    mind "Наверно она пошла переодеваться?"
    show nag grin_battle6 with dissolve
    "Полностью обнаженная [nag.name] вошла в комнату"
    p "!!!!!"
    nag "Не будем терять время.."
    "Ты был не в том состоянии, чтобы спорить"

    scene bg nag_titjob1 with dissolve
    "[nag.name] быстро стягивает с тебя всю одежду и садит на кровать"
    "Ты и не думаешь сопротивляться"
    mind "Я думал, что ее грудь меньше. Такое нельзя скрывать под кейроги."
    
    scene bg nag_titjob2 with dissolve
    "[nag.name] прижимается своей грудью к твоим ногам, это очень заводит"
    nag "Аааааа..."

    scene bg nag_titjob3 with dissolve
    mind "Так сразу? Просит ее \"накормить\"?"
    "Твой член еще сильнее напрягается от ее выражения лица, [nag.name] это замечает"
    
    scene bg nag_titjob4 with dissolve
    p "Ты опять издеваешься! [nag.name], я так и знал, все по лицу видно!"
    nag "Хах, может быть.."

    scene bg nag_titjob5 with dissolve
    "Ты уже напрягся до предела и не можешь держать свой член между ног"
    "Твой член выпрыгивает, слегка задевая по щеке [nag.name]"
    
    scene bg nag_titjob6 with dissolve
    nag "!!!!!"
    nag "[hero_name]! Что это такое?!"
    nag "Что за гигант!"
    
    scene bg nag_titjob7 with dissolve
    nag "Ты знал, что именно такие я люблю больше всего?~~"
    "[nag.name] прижимается грудями к твоему члену"
    p "Ах, ты так прижимаешься.."

    scene bg nag_titjob8 with dissolve
    "Теперь она прижалась личиком к твоему члену, мягко поглаживая его своей нежной кожей"
    nag "Так лучше?"
    p "Ухх.."

    scene bg nag_titjob9 with dissolve
    "Она взяла твой член у основания, готовясь к чему-то"
    nag "Ну же, что молчишь?"
    p "Д-да, так хорошо."
    nag "Тогда я сделаю еще лучше~~"
    
    scene bg nag_titjob10 with dissolve
    mind "!!!!"
    mind "Она лижет мой член!!!"

    scene bg nag_titjob11 with dissolve
    p "А-ах.."
    nag "Мммм, какой вкусный~~"

    scene bg nag_titjob12 with dissolve
    nag "Пора начинать, да, [hero_name]?"
    "[nag.name] мягко обхватила твой член грудями"
    mind "Это блаженство~"
    p "Чт-то начинать?"

    scene bg nag_titjob13 with dissolve
    "Ты чувствуешь горячее дыхание [nag.name] головкой, твой член начинает пульсировать, [nag.name] явно это заметила"
    
    scene bg nag_titjob14 with dissolve
    "Теперь она касается уздечки члена своим язычком, у тебя бегут мурашки по телу"
    nag "Тебе так нравится, [hero_name]?"

    scene bg nag_titjob16 with dissolve
    "Ты не успеваешь ответить, твой член уже почти во рту у [nag.name]"
    mind "Охх, этот взгляд, как же заводит.."

    scene bg nag_titjob16 with dissolve
    "Слюни стекают с ее языка на твой член и на ее упругие груди"
    mind "Ахх, так хорошо! Между ее грудей так скользко, тепло и приятно"
    mind "Я больше не могу держаться!"
    p "Только не сопротивляйся, [nag.name]!"
    
    scene bg nag_titjob17 with dissolve
    "Ты слегка наклоняешь голову [nag.name], чтобы головка члена оказалась у нее во рту"
    nag "Мммммффф"
    p "Ах, да, именно так, двигай язычком"
    
    scene bg nag_titjob18 with dissolve
    "[nag.name] начала активно двигать язычком"
    p "Нет, держи его во рту"
    nag "Угумфф"
    mind "Думаю она согласилась"
    
    scene bg nag_titjob19 with dissolve
    "Она прикрыла глаза, это явное согласие на то, чтобы ты ее направлял"
    
    scene bg nag_titjob20 with dissolve
    "Ты пркладываешь чуть больше усилий так, что [nag.name] почти взяла всю головку в рот"
    mind "Да, возьми побольше в свой теплый ротик"
    nag "Мммнн"
    
    scene bg nag_titjob18 with dissolve
    nag "Ах, тебе хорошо?"
    mind "Да, блять, не останавливайся!"
    p "Я уже н-на грани.."
    
    scene bg nag_titjob19 with dissolve
    pause .3
    scene bg nag_titjob20 with dissolve
    pause .3
    scene bg nag_titjob19 with dissolve
    pause .3
    scene bg nag_titjob20 with dissolve
    pause .3
    scene bg nag_titjob19 with dissolve
    pause .3
    scene bg nag_titjob20 with dissolve
    pause .2
    scene bg nag_titjob20 with flash
    pause .2
    scene bg nag_titjob20 with flash
    pause .2
    scene bg nag_titjob_cum21 with flash

    "Ты начинаешь кончать"
    
    if nag_love < 70:
        $customNotify("Недостаточно симпатии")
        "[nag.name] вырвалась"
        scene bg nagatoro_dodjo with fade
        show nag normal_shy_battle6 with dissolve
        nag "Эй, подожди, я не готова!"
        nag "Тебе лучше уйти..."
        jump city

    mind "Аргх, получай!"
    nag "ММММННННФФФФ!"

    scene bg nag_titjob_cum22 with flash
    "[nag.name] этого не ожидала"
    nag "ММММММММММННН!"

    scene bg nag_titjob_cum23 with flash
    "[nag.name] сопротивляется все сильнее, пока ты заливаешь в ее рот сперму порцию за порцией"

    if strength < nag_str:
        $customNotify("Недостаточно силы")
        "[nag.name] вырвалась из твой хватки и вздохнула воздуха"
        scene bg nagatoro_dodjo with fade
        show nag angry_cummed with dissolve
        nag "О таком нужно предупреждать!"
        nag "Я ухожу."
        $minusLove("nag", 10)
        jump city
    "Ты смог удержать порыв [nag.name]"

    scene bg nag_titjob_cum24 with flash
    "Она поняла, что сопротивляться бесполезно, ты сильнее"
    "[nag.name] смотрит на тебя умоляющим взглядом, сжимая твой пульсирующий член меж грудей"
    nag "Умммммнф~~"
    
    scene bg nag_titjob_cum25 with flash
    "Тебя это раззадорило и ты лишь сильнее вгоняешь свой член в её узенький ротик"
    "Глаза [nag.name] начали закатываться от обилия спермы"
    mind "Аргх, глотай всё, что я тебе даю!"
    
    scene bg nag_titjob_cum26 with flash
    "[nag.name] смотрит на тебя щенячьими глаза, а из ее рта брызжет спермы"
    nag "Ммммннуууу~~"

    scene bg nag_titjob_cum27 with flash
    "Ей очень тяжело, но она все еще двигает грудями дволь твоего члена, стимулируя его всё сильнее"
    p "Арргх, да, да, глотай!"

    scene bg nag_titjob_cum27 with flash
    "По щекам [nag.name] текут слезы"
    mind "Кажется она начала задыхаться..."
    nag "Ммммффрр.."
    
    scene bg nag_titjob_cum28 with flash
    "Ты даешь ей возможность вдохнуть немного воздуха, и продолжаешь обильно кончать в ее рот"

    if strength < nag_str * 1.5:
        scene bg nag_titjob_cum28_1 with flash
        "Почти сразу ты насаживаешь ее ротик обратно на свой член"
        "Грудь [nag.name] покрылась спермой, а сама она смотрит на тебя гневным взглядом"
        mind "Потерпи, [nag.name], еще немного, уххх"
        p "Уффффхх.."
        
        scene bg nag_titjob_cum28_2 with flash
        "Ты стараешься насадить ее еще сильнее на свой член, но сопротивление [nag.name] лишь растет"
        "[nag.name] старается изо всех сил, ты действительно ее разозлил"
        
        $customNotify("Недостаточно силы")
        scene bg nag_titjob_cum28_3 with flash
        "Наконец [nag.name] вырывается"
        scene bg nagatoro_dodjo with fade
        show nag angry_cummed with dissolve
        nag "Больше! Так! Не! Делай!"
        nag "Я ухожу!"
        $minusLove("nag", 10)
        jump city

    scene bg nag_titjob_cum29 with flash
    "[nag.name] смиряется, слезы ручьями текут по ее щекам, а изо рта вырываются струи своей спермы"
    mind "Вот он, взгляд полный любви и доверия~"

    scene bg nag_titjob_cum30 with flash
    "Ты отпускаешь ее голову, [nag.name] начинает жадно глотать воздух"
    "Ты не останавливаешься, продолжая заливать ее личико спермой"
    p "А-а-ааааах.."
    
    scene bg nag_titjob_cum31 with flash
    "Лицо [nag.name] покрывается твоей спермой, а сама она все еще не может надышаться"
    
    scene bg nag_titjob_cum32 with flash
    "Наконец твой член успокаивается и лишь пара струй спермы свисают с языка [nag.name]"
    p "Ты хорошо постаралась."
    
    scene bg nag_titjob_cum33 with flash
    "[nag.name] выбилась из сил и уже истощена, но, будто по привычке, она облизывает головку твоего члена, пытаясь почистить"
    
    scene bg nag_titjob_cum34 with flash
    "Но делает только хуже, рот [nag.name] переполнен спермой"
    "Ее грудь и лицо тоже полностью залиты твоим семенем"
    
    scene bg nag_titjob_cum35 with dissolve
    "Она быстро закрывает рот, чтобы не испачкать тебя еще сильнее"
    "А сама она старается сильнее обхватывать своей грудью твой член"
    "Ты наслаждаешься зрелищем"
    p "Ты молодец, [nag.name]"
    
    scene bg nag_titjob_cum36 with dissolve
    "[nag.name] будто готова расплакаться, по ее щекам текут слезы в перемешку со спермой, и даже весь ее рот переполнен твоим угощением"
    nag "Уфу фруфу?"
    p "Да, [nag.name], мне очень понравилось, ты умничка!"

    scene bg nag_titjob_cum37 with dissolve
    "Довольная [nag.name] открыла свой ротик, чтобы показать, сколько угощения ты ей оставил"
    p "Приятного аппетита, [nag.name]!"

    scene bg nag_titjob_cum36 with dissolve
    mind "Кажется она все проглотила.."
    "И это тебя очень радует"

    "Довольная [nag.name] встает"
    scene bg nagatoro_dodjo with fade
    show nag smile_cummed with dissolve
    nag "Хорошая вышла тренировка!"
    p "Да!"
    nag "А сейчас мне нужно идти. Еще увидимся, [hero_name]!"
    hide nag
    mind "Уверен она пошла в душ."
    "Полностью удовлетворенный, ты уходишь"
    jump city
    
        







