init python:
    class Blessing:
        def __init__(self, name, description, grade, spell_copy=None):
            self.name = name  # Название дара
            self.description = description  # Описание дара
            self.grade = 0  # Уровень дара
            self.spell_copy = None  # Для копирования способностей

        def upgrade(self):
            if persistent.lang == "russian":
                if self.upgradeable:
                    return f"Дар '{self.name}' улучшен!"
                    # TODO дописать что при улучшении дара
                else:
                    return f"Дар '{self.name}' нельзя улучшить."
            if persistent.lang == "english":
                if self.upgradeable:
                    return f"Blessing '{self.name}' was upgraded!"
                    # TODO дописать что при улучшении дара
                else:
                    return f"Blessing '{self.name}' can't be upgraded."


    if persistent.lang == "russian":
        # Пример доступных даров (благословений)
        blessing_stamina = Blessing(
            name="Дар Выносливости",
            description="Увеличивает твою выносливость и физическую стойкость, позволяя дольше сражаться и выдерживать больше урона.",
            grade=0  #грейд
        )
        blessing_magic = Blessing(
            name="Магический Потенциал",
            description="Открывает твой магический потенциал, позволяя накапливать знания с удвоенной скоростью, использовать магию и увеличивая ману.",
            grade=0,  #грейд
            spell_copy=False # Копирования чужого заклинания
        )
        blessing_seduction = Blessing(
            name="Дар Соблазнителя",
            description="Увеличивает твою харизму и магнетизм, позволяя влиять на людей и манипулировать ими.",
            grade=0  #грейд
        )

        blessing_nothing = Blessing(
            name="Дар свободы", #от линейного сюжета
            description="Ничего не увеличивает, лишь делает жизнь немного сложнее.",
            grade=0  #грейд
        )
    if persistent.lang == "english":
        # Пример доступных даров (благословений)
        blessing_stamina = Blessing(
        name="Gift of Endurance",
        description="Increases your stamina and physical endurance, allowing you to fight longer and withstand more damage.",
        grade=0 #grade
        )
        blessing_magic = Blessing(
        name="Magic Potential",
        description="Unlocks your magical potential, allowing you to accumulate knowledge at double the speed, use magic and increase mana.",
        grade=0, #grade
        spell_copy=False # Copy someone else's spell
        )
        blessing_seduction = Blessing(
        name="Gift of the Seducer",
        description="Increases your charisma and magnetism, allowing you to influence and manipulate people.",
        grade=0 #grade
        )

        blessing_nothing = Blessing(
        name="Gift of Freedom", #from the linear plot
        description="Doesn't increase anything, just makes life a little more difficult.", 
        grade=0 #grade
        )

    available_blessings = [blessing_stamina, blessing_magic, blessing_seduction, blessing_nothing]
