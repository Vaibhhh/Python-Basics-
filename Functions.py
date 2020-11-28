#Functions

#First-Class Object
def func1(name):
  return f"Hello{name}"

def func2(name):
  return f"{name} , how you doin ?"  

def func3(func4) :
  return func4("Coder")

print(func3(func1))
print(func3(func2))

#Inner Functions

def func():
  print("Function A")
  def funcA():
    print ("First child function")

  def funcB():
    print ("Second child function")  
  
  funcA()
  funcB()

func()

#

def func(n):
  def funca():
    return "Hello"
  def funcb():
    return 'Coder'
  if n == 1:
    return funca
  else:
    return funcb

a = func(1)
b= func(2)
print(a())
print(b())
