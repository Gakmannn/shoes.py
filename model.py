import statemanager as sm

# Создайте класс Обувь. Необходимо хранить следующую информацию:
# ■ тип обуви;
# ✓мужская,
# ✓женская;
# ■ вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);
# ■ цвет;
# ■ цена;
# ■ производитель;
# ■ размер.
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Обувь и код для использования модели, контроллера и представления.

def all(arr:list):
  flag = True
  for el in arr:
    if not el:
      flag = False
  return flag

class Shoe:
  def __init__(self, sex, type, color, price, maker, size):
    self.sex = sex
    self.type = type
    self.color = color
    self.price = price
    self.maker = maker
    self.size = size
  
SEX = (
  'Муж.',
  'Жен.',
  'Уни.'
)
  
class ShoeModel:
  __instance = None
  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance
  def __init__(self):
    self.data = {'shoes':[]}
    sm.load(self.data)
    self.current = None  
  def add(self, sex, type, color, price, maker, size):
    el = Shoe(sex, type, color, price, maker, size)
    self.data['shoes'].append(el)
    sm.save(el, self.data)
  def sell(self):
    if self.current:
      self.data['shoes'].remove(self.current)
      self.sm.save(self.current)
      self.current = None  
  def find(self, sex='', type='', color='', minPrice=None, maxPrice=None, maker='', size=''):
    for el in self.data['shoes']:
      flags = []
      if sex:
        flags.append(True) if el.sex==sex else flags.append(False)
      if type:
        flags.append(True) if el.type==type else flags.append(False)
      if color:
        flags.append(True) if el.color==color else flags.append(False)
      if minPrice:
        flags.append(True) if el.price>minPrice else flags.append(False)
      if maxPrice:
        flags.append(True) if el.price<maxPrice else flags.append(False)
      if maker:
        flags.append(True) if el.maker==maker else flags.append(False)
      if size:
        flags.append(True) if el.size==size else flags.append(False)
      if all(flags):
        self.current = el
      else:
        self.current = None  
    return self
    