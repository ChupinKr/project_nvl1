init python:
    class Location:
        def __init__(self, tag, name):
            self.tag = tag  # Название локации
            self.name = name  # Название локации

    def getLocByTag(locList, tag):
        for loc in locList:
            if(tag == loc.tag):
                return loc

    def getLocCanVisitByTag(tag):
        global city_canVisit, forest_canVisit, rt_canVisit, market_canVisit, bm_canVisit
        global tavern_canVisit, room_canVisit, room_canVisit, hospital_canVisit, surgency_canVisit
        global brothel_canVisit, mt_canVisit, lib_canVisit, guild_canVisit, tg_canVisit
        if(tag == "tavern"):
            return tavern_canVisit
        if(tag == "city"):
            return city_canVisit
        if(tag == "forest"):
            return forest_canVisit
        if(tag == "rt"):
            return rt_canVisit
        if(tag == "market"):
            return market_canVisit
        if(tag == "bm"):
            return bm_canVisit
        if(tag == "room"):
            return room_canVisit
        if(tag == "hospital"):
            return hospital_canVisit
        if(tag == "surgency"):
            return surgency_canVisit
        if(tag == "brothel"):
            return brothel_canVisit
        if(tag == "mt"):
            return mt_canVisit
        if(tag == "lib"):
            return lib_canVisit
        if(tag == "guild"):
            return guild_canVisit
        if(tag == "tg"):
            return tg_canVisit
        return False

    def setCanVisitByTag(tag, canVisit):
        global city_canVisit, forest_canVisit, rt_canVisit, market_canVisit, bm_canVisit
        global tavern_canVisit, room_canVisit, room_canVisit, hospital_canVisit, surgency_canVisit
        global brothel_canVisit, mt_canVisit, lib_canVisit, guild_canVisit, tg_canVisit
        if(tag == "tavern"):
            tavern_canVisit = canVisit
        if(tag == "city"):
            city_canVisit = canVisit
        if(tag == "forest"):
            forest_canVisit = canVisit
        if(tag == "rt"):
            rt_canVisit = canVisit
        if(tag == "market"):
            market_canVisit = canVisit
        if(tag == "bm"):
            bm_canVisit = canVisit
        if(tag == "room"):
            room_canVisit = canVisit
        if(tag == "hospital"):
            hospital_canVisit = canVisit
        if(tag == "surgency"):
            surgency_canVisit = canVisit
        if(tag == "brothel"):
            brothel_canVisit = canVisit
        if(tag == "mt"):
            mt_canVisit = canVisit
        if(tag == "lib"):
            lib_canVisit = canVisit
        if(tag == "guild"):
            guild_canVisit = canVisit
        if(tag == "tg"):
            tg_canVisit = canVisit
        return

    def setVisit(tag, canVisit):
        global notices, locList
        if getLocCanVisitByTag(tag) != canVisit:
            setCanVisitByTag(tag, canVisit)
            if persistent.lang == "russian":
                if canVisit:
                    notices.append("Теперь вам доступна локация "+ getLocByTag(locList, tag).name)
                else:
                    notices.append("Теперь вам недоступна локация "+ getLocByTag(locList, tag).name)
            if persistent.lang == "english":
                if canVisit:
                    notices.append("You can now access location "+ getLocByTag(locList, tag).name)
                else:
                    notices.append("You can now access location "+ getLocByTag(locList, tag).name)

            renpy.show_screen('notify_plus', notices=notices)
            notices = []
            return True
        else:
            return False

    def canVisit(locationTag):
        return getLocCanVisitByTag(locationTag)

    def updateCanVisit(locListLocationTag, canVisit):
        return setVisit(locListLocationTag, canVisit)

define locList = []
define city_canVisit = True
define forest_canVisit = True
define rt_canVisit = True
define market_canVisit = True
define bm_canVisit = False
define room_canVisit = False
define hospital_canVisit = False
define surgency_canVisit = False
define brothel_canVisit = False
define mt_canVisit = False
define lib_canVisit = False
define guild_canVisit = False
define tg_canVisit = False
define tavern_canVisit = False

