from tkinter import *

from tkinter import font
import tkinter.messagebox
tk = Tk()
tk.title("Widget designer")

blank_image = PhotoImage()

ROWS = 15

COLS = ROWS

square_size = 10

global_color = "#00FF80"
array_size = 0

default_color = "#FFFFFF"

from tkinter.colorchooser import *



select_color = Button(tk, text='Pixel Color')
select_color.grid(row=ROWS+1, column=COLS+1)

def getColor():
    global global_color
    color = askcolor()
    print(color)
    rgb_color = color[1]
    print(rgb_color)
    #print(rgb_color[1:])
    #int(rgb_color, 16)
    #print("R: {}, G: {}, B: {}".format(int(rgb_color[1:3], 16), int(rgb_color[3:5], 16), int(rgb_color[5:7], 16)))
    global_color=rgb_color
    select_color.config(bg=rgb_color)

    
select_color.config(bg=global_color, command=getColor)


buttons = []


pixel_array = [];

def onClick(idx):
    global array_size
    array_size+=1
    
    global print_tuple
    
    global buttons
    print(idx, global_color)
    print("(X,Y): ({},{}) | (R,G,B): ({},{},{})".format(int(idx/ROWS), idx%ROWS, int(global_color[1:3], 16), int(global_color[3:5], 16), int(global_color[5:7], 16)))
    print("Size: {}".format(array_size))
    print_tuple = int(idx/ROWS), idx%ROWS, int(global_color[1:3], 16), int(global_color[3:5], 16), int(global_color[5:7], 16)
    #print(print_tuple);
    pixel_array.append(print_tuple)
    
    #buttons[idx]["bg"] = global_color
    buttons[idx].config(bg=global_color)
    

    

menubar = tkinter.Menu(tk)
menusize = tkinter.Menu(tk, tearoff=0)
menusize.add_command(label="small (10x10 with 10 mines)")
menusize.add_command(label="medium (20x20 with 40 mines)")
menusize.add_command(label="big (35x35 with 120 mines)")
menusize.add_command(label="custom")
menusize.add_separator()

menubar.add_cascade(label="size", menu=menusize)
menubar.add_command(label="exit", command=lambda: tk.destroy())
tk.config(menu=menubar)

index = 0

for x in range(ROWS):
    for y in range(COLS):

        button = Button(tk, image=blank_image, text=" ", font='Times 12', bg='white', fg='white', compound=CENTER, command = lambda idx = index: onClick(idx))
        
        button.config(width=square_size, height=square_size)
        button.config(bg=default_color)
        button.grid(row=x, column=y, sticky="NWSE") #makes the button expand
        index += 1
        buttons.append(button)


font = font.Font(family = 'Times', size = '8')

canvas = Canvas(tk, width=160, height=80, bg="blue")

canvas.create_text(40, 20, font = font, text="Hello World", fill="white");

canvas.create_oval(81, 0+2, 160, 79+2, fill="orange", outline="orange")
#canvas.pack()
canvas.grid(row=ROWS+2, column=COLS+1)


tk.mainloop()


WIDGET_NAME = "bluetooth"

"""
import cfile as C
hello = C.cfile('hello.c')
hello.code.append(C.sysinclude('stdio.h'))
hello.code.append(C.blank())

hello.code.append(C.function('draw_' + WIDGET_NAME + '_widget', 'void',).add_param(C.variable('start_x', 'int')).add_param(C.variable('start_y', 'int')))

body = C.block(innerIndent=4)

body.append(C.statement(C.fcall('st7735_draw_pixel').add_arg('start_x + 0').add_arg('start_y + 5').add_arg('color')))
body.append(C.statement(C.fcall('st7735_draw_pixel').add_arg('start_x + 1').add_arg('start_y + 2').add_arg('color')))
body.append(C.statement(C.fcall('st7735_draw_pixel').add_arg('start_x + 0').add_arg('start_y + 1').add_arg('color')))

#body.append(C.statement('return'))
hello.code.append(body)
print(str(hello))

f = open("hello.c", "w")
f.write(str(hello))
f.close()
"""

import cfile as C
hello = C.cfile('hello.c')

hello.code.append(C.variable(WIDGET_NAME + '_widget', typename='widget_t'))
hello.code.append(C.line(' = '))



body = C.block(innerIndent=4)
#body.append(C.line('{0, 0, 128, 128, 255},'))

body.append(C.line("{},{{".format(array_size)))
for i in pixel_array:
    body.append(C.line("{{{}, {}, {}, {}, {}}},".format(i[1], i[0], i[2], i[3], i[4])))

body.append('}')

hello.code.append(body)
hello.code.append(C.statement(''))
print(str(hello))

f = open("hello.c", "w")
f.write(str(hello))
f.close()





#void st7735_draw_pixel(uint16_t x, uint16_t y, uint16_t color)






#generáljunk inkább valami struktúratömböt, vagy ilyesmit és csak egy for ciklussak hívjuk meg a draw_pixel függvényt



"""
.h fájl: (mondjuk widgets.h???)

#include "st7735.h"

typedef struct {
    uint16_t x;
    uint16_t y;
    uint16_t color;
} point_t;

typedef struct {
    point_t point_array[MAX_SIZE??? vagy dyn?];
    uint16_t size;
} widget_t;

extern widget_t bluetooth_widget;
extern widget_t clock_widgets;


void draw_widget(widget_t widget, uint8_t start_x, uint8_t start_y);

--------------------------------------------------------------------------------
.c fájl (widgets.c):

#include "widgets.h"

widget_t bluetooth_widget = {
    {0, 4, 5698},
    {0, 5, 5698},
    {0, 6, 5698},
    ...
    ...
    ...
    234
};

widget_t clock_widgets = {
    {0, 4, 5698},
    {0, 5, 5698},
    {0, 6, 5698},
    ...
    ...
    521
};


void draw_widget(widget_t widget, uint8_t start_x, uint8_t start_y)
{
    for (int i = 0; i < widget.size; i++) {
        st7735_draw_pixel(start_x + widget.point_array[i].x, start_y + widget.point_array[i].y, widget.point_array[i].color)
    }
}

--------------------------------------------------------------------------------

- xml-be is mentődjön
Elementtree : https://www.datacamp.com/community/tutorials/python-xml-elementtree
- egyszerre több widget-et lehessen mozgatni rtt-vel, lehessen egyiket eltüntetni aztán újramegjeleníteni akár
- jó lenne ha a háttérszínt lehetne állítani az appból
- illetve a widget színét is, bár annak nem kedvez a tömb generálás



"""




