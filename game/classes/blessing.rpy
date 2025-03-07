init python:
    class Blessing:
        def __init__(self, name, description, grade, spell_copy=None):
            self.name = name  # Название дара
            self.description = description  # Описание дара
            self.grade = 0  # Уровень дара
            self.spell_copy = None  # Для копирования способностей

        def upgrade(self):
            if self.upgradeable:
                return f"Дар '{self.name}' улучшен!"
                # TODO дописать что при улучшении дара
            else:
                return f"Дар '{self.name}' нельзя улучшить."


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

    available_blessings = [blessing_stamina, blessing_magic, blessing_seduction, blessing_nothing]
