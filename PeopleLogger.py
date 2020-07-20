import tkinter as tk
import time

def export():
    with open("people.txt", "a") as f:
        f.write("Name:" + Name.get() + "\n"
         + "Age:" + age.get() + "\n"
          + "Phone:" + phone.get() + "\n"
           + "Gender:" + str(v.get()) + " (1 means male, 2 means female)" + "\n"
            + "Relationship status:" + str(var.get()) + " (1 means taken, 2 means free)" + "\n")
        Name.delete(0, 'end')
        age.delete(0, 'end')
        phone.delete(0, 'end')

def clearyes():
    global clear
    with open("people.txt", "w") as f:
        f.write("")
    clear.destroy()

def no():
    global clear
    clear.destroy()

def clearconfirm():
    global clear
    clear = tk.Tk()
    clear.title("Confirm clearing data")
    tk.Label(clear, text="Do you want to earse all data?", bg="RED", height=2).grid(row=0, columnspan=2)
    yesbt = tk.Button(clear, text="Yes", fg="Dark red", command=clearyes)
    nobt = tk.Button(clear, text="No", fg="Dark green", command=no)
    nobt.grid(row=1, column=1)
    yesbt.grid(row=1, column=0)
    clear.mainloop()

main = tk.Tk()
main.title("PeopleLogger")
#labes
tk.Label(main, text="Name:").grid(row=0, column=0)
tk.Label(main, text="Age:").grid(row=1, column=0)
tk.Label(main, text="Phone:").grid(row=2, column=0)
tk.Label(main, text="gender:").grid(row=3, column=0)
tk.Label(main, text="Relationship status:").grid(row=4, column=0)
#entries
Name = tk.Entry(main)
Name.grid(row=0, column=1)
age = tk.Entry(main)
age.grid(row=1, column=1)
phone = tk.Entry(main)
phone.grid(row=2, column=1)
#Radiobuttons
v = tk.IntVar()
var = tk.IntVar()
Genderm = tk.Radiobutton(main, text="Male", value=1, variable=v)
Genderm.grid(row=3, columnspan=2, sticky="e")
Genderf = tk.Radiobutton(main, text="female", value=2, variable=v)
Genderf.grid(row=3, column=1, sticky="w")
Statusf = tk.Radiobutton(main, text="Free", value=1, variable=var)
Statusf.grid(row=4, columnspan=2, sticky="e")
Statust = tk.Radiobutton(main,text="Taken", value=2, variable=var)
Statust.grid(row=4, column=1, sticky="w")
#buttons
Save = tk.Button(main, text="save infomation", command=export)
Save.grid(row=5, columnspan=2)
Clear = tk.Button(main, text="clear all data", fg="dark red", command=clearconfirm)
Clear.grid(row=6, columnspan=2)
main.mainloop()
