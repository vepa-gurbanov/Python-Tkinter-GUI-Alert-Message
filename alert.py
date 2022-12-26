from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("1920x1080")
def msg():
    messagebox.showwarning(".rigj", "Your data is encrypted with VeraCrypt encryption tool by RIGJ Ransomware family. (C:\Program Files (x86)\RIGJ Ransomware\.rigj extension\ rigj.exe)")
en = 0
but = Button(root, text="Click to earn $1000 real cash. Don't miss!", background='red', activebackground='gray', activeforeground='white', command=msg, border='5', foreground='white', font='Consolas')
but.place(x=200, y=200)
root.mainloop()
