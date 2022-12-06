# adding methods
class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    def add_trick(self, new_trick):
        self.tricks.append(new_trick)

    def bark(self):
        print(f'{self.name} says WOOF!')

    def learn_trick(self, new_trick):
        if (new_trick not in self.tricks):
            self.tricks.append(new_trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}  ")
        else:
            print(f"{self.name} does not know {trick}  ")


otter = Dog('Lucky', 'Husky', 89756)
otter.add_trick('swim')
# otter.add_trick('jump')
# otter.add_trick('sit')
otter.bark()
otter.learn_trick('stand')
otter.learn_trick('spin')
otter.perform_trick('prat')
