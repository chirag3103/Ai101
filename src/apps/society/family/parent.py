from apps.society.self.person import Person


class Parent(Person):
    def __init__(self, person):
        super().__init__(person.name, person.age)
        self.parent_status = 'AVAILABLE'

    def help_with_exam(self):
        # Temp logic for being able to help a child with an exam
        return True if self.parent_status == 'AVAILABLE' else False
