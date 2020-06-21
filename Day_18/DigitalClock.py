from tkinter import *
from tkinter import font
from datetime import *

def ShowClock():
    time=datetime.now()
    time=time.strftime('%H:%M:%S')
    txt.set(time)
    win.after(1000,ShowClock) 

win = Tk()
win.title("Digital Clock")
win.geometry('850x200')

win.configure(background='black')
win.after(1000,ShowClock)

fnt = font.Font(family = 'Helvetica', size = 80, weight = 'bold')

txt = StringVar()


lbl = Label(win,textvariable=txt, background='black', foreground ='white', font = fnt)
lbl.place(relx=0.5,rely=0.5,anchor =CENTER)

win.mainloop()