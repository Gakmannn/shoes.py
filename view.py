from tkinter import * 
import tkinter.ttk as ttk
from model import SEX
from controller import getShoe, addShoe, findShoe, sellShoe, editShoe
from abc import ABC

class Frame(ABC):
  def __init__(self, frame):
    self.sex = StringVar(value=SEX[0])
    self.type = StringVar()
    self.color = StringVar()
    self.price = StringVar()
    self.minPrice = StringVar()
    self.maxPrice = StringVar()
    self.maker = StringVar()
    self.size = StringVar()
    self.frame = frame
  def fillDataFrame(self):
    frame = ttk.Frame(self.frame)
    label = ttk.Label(frame, text='Пол')
    label.pack(anchor=NW)
    combobox = ttk.Combobox(frame, values=SEX, textvariable=self.sex)
    combobox.pack(anchor=NW)
    frame.grid(row=1, column=1)
    # type, color, price, maker, size
    typeFrame = self.create_frame('Тип', self.frame, 'type')
    typeFrame.grid(row=2, column=1)
    colorFrame = self.create_frame('Цвет', self.frame, 'color')
    colorFrame.grid(row=3, column=1)
    makerFrame = self.create_frame('Производитель', self.frame, 'maker')
    makerFrame.grid(row=4, column=1)
    sizeFrame = self.create_frame('Размер', self.frame, 'size')
    sizeFrame.grid(row=5, column=1)
    
    columns = ('sex', 'type', 'color', 'price', 'maker', 'size')
    
    self.sellTree = ttk.Treeview(self.frame, columns=columns, show="headings")
    self.sellTree.grid(row=1, column=2, rowspan=6)
  
    # определяем заголовки
    columns = ('sex', 'type', 'color', 'price', 'maker', 'size')
    self.sellTree.heading("sex", text="Пол")
    self.sellTree.heading("type", text="Тип")
    self.sellTree.heading("color", text="Цвет")
    self.sellTree.heading("price", text="Цена")
    self.sellTree.heading("maker", text="Производитель")
    self.sellTree.heading("size", text="Размер")

    self.sellTree.column("#1", stretch=NO, width=50)
    self.sellTree.column("#2", stretch=NO, width=50)
    self.sellTree.column("#3", stretch=NO, width=50)
    self.sellTree.column("#4", stretch=NO, width=50)
    self.sellTree.column("#5", stretch=NO, width=50)
    self.sellTree.column("#6", stretch=NO, width=50)
  
    self.fillTable()
  
  def fillTable(self):
    self.arr = getShoe()
    for i in self.sellTree.get_children():
      self.sellTree.delete(i)
    for shoe in self.arr:
        self.sellTree.insert("", END, values=(shoe.sex, shoe.type, shoe.color, shoe.price, shoe.maker, shoe.size))

  def create_frame(self, label_text, root, var):
    frame = ttk.Frame(root)
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    entry = ttk.Entry(frame,textvariable=getattr(self,var))   
    entry.pack(anchor=NW)
    return frame 
  
class StorageFrame(Frame):
  def addFunc(self):
    addShoe(self.sex.get(), self.type.get(), self.color.get(),self.price.get(), self.maker.get(), self.size.get())
    self.sex.set(SEX[0])
    self.type.set('')
    self.color.set('')
    self.price.set('')
    self.maker.set('')
    self.size.set('')
    self.fillTable()
  def editFunc(self):
    item = self.sellTree.selection()[0]
    i = int(item[1:])-1
    self.el = self.arr[i]
    self.sex.set(self.el.sex)
    self.type.set(self.el.type)
    self.color.set(self.el.color)
    self.price.set(self.el.price)
    self.maker.set(self.el.maker)
    self.size.set(self.el.size)
  def updateFunc(self):
    editShoe(self.el, self.sex.get(), self.type.get(), self.color.get(),self.price.get(), self.maker.get(), self.size.get())
    self.sex.set(SEX[0])
    self.type.set('')
    self.color.set('')
    self.price.set('')
    self.maker.set('')
    self.size.set('')
    self.fillTable()
  def fillDataFrame(self):
    super().fillDataFrame()
    priceFrame = self.create_frame('Цена', self.frame, 'price')
    priceFrame.grid(row=6, column=1)
    addBtn = ttk.Button(self.frame, text="Добавить товар", command=self.addFunc)
    addBtn.grid(row=7, column=1)
    addBtn = ttk.Button(self.frame, text="Изменить", command=self.editFunc)
    addBtn.grid(row=7, column=2)
    addBtn = ttk.Button(self.frame, text="Сохранить", command=self.updateFunc)
    addBtn.grid(row=7, column=3)

class SellFrame(Frame):
  def find(self):
    self.arr = findShoe(self.sex.get(), self.type.get(), self.color.get(),self.minPrice.get(),self.maxPrice.get(), self.maker.get(), self.size.get())
    for i in self.sellTree.get_children():
      self.sellTree.delete(i)
    for shoe in self.arr:
      self.sellTree.insert("", END, values=(shoe.sex, shoe.type, shoe.color, shoe.price, shoe.maker, shoe.size))
  def sell(self):
    # !Базвая валидация
    item = self.sellTree.selection()[0]
    self.sellTree.delete(item)
    i = int(item[1:])-1
    el = self.arr[i]
    sellShoe(el)
  def fillDataFrame(self):
    super().fillDataFrame()
    minPriceFrame = self.create_frame('Мин. цена', self.frame, 'minPrice')
    minPriceFrame.grid(row=6, column=1)
    maxPriceFrame = self.create_frame('Макс. цена', self.frame, 'maxPrice')
    maxPriceFrame.grid(row=7, column=1)
    findBtn = ttk.Button(self.frame, text="Поиск", command=self.find)
    findBtn.grid(row=8, column=1)
    sellBtn = ttk.Button(self.frame, text="Продать", command=self.sell)
    sellBtn.grid(row=9, column=1)

class Main(Tk):
  def __init__(self):
    super().__init__()
    self.title("Обувной магазин")
    self.geometry("800x450")
    
    self.notebook = ttk.Notebook()
    self.notebook.pack(expand=True, fill=BOTH)
    
    sellsFrame = ttk.Frame(self.notebook)
    sellsFrame.pack(fill=BOTH, expand=True)
    sellFrameObj = SellFrame(sellsFrame)
    sellFrameObj.fillDataFrame()
    storageFrame = ttk.Frame(self.notebook)
    storageFrameObj = StorageFrame(storageFrame)
    storageFrameObj.fillDataFrame()
    dataFrame = ttk.Frame(self.notebook)
    storageFrame.pack(fill=BOTH, expand=True)
    dataFrame.pack(fill=BOTH, expand=True)
    
    # добавляем фреймы в качестве вкладок
    self.notebook.add(sellsFrame, text="Продажи")
    self.notebook.add(storageFrame, text="Склад")
    self.notebook.add(dataFrame, text="Отчеты")
    