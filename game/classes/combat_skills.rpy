init python:
    # Класс для физических умений
    class CombatSkill:
        def __init__(self, name, energy_cost, effect, description, upgradeable=False):
            self.name = name  # Название умения
            self.energy_cost = energy_cost  # Стоимость энергии для использования
            self.effect = effect  # Эффект умения (например, урон)
            self.description = description  # Описание умения
            self.upgradeable = upgradeable  # Можно ли улучшать умение?

        def upgrade(self):
            if persistent.lang == "russian":
                if self.upgradeable:
                    self.effect *= 1.5  # Пример улучшения эффекта умения (например, увеличение урона)
                    self.energy_cost *= 0.9  # Пример уменьшения затрат энергии при улучшении
                    return f"Умение '{self.name}' улучшено!"
                else:
                    return f"Умение '{self.name}' нельзя улучшить."
            if persistent.lang == "english":
                if self.upgradeable:
                    self.effect *= 1.5  # Пример улучшения эффекта умения (например, увеличение урона)
                    self.energy_cost *= 0.9  # Пример уменьшения затрат энергии при улучшении
                    return f"Skill '{self.name}' was upgraded!"
                else:
                    return f"Skill '{self.name}' can't be upgraded."

    if persistent.lang == "russian":
        # Пример доступных физических умений
        punch = CombatSkill(
            name="Удар кулаком",
            energy_cost=10,
            effect=15,  # Урон
            description="Простой удар кулаком по противнику. Эффективен против слабых врагов.",
            upgradeable=True
        )

        kick = CombatSkill(
            name="Удар ногой",
            energy_cost=20,
            effect=25,
            description="Мощный удар ногой по противнику, требует больше энергии, но даёт больший урон.",
            upgradeable=True
        )

        block = CombatSkill(
            name="Блокировка",
            energy_cost=5,
            effect=0,
            description="Защита от атак противника, позволяет уменьшить получаемый урон.",
            upgradeable=False
        )
    if persistent.lang == "english":
        # Example of available physical skills
        punch = CombatSkill(
        name="Punch",
        energy_cost=10,
        effect=15, # Damage
        description="A simple punch at the enemy. Effective against weak enemies.",
        upgradeable=True
        )

        kick = CombatSkill(
        name="Kick",
        energy_cost=20,
        effect=25,
        description="A powerful kick at the enemy, requires more energy, but gives more damage.",
        upgradeable=True
        )

        block = CombatSkill(
        name="Block",
        energy_cost=5,
        effect=0,
        description="Protection from enemy attacks, allows you to reduce damage taken.",
        upgradeable=False
        )

    # Массив физических умений для главного героя
    available_combat_skills = [punch, kick, block]

    # Пример того, как создать массив для улучшенных физических умений
    # Все умения, которые будут доступны для главного героя, можно улучшать или нет, в зависимости от выбранных характеристик