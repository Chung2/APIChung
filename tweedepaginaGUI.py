from tkinter import *
from tkinter.messagebox import showinfo
from API_test_marvel import *
import textwrap
import random

root = Tk()   # maakt het hoofdscherm

lijst1 = result
NaamHeld = lijst1[0].get('name')
IdHeld = lijst1[0].get('id')
BeschrijvingHeld = lijst1[0].get('description')


#if NaamHeld == 'Iron Man':
   # BeschrijvingHeld2 = BeschrijvingHeld.replace('Tony Stark', '-----')
  #  if NaamHeld in BeschrijvingHeld2:
 #       BeschrijvingHeld2 = BeschrijvingHeld.replace(NaamHeld, '-----')

if NaamHeld in BeschrijvingHeld:
    BeschrijvingHeld2 = BeschrijvingHeld.replace(NaamHeld, '-----')



# pop-up checked of iron man wordt opgegeven
def clicked():
    invoer = entry.get()
    if invoer == NaamHeld:
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
    label = Label(master=root,
              text=BeschrijvingHeld2,
              background='red',
              font=('Helvetica', 10, 'bold italic'),
              height=10,
                width=100,
              wraplength = 500 )
    label.pack()




label = Label(master=root,
              text='Hint#1',
              background='red',
              command=clicked3(),
              font=('Helvetica', 10, 'bold italic'),
              height=3)
label.pack()

#labeltext= textwrap.fill(labeltext,width=30)

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


