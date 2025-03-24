init python:
    # Класс для умений соблазнения
    class SeductionSkill:
        def __init__(self, name, effect):
            self.name = name  # Название умения
            self.effect = effect  # Эффект умения
    if persistent.lang == "russian":
        # Массив всех умений для соблазнения
        seduction_skills = [
            SeductionSkill("Очарование", "Увеличивает привлекательность, делает собеседника более восприимчивым."),
            SeductionSkill("Манипуляция", "Позволяет влиять на эмоции и поведение окружающих."),
            SeductionSkill("Флирт", "Показывает свою сексуальную привлекательность, заставляя собеседника терять бдительность.")
        ]
    if persistent.lang == "english":
        # Массив всех умений для соблазнения
        seduction_skills = [
            SeductionSkill("Charm", "Increases attractiveness, makes the interlocutor more receptive."),
            SeductionSkill("Manipulation", "Allows you to influence the emotions and behavior of others."),
            SeductionSkill("Flirt", "Shows off your sexual attractiveness, making the interlocutor lose their vigilance.")
        ]