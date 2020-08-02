class Dog:

    animal_kind = "canine" # class variable - dangerous

    def bark(self):
        self.animal_kind # Method variable inside the class
        return "Woof Woof Woof"

    def eat(self, eat):
        self.eat = eat

fido = dog() # instantiating our class/creating an object
lucy = dog()

print(lucy.animal_kind)
print(fido.animal_kind)
print(fido.bark())

fido.animal_kind = "fish"
print(fido.animal_kind)