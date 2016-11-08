from tkinter import *

root = Tk()

label = Label(master=root, text='Hello world', height=2)
label.pack()

button = Button(master=root, text='Druk hier')
button.pack(pady=10)

button2 = Button(master=root, text='Druk hier 2 keer')
button2.pack(pady=40)

root.mainloop()