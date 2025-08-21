class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat

class animal:

  def __init__(self, name, color):
    self.name = name
    self.color = color

  def details(self):
    print(f"i have a {self.name} which is {self.color} in color")


class cat(animal):

  def __init__(self, name,  age):
    animal.__init__(self, name,color="gray")
    self.age = age

  def details(self):
    print(
      f"i have a {self.name} which is {self.color} in color whoes age is {self.age}"
    )


ani = animal('buffalow', 'black and white')
ani.details()

ani1 = cat('cat',3)
ani1.details()