
# Parent class
class Animal :
    def speak(self):
        print("Animal is speaking")

class Dog(Animal) :
    def bark(self):
        print("Dog is barking")

class Cat(Dog) :
    def purr(self):
        print("Cat is purring")

class Lion(Animal) :
    def roar(self):
       print("Lion is roaring")

a = Animal()
d = Dog()
c = Cat()
c.speak()