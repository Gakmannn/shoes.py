from tkinter import * 
import tkinter.ttk as ttk
from model import SEX
from controller import getShoe, addShoe


class Main(Tk):
  def __init__(self):
    super().__init__()
    self.title("Обувной магазин")
    self.geometry("800x450")
    self.sex = StringVar(value=SEX[0])
    self.type = StringVar()
    self.color = StringVar()
    self.price = StringVar()
    self.minPrice = StringVar()
    self.maxPrice = StringVar()
    self.maker = StringVar()
    self.size = StringVar()
    self.sellTree = None
    self.dataTree = None
    
    notebook = ttk.Notebook()
    notebook.pack(expand=True, fill=BOTH)
    
    sellsFrame = ttk.Frame(notebook)
    sellsFrame.pack(fill=BOTH, expand=True)
    # self.fillSellsFrame(sellsFrame)
    storageFrame = ttk.Frame(notebook)
    dataFrame = ttk.Frame(notebook)
    self.fillDataFrame(storageFrame)
    storageFrame.pack(fill=BOTH, expand=True)
    dataFrame.pack(fill=BOTH, expand=True)
    
    # добавляем фреймы в качестве вкладок
    notebook.add(sellsFrame, text="Продажи")
    notebook.add(storageFrame, text="Склад")
    notebook.add(dataFrame, text="Отчеты")
    
  def create_frame(self, label_text, root, var):
    frame = ttk.Frame(root)
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    entry = ttk.Entry(frame,textvariable=self[var])   
    entry.pack(anchor=NW)
    return frame      
  def addFunc(self):
    addShoe(self.sex.get(), self.type.get(), self.color.get(),self.price.get(), self.maker.get(), self.size.get())
    self.sex.set(SEX[0])
    self.type.set('')
    self.color.set('')
    self.price.set('')
    self.maker.set('')
    self.size.set('')
    self.fillTable()
  def fillDataFrame(self,root):
    frame = ttk.Frame(root)
    label = ttk.Label(frame, text='Пол')
    label.pack(anchor=NW)
    combobox = ttk.Combobox(frame, values=SEX, textvariable=self.sex)
    combobox.pack(anchor=NW)
    frame.grid(row=1, column=1)
    # type, color, price, maker, size
    typeFrame = self.create_frame('Тип', root, 'type')
    typeFrame.grid(row=2, column=1)
    colorFrame = self.create_frame('Цвет', root, 'color')
    colorFrame.grid(row=3, column=1)
    PriceFrame = self.create_frame('Цена', root, 'price')
    PriceFrame.grid(row=4, column=1)
    makerFrame = self.create_frame('Производитель', root, 'maker')
    makerFrame.grid(row=5, column=1)
    sizeFrame = self.create_frame('Размер', root, 'size')
    sizeFrame.grid(row=6, column=1)

    addBtn = ttk.Button(root, text="Добавить товар", command=self.addFunc)
    addBtn.grid(row=7, column=1)
    
    columns = ('sex', 'type', 'color', 'price', 'maker', 'size')
    
    self.sellTree = ttk.Treeview(root, columns=columns, show="headings")
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
  
  def fillTable(self):
    for i in self.sellTree.get_children():
      self.sellTree.delete(i)
    for shoe in getShoe():
        self.sellTree.insert("", END, values=(shoe.sex, shoe.type, shoe.color, shoe.price, shoe.maker, shoe.size))
  
  

# def fillSellsFrame(root,data):
#   global sex
#   global type 
#   global color
#   global minPrice
#   global maxPrice
#   global maker
#   global size
#   frame = ttk.Frame(root)
#   label = ttk.Label(frame, text='Пол')
#   label.pack(anchor=NW)
#   combobox = ttk.Combobox(frame, values=SEX)
#   combobox.pack(anchor=NW)
#   frame.grid(row=1, column=1)
#   # type, color, price, maker, size
#   typeFrame = create_frame('Тип', root, data, 'type')
#   typeFrame.grid(row=2, column=1)
#   colorFrame = create_frame('Цвет', root, data, 'color')
#   colorFrame.grid(row=3, column=1)
#   minPriceFrame = create_frame('Мин.цена', root, data, 'minPrice')
#   minPriceFrame.grid(row=4, column=1)
#   maxPriceFrame = create_frame('Макс.цена', root, data, 'maxPrice')
#   maxPriceFrame.grid(row=5, column=1)
#   makerFrame = create_frame('Производитель', root, data, 'maker')
#   makerFrame.grid(row=6, column=1)
#   sizeFrame = create_frame('Размер', root, data, 'size')
#   sizeFrame.grid(row=7, column=1)

#   columns = ('sex', 'type', 'color', 'price', 'maker', 'size')
  
#   tree = ttk.Treeview(root, columns=columns, show="headings")
#   tree.grid(row=1, column=2, rowspan=7)
 
#   # определяем заголовки
#   columns = ('sex', 'type', 'color', 'price', 'maker', 'size')
#   tree.heading("sex", text="Пол")
#   tree.heading("type", text="Тип")
#   tree.heading("color", text="Цвет")
#   tree.heading("price", text="Цена")
#   tree.heading("maker", text="Производитель")
#   tree.heading("size", text="Размер")

#   tree.column("#1", stretch=NO, width=50)
#   tree.column("#2", stretch=NO, width=50)
#   tree.column("#3", stretch=NO, width=50)
#   tree.column("#4", stretch=NO, width=50)
#   tree.column("#5", stretch=NO, width=50)
#   tree.column("#6", stretch=NO, width=50)
  
#   # # добавляем данные
#   # for person in people:
#   #     tree.insert("", END, values=person)

