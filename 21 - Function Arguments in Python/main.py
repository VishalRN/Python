# There are four types of arguments:

# Default Arguments
# Keyword Arguments
# Required Arguments
# Variable-length Arguments

# 1. Default Arguments
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# 2. Required Arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")

# 3. Keyword Arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")


# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)
# average(4, 6)

# 4. Variable-length Arguments
def average(*numbers):
  # print(type(numbers)) # <class 'tuple'>
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  return sum / len(numbers) # The return statement is used to return the value of the expression back to the main function.

c = average(5, 6, 7, 1)
print(c)

# For now if u do not understand the below code its okay
# def name(**name):
#   # print(type(name)) # <class 'dict'>
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")
