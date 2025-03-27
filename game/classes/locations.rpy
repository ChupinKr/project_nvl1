init python:
    class Location:
        def __init__(self, tag, name, canVisit):
            self.tag = tag  # Название локации
            self.name = name  # Название локации
            self.canVisit = canVisit  # Возможность посетить

    class LocList:
        def __init__(self):
            if persistent.lang == "russian":
                self.list = [
                    Location(tag="city",name="Город", canVisit=True),
                    Location(tag="forest",name="Лес", canVisit=True),
                    Location(tag="rt",name="Разрушенный храм", canVisit=True),
                    Location(tag="market",name="Городской рынок", canVisit=True),
                    Location(tag="bm",name="Черный рынок", canVisit=False),
                    Location(tag="tavern",name="Таверна", canVisit=False),
                    Location(tag="room",name="Моя комната", canVisit=False),
                    Location(tag="hospital",name="Больница", canVisit=False),
                    Location(tag="surgency",name="Хирургия", canVisit=False),
                    Location(tag="bar",name="Бар", canVisit=False),
                    Location(tag="brothel",name="Бордель", canVisit=False),
                    Location(tag="mt",name="Магическая башня", canVisit=False),
                    Location(tag="lib",name="Библиотека", canVisit=False),
                    Location(tag="guild",name="Гильдия", canVisit=False),
                    Location(tag="tg",name="Тренировочная площадка", canVisit=False)
                ]
            if persistent.lang == "english":
                self.list = [
                    Location(tag="city",name="City", canVisit=True),
                    Location(tag="forest",name="Forest", canVisit=True),
                    Location(tag="rt",name="Ruined Temple", canVisit=True),
                    Location(tag="market",name="City Market", canVisit=True),
                    Location(tag="bm",name="Black Market", canVisit=False),
                    Location(tag="tavern",name="Tavern", canVisit=False),
                    Location(tag="room",name="My Room", canVisit=False),
                    Location(tag="hospital",name="Hospital", canVisit=False),
                    Location(tag="surgency",name="Surgery", canVisit=False),
                    Location(tag="bar",name="Bar", canVisit=False),
                    Location(tag="brothel",name="Brothel", canVisit=False),
                    Location(tag="mt",name="Magic Tower", canVisit=False),
                    Location(tag="lib",name="Library", canVisit=False),
                    Location(tag="guild",name="Guild", canVisit=False),
                    Location(tag="tg",name="Training Ground", canVisit=False)
                ]
        
        def getLocByTag(self, tag):
            for loc in self.list:
                if(tag == loc.tag):
                    return loc

        def setVisit(self, tag, canVisit):
            global notices
            if self.getLocByTag(tag).canVisit != canVisit:
                self.getLocByTag(tag).canVisit = canVisit
                if persistent.lang == "russian":
                    if canVisit:
                        notices.append("Теперь вам доступна локация "+ self.getLocByTag(tag).name)
                    else:
                        notices.append("Теперь вам недоступна локация "+ self.getLocByTag(tag).name)
                if persistent.lang == "english":
                    if canVisit:
                        notices.append("You can now access location "+ self.getLocByTag(tag).name)
                    else:
                        notices.append("You can now access location "+ self.getLocByTag(tag).name)

                renpy.show_screen('notify_plus', notices=notices)
                notices = []
                return True
            else:
                return False
    
    all_locs = LocList()


    def canVisit(locationtag):
        return all_locs.getLocByTag(locationtag).canVisit

    def updateCanVisit(locationtag, canVisit):
        return all_locs.setVisit(locationtag,canVisit)


label steps_sound:
    play sound "audio/steps.ogg"
return

label forest_scene:
    call forest_scene_music
    $setLocation("forest")
    if isMorning():
        scene bg forest_morning with fade
    elif isDay():
        scene bg forest_day with fade
    elif isEvening():
        scene bg forest_evening with fade
    elif isNight():
        scene bg forest_night with fade
    else:
        scene bg forest_day with fade
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
        scene bg forest_day with fade
    return

label tavern_scene:
    $setLocation("tavern")
    play sound "audio/steps.ogg"
    if renpy.music.get_playing("music") != "audio/tavern_music.ogg":
        play music "audio/tavern_music.ogg" fadein 5.0 loop
    if isMorning():
        scene bg tavern_morning with fade
    elif isDay():
        scene bg tavern_day with fade
    elif isEvening():
        scene bg tavern_evening with fade
    elif isNight():
        scene bg tavern_night with fade
    else:
        scene bg tavern_day with fade
    return

label city_scene(bgc = None):
    $setLocation("city")
    play sound "audio/steps.ogg"
    if bgc:
        if bgc == "morning":
            if renpy.music.get_playing("music") != "audio/city_day.ogg":
                play music "audio/city_day.ogg" fadein 5.0 loop
            scene bg city_morning with fade
        elif bgc == "day":
            if renpy.music.get_playing("music") != "audio/city_day.ogg":
                play music "audio/city_day.ogg" fadein 5.0 loop
            scene bg city_day with fade
        elif bgc == "evening":
            if renpy.music.get_playing("music") != "audio/city_night.ogg":
                play music "audio/city_night.ogg" fadein 5.0 loop
            scene bg city_evening with fade
        elif bgc == "night":
            if renpy.music.get_playing("music") != "audio/city_night.ogg":
                play music "audio/city_night.ogg" fadein 5.0 loop
            scene bg city_night with fade
        return
    if isMorning():
        if renpy.music.get_playing("music") != "audio/city_day.ogg":
            play music "audio/city_day.ogg" fadein 5.0 loop
        scene bg city_morning with fade
    elif isDay():
        if renpy.music.get_playing("music") != "audio/city_day.ogg":
            play music "audio/city_day.ogg" fadein 5.0 loop
        scene bg city_day with fade
    elif isEvening():
        if renpy.music.get_playing("music") != "audio/city_night.ogg":
            play music "audio/city_night.ogg" fadein 5.0 loop
        scene bg city_evening with fade
    elif isNight():
        if renpy.music.get_playing("music") != "audio/city_night.ogg":
            play music "audio/city_night.ogg" fadein 5.0 loop
        scene bg city_night with fade
    else:
        scene bg city_day with fade
    return

label market_scene:
    $setLocation("market")
    play sound "audio/steps.ogg"
    if isMorning():
        scene bg market_morning with fade
    elif isDay():
        scene bg market_day with fade
    elif isEvening():
        scene bg market_evening with fade
    elif isNight():
        scene bg market_night with fade
    else:
        scene bg market_day with fade
    return

label ruined_temple_scene:
    $setLocation("ruined_temple")
    if isMorning():
        scene bg ruined_temple_morning with fade
    elif isDay():
        scene bg ruined_temple_day with fade
    elif isEvening():
        scene bg ruined_temple_evening with fade
    elif isNight():
        scene bg ruined_temple_night with fade
    else:
        scene bg ruined_temple_day with fade
    return

label training_ground_scene:
    $setLocation("tg")
    if renpy.music.get_playing("music") != "audio/tg_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/tg_sound.ogg" fadein 5.0 loop
    if isMorning():
        scene bg training_ground_morning with fade
    elif isDay():
        scene bg training_ground_day with fade
    elif isEvening():
        scene bg training_ground_evening with fade
    elif isNight():
        scene bg training_ground_night with fade
    else:
        scene bg training_ground_day with fade
    return

label magic_tower_scene:
    $setLocation("mt")
    play sound "audio/steps.ogg"
    if renpy.music.get_playing("music") != "audio/mt_sound.ogg":
        play music "audio/mt_sound.ogg" fadein 5.0 loop
    scene bg magic_tower with fade
    return

label tower_training_scene:
    $setLocation("tower_training")
    if renpy.music.get_playing("music") != "audio/mt_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/mt_sound.ogg" fadein 5.0 loop
    scene bg tower_training with fade
    return

label ice_caves_scene:
    $setLocation("ice_caves")
    play sound "audio/steps.ogg"
    if renpy.music.get_playing("music") != "audio/arctic_wind.ogg":
        play music "audio/arctic_wind.ogg" fadein 5.0 loop
    scene bg ice_caves at Transform(zoom=1.5) with fade
    return

label hospital_scene:
    $setLocation("hospital")
    if renpy.music.get_playing("music") != "audio/hospital_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/hospital_sound.ogg" fadein 5.0 loop
    scene bg hospital with fade
    return

label haven_scene:
    $setLocation("haven")
    if renpy.music.get_playing("music") != "audio/haven.ogg":
        play sound "audio/magic_dissapear.ogg"
        play music "audio/haven.ogg" fadein 5.0 loop
    scene bg haven with fade
    return

label surgency_scene:
    $setLocation("surgency")
    if renpy.music.get_playing("music") != "audio/surgency.ogg":
        play sound "audio/steps.ogg"
        play music "audio/surgency.ogg" fadein 5.0 loop
    scene bg surgery with fade
    return

label brothel_scene:
    $setLocation("brothel")
    if renpy.music.get_playing("music") != "audio/brothel_sound.ogg":
        play sound "audio/door_enter.ogg"
        play music "audio/brothel_sound.ogg" fadein 5.0 loop
    $ girl = renpy.random.randint(1, 100)
    if girl < 20:
        scene bg brothel_girl1 with fade
    if girl >= 20 and girl < 40:
        scene bg brothel_girl2 with fade
    if girl >= 40 and girl < 60:
        scene bg brothel_girl3 with fade
    if girl >= 60 and girl < 80:
        scene bg brothel_girl4 with fade
    if girl >= 80 and girl < 100:
        scene bg brothel_girl5 with fade
    return

label room_scene:
    $setLocation("room")
    if renpy.music.get_playing("music") != "audio/room_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/room_sound.ogg" fadein 5.0 loop
    scene bg room with fade
    return

label guild_scene:
    $setLocation("guild")
    if renpy.music.get_playing("music") != "audio/guild_sound.ogg":
        play sound "audio/steps.ogg"
        play music "audio/guild_sound.ogg" fadein 5.0 loop
    scene bg guild with fade
    return

label dodjo_scene:
    $setLocation("dodjo")
    if renpy.music.get_playing("music") != "audio/dodjo_music.ogg":
        play sound "audio/steps.ogg"
        play music "audio/dodjo_music.ogg" fadein 5.0 loop
    scene bg nagatoro_dodjo with fade
    return

    
label dark_forest_scene:
    $setLocation("dark_forest")
    if renpy.music.get_playing("music") != "audio/forest_evening_night_music.ogg":
        play sound "audio/steps.ogg"
        play music "audio/forest_evening_night_music.ogg" fadein 5.0 loop
    scene bg dark_forest with fade
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