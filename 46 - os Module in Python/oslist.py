import os 
folders = os.listdir("data")

# print(os.getcwd()) # Get current working directory
# os.chdir("/Github") # Change working directory
# print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
