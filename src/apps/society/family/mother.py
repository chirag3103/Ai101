from apps.society.family.parent import Parent


class Mother(Parent):
    def __init__(self, name):
        super().__init__()
        self.name = name