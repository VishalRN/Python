# Constructor helps in creating objects
# Constructor in Python are used to initialize the attributes of a class.
# Two types of constructors in Python are:
# 1. Default constructor
# 2. Parameterized constructor

class Person:
  # the below type of constructor is called parameterized constructor
  #constructor method
  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self): # self is required while defining classes
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
# c = Person(1, 2, 3) # it will throw an error because the __init__ takes only 3 positional arguments but 4 very given (by default self will be passed automatically)
# d = Person() # it will throw an error because the __init__ takes 2 positional arguments but 0 were given
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
