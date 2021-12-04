from tkinter import *
from math import *

def Calculatrice():

    window = Tk()
    boite=Frame(window,bg='#008DFF')
    boite2=Frame(window,bg='#008DFF')
    window.title('Calculatrice')

    def pourcent():
        contenu = champs.get() + '%'
        champs.delete(0, contenu)
        champs.insert(END, contenu)
    def A0():
        contenu = champs.get() + '0'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A1():
        contenu = champs.get() + '1'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A2():
        contenu = champs.get() + '2'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A3():
        contenu = champs.get() + '3'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A4():
        contenu = champs.get() + '4'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A5():
        contenu = champs.get() + '5'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A6():
        contenu = champs.get() + '6'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A7():
        contenu = champs.get() + '7'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A8():
        contenu = champs.get() + '8'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def A9():
        contenu = champs.get() + '9'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def paranGauche():
        contenu = champs.get() + '('
        champs.delete(0, END)
        champs.insert(END, contenu)
    def paranDroite():
        contenu = champs.get() + ')'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def pi():
        contenu = champs.get() + 'π'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def c():
        champs.delete(0, END)
    def plus():
        contenu = champs.get() + '+'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def moins():
        contenu = champs.get() + '-'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def diviser():
        contenu = champs.get() + '/'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def fois():
        contenu = champs.get() + 'x'
        champs.delete(0, END)
        champs.insert(END, contenu)
    def égale():
        contenu = champs.get()
        contenu = contenu.replace("π", "3.14")
        contenu = contenu.replace("x", "*")
        résultat = str(eval(contenu))
        champs.delete(0, END)
        champs.insert(0, résultat)

    #Déclaration des boutons
    Bpi=Button(boite2,text='π',bg='white',fg='black',font=('Arial',15),command=pi)
    Bpourcent=Button(boite2,text='%',bg='white',fg='black',font=('Arial',15),command=pourcent)
    BParangauche=Button(boite2,text='(',bg='white',fg='black',font=('Arial',15),command=paranGauche)
    BParandroite=Button(boite2,text=')',bg='white',fg='black',font=('Arial',15),command=paranDroite)
    B1=Button(boite2,text='1',bg='white',fg='black',font=('Arial',15),command=A1)
    B2=Button(boite2,text='2',bg='white',fg='black',font=('Arial',15),command=A2)
    B3=Button(boite2,text='3',bg='white',fg='black',font=('Arial',15),command=A3)
    B4=Button(boite2,text='4',bg='white',fg='black',font=('Arial',15),command=A4)
    B5=Button(boite2,text='5',bg='white',fg='black',font=('Arial',15),command=A5)
    B6=Button(boite2,text='6',bg='white',fg='black',font=('Arial',15),command=A6)
    B7=Button(boite2,text='7',bg='white',fg='black',font=('Arial',15),command=A7)
    B8=Button(boite2,text='8',bg='white',fg='black',font=('Arial',15),command=A8)
    B9=Button(boite2,text='9',bg='white',fg='black',font=('Arial',15),command=A9)
    B0=Button(boite2,text='0',bg='white',fg='black',font=('Arial',15),command=A0)
    BPlus=Button(boite2,text='+',bg='white',fg='black',font=('Arial',15),command=plus)
    Bmoins=Button(boite2,text='-',bg='white',fg='black',font=('Arial',15),command=moins)
    Bdiviser=Button(boite2,text='/',bg='white',fg='black',font=('Arial',15),command=diviser)
    Bfois=Button(boite2,text='x',bg='white',fg='black',font=('Arial',15),command=fois)
    Bégale=Button(boite2,text='=',bg='white',fg='black',font=('Arial',15),command=égale)
    Bc=Button(boite2,text='C',bg='white',fg='black',font=('Arial',15),command=c)
    champs=Entry(boite,text='Sa',fg='white',bg ="white",font=('Arial',15))
    champs.pack(expand=YES,pady=10, padx=5)
    B9.grid(row=2 , column=2,pady=5,padx=5)
    B8.grid(row=2 , column=1,pady=5,padx=5)
    B7.grid(row=2 , column=0,pady=5,padx=5)
    B6.grid(row=3 , column=2,pady=5,padx=5)
    B5.grid(row=3 , column=1,pady=5,padx=5)
    B4.grid(row=3 , column=0,pady=5,padx=5)
    B3.grid(row=4 , column=2,pady=5,padx=5)
    B2.grid(row=4 , column=1,pady=5,padx=5)
    B1.grid(row=4 , column=0,pady=5,padx=5)
    B0.grid(row=5 , column=0,pady=5,padx=5)
    BPlus.grid(row=2 , column=3,padx=5)
    Bégale.grid(row=5 , column=2,padx=5)
    Bmoins.grid(row=3 , column=3,padx=5)
    Bfois.grid(row=4 , column=3,padx=5)
    Bdiviser.grid(row=5 , column=3,padx=5)
    Bc.grid(row=5 , column=1,padx=5)
    BParangauche.grid(row=2 , column=4,pady=5,padx=5)
    BParandroite.grid(row=2 , column=5,pady=5,padx=5)
    Bpi.grid(row=3 , column=4,pady=5,padx=5)

    boite.pack(side=TOP, fill = X)
    boite2.pack()

    window.mainloop()