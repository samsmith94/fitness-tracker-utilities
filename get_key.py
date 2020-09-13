"""
import tkinter as tk
 
class App(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        entry = tk.Entry(self) 
        entry.bind("<FocusIn>", self.print_type)  
        entry.bind("<Key>", self.print_key) 
        entry.pack(padx=20, pady=20) 
 
    def print_type(self, event): 
        print(event.type) 
 
    def print_key(self, event): 
        args = event.keysym, event.keycode, event.char 
        print("Symbol: {}, Code: {}, Char: {}".format(*args)) 
 
if __name__ == "__main__": 
    app = App() 
    app.mainloop()
"""  


from tkinter import *

root = Tk()

def key(event):

    #print("pressed", repr(event.char), repr(event.keycode))
    args = repr(event.keysym), repr(event.keycode), repr(event.char)
    print("Symbol: {}, Code: {}, Char: {}".format(*args)) 
    
    #print("Pressed: ", repr(event.keysym), repr(event.keycode), repr(event.char))

def callback(event):

    frame.focus_set()

    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)

frame.bind("<Key>", key)

frame.bind("<Button-1>", callback)

frame.pack()

root.mainloop()