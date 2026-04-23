class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany): # the first argument cls is the class itself and allows us to access class variables(but it works only in class methods)
    cls.company = newCompany


e1 = Employee()
e1.name = "Vishal"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

