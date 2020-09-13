from tkinter import *
#from util.color import Color

tk = Tk()

#from util.color import Color
from colorutils import Color


def get_pixels_of(canvas):
    width = int(canvas["width"])
    height = int(canvas["height"])
    colors = []

    for x in range(width):
        column = []
        for y in range(height):
            column.append(get_pixel_color(canvas, x, y))
        colors.append(column)

    return colors

def get_pixel_color(canvas, x, y):
    ids = canvas.find_overlapping(x, y, x+1, y+1)
    
    #print(ids)
    if len(ids) > 0:
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        if color == "white":
            print(color, x, y)
        return color
        #color = color.upper()
        #if color != '':
            #return Color[color.upper()]

    #return "WHITE"




canvas = Canvas(tk, width=160, height=80, bg="red")
canvas.pack()

#canvas.create_rectangle(0, 0, 160, 80, fill='red', outline='red')
canvas.create_text(3,50,fill="white",font="Times 12 bold", text="O", activefill="white")
canvas.update

pix = get_pixels_of(canvas)

canvas.create_rectangle(156, 76, 160, 80, fill='white', outline='white')
canvas.update

pix = get_pixels_of(canvas)
#print(pix)

mainloop()



