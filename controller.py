from model import ShoeModel

shoes = ShoeModel()

def getShoe():
  # for el in shoes.data['shoes']:
  #   print(el.__dict__)
  return shoes.data['shoes']

def addShoe(sex, type, color, price, maker, size):
  print(sex, type, color, price, maker, size)
  shoes.add(sex, type, color, price, maker, size)