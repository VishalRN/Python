x = 10  # global variable
print(x)  # prints 10

def my_function():
  global x # declare x as global to modify it
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function