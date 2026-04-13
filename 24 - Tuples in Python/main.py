tup = (1, 2, 76, 342, 32, "green", True)
tup1 = (90)
print(type(tup1), tup1) # type is int
print(type(tup), tup) # type is tuple
# tup[0] = 90
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)