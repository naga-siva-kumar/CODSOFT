from tkinter import *
from tkinter import messagebox
from string import *
import random
from pyperclip import *
def pass_Generator():
    s_letters=ascii_lowercase
    C_letters=ascii_uppercase
    Digits=digits
    Spl_char=punctuation
    Allchar=s_letters+C_letters+Digits+Spl_char
    # print(Allchar)
    Length=int(pass_Spinbox.get())
    if Choice.get() ==1:
        display_pass.insert(0,random.sample(s_letters,Length))
    if Choice.get()==2:
        display_pass.insert(0,random.sample(s_letters+C_letters+Digits,Length))
    if Choice.get()==3:
        display_pass.insert(0,random.sample(Allchar,Length))

def reset():
    global var
    var=" "
    display_pass.delete(0,END)

def Copy():
    var1=display_pass.get()
    copy(var1)
    messagebox.showinfo(title="Message",message="**Message copied! Successfully! **")

win=Tk()
win.config(bg="Orange")
# Font=("Arial",12,"bold")
Password_Generator=Label(win,text="Password Generator",bg="orange",fg="Blue",font=("Arial",25,"bold"))
Password_Generator.grid()
Choice=IntVar()
Weak_Radio=Radiobutton(win,text="Weak",value=1,variable=Choice,font=("Arial",12,"bold"))
Weak_Radio.grid(pady=5)
medium_Radio=Radiobutton(win,text="Medium",value=2,variable=Choice,font=("Arial",12,"bold"))
medium_Radio.grid(pady=5)
strong_Radio=Radiobutton(win,text="Strong",value=3,variable=Choice,font=("Arial",12,"bold"))
strong_Radio.grid(pady=5)
pass_Len=Label(win,text="Password Length",fg="white",bg="black",font=("Arial",12))
pass_Len.grid(pady=15)
pass_Spinbox=Spinbox(win,from_=5,to=20,font=("Arial",15))
pass_Spinbox.grid(pady=5)
generate_button=Button(win,text="Generate",font=("Arial",12,"bold"),command=pass_Generator)
generate_button.grid(pady=5)
display_pass=Entry(win,font=("Arial",15,"bold"))
display_pass.grid(pady=15)

Reset_button=Button(win,text="Reset",command=reset,font=("Arial",13,"bold"))
Reset_button.grid(pady=5)
Copy_button=Button(win,text="Copy",font=("Arial",13,"bold"),command=Copy)
Copy_button.grid()
win.mainloop()