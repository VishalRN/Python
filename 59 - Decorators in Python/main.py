def greet(fx):
  def mfx(*args, **kwargs): # * will take any arguments as tuple and ** will take any keyword arguments as dictionary
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)
