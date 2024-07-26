from model import ShoeModel

shoes = ShoeModel()

def getShoe():
  # for el in shoes.data['shoes']:
  #   print(el.__dict__)
  return shoes.data['shoes']

def addShoe(sex, type, color, price, maker, size):
  # print(sex, type, color, price, maker, size)
  # !Валидация должна быть тут
  shoes.add(sex, type, color, price, maker, size)
  
def findShoe(sex, type, color, minPrice, maxPrice, maker, size):
  # !Валидация должна быть тут
  return shoes.find(sex, type, color, minPrice, maxPrice, maker, size)

def sellShoe(el):
  # !Валидация должна быть тут
  shoes.sell(el)

def editShoe(el, sex, type, color, price, maker, size):
  # !Валидация должна быть тут
  shoes.edit(el, sex, type, color, price, maker, size)