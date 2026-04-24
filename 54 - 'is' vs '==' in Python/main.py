# == compares values, while is checks whether two variables refer to the exact same object in memory
a = None
b = None

print(a is b) # exact location of object in memory
print(id(a)) # memory address of a
print(id(b)) # memory address of b
print(a is None) # exact location of object in memory
print(a == b) # value