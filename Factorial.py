#Factorial
num = int(input('Number:'))
factorial = 1

if num <0:
  print('Must be positive')
elif num == 0:
  print("Factorial = 1")
else:
  for i in range (1,num+1):
    factorial = factorial*1
print(factorial)       
