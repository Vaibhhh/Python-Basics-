from collections import OrderedDict

d=OrderedDict()
d[1]= "v"
d[2]= 'a'
d[3]= "i"
d[4]= "b"
d[5]="h"

print(d)
print(d.keys())
print(d.items())
d[1]="V"
print(d)
