# 1 - seek()
with open('file.txt', 'r') as f:
  print(type(f))  # <class '_io.TextIOWrapper'>
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)
  print(data)

# 2 - tell()
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()
  print(current_position)  # Prints the position after reading 10 bytes

  # Seek to the saved position
  f.seek(current_position)

# 3 - truncate()
with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())