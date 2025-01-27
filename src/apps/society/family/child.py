from apps.society.self.person import Person


class Child(Person):
    def __init__(self, name, age, father, mother):
        super().__init__(name, age)
        self.father = father
        self.mother = mother
        self.take_home_status = None

    @staticmethod
    def ask_parent(coach_parent):
        # Logic to decide which parent to ask, temp criteria greaterThan <age> (only father passes)
        return coach_parent.help_with_exam() if coach_parent.age < 30 else False
