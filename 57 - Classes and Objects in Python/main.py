# class is a blueprint for creating objects
class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self): # self is a reference to the current instance of the class and is used to access variables that belong to the class
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
