from klase.auti import *
from klase.bicikli import *
from klase.busevi import *
from klase.kamioni import *
from klase.motocikli import *
from klase.traktori import *
from tkinter import *

def trazi_auto(e,izbor):
    L_pickup=[
        Pickup(4,'prijevoz tereta',2,'3000 kg'),
        Pickup(4,'obiteljski prijevoz',2,'1000 kg'),
        Pickup(4,'kampiranje',2,'2000 kg')]
    broj_vrata=int(e.get())
    
    L_SUV=[
        SUV(4,'obiteljska', '30 000 USD', '170 cm'),
        SUV(4,'terenska', '40 000 USD', '185 cm'),
        SUV(4,'vlačenje prikolica', '55 000 USD', '190 cm')]
    broj_kotača=int(e.get())
    
    L_Limuzina=[
        SUV(4,'vjenčanja', '7 m', 'bijela'),
        SUV(4,'parti', '8 m', 'crna'),
        SUV(4,'luksuzna', '10 m', 'crvena')]
     broj_kotača=int(e.get())
   
    novi=Toplevel(p)
    Label(novi,text='Rezultati pretraživanja:').pack()
    if izbor.get()==1:
        for i in range(len(L_Pickup)):
            if L_Pickup[i].k>=broj_kotača:
                Label(novi,text=L_Pickup[i]).pack()
    else:
        for i in range(len(L_SUV)):
            if L_SUV[i].k>=broj_kotača:
                Label(novi,text=L_SUV[i]).pack()
    else:
        for i in range(len(L_Limuzina)):
            if L_Limuzina[i].k>=broj_kotača:
                Label(novi,text=L_Limuzina[i]).pack()
    novi.mainloop()

def test_Auto():
    l=Label(p,text='Unesi podatke o autu')
    l.grid(row=0,column=0)
    l=Label(p,text='Vrsta auta:')
    l.grid(row=1,column=0)
    izbor=IntVar()
    Radiobutton(p,variable=izbor,text='Pickup',value=1).grid(row=1,column=1)
    Radiobutton(p,variable=izbor,text='SUV',value=2).grid(row=1,column=2)
    Radiobutton(p,variable=izbor,text='Limuzina',value=2).grid(row=1,column=2)
    l=Label(p,text='Broj kotača:')
    l.grid(row=2,column=0)
    e=Entry(p, width=20)
    e.grid(row=2,column=1)
    b=Button(p,text='PRETRAZI',command=lambda:trazi_auto(e,izbor))
    b.grid(row=3,column=0)
def test_Pickup():
    l = Label(p, text='Pretraži Pickup aute')
    l.grid(row=0, column=0, columnspan=3)

    l = Label(p, text='Broj kotača:')
    l.grid(row=1, column=0)
    e = Entry(p, width=20)
    e.grid(row=1, column=1)

    b = Button(p, text='PRETRAŽI', command=lambda: trazi_auto(e, None, 'Pickup'))
    b.grid(row=2, column=0, columnspan=2)

def test_SUV():
    l = Label(p, text='Pretraži SUV aute')
    l.grid(row=0, column=0, columnspan=3)

    l = Label(p, text='Broj kotača:')
    l.grid(row=1, column=0)
    e = Entry(p, width=20)
    e.grid(row=1, column=1)

    b = Button(p, text='PRETRAŽI', command=lambda: trazi_auto(e, None, 'SUV'))
    b.grid(row=2, column=0, columnspan=2)

def test_Limuzina():
    l = Label(p, text='Pretraži Limuzine')
    l.grid(row=0, column=0, columnspan=3)

    l = Label(p, text='Broj kotača:')
    l.grid(row=1, column=0)
    e = Entry(p, width=20)
    e.grid(row=1, column=1)

    b = Button(p, text='PRETRAŽI', command=lambda: trazi_auto(e, None, 'Limuzina'))
    b.grid(row=2, column=0, columnspan=2)




def trazi_bicikl(e,izbor):
    L_pickup=[
        Pickup(4,'prijevoz tereta',2,'3000 kg'),
        Pickup(4,'obiteljski prijevoz',2,'1000 kg'),
        Pickup(4,'kampiranje',2,'2000 kg')]
    broj_vrata=int(e.get())
    
    L_SUV=[
        SUV(4,'obiteljska', '30 000 USD', '170 cm'),
        SUV(4,'terenska', '40 000 USD', '185 cm'),
        SUV(4,'vlačenje prikolica', '55 000 USD', '190 cm')]
    broj_kotača=int(e.get())
    
    L_Limuzina=[
        SUV(4,'vjenčanja', '7 m', 'bijela'),
        SUV(4,'parti', '8 m', 'crna'),
        SUV(4,'luksuzna', '10 m', 'crvena')]
     broj_kotača=int(e.get())
   
    novi=Toplevel(p)
    Label(novi,text='Rezultati pretraživanja:').pack()
    if izbor.get()==1:
        for i in range(len(L_Pickup)):
            if L_Pickup[i].k>=broj_kotača:
                Label(novi,text=L_Pickup[i]).pack()
    else:
        for i in range(len(L_SUV)):
            if L_SUV[i].k>=broj_kotača:
                Label(novi,text=L_SUV[i]).pack()
    else:
        for i in range(len(L_Limuzina)):
            if L_Limuzina[i].k>=broj_kotača:
                Label(novi,text=L_Limuzina[i]).pack()
    novi.mainloop()

def test_Auto():
    l=Label(p,text='Unesi podatke o autu')
    l.grid(row=0,column=0)
    l=Label(p,text='Vrsta auta:')
    l.grid(row=1,column=0)
    izbor=IntVar()
    Radiobutton(p,variable=izbor,text='Pickup',value=1).grid(row=1,column=1)
    Radiobutton(p,variable=izbor,text='SUV',value=2).grid(row=1,column=2)
    Radiobutton(p,variable=izbor,text='Limuzina',value=2).grid(row=1,column=2)
    l=Label(p,text='Broj kotača:')
    l.grid(row=2,column=0)
    e=Entry(p, width=20)
    e.grid(row=2,column=1)
    b=Button(p,text='PRETRAZI',command=lambda:trazi_auto(e,izbor))
    b.grid(row=3,column=0)
def test_Pickup():
    l = Label(p, text='Pretraži Pickup aute')
    l.grid(row=0, column=0, columnspan=3)

    l = Label(p, text='Broj kotača:')
    l.grid(row=1, column=0)
    e = Entry(p, width=20)
    e.grid(row=1, column=1)

    b = Button(p, text='PRETRAŽI', command=lambda: trazi_auto(e, None, 'Pickup'))
    b.grid(row=2, column=0, columnspan=2)

def test_SUV():
    l = Label(p, text='Pretraži SUV aute')
    l.grid(row=0, column=0, columnspan=3)

    l = Label(p, text='Broj kotača:')
    l.grid(row=1, column=0)
    e = Entry(p, width=20)
    e.grid(row=1, column=1)

    b = Button(p, text='PRETRAŽI', command=lambda: trazi_auto(e, None, 'SUV'))
    b.grid(row=2, column=0, columnspan=2)

def test_Limuzina():
    l = Label(p, text='Pretraži Limuzine')
    l.grid(row=0, column=0, columnspan=3)

    l = Label(p, text='Broj kotača:')
    l.grid(row=1, column=0)
    e = Entry(p, width=20)
    e.grid(row=1, column=1)

    b = Button(p, text='PRETRAŽI', command=lambda: trazi_auto(e, None, 'Limuzina'))
    b.grid(row=2, column=0, columnspan=2)

if __name__=='__main__':
    p=Tk()
    p.geometry('600x300+100+100')
    menibar=Menu(p)
    podmeni=Menu(menibar)
    podmeni.add_command(label='Aktivnosti', command=test_aktivnosti)
    podmeni.add_command(label='Putovanja',command=test_putovanja)
    podmeni.add_command(label='Smještaj',underline= 1, command=test_smjestaj)
    podmeni.add_command(label="Izlaz", underline= 1, command= exit, accelerator= "Ctrl+Q")
    menibar.add_cascade(label='Izbornik', menu=podmeni)
    p.config(menu=menibar)
    test_aktivnosti()
    p.mainloop()
