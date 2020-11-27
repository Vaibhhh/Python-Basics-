frpm collections import defaultdict

d = defaultdict(int)

d[1]="Mr"
d[2]="Vaibhav"
#Dynamically space is already alotted 
print(d[3])
#This does not work in the case of Normal Dictionary
a = {1:"Mr",2:"Vaibhav"}
