marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

# The enumerate function is a built-in function in Python that allows u loop over an sequence(list,tuple,string) and get the index and value at the same time.
for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")

for index, mark in enumerate(marks, start=1):
  print(index, mark)
