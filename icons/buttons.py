




# importing only those functions 
# which are needed 
from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window 
root = Tk()

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)




menubar = Menu(root)
menusize = Menu(root, tearoff=0)
menusize.add_command(label="small (10x10 with 10 mines)")
menusize.add_command(label="medium (20x20 with 40 mines)")
menusize.add_command(label="big (35x35 with 120 mines)")
menusize.add_command(label="custom")
menusize.add_separator()

menubar.add_cascade(label="size", menu=menusize)
menubar.add_command(label="exit", command=lambda: root.destroy())
root.config(menu=menubar)


"""
root.title("Tab Widget")

tabControl = Notebook(root) 

tab1 = Frame(tabControl) 
tab2 = Frame(tabControl) 
  
tabControl.add(tab1, text ='Tab 1') 
tabControl.add(tab2, text ='Tab 2') 
tabControl.grid(row=0, column=0)
  
Label(tab1, text ="Welcome to GeeksForGeeks").grid(column = 0, row = 0, padx = 30, pady = 30)
Label(tab2, text ="Lets dive into the world of computers").grid(column = 0, row = 0, padx = 30, pady = 30)
"""


# Creating a photoimage object to use image 
pen = PhotoImage(file = r"pen.png").subsample(4)
fill = PhotoImage(file = r"fill.png").subsample(4)
rubber = PhotoImage(file = r"rubber.png").subsample(4)

circle = PhotoImage(file = r"circle.png").subsample(4)
square = PhotoImage(file = r"square.png").subsample(4)
  
# here, image option is used to 
# set image on button 
Button(root, text='', image = pen).grid(row=1, column=0)
Button(root, text='', image = fill).grid(row=2, column=0)
Button(root, text='', image = rubber).grid(row=3, column=0)
Button(root, text='', image = circle).grid(row=4, column=0)
Button(root, text='', image = square).grid(row=5, column=0)


L1 = Label(root, text="Kör")
L1.grid(row=0, column=0)

L1 = Label(root, text="x:")
L1.grid(row=0, column=1)
E1 = Entry(root, width=10)
E1.grid(row=0, column=2)

L1 = Label(root, text="y:")
L1.grid(row=0, column=3)
E1 = Entry(root, width=10)
E1.grid(row=0, column=4)

L1 = Label(root, text="r:")
L1.grid(row=0, column=5)
E1 = Entry(root, width=10)
E1.grid(row=0, column=6)

mainloop()





  
#root.mainloop()