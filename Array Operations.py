import array as arr
#Adding elements to an Array
a=arr.array('d',[1.1,2.1,3.1])
a.append(3.4)
print("Array a=",a)
b=arr.array('d',[2.1,3.2,4.6])
b.extend([4.5,3.6,7.2])
print("Array b=",b)
c=arr.array('d',[1.1,2.1,3.1])
c.insert(2,3.4)
print("Arrays c=",c)

#Removing elements
print("Popping last elements",a.pop())
print("Popping 3rd element", a.pop(2))
a.remove(1.1)
print(a)

#Array Concatenation
c =a+b
print("Array c = ",c)

#Slicing an Array
print(c[0:3])

#Looping an Array using for loop 
print("All Values")
for x in c:
  print(x)

#Looping through While loop
b=0
while b<len(c):
  print(c[b])
  b=b+1
  
