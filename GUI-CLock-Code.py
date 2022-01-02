import tkinter
import mp3play
from time import strftime

def tym():
    t = strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    lbl.after(500, tym)
    # print(temp)
    pass


clock = tkinter.Tk()
clock.config(background='black')
# photo=PhotoImage(file='test.png')
tkinter.Label(clock,bg='grey').pack()

clock.geometry('100x100')
btn = tkinter.Button(clock, text='Play Sound', bd='5', command=clock.play)
btn.pack(side='top')
btn.pack()
lbl2 = tkinter.Label(clock, text='Time is: ', foreground='white', background='black', font=('comic sans MS', 72, 'bold') )
lbl2.pack()
lbl = tkinter.Label(clock, foreground='white', background='black', font=('comic sans MS', 36, 'bold'))
tym()

clock.mainloop()

# lbl.pack(anchor="w")


    # temp = f"Current time is {t}"
    # t = "a\\nb"                      #escape sequencing
    #t = r"a\\nb"                       #raw string
