from collections import ChainMap

a = {1:'python',2:'Numpy'}
b = {3:'ML',4: 'AI'}

a1 = ChainMap(a,b)
print(a1)
