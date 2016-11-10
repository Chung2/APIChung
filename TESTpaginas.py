from tkinter import *
from tkinter.messagebox import showinfo
from API_test_marvel import *


def toonVenster():
    gebruiker = entry_1.get()

    def close():
        subwindow.withdraw()
    subwindow = Toplevel(master=root)

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

    subwindow.configure(background='#C92D39')



    #button 2
    def clicked2():
        print("Hello")
        pass
    #button 3
    def clicked3():
        T = Text(subwindow,height=8, width=50)
        T.pack(side=RIGHT,fill=Y)
        T.insert(END, BeschrijvingHeld2)
        bericht = BeschrijvingHeld2
        showinfo(title='hint1', message=bericht)

        pass

    #label = Label(master=root,
    #             text=BeschrijvingHeld2,
    #            background='red',
    #           font=('Helvetica', 10, 'bold italic'),
    #          height=10,
    #           width=100)
    #label.pack()




    label2 = Label(master=subwindow,
              text=entry_1.get(),
              background='red',
              font=('Helvetica', 10, 'bold italic'),
              height=3)
    label2.pack()

    #rechterframe = Frame(master=subwindow)
    #rechterframe.pack(side=RIGHT)

    #linkerframe = Frame(master=subwindow)
    #linkerframe.pack(side=LEFT)


    Randomize = Button(master=subwindow, text='nieuwe superheld', command=clicked2)
    Randomize.pack(pady=10)

    InvoerButton = Button(master=subwindow, text='       Invoer       ', command=clicked)
    InvoerButton.pack(pady=10,ipadx=50)
    #de Hint button
    HintButton = Button(master=subwindow, text='        Hint       ', command=clicked3)
    HintButton.pack(pady=10, ipadx=50)

    BackButton = Button(master=subwindow, text='Back', command=close)
    BackButton.pack(side=BOTTOM,padx=10, pady=10)

    entry = Entry(master=subwindow)
    entry.pack(padx=10, pady=10)

    subwindow.mainloop() # toon het hoofdscherm




root = Tk()
root.configure(background='#C92D39')
logo = PhotoImage(file="Marvel_Beginscherm.gif")
label_logo = Label(root, image=logo).pack()
entry_1 = Entry(master=root)
entry_1.pack(padx=10, pady=10)

StartButton = Button(master=root, text="Start", command=toonVenster)
StartButton.pack()

root.mainloop()
