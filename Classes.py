class Car():
  def __init__(self,modelname,yearm,price):
    self.modelname=modelname
    self.yearm = yearm
    self.price = price
honda = Car('City',2017,1000000)
tata = Car('Bolt',2016,600000)

honda.cc = 1500


print(tata.__dict__)


