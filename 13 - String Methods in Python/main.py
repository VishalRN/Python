# Strings are immutable (they cannot be changed)
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # removes trailing "!"
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) # Capitalizes the first letter and makes the rest of the letters lowercase

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) # checks if the string ends with "!!!"

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) # checks if the substring "to" is present between indices 4 and 10

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh")) # returns -1
# print(str1.index("ishh")) # raises ValueError

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # a-z, A-Z, 0-9 
str1 = "Welcome"
print(str1.isalpha()) # a-z, A-Z

str1 = "hello world"
print(str1.islower()) 

str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable()) # checks if all characters are printable
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle()) 

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())