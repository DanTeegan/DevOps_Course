# OOP - 4 pillars of OOP

# Inheritence
# Polymorphism
# Encapsulation
# Abstraction

#Here we are creating the class called "Dog"
class Dog:
    animal_kind = "canine" # class variable

    def __init__(self, name, color): # Initializing the class
        self.name = name
        self.color = color

    # Here we are creating the method of barking
    def bark(self): # Method variable inside the class
        return "Woof Woof"

    # Here we are creating the method of sleeping
    def sleep(self):
        return "ZzZzZzZz"

    # Here we are creating the method of breathing
    def breath(self):
        return "*Breathing*"

    # Here we are creating the method of running
    def run(self):
        return "Wouuuuf wuuuuf"

    # Here we are creating the method of eating
    def eat(self):
        return "NoM NoM NoM"




fido = Dog("canine", "white") # Creating an object of our class

print(fido.color) # Printing an attribute of our class

lucy = Dog("lucy", "brown")
print(lucy.color)

# Create a method inside for sleep, breath, run, eat