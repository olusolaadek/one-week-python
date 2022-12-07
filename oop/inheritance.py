class Cat:
    def __init__(self, name) -> None:
        print("INSIDE CAT INIT")
        self.name = name

    def meow(self):
        print(f"{self.name} meows")


class Lion(Cat):
    def __init__(self, name, pride_name='xyz') -> None:
        print("INSIDE LION INIT")
        super().__init__(name)
        self.name = name
        self.pride_name = pride_name

    def roar(self):
        print(f'{self.name} roars ')

    def to_string(self):
        print(f"Name: {self.name}, Pride Name: {self.pride_name}  ")

        # test
# elsa = Cat('Elsa')
# elsa.meow()


lion = Lion('Jungler', 'king of Orb')

lion.meow()
lion.roar()
lion.to_string()
