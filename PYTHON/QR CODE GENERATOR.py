from tkinter import *
import os
import pyqrcode

window = Tk()
window.title("QR Code Generator")

def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showinfo("Please enter url ")
    try:
        showcode()
    except:
        pass

def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + Subject.get())

def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            qr.png(os.path.join(dir,name.get()+".png"),scale=8)
        else:
            messagebox.showinfo("Please enter a File Name")
    except:
        messagebox.showinfo("Generate the QR code first!")

Sub = Label(window,text="Enter subject")
Sub.grid(row =0,column =0,sticky=N+S+W+E)

FName = Label(window,text="Enter FileName")
FName.grid(row =1,column =0,sticky=N+S+W+E)

Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject)
SubEntry.grid(row =0,column =1,sticky=N+S+W+E)

name = StringVar()
nameEntry = Entry(window,textvariable = name)
nameEntry.grid(row =1,column =1,sticky=N+S+W+E)

button = Button(window,text = "Generate",width=15,command = generate)
button.grid(row =0,column =3,sticky=N+S+W+E)

imageLabel = Label(window)
imageLabel.grid(row =2,column =1,sticky=N+S+W+E)

subLabel = Label(window,text="")
subLabel.grid(row =3,column =1,sticky=N+S+W+E)

saveB = Button(window,text="Save as PNG",width=15,command = save)
saveB.grid(row =1,column =3,sticky=N+S+W+E)

#making this resposnsive
Rows = 3
Columns = 3

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)
 
window.mainloop()

