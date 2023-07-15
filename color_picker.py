from tkinter import *
import tkinter.messagebox
from turtle import right,width
from matplotlib import scale

co0="#444466" #Black
co1="#feffff" #white

window = Tk()
window.geometry("530x205")
window.configure(bg=co1)
window.resizable(width=FALSE, height=FALSE)

def scale(value):
    r=red_scale.get()
    g=green_scale.get()
    b=blue_scale.get()

    rgb=f'{r},{g},{b}'
    hexadecimal="#%02x%02x%02x" % (r,g,b)

    screen['bg']=hexadecimal

    color_entry.delete(0,END)
    color_entry.insert(0,hexadecimal)

def onclick():
    tkinter.messagebox.showinfo("Color", "Coppied!")
    clip=Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(color_entry.get())
    clip.update()
    clip.destroy()

screen = Label(window, bg=co0, width=40, height =10)
screen.grid(row=0, column=0)

right_frame= Frame(window,bg=co1)
right_frame.grid(row=0,column=1,padx=5)

down_frame=Frame(window, bg=co1)
down_frame.grid(row=1, column =0, columnspan=2, padx=15)

red=Label(right_frame,text="Red", bg=co1,fg ="red", width=7, anchor=NW, font=("Ivy", 12, "bold"))
red.grid(row=0, column=0)
red_scale=Scale(right_frame, command=scale, from_=0,to=255, length=150, orient=HORIZONTAL)
red_scale.grid(row=0, column=1)

blue=Label(right_frame,text="Blue", bg=co1,fg ="blue", width=7, anchor=NW, font=("Ivy", 12, "bold"))
blue.grid(row=2, column=0)
blue_scale=Scale(right_frame, command=scale,from_=0, to=255,length=150, orient=HORIZONTAL)
blue_scale.grid(row=2,column=1)

green=Label(right_frame,text="Green", bg=co1,fg ="green", width=7, anchor=NW, font=("Ivy", 12, "bold"))
green.grid(row=1, column=0)
green_scale=Scale(right_frame, command=scale,from_=0, to=255,length=150, orient=HORIZONTAL)
green_scale.grid(row=1,column=1)

rgb_label = Label(down_frame, text="HEX CODE: ", bg=co1, anchor=NW, font=("Ivy", 10, "bold"))
rgb_label.grid(row=0, column=0, pady=15)

color_entry = Entry(down_frame, width=12, font=("Ivy", 10, "bold"), justify=CENTER)
color_entry.grid(row=0, column=1, padx=5)

coppy_button = Button(down_frame, text="Copy Color", bg=co1, font=("Ivy", 10, "bold"), command=onclick)
coppy_button.grid(row=0, column = 2, padx=5)

app_name=Label(down_frame, text="Color Picker App", bg=co1, font=("Ivy", 15, "bold"))
app_name.grid(row=0, column=3, padx=40)






window.mainloop()