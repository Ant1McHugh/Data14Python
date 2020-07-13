class GoodDog:

    def __init__(self, name, colour, gender, age, size):     # Initialisation
        self.name = name
        self.legs = 4
        self.animal_type = "Canine"
        self.colour = colour
        self.gender = gender
        self.age = age
        self.size = size
        self._secret = "I hid my bone in the garden"
        self.__shy = "I can't catch squirrels"

    def bark(self):  # Functions in classes are called methods
        return "Woof!"

    def speak(self):
        return f"Hello Hooman!! My name is {self.name}"

    def reveal(self):  # GETTER
        return self.__shy

    def set(self, shy):  # SETTER
        self.__shy = shy

        
# Instance of the class is called an object(INSTANTIATION)

tizer = GoodDog("Tizer", "Brown", "Female", 15, "Large")

print(tizer.name)
print(tizer.colour)
print(tizer.gender)
print(tizer.age)
print(tizer.size)
print(tizer.speak())
print(tizer._secret)
print(tizer.reveal())