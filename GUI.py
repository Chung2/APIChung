from tkinter import *
from tkinter.messagebox import showinfo
from API_test_marvel import *
from Databasemarvelscore import *

root = Tk()
punten = 25
counter = 30
datumVandaag = datetime.date.today()


def toonVenster():
    gebruiker = entry_1.get()

    def close():
        subwindow.withdraw()

    subwindow = Toplevel(master=root)

    # Maakt het hoofdscherm

    naam = gebruiker  # dit natuurlijk veranderen

    # result wordt opgehaald en in een lijst gezet
    lijst1 = result
    NaamHeld = lijst1[0].get('name')
    IdHeld = lijst1[0].get('id')
    BeschrijvingHeld = lijst1[0].get('description')

    if NaamHeld in BeschrijvingHeld:
        BeschrijvingHeld2 = BeschrijvingHeld.replace(NaamHeld, '-----')

    # aantal punten bij het begin
    # pop-up checked of iron man wordt opgegeven
    def clicked():
        global punten
        invoer = entry.get()

        if invoer == NaamHeld:
            bericht = 'Dit was het juiste antwoord!'
            print(naam, datumVandaag, str(punten))
            showinfo(title='Goed', message=bericht)
            Gegevensinvoeren(naam, datumVandaag, punten)
        else:
            bericht = 'Je hebt het fout'
            punten -= 1
            showinfo(title='Fout', message=bericht)
            label3['text'] = punten

    # achtergrond wordt rood gemaakt
    subwindow.configure(background='#C92D39')

    label3 = Label(master=subwindow,
                   background='#C92D39',
                   text=punten,
                   wraplength=500,
                   height=3,
                   padx=50)
    label3.grid(row=0, column=5)

    # Titel label ( wordt veranderd )
    logo = PhotoImage(file="background_helden.png")
    Titel = Label(master=subwindow, image=logo, background="#C92D39")

    Titel.grid(row=1, column=5)

    # functie timer (maakt hiervoor label_timer aan!!)
    def counter_label(label_timer):
        def count():
            global counter
            counter -= 1
            label_timer.config(text=str(counter))
            label_timer.after(1000, count)

        count()

    # De Question knop
    def QuestionKnop():
        bericht = "De bedoeling van het spel is dat je een Marvel Hero raadt, Je krijgt hiervoor in het begin al een zetje in de goede richting Je start met 25 punten. Een fout antwoord kost je 1 punt en een hint kost je 3 punten! Probeer zo snel mogelijk de Marvel Hero te raden om met zoveel mogelijk punten te eindigen."
        showinfo(title='Informatie', message=bericht)

    # de Functie voor de hintknop
    def HintKnop():
        global punten
        Hint1["text"] = BeschrijvingHeld2
        punten -= 3
        label3['text'] = punten

    # de Hint labellen
    Hint1 = Label(master=subwindow,
                  background='#C92D39',
                  text='Hint 1',
                  wraplength=500,
                  height=6,
                  padx=50)
    Hint1.grid(row=2, column=5)
    Hint2 = Label(master=subwindow,
                  background='#C92D39',
                  text='Hint 2',
                  wraplength=500,
                  height=3,
                  padx=50)
    Hint2.grid(row=3, column=5)
    Hint3 = Label(master=subwindow,
                  background='#C92D39',
                  text='Hint 3',
                  wraplength=500,
                  height=3,
                  padx=50)
    Hint3.grid(row=4, column=5)

    Naam = Label(master=subwindow,
                 background='#C92D39',
                 text=naam,  # variable waar de naam inzit met input.
                 wraplength=500,
                 font=(10),
                 height=6,
                 padx=50)
    Naam.grid(row=3, column=4)

    #    de invoer button
    InvoerButton = Button(master=subwindow, text='       Enter       ', command=clicked)
    InvoerButton.grid(row=6, column=6)

    # de Hint button
    HintButton = Button(master=subwindow, text='        Hint       ', command=HintKnop)
    HintButton.grid(row=6, column=4)

    # de Help button ( spelregels )
    QuestionButton = Button(master=subwindow, text='?', command=QuestionKnop)
    QuestionButton.place(x=1500, y=0)

    # de entry balk (input)
    entry = Entry(master=subwindow)
    entry.grid(row=5, column=5)

    # toon het hoofdscherm
    subwindow.mainloop()


root.configure(background='#C92D39')
logo = PhotoImage(file="Marvel_Beginscherm.gif")
label_logo = Label(root, image=logo).pack()
entry_1 = Entry(master=root)
entry_1.pack(padx=10, pady=10,)

StartButton = Button(master=root, text="Start", command=toonVenster)
StartButton.pack()

root.mainloop()
