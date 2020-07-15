class Animal:

    def __init__(self):
        self._hunger = 5
        print("I exist.")

    def eat(self):
        print("NOM")
        self._hunger -= 3


class Mammal(Animal):

    def breed(self):
        print("I procreated!")
        self._hunger += 5


class Dog(Mammal):

    def woof(self):
        print("Woof!")
        self._hunger += 1


class Husky(Dog):

    def pull(self):
        print("I pull the sledge!")
        self._hunger += 4



my_dog = Husky()
my_dog.pull()
my_dog.eat()
