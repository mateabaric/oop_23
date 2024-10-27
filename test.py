from klase.auti import *
from klase.bicikli import *
from klase.busevi import *
from klase.kamioni import *
from klase.motocikli import *
from klase.traktori import *
from tkinter import *


def trazi_busevi(e,izbor):
    L_gradski=[
        Gradski('prijevoz ljudi iz sela prema gradu',50,12,15),
        Gradski('prijevoz po gradu',55,35,20)]
    L_turist=[
        Turistički('prijevoz između gradova',70,'zatvoreni','ima'),
        Turistički('prijevoz po gradu',30,'otvoreni','nema'),
        Turistički('prijevoz po gradu',60,'otvoreni','ima')]
    kapacitet=int(e.get())

    novi=Toplevel(p)
    Label(novi,text='Rezultati pretraživanja:').pack()
    if izbor.get()==1:
        for i in range(len(L_gradski)):
            if L_gradski[i].k>=kapacitet:
                Label(novi,text=L_razgl[i]).pack()
    else:
        for i in range(len(L_turist)):
            if L_turist[i].k>=kapacitet:
                Label(novi,text=L_izl[i]).pack()
    novi.mainloop()

def test_busevi():
    l=Label(p,text='Unesi podatke o busu')
    l.grid(row=0,column=0)
    l=Label(p,text='Vrsta busa:')
    l.grid(row=1,column=0)
    izbor=IntVar()
    Radiobutton(p,variable=izbor,text='Gradski',value=1).grid(row=1,column=1)
    Radiobutton(p,variable=izbor,text='Turistički',value=2).grid(row=1,column=2)
    l=Label(p,text='Broj osoba:')
    l.grid(row=2,column=0)
    e=Entry(p, width=20)
    e.grid(row=2,column=1)
    b=Button(p,text='PRETRAZI',command=lambda:trazi_busevi(e,izbor))
    b.grid(row=3,column=0)

def trazi_kamioni(e,izbor):
    L_šlep=[
        Šleper(12,'prijevoz prehrambenih proizvoda','hrana','hladnjača'),
        Šleper(14,'prijevoz teške opreme','čelik','s platformom')]
    L_autotrans=[
        Autotransporter(13.5,'prijevoz rabljenih vozila',1,'otvorena'),
        Autotransporter(16,'prijevoz luksuznih vozila',2,'zatvorena'),
        Autotransporter(10,'prijevoz motocikala',2,'s rampom'),]
    dužina=int(e.get())

    novi=Toplevel(p)
    Label(novi,text='Rezultati pretraživanja:').pack()
    if izbor.get()==1:
        for i in range(len(L_šlep)):
            if L_šlep[i].d>=dužina:
                Label(novi,text=L_šlep[i]).pack()
    else:
        for i in range(len(L_turist)):
            if L_turist[i].k>=kapacitet:
                Label(novi,text=L_izl[i]).pack()
    novi.mainloop()

def test_busevi():
    l=Label(p,text='Unesi podatke o busu')
    l.grid(row=0,column=0)
    l=Label(p,text='Vrsta busa:')
    l.grid(row=1,column=0)
    izbor=IntVar()
    Radiobutton(p,variable=izbor,text='Gradski',value=1).grid(row=1,column=1)
    Radiobutton(p,variable=izbor,text='Turistički',value=2).grid(row=1,column=2)
    l=Label(p,text='Broj osoba:')
    l.grid(row=2,column=0)
    e=Entry(p, width=20)
    e.grid(row=2,column=1)
    b=Button(p,text='PRETRAZI',command=lambda:trazi_busevi(e,izbor))
    b.grid(row=3,column=0)


if __name__=='__main__':
    p=Tk()
    p.geometry('600x300+100+100')
    menibar=Menu(p)
    podmeni=Menu(menibar)
    podmeni.add_command(label='Busevi', command=test_busevi)
    podmeni.add_command(label='Putovanja',command=test_putovanja)
    podmeni.add_command(label='Smještaj',underline= 1, command=test_smjestaj)
    podmeni.add_command(label="Izlaz", underline= 1, command= exit, accelerator= "Ctrl+Q")
    menibar.add_cascade(label='Izbornik', menu=podmeni)
    p.config(menu=menibar)
    test_aktivnosti()
    p.mainloop()