init:
    if persistent.lang == "russian":
        $locList = [
            Location(tag="city",name="Город"),
            Location(tag="forest",name="Лес"),
            Location(tag="rt",name="Разрушенный храм"),
            Location(tag="market",name="Городской рынок"),
            Location(tag="bm",name="Черный рынок"),
            Location(tag="tavern",name="Таверна"),
            Location(tag="room",name="Моя комната"),
            Location(tag="hospital",name="Больница"),
            Location(tag="surgency",name="Хирургия"),
            Location(tag="brothel",name="Бордель"),
            Location(tag="mt",name="Магическая башня"),
            Location(tag="lib",name="Библиотека"),
            Location(tag="guild",name="Гильдия"),
            Location(tag="tg",name="Тренировочная площадка")
        ]
    if persistent.lang == "english":
        $locList = [
            Location(tag="city",name="City"),
            Location(tag="city",name="City"),
            Location(tag="forest",name="Forest"),
            Location(tag="rt",name="Ruined Temple"),
            Location(tag="market",name="City Market"),
            Location(tag="bm",name="Black Market"),
            Location(tag="tavern",name="Tavern"),
            Location(tag="room",name="My Room"),
            Location(tag="hospital",name="Hospital"),
            Location(tag="surgency",name="Surgery"),
            Location(tag="brothel",name="Brothel"),
            Location(tag="mt",name="Magic Tower"),
            Location(tag="lib",name="Library"),
            Location(tag="guild",name="Guild"),
            Location(tag="tg",name="Training Ground")
        ]


label steps_sound:
    play sound "audio/steps.ogg"
return

label sand_steps_sound:
    play sound "audio/sand_steps.ogg"
return

label forest_scene:
    call forest_scene_music
    $setLocation("forest")
    if isMorning():
        scene bg forest_morning at bg_size with fade
    elif isDay():
        scene bg forest_day at bg_size with fade
    elif isEvening():
        scene bg forest_evening at bg_size with fade
    elif isNight():
        scene bg forest_night at bg_size with fade
    else:
        scene bg forest_day at bg_size with fade
    return
    
label forest_scene_music:
    if isMorning():
        if renpy.music.get_playing("music") != "audio/forest_day_morning_music.ogg":
            play music "audio/forest_day_morning_music.ogg" fadein 5.0 loop
    elif isDay():
        if renpy.music.get_playing("music") != "audio/forest_day_morning_music.ogg":
            play music "audio/forest_day_morning_music.ogg" fadein 5.0 loop
    elif isEvening():
        if renpy.music.get_playing("music") != "audio/forest_evening_night_music.ogg":
            play music "audio/forest_evening_night_music.ogg" fadein 5.0 loop
    elif isNight():
        if renpy.music.get_playing("music") != "audio/forest_evening_night_music.ogg":
            play music "audio/forest_evening_night_music.ogg" fadein 5.0 loop
    else:
        if renpy.music.get_playing("music") != "audio/forest_day_morning_music.ogg":
            play music "audio/forest_day_morning_music.ogg" fadein 5.0 loop
    return

label tavern_scene:
    $setLocation("tavern")
    play sound "audio/steps.ogg"
    if renpy.music.get_playing("music") != "audio/tavern_music.ogg":
        play music "audio/tavern_music.ogg" fadein 5.0 loop
    if isMorning():
        scene bg tavern_morning at bg_size with fade
    elif isDay():
        scene bg tavern_day at bg_size with fade
    elif isEvening():
        scene bg tavern_evening at bg_size with fade
    elif isNight():
        scene bg tavern_night at bg_size with fade
    else:
        scene bg tavern_day at bg_size with fade
    return

label city_scene(bgc = None):
    $setLocation("city")
    play sound "audio/steps.ogg"
    call city_music_scene
    if bgc:
        if bgc == "morning":
            scene bg city_morning at bg_size with fade
        elif bgc == "day":
            scene bg city_day at bg_size with fade
        elif bgc == "evening":
            scene bg city_evening at bg_size with fade
        elif bgc == "night":
            scene bg city_night at bg_size with fade
        return
    if isMorning():
        scene bg city_morning at bg_size with fade
    elif isDay():
        scene bg city_day at bg_size with fade
    elif isEvening():
        scene bg city_evening at bg_size with fade
    elif isNight():
        scene bg city_night at bg_size with fade
    else:
        scene bg city_day at bg_size with fade
    return

label city_scene_bg():
    $setLocation("city")
    call city_music_scene
    if isMorning():
        scene bg city_morning at bg_size with fade
    elif isDay():
        scene bg city_day at bg_size with fade
    elif isEvening():
        scene bg city_evening at bg_size with fade
    elif isNight():
        scene bg city_night at bg_size with fade
    else:
        scene bg city_day at bg_size with fade
    return

label city_music_scene(bgc = None):
    if bgc:
        if bgc == "morning":
            if renpy.music.get_playing("music") != "audio/city_day.ogg":
                play music "audio/city_day.ogg" fadein 5.0 loop
        elif bgc == "day":
            if renpy.music.get_playing("music") != "audio/city_day.ogg":
                play music "audio/city_day.ogg" fadein 5.0 loop
        elif bgc == "evening":
            if renpy.music.get_playing("music") != "audio/city_night.ogg":
                play music "audio/city_night.ogg" fadein 5.0 loop
        elif bgc == "night":
            if renpy.music.get_playing("music") != "audio/city_night.ogg":
                play music "audio/city_night.ogg" fadein 5.0 loop
        return
    if isMorning():
        if renpy.music.get_playing("music") != "audio/city_day.ogg":
            play music "audio/city_day.ogg" fadein 5.0 loop
    elif isDay():
        if renpy.music.get_playing("music") != "audio/city_day.ogg":
            play music "audio/city_day.ogg" fadein 5.0 loop
    elif isEvening():
        if renpy.music.get_playing("music") != "audio/city_night.ogg":
            play music "audio/city_night.ogg" fadein 5.0 loop
    elif isNight():
        if renpy.music.get_playing("music") != "audio/city_night.ogg":
            play music "audio/city_night.ogg" fadein 5.0 loop
    return

label market_scene:
    $setLocation("market")
    play sound "audio/steps.ogg"
    call city_music_scene
    if isMorning():
        scene bg market_morning at bg_size with fade
    elif isDay():
        scene bg market_day at bg_size with fade
    elif isEvening():
        scene bg market_evening at bg_size with fade
    elif isNight():
        scene bg market_night at bg_size with fade
    else:
        scene bg market_day at bg_size with fade
    return

label black_alley_scene:
    $setLocation("black_alley")
    play sound "audio/steps.ogg"
    call city_music_scene
    if isMorning():
        scene bg market_morning at bg_size with fade
    elif isDay():
        scene bg market_day at bg_size with fade
    elif isEvening():
        scene bg market_evening at bg_size with fade
    elif isNight():
        scene bg black_alley_night at bg_size with fade
    else:
        scene bg black_alley_night at bg_size with fade
    return

label ruined_temple_scene:
    $setLocation("ruined_temple")
    if isMorning():
        scene bg ruined_temple_morning at bg_size with fade
    elif isDay():
        scene bg ruined_temple_day at bg_size with fade
    elif isEvening():
        scene bg ruined_temple_evening at bg_size with fade
    elif isNight():
        scene bg ruined_temple_night at bg_size with fade
    else:
        scene bg ruined_temple_day at bg_size with fade
    return

label training_ground_scene:
    $setLocation("tg")
    if renpy.music.get_playing("music") != "audio/tg_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/tg_sound.ogg" fadein 5.0 loop
    if isMorning():
        scene bg training_ground_morning at bg_size with fade
    elif isDay():
        scene bg training_ground_day at bg_size with fade
    elif isEvening():
        scene bg training_ground_evening at bg_size with fade
    elif isNight():
        scene bg training_ground_night at bg_size with fade
    else:
        scene bg training_ground_day at bg_size with fade
    return

label magic_tower_scene:
    $setLocation("mt")
    play sound "audio/steps.ogg"
    if renpy.music.get_playing("music") != "audio/mt_sound.ogg":
        play music "audio/mt_sound.ogg" fadein 5.0 loop
    scene bg magic_tower at bg_size with fade
    return

label tower_training_scene:
    $setLocation("tower_training")
    if renpy.music.get_playing("music") != "audio/mt_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/mt_sound.ogg" fadein 5.0 loop
    scene bg tower_training at bg_size with fade
    return

label ice_caves_scene:
    $setLocation("ice_caves")
    play sound "audio/steps.ogg"
    if renpy.music.get_playing("music") != "audio/arctic_wind.ogg":
        play music "audio/arctic_wind.ogg" fadein 5.0 loop
    scene bg ice_caves at bg_size with fade
    return

label hospital_scene:
    $setLocation("hospital")
    if renpy.music.get_playing("music") != "audio/hospital_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/hospital_sound.ogg" fadein 5.0 loop
    scene bg hospital at bg_size with fade
    return

label haven_scene:
    $setLocation("haven")
    if renpy.music.get_playing("music") != "audio/haven.ogg":
        call magic_dissapear
        play music "audio/haven.ogg" fadein 5.0 loop
    scene bg haven at bg_size with fade
    return

label magic_dissapear:
    play sound "audio/magic_dissapear.ogg"
    return

label surgency_scene:
    $setLocation("surgency")
    if renpy.music.get_playing("music") != "audio/surgency.ogg":
        play sound "audio/steps.ogg"
        play music "audio/surgency.ogg" fadein 5.0 loop
    scene bg surgery at bg_size with fade
    return

label brothel_scene:
    $setLocation("brothel")
    if renpy.music.get_playing("music") != "audio/brothel_sound.ogg":
        play sound "audio/door_enter.ogg"
        play music "audio/brothel_sound.ogg" fadein 5.0 loop
    $ girl = renpy.random.randint(1, 100)
    if girl < 20:
        scene bg brothel_girl1 at bg_size with fade
    if girl >= 20 and girl < 40:
        scene bg brothel_girl2 at bg_size with fade
    if girl >= 40 and girl < 60:
        scene bg brothel_girl3 at bg_size with fade
    if girl >= 60 and girl < 80:
        scene bg brothel_girl4 at bg_size with fade
    if girl >= 80 and girl < 100:
        scene bg brothel_girl5 at bg_size with fade
    return

label room_scene:
    $setLocation("room")
    if renpy.music.get_playing("music") != "audio/room_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/room_sound.ogg" fadein 5.0 loop
    scene bg room at bg_size with fade
    return

label guild_scene:
    $setLocation("guild")
    if renpy.music.get_playing("music") != "audio/guild_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/guild_sound.ogg" fadein 5.0 loop
    scene bg guild at bg_size with fade
    return

label dodjo_scene:
    $setLocation("dodjo")
    if renpy.music.get_playing("music") != "audio/dodjo_music.ogg":
        play sound "audio/steps.ogg"
        play music "audio/dodjo_music.ogg" fadein 5.0 loop
    scene bg nagatoro_dodjo at bg_size with fade
    return

    
label dark_forest_scene:
    $setLocation("dark_forest")
    if renpy.music.get_playing("music") != "audio/forest_evening_night_music.ogg":
        play sound "audio/steps.ogg"
        play music "audio/forest_evening_night_music.ogg" fadein 5.0 loop
    scene bg dark_forest at bg_size with fade
    return
    
label village_scene:
    $setLocation("village")
    play sound "audio/steps.ogg"
    if isMorning():
        if renpy.music.get_playing("music") != "audio/forest_day_morning_music.ogg":
            play music "audio/forest_day_morning_music.ogg" fadein 5.0 loop
        scene bg village_day at bg_size with fade
    elif isDay():
        if renpy.music.get_playing("music") != "audio/forest_day_morning_music.ogg":
            play music "audio/forest_day_morning_music.ogg" fadein 5.0 loop
        scene bg village_day at bg_size with fade
    elif isEvening():
        if renpy.music.get_playing("music") != "audio/forest_evening_night_music.ogg":
            play music "audio/forest_evening_night_music.ogg" fadein 5.0 loop
        scene bg village_night at bg_size with fade
    elif isNight():
        if renpy.music.get_playing("music") != "audio/forest_evening_night_music.ogg":
            play music "audio/forest_evening_night_music.ogg" fadein 5.0 loop
        scene bg village_night at bg_size with fade
    else:
        if renpy.music.get_playing("music") != "audio/forest_day_morning_music.ogg":
            play music "audio/forest_day_morning_music.ogg" fadein 5.0 loop
        scene bg village_day at bg_size with fade
    return
    
label river_scene_music:
    if renpy.music.get_playing("music") != "audio/river_music.ogg":
        play music "audio/river_music.ogg" fadein 1.0 loop
    return
    
label cave_scene_music:
    if renpy.music.get_playing("music") != "audio/cave_music.ogg":
        play music "audio/cave_music.ogg" fadein 1.0 loop
    return
    
label dance_scene:
    $setLocation("club")
    call dance_scene_music
    scene bg city_dance at bg_size with fade
    return

label dance_scene_music:
    if renpy.music.get_playing("music") != "audio/brothel_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/brothel_sound.ogg" fadein 1.0 loop
    return

label brothel_bass_sound:
    if renpy.music.get_playing("music") != "audio/brothel_sound_bass.ogg":
        play sound "audio/door_enter.ogg"
        play music "audio/brothel_sound_bass.ogg" fadein 5.0 loop
    return

label door_enter_sound:
    play sound "audio/door_enter.ogg"
    return

label battle_music:
    if renpy.music.get_playing("music") != "audio/fight.ogg":
        play music "audio/fight.ogg" fadein 1.0 loop
    return

label battle_music_stop:
    if renpy.music.get_playing("music") == "audio/fight.ogg":
        stop music fadeout 1.0
    return

label magic_wind_music:
    if renpy.music.get_playing("music") != "audio/magic_portal_music.ogg":
        play music "audio/magic_portal_music.ogg" fadein 1.0
    return

label desert_wind_music:
    if renpy.music.get_playing("music") != "audio/desert_wind.ogg":
        play music "audio/desert_wind.ogg" fadein 1.0
    return