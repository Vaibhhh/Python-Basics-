#Hash Operations
my_dict={'Dave':'001','Ava':'002','Joe':'003'}
#Accessing
print(my_dict['Dave'])
print(my_dict.keys())
print(my_dict.get('Ava'))

for x in my_dict:
  print(x)

for x in my_dict.values():
  print(x)

#Updating
my_dict['Dave']='004'
my_dict['Chris']='003'
print(my_dict)

#Deleting
print(my_dict.pop('Ava'))
print(my_dict.popitem())

