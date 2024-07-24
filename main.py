from view import Main
# from tkinter import * 
# import tkinter.ttk as ttk
# from model import SEX
# from controller import getShoe, addShoe

# window = Tk() 
# window.title("Обувной магазин")
# window.geometry("800x450")

# # btn2 = ttk.Button(text="Склад", command=print('a'))
# # btn2.grid(row=1, column=2)

# data = {
#   'sex': StringVar(value=SEX[0]),
#   'type': StringVar(),
#   'color': StringVar(),
#   'price': StringVar(),
#   'minPrice': StringVar(),
#   'maxPrice': StringVar(),
#   'maker': StringVar(),
#   'size': StringVar(),
# }

# # btn3 = ttk.Button(text="Отчеты", command=print('a'))
# # btn3.grid(row=1, column=3)

# def create_frame(label_text, root, data, var):
#     frame = ttk.Frame(root)
#     # добавляем на фрейм метку
#     label = ttk.Label(frame, text=label_text)
#     label.pack(anchor=NW)
#     # добавляем на фрейм текстовое поле
#     entry = ttk.Entry(frame,textvariable=data[var])   
#     entry.pack(anchor=NW)
#     # возвращаем фрейм из функции
#     return frame

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

# def fillDataFrame(root, data):
  
#   def addFunc():
#     addShoe(data['sex'].get(), data['type'].get(), data['color'].get(), data['price'].get(), data['maker'].get(), data['size'].get())
#     data['sex'].set(SEX[0])
#     data['type'].set('')
#     data['color'].set('')
#     data['price'].set('')
#     data['maker'].set('')
#     data['size'].set('')
#     fillTavle()
  
#   frame = ttk.Frame(root)
#   label = ttk.Label(frame, text='Пол')
#   label.pack(anchor=NW)
#   combobox = ttk.Combobox(frame, values=SEX, textvariable=data['sex'])
#   combobox.pack(anchor=NW)
#   frame.grid(row=1, column=1)
#   # type, color, price, maker, size
#   typeFrame = create_frame('Тип', root, data, 'type')
#   typeFrame.grid(row=2, column=1)
#   colorFrame = create_frame('Цвет', root, data, 'color')
#   colorFrame.grid(row=3, column=1)
#   PriceFrame = create_frame('Цена', root, data, 'price')
#   PriceFrame.grid(row=4, column=1)
#   makerFrame = create_frame('Производитель', root, data, 'maker')
#   makerFrame.grid(row=5, column=1)
#   sizeFrame = create_frame('Размер', root, data, 'size')
#   sizeFrame.grid(row=6, column=1)

#   addBtn = ttk.Button(root, text="Добавить товар", command=addFunc)
#   addBtn.grid(row=7, column=1)
  
#   columns = ('sex', 'type', 'color', 'price', 'maker', 'size')
  
#   tree = ttk.Treeview(root, columns=columns, show="headings")
#   tree.grid(row=1, column=2, rowspan=6)
 
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
  

#   def fillTavle():
#     for i in tree.get_children():
#       tree.delete(i)
#     for shoe in getShoe():
#         tree.insert("", END, values=(shoe.sex, shoe.type, shoe.color, shoe.price, shoe.maker, shoe.size))
  
#   fillTavle()
  

# notebook = ttk.Notebook()
# notebook.pack(expand=True, fill=BOTH)
 
# sellsFrame = ttk.Frame(notebook)
# sellsFrame.pack(fill=BOTH, expand=True)
# fillSellsFrame(sellsFrame,data)
# storageFrame = ttk.Frame(notebook)
# dataFrame = ttk.Frame(notebook)
# fillDataFrame(storageFrame,data)
# storageFrame.pack(fill=BOTH, expand=True)
# dataFrame.pack(fill=BOTH, expand=True)
 
# # добавляем фреймы в качестве вкладок
# notebook.add(sellsFrame, text="Продажи")
# notebook.add(storageFrame, text="Склад")
# notebook.add(dataFrame, text="Отчеты")


# window.mainloop()

if __name__ == "__main__":
  root = Main()
  root.mainloop()