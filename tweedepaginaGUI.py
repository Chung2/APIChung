from tkinter import *
from tkinter.messagebox import showinfo
from API_test_marvel import *
from time import sleep
#import datetime

#Maakt het hoofdscherm
root = Tk()

# result wordt opgehaald en in een lijst gezet
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

lab = Label(root)
lab.pack()
# aantal punten bij het begin
# pop-up checked of iron man wordt opgegeven
def clicked():
    punten = 25
    invoer = entry.get()
    if invoer == NaamHeld:
        bericht = 'Je hebt het goed'
        showinfo(title='Goed', message=bericht)
    else:
        bericht = 'Je hebt het fout'
       # lab.config(text=punten)
      #  lab['text'] = punten

        punten -= 5
        showinfo(title='Fout', message=bericht)
        label3["text"] =  punten
    #root.after(1000, clicked)
    return punten
#clicked()

#achtergrond wordt rood gemaakt
root.configure(background='red')

# timer
#lab = Label(root)
#lab.pack()

#def clock():
 #   time = 0
 #   while time != 20:
     #   time += 1
     #   lab.config(text=time)
     #   lab['text'] = time
        #root.after(1000, clock) # run itself again after 1000 ms
    #sleep(1)
#  run first time
#clock()

#button 2
def clicked2():
    pass

label3 = Label(master=root,
              background='red',
              text='punten',
              wraplength = 500,
              height=3,
              padx = 50)
label3.pack()

#Titel label ( wordt veranderd )
Titel = Label(master=root,
              background='red',
              text='Raad het personage!',
              wraplength = 500,
              font=('Helvetica', 30, 'bold italic'),
              height=6,

              padx = 50)
Titel.pack()


# De Question knop
def QuestionKnop():
    bericht = "De bedoeling van het spel is dat je een Marvel Hero raadt, Je krijgt hiervoor in het begin al een zetje in de goede richting Je start met 25 punten. Een fout antwoord kost je 1 punt en een hint kost je 3 punten! Probeer zo snel mogelijk de Marvel Hero te raden om met zoveel mogelijk punten te eindigen."
    showinfo(title='Informatie', message=bericht)

# de Functie voor de hintknop
def HintKnop(punten):
    label["text"] = punten
    punten -=3
    return punten

# de Hint labellen
Hint1 = Label(master=root,
              background='red',
              text='Hint 1',
              wraplength = 500,
              height=3,
              padx = 50)
Hint1.pack()
Hint2 = Label(master=root,
              background='red',
              text='Hint 2',
              wraplength = 500,
              height=3,
              padx = 50)
Hint2.pack()
Hint3 = Label(master=root,
              background='red',
              text='Hint 3',
              wraplength = 500,
              height=3,
              padx = 50)
Hint3.pack()

# de randomize button
Randomize = Button(master=root, text='punten', command=clicked2)
Randomize.pack(pady=10)

# de invoer button
InvoerButton = Button(master=root, text='       Invoer       ', command=clicked)
InvoerButton.pack(pady=10,ipadx=50)

#de Hint button
HintButton = Button(master=root, text='        Hint       ', command=HintKnop)
HintButton.pack(pady=10, ipadx=50)

#de Help button ( spelregels )
HintButton = Button(master=root, text='?', command=QuestionKnop)
HintButton.pack(pady=10, ipadx=50)
# de entry button (input)
entry = Entry(master=root)
entry.pack(padx=10, pady=10)

# toon het hoofdscherm
root.mainloop()


