# single inheritance
class Animal(object):
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")
        
d = Dog()
d.whoAmI()
d.bark()
d.eat()
        

# multiple inheritance
class Animal(object):
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self, name = 'No name'):
        Animal.__init__(self)
        self.name = name
        print("Dog is created with name", self.name)

    def whoAmI(self, name):
        self.name = name
        print("Dog's name is", self.name)

    def bark(self):
        print(self.name,"is barking - Woof!")
        
class Cat(Animal):
    def __init__(self, name = 'No name'):
        Animal.__init__(self)
        print("Cat is created")
        self.name = name
        print("Cat is created with name", self.name)
        
    def whoAmI(self, name):
        self.name = name
        print("Cat's name is", self.name)
        
    def meow(self):
        print(self.name,"Cat is meowing - meow!")

d = Dog()
d.whoAmI('Sam')
d.bark()

c = Cat()
c.whoAmI('Chester')
c.meow()

# multi level inheritance
class Animal(object):
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        
class Name(Dog):
    def __init__(self, name = 'no name'):
        Dog.__init__(self)
        self.name = name
        print("Dog is created with name", self.name)
        
    def whoAmI(self, name):
        self.name = name
        print("Dog's name is", self.name)
        
    def bark(self):
        print(self.name, "barking - Woof!")
        
n1 = Name()
n1.whoAmI('Same')
n2 = Name()
n2.whoAmI('Buddy')
n1.bark()
n2.bark()