def new(dict):
  for x,y in dict.items():
    yield x,y
a={1:"Hi",2:"Coders"}
b=new(a)
print(b)
next()

#
def ex():
  n=3
  yield n
  n=n*n
  yield n
v=ex()
for x in v:
  print(x)  
  
 #Generaator Expression
 f=range(6)
print("List comp",end=":")
q=[x+2 for x in f]
print(q)
print("gen exp",end=":")
r=(x+2 for x in f)
print(r)
