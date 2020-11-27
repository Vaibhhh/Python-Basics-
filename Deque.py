from collections import deque
a = ['v','a','i','b','h']
d = deque(a)
print (d)
d.append("Python")
d.appendleft("Mr")
print(d)

d.pop()
print(d)

