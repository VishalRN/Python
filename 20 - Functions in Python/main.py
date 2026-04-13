# Two Type of Functions in Python:
# 1. User Defined Functions(example: def my_function():)
# 2. Built-in Functions(example: print(), input(), etc.)

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
# isGreater(a, b) # This also works
isGreater(9, 8)
# calculateGmean(a, b)
calculateGmean
# gmean1 = (a*b)/(a+b)
# print(gmean1)

c = 8
d = 74
# isGreater(c, d)
isGreater(8, 74)
# calculateGmean(c, d)
calculateGmean(8, 74)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
