# READING A FILE

# f = open('myfile.txt', 'r') # read mode will be default
# print(f)
# text = f.read()
# print(text)
# f.close()


# WRITING A FILE

f = open('myfile.txt', 'a')
f.write('Hello, world!')
f.close()

with open('myfile.txt', 'a') as f:
  f.write("Hey I am inside with")