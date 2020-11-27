from collections import Counter

a=[1,1,2,3,4,3,2,1,2,3,4,5,6,4,3,4,5,2,4,5]
c = Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub = {2:1,6:1}
print(c.subtract(sub))
print(c.most_common())
