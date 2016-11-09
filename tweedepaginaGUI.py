from tkinter import *
from tkinter.messagebox import showinfo
import random

root = Tk()   # maakt het hoofdscherm

# pop-up checked of iron man wordt opgegeven
def clicked():
    invoer = entry.get()
    if invoer == 'iron man':
        bericht = 'Je hebt het goed'
        showinfo(title='Goed', message=bericht)
    else:
        bericht = 'Je hebt het fout'
        showinfo(title='Fout', message=bericht)

root.configure(background='red')



#button 2
def clicked2():
    print("Hello")
    pass
#button 3
def clicked3():
    print("Hello")
    pass

label = Label(master=root,
              text='Hier komt een random message te staan over de superheld',
              background='red',
              font=('Helvetica', 10, 'bold italic'),
              height=3)
label.pack()

label2 = Label(master=root,
              text='vul cijfer in voor een kwadraat',
              background='red',
              font=('Helvetica', 10, 'bold italic'),
              height=3)
label2.pack()

#rechterframe = Frame(master=root)
#rechterframe.pack(side=RIGHT)

#linkerframe = Frame(master=root)
#linkerframe.pack(side=LEFT)


Randomize = Button(master=root, text='nieuwe superheld', command=clicked2)
Randomize.pack(pady=10)

InvoerButton = Button(master=root, text='       Invoer       ', command=clicked)
InvoerButton.pack(pady=10,ipadx=50)
#de Hint button
HintButton = Button(master=root, text='        Hint       ', command=clicked3)
HintButton.pack(pady=10, ipadx=50)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)


root.mainloop() # toon het hoofdscherm


