from tkinter import *
from datetime import datetime
temp=0
after_id=''
def tick():
    global temp, after_id
    after_id=tk.after(1000, tick)
    temp = temp + 1
    f_temp=datetime.fromtimestamp(temp).strftime('%M:%S')
    l1.configure(text=str(temp))
def start_sw():
    b1.grid_forget()
    b2.grid(row=1, columnspan=2, sticky='ew')
    tick()
tk = Tk()
tk.title('Storwatch')
l1=Label(tk, width=5, font=('Ubuntu', 100), text='00:00')
l1.grid(row=0, columnspan=2)
b1=Button(tk, text='Start', font=('Ubuntu', 30), command=start_sw)
b2=Button(tk, text='Stop', font=('Ubuntu', 30))
b3=Button(tk, text='Continue', font=('Ubuntu', 30))
b4=Button(tk, text='Reset', font=('Ubuntu', 30))
b1.grid(row=1, columnspan=2, sticky='ew')
tk.mainloop()
