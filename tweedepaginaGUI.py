from tkinter import *
from tkinter.messagebox import showinfo
from API_test_marvel import *
from time import sleep

#Maakt het hoofdscherm
root = Tk()

punten = 25

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
        bericht = 'Je hebt het goed'
        showinfo(title='Goed', message=bericht)
    else:
        bericht = 'Je hebt het fout'
        punten -= 1
        showinfo(title='Fout', message=bericht)
        label3['text'] = punten

#achtergrond wordt rood gemaakt
root.configure(background='red')

label3 = Label(master=root,
              background='red',
              text=punten,
              wraplength = 500,
              height=3,
              padx = 50)
label3.grid(row=0,column=5)

#Titel label ( wordt veranderd )
Titel = Label(master=root,
              background='red',
              text='Raad het personage!',
              wraplength = 500,
              font=('Helvetica', 30, 'bold italic'),
              height=6,

              padx = 50)
Titel.grid(row=1,column=5)



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
Hint1 = Label(master=root,
              background='red',
              text='Hint 1',
              wraplength = 500,
              height=6,
              padx = 50)
Hint1.grid(row=2,column=5)
Hint2 = Label(master=root,
              background='red',
              text='Hint 2',
              wraplength = 500,
              height=3,
              padx = 50)
Hint2.grid(row=3,column=5)
Hint3 = Label(master=root,
              background='red',
              text='Hint 3',
              wraplength = 500,
              height=3,
              padx = 50)
Hint3.grid(row=4,column=5)

#bottomframe= Frame(master=root)
#bottomframe.grid(row=6,column=5)


Naam = Label(master=root,
              background='red',
              text='Hier komt de naam',   # variable waar de naam inzit met input.
              wraplength = 500,
              font=(10),
              height=6,
              padx = 50)
Naam.grid(row=3,column=0)

# de invoer button
InvoerButton = Button(master=root, text='       Enter       ', command=clicked)
InvoerButton.grid(row=6,column=6)

#de Hint button
HintButton = Button(master=root, text='        Hint       ', command=HintKnop)
HintButton.grid(row=6,column=4)

#de Help button ( spelregels )
QuestionButton = Button(master=root, text='?', command=QuestionKnop)
QuestionButton.place(x=1500,y=0)

# de entry balk (input)
entry = Entry(master=root)
entry.grid(row=5,column=5)

# toon het hoofdscherm
root.mainloop()


