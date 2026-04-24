class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer): # it will give only employee attributes not dancer attributes 
  def __init__(self, name, dance):
    self.name = name
    self.dance = dance

o  = DancerEmployee("Shivani", "Kathak") 
print(o.name)
print(o.dance)
o.show() # The show method from Employee will be called
print(DancerEmployee.mro())