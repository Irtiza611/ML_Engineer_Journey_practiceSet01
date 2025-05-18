class Dog(object):
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def speak(self):
        print("hi i am ",self.name, "and i am ",self.age, " years old")

    def talk(self):
        print("bark")

class Cat(Dog):
    def __init__(self, name, age, color ):
        super().__init__(name, age)
        self.color = color


    def speak(self):
        print("hi i am ",self.name, "and i am ",self.age, " years old and my color is ",self.color)

    def talk(self):
        print("meow")

ct = Cat("mano", 4, "blue")
ct.speak()