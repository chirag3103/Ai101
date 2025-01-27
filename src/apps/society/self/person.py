class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive = False

    def __str__(self):
        # Return a readable string representation
        return f"{self.name}, age {self.age}"

    def __repr__(self):
        # Used for debugging or development representation
        return f"Person(name={self.name}, age={self.age})"

    def birth(self):
        self.alive = True

