# Dictionaries are ordered collections of data items
# Dictionary items are stored as key-value pairs

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info['name']) # Throws an error if key doesn't exist
# print(info.get('name')) # Returns None if key doesn't exist
print(info.keys())
print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}") # it will find the key and return the value

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  