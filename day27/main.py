from tkinter import *
# cal
def cal():
    to_Km["text"]=str(int(input_Miles.get())*1.609)

# window / title
window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)

# input
input_Miles=Entry(width=10)
input_Miles.grid(column=1,row=0)

# label
Km=Label(text="Km")
Km.grid(column=2,row=1)
Km.config(padx=20,pady=20)

Miles=Label(text="Miles")
Miles.grid(column=2,row=0)
Miles.config(padx=20,pady=20)

equal=Label(text="is qual to")
equal.grid(column=0,row=1)
equal.config(padx=20,pady=20)

to_Km=Label(text="   ")
to_Km.grid(column=1,row=1)
to_Km.config(padx=20,pady=20)

# button
button=Button()
button=Button(text='Calculate',command=cal,height=1 ,width=5)
button.grid(column=1,row=2)
button.config(padx=20,pady=20)

window.mainloop()