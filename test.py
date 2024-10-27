
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
                Label(novi,text=L_gradski[i]).pack()
    else:
        for i in range(len(L_turist)):
            if L_turist[i].k>=kapacitet:
                Label(novi,text=L_turist[i]).pack()
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
        Autotransporter(10,'prijevoz motocikala',2,'s rampom')]
    dužina=int(e.get())

    novi=Toplevel(p)
    Label(novi,text='Rezultati pretraživanja:').pack()
    if izbor.get()==1:
        for i in range(len(L_šlep)):
            if L_šlep[i].d>=dužina:
                Label(novi,text=L_šlep[i]).pack()
    else:
        for i in range(len(L_autotrans)):
            if L_autotrans[i].d>=dužina:
                Label(novi,text=L_autotrans[i]).pack()
    novi.mainloop()

def test_kamioni():
    l=Label(p,text='Unesi podatke o kamionu')
    l.grid(row=0,column=0)
    l=Label(p,text='Vrsta kamiona:')
    l.grid(row=1,column=0)
    izbor=IntVar()
    Radiobutton(p,variable=izbor,text='Šleper',value=1).grid(row=1,column=1)
    Radiobutton(p,variable=izbor,text='Autotransporter',value=2).grid(row=1,column=2)
    l=Label(p,text='Dužina kamiona:')
    l.grid(row=2,column=0)
    e=Entry(p, width=20)
    e.grid(row=2,column=1)
    b=Button(p,text='PRETRAZI',command=lambda:trazi_kamioni(e,izbor))
    b.grid(row=3,column=0)

def trazi_motocikli(e,izbor):
    L_sport=[
        Sportski('200 km/h','15 000 eura','147 kW','Suzuki'),
        Sportski('240 km/h','22 000 eura','147 kW','Yamaha'),
        Sportski('300 km/h','30 000 eura','168 kW','Kawasaki')]
    L_cruiser=[
        Cruiser('160 km/h','17 000 eura','65 cm','1984. godina'),
        Cruiser('140 km/h','9 500 eura','69 cm','2005. godina'),
        Cruiser('190 km/h','14 000 eura','64 cm','1920. godina')]
    brzina=e.get().strip()

    if not brzina:
        showerror("Greška", "Unesite brzinu!")
        return

    novi=Toplevel(p)
    Label(novi,text='Rezultati pretraživanja:').pack()
    if izbor.get()==1:
        for i in range(len(L_sport)):
            if L_sport[i].b==brzina:
                Label(novi,text=L_sport[i]).pack()
    else:
        for i in range(len(L_cruiser)):
            if L_cruiser[i].b==brzina:
                Label(novi,text=L_cruiser[i]).pack()
    novi.mainloop()

def test_motocikli():
    l=Label(p,text='Unesi podatke o motociklu')
    l.grid(row=0,column=0)
    l=Label(p,text='Vrsta motocikla:')
    l.grid(row=1,column=0)
    izbor=IntVar()
    Radiobutton(p,variable=izbor,text='Sportski',value=1).grid(row=1,column=1)
    Radiobutton(p,variable=izbor,text='Cruiser',value=2).grid(row=1,column=2)
    l=Label(p,text='Brzina:')
    l.grid(row=2,column=0)
    e=Entry(p, width=20)
    e.grid(row=2,column=1)
    b=Button(p,text='PRETRAZI',command=lambda:trazi_motocikli(e,izbor))
    b.grid(row=3,column=0)


def trazi_traktori(e,izbor):
    L_poljoprivredni=[
        Poljoprivredni('1000 kg','rad na žitu','John Deere 6M Series','50 KS'),
        Poljoprivredni('980 kg','rad na kukuruzima','New Holland T8','100 KS'),
        Poljoprivredni('1500 kg','rad na bućama','Fendt 700 Vario','200 KS')]
    L_vinogradarski=[
        Vinogradarski('1599 kg','rad u vinogradima','5000 eur','50 L'),
        Vinogradarski('600 kg','rad u vinogradima','35000 eur','100 L'),
        Vinogradarski('500 kg','rad u vinogradima','9000 eur','70 L')]

    novi=Toplevel(p)
    Label(novi,text='Rezultati pretraživanja:').pack()
    if izbor.get()==1:
        for i in range(len(L_poljoprivredni)):
            if L_poljoprivredni[i].b==brzina:
                Label(novi,text=L_poljoprivredni[i]).pack()
    else:
        for i in range(len(L_vinogradarski)):
            if L_vinogradarski[i].b==brzina:
                Label(novi,text=L_vinogradarski[i]).pack()
    novi.mainloop()

def test_traktori():
    l=Label(p,text='Unesi podatke o traktoru')
    l.grid(row=0,column=0)
    l=Label(p,text='Vrsta traktora:')
    l.grid(row=1,column=0)
    izbor=IntVar()
    Radiobutton(p,variable=izbor,text='Poljoprivredni',value=1).grid(row=1,column=1)
    Radiobutton(p,variable=izbor,text='Vinogradski',value=2).grid(row=1,column=2)
    l=Label(p,text='težina')
    l.grid(row=2,column=0)
    e=Entry(p, width=20)
    e.grid(row=2,column=1)
    b=Button(p,text='PRETRAZI',command=lambda:trazi_traktori(e,izbor))
    b.grid(row=3,column=0)

if __name__=='__main__':
    p=Tk()
    p.geometry('600x300+100+100')
    menibar=Menu(p)
    podmeni=Menu(menibar)
    podmeni.add_command(label='Busevi', command=test_busevi)
    podmeni.add_command(label='Kamioni',command=test_kamioni)
    podmeni.add_command(label='Motocikli',command=test_motocikli)
    podmeni.add_command(label='Traktori',command=test_traktori)
    podmeni.add_command(label="Izlaz", underline= 1, command= exit, accelerator= "Ctrl+Q")
    menibar.add_cascade(label='Izbornik', menu=podmeni)
    p.config(menu=menibar)
    test_busevi()
    test_kamioni()
    test_motocikli()
    test_traktori()
    p.mainloop()
