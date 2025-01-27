from apps.society.family.child import Child


class Student(Child):
    def __init__(self, child):
        super().__init__(child.name, child.age, child.father, child.mother)
        self.child = child
        self.take_home_status = None

    @staticmethod
    def mark_present():
        return True

    @staticmethod
    def mark_absent():
        return False

    def prepared(self):
        return self.take_home_stats()

    def complete_take_home(self):
        # gathers score
        # help = self.ask_parent()
        # self.take_home_status = 'PENDING'
        self.take_home_status = 'COMPLETE'

    def take_home_stats(self):
        return True if self.take_home_status == 'COMPLETE' else False
