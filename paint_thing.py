# paint
import turtle
from tkinter import Frame, Label, Button, mainloop


# function received from tech with tim
def dragging(x, y):
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.ondrag(dragging)


# function to change turtle colour
def colourer(colour):
    turtle.color(colour)


def size(num):
    turtle.pensize(num)


def pen_state(state):
    if state == 'up':
        turtle.penup()
    else:
        turtle.pendown()


turtle.speed(-1)
wn = turtle.Screen()
wn.title('Paint by Daniel')
master_frame = Frame(height=500, width=500)
master_frame.pack(side='left')
turtle.shape("classic")
turtle.fillcolor((0, 0 , 0))
# space holder
space_holder1 = Label(master_frame)
space_holder1.grid(row=0, column=1)


turtle.listen()
turtle.ondrag(dragging)



# Colour Frame Codes
colour_frame = Frame(master_frame, height=10, width=10, cursor='man')
colour_frame.grid(row=0, column=0)

colour_frame_label = Label(colour_frame, text='Colours')
colour_frame_label.grid(row=0, column=0, columnspan=2)

Button1 = Button(colour_frame, bg='red', padx=9, border=2, command=lambda: colourer('red'))
Button1.grid(row=1, column=0)

Button2 = Button(colour_frame, bg='yellow', padx=9, border=2,
                 command=lambda: colourer('yellow'))
Button2.grid(row=1, column=1)

Button3 = Button(colour_frame, bg='blue', padx=9, border=2,
                 command=lambda: colourer('blue'))
Button3.grid(row=1, column=2)

Button4 = Button(colour_frame, bg='green', padx=9, border=2,
                 command=lambda: colourer('green'))
Button4.grid(row=2, column=0)

Button5 = Button(colour_frame, bg='black', padx=9, border=2,
                 command=lambda: colourer('black'))
Button5.grid(row=2, column=1)

Button6 = Button(colour_frame, bg='white', padx=9, border=2,
                 command=lambda: colourer('white'))
Button6.grid(row=2, column=2)

Button7 = Button(colour_frame, bg='orange', padx=9, border=2,
                 command=lambda: colourer('orange'))
Button7.grid(row=3, column=0)

Button8 = Button(colour_frame, bg='purple', padx=9, border=2,
                 command=lambda: colourer('purple'))
Button8.grid(row=3, column=1)

Button9 = Button(colour_frame, bg='pink', padx=9, border=2,
                 command=lambda: colourer('pink'))
Button9.grid(row=3, column=2)

# Brush size frame
brush_frame = Frame(master_frame, height=12, width=50)
brush_frame.grid(row=0, column=2)

brush_frame_label = Label(brush_frame, text='Brush size')
brush_frame_label.grid(row=0, column=0)

pencil_button = Button(brush_frame, text='pencil', command=lambda: size(1), padx=8)
pencil_button.grid(row=1, column=0)

marker_size1 = Button(brush_frame, text='Size 1', command=lambda: size(3), padx=8, )
marker_size1.grid(row=1, column=1)

marker_size2 = Button(brush_frame, text='Size 2', command=lambda: size(5), padx=8)
marker_size2.grid(row=2, column=0)

marker_size3 = Button(brush_frame, text='Size 3', command=lambda: size(7), padx=8)
marker_size3.grid(row=2, column=1)

marker_size4 = Button(brush_frame, text='Size 4', command=lambda: size(9), padx=8)
marker_size4.grid(row=3, column=0)

marker_size5 = Button(brush_frame, text='Size 5', command=lambda: size(11), padx=8)
marker_size5.grid(row=3, column=1)

# pen up and pen down


Pen_up = Button(master_frame, text='Pen up', command=lambda: pen_state('up'))
Pen_up.grid(row=0, column=4)
Pen_down = Button(master_frame, text='Pen Down',
                  command=lambda: pen_state('down'))
Pen_down.grid(row=0, column=5)
mainloop()
