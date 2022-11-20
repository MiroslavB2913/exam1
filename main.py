class UnderwaterEntities:
  def __init__(self, name):
    self.name = name 
    self.breathing = 'underwater'
    self.liveIn = 'bikini bottom'
    self.eat = 'Krabby Patty'
  def liveIn1(self):
    print(self.name,'live in', self.liveIn)
  def eat1(self):
    print(self.name, 'eat', self.eat)
  def breathing1(self):
    print(self.name, 'breathing', self.breathing)
class SpongeBob(UnderwaterEntities):
  def house1(self):
    print(self.name,' live in the pineapple!')
  def pet1(self):
    print(self.name,' have Gerry the snail!')

class Patrick(UnderwaterEntities):
  def house(self):
    print(self.name,' live under the stone!')
  def pet(self):
    print(self.name,' have Sqwidward!')

obj = SpongeBob('SpongeBob')
obj.house1()
obj.liveIn1()
obj.pet1()
obj.eat1()
obj.breathing1()
print('----------------------------------------')
a = Patrick('Patrick')
a.house()
a.liveIn1()
a.pet()
a.eat1()
a.breathing1()