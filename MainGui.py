import tkinter as tk
from Turtle import Turtle
from movefortkinter import Move
import tkinter.messagebox
import PIL.ImageGrab as ImageGrab
import sys


def main_gui(file_name):

    root = tk.Tk()
    root.title('Symulator logomocji')

    root.geometry("800x500")
    root.resizable(0, 0)

    # creating turtle
    turtle = Turtle([0, 0], 0)

    # function which is setting leave of turtle as True
    def leaving(leave):
        leave.set(True)

    # function which is setting leave of turtle as False
    def up(leave):
        leave.set(False)

    # checking if turtle is out of background
    def out_of_background(x_size, y_size):
        tk.messagebox.Message(root)
        tk.messagebox.showinfo(title='error', message='Ruch poza polem')
        back_to_background(x_size, y_size)

    def back_to_background(x_size, y_size):
        if turtle.position[0] < 0:
            turtle.position[0] = 0
        elif turtle.position[0] > x_size:
            turtle.position = x_size
        elif turtle.position[1] < 0:
            turtle.position[1] = 0
        elif turtle.position[1] > y_size:
            turtle.position[1] = y_size

    # moving of turtle
    def movement(value, type_of_move, leave, x_size, y_size):
        move = Move(value, leave)
        if type_of_move == 'naprzod':
            if (int(turtle.position[0]) > int(x_size) or
                int(turtle.position[1]) > int(y_size)or
                turtle.position[0] < 0 or
                turtle.position[1] < 0):

                out_of_background(x_size, y_size)

            else:
                move.go_forward(canvas, turtle)
        if type_of_move == 'obrot':
            move.turn_move(turtle)

    # returning turtle to previous position
    def back(value, leave):
        move = Move(value, leave)
        move.back_move(canvas, turtle)

    leave = tk.BooleanVar()
    leave.set(False)
    image = tk.PhotoImage(file='amphibian.png')
    # creating paintbacground
    canvas = tk.Canvas(root, bg='white', width=800, height=470)
    canvas.pack(side=tk.BOTTOM)
    canvas.create_image(780, 460, image=image)

    def save_canvas(file_name):
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        xx = x + canvas.winfo_width()
        yy = y + canvas.winfo_height()
        ImageGrab.grab(bbox=(x, y, xx, yy)).save(file_name)

    def saving(file_name):
        root.after(1000, save_canvas(file_name))

    def exit():
        root.destroy()

    def new_file():
        canvas.delete(tk.ALL)
        turtle.position = [0, 0]
        turtle.turn = 0

    # creating menu
    menu = tk.Menu(root)
    root.config(menu=menu)

    # creating submenu
    subMenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=subMenu)
    subMenu.add_command(label='New Project', command=new_file)
    subMenu.add_separator()
    subMenu.add_command(label='Save', command=lambda: saving(file_name))
    subMenu.add_separator()
    subMenu.add_command(label='Exit', command=exit)

    toolbar = tk.Frame(root, bg='lightpink')

    # creating enter
    value = tk.IntVar()
    inputbox = tk.Entry(toolbar, width=30, textvariable=value)
    inputbox.pack(side=tk.LEFT)
    button_to_input = tk.Button(toolbar, text='Enter',
                                command=lambda: value.get())
    button_to_input.pack(side=tk.LEFT)

    # creating buttons
    leave_button = tk.Button(toolbar, text='Opusc', command=lambda:
                             movement(value.get(), 'opusc', leaving(leave),
                                      800, 470))
    up_button = tk.Button(toolbar, text='Podnies', command=lambda:
                          movement(value.get(), 'podnies', up(leave),
                                   800, 470))
    forward_button = tk.Button(toolbar, text='Naprzod', command=lambda:
                               movement(value.get(), 'naprzod', leave.get(),
                                        800, 470))
    turn_button = tk.Button(toolbar, text='Obrot', command=lambda:
                            movement(value.get(), 'obrot', leave.get(),
                                     800, 470))
    return_button = tk.Button(toolbar, text='Cofnij', command=lambda:
                              back(value.get(), leave.get()))

    leave_button.pack(side=tk.LEFT)
    up_button.pack(side=tk.LEFT)
    forward_button.pack(side=tk.LEFT)
    turn_button.pack(side=tk.LEFT)
    return_button.pack(side=tk.LEFT)

    toolbar.pack(side=tk.TOP, fill=tk.X)

    root.mainloop()


if __name__ == '__main__':
    file_name = sys.argv[1]
    main_gui(file_name)
