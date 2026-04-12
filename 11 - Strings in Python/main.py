name = "Vishal"
friend = "Rohan"
anotherFriend = 'Lovish'
# apple = 'He said, "I want to eat an apple' # This will also work
# apple = "He said \"I want to eat an apple" # This will also work
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple''' # Multi-line string

print("Hello, " + name)
print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)