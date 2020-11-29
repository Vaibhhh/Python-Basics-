class Parent:
  def __init__(self,fname,fage):
    self.name = fname
    self.age = fage

  def view(self):
      print(self.name,self.age)
class Child(Parent):
  def __init__(self ,fname,fage):
    self.lastname = 'Hello'

def view(self):
  print(self.age,self.lastname,self.name)
  cb = Child()
  cb.func1()
  cb.func2()
