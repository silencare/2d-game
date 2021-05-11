from tkinter import *
import threading


def start1():
    okno.resizable(width=True, height=True)
    import main.py

def start_duo1():
    okno.resizable(width=True, height=True)
    import main2.py


x = threading.Thread(target=start_duo1)
y = threading.Thread(target=start1)

def start():
    y.start()

def start_duo():
    x.start()

okno=Tk()
okno.geometry('1270x720')
okno.wm_title('road traveler')
okno.resizable(width=False, height=False)

img = PhotoImage(file='tlo3.png')


bg=Label(okno, image=img)
bg.place(x=-10,y=-10)

logo = Label(okno, width=30, height=3, bg="red", text="Road Traveler") 
logo.config(font=("Arial", 40))
logo.place(x=160,y=10)

guzik1=Button(okno, bg='green', bd=0, width=10, height=1, text="jeden gracz")             
guzik1.config(font=("Arial", 25))
guzik1['command'] = start
guzik1.place(x=550,y=250)

guzik2=Button(okno, bg="purple", bd=0, width=10, height=1, text="dwóch graczy")
guzik2.config(font=("Arial", 25))
guzik2['command'] = start_duo
guzik2.place(x=550,y=350)

guzik3=Button(okno, bg="red", bd=0, width=10, height=1, text="wyjście")
guzik3.config(font=("Arial", 25))
guzik3['command'] = quit
guzik3.place(x=550,y=450)

okno.mainloop()






              
