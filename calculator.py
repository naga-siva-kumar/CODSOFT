import tkinter as tk
ft=""
def ad(sth):
    global ft
    ft=ft+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",ft)
def calculate():
    global ft
    result=str(eval(ft))
    field.delete("1.0", "end")
    field.insert("1.0", result)
def clear():
    global ft
    ft=""
    field.delete("1.0", "end")

window=tk.Tk()
window.geometry("300x300")
field=tk.Text(window,height=2,width=21,font=("Times New Roman",20))
field.grid(row=1,column=1,columnspan=4)
btn_1=tk.Button(window,text="1",command=lambda: ad(1),width=5,font=("Times New Roman",14))
btn_1.grid(row=4,column=1)

btn_2=tk.Button(window,text="2",command=lambda: ad(2),width=5,font=("Times New Roman",14))
btn_2.grid(row=4,column=2)

btn_3=tk.Button(window,text="3",command=lambda: ad(3),width=5,font=("Times New Roman",14))
btn_3.grid(row=4,column=3)

btn_4=tk.Button(window,text="4",command=lambda: ad(4),width=5,font=("Times New Roman",14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(window,text="5",command=lambda: ad(5),width=5,font=("Times New Roman",14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(window,text="6",command=lambda: ad(6),width=5,font=("Times New Roman",14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(window,text="7",command=lambda: ad(7),width=5,font=("Times New Roman",14))
btn_7.grid(row=2,column=1)

btn_8=tk.Button(window,text="8",command=lambda: ad(8),width=5,font=("Times New Roman",14))
btn_8.grid(row=2,column=2)

btn_9=tk.Button(window,text="9",command=lambda: ad(9),width=5,font=("Times New Roman",14))
btn_9.grid(row=2,column=3)

btn_0=tk.Button(window,text="0",command=lambda: ad(0),width=5,font=("Times New Roman",14))
btn_0.grid(row=5,column=1)
btn_plus=tk.Button(window,text="+",command=lambda: ad("+"),width=5,font=("Times New Roman",14))
btn_plus.grid(row=4,column=4)

btn_minus=tk.Button(window,text="-",command=lambda: ad("-"),width=5,font=("Times New Roman",14))
btn_minus.grid(row=5,column=4)

btn_times=tk.Button(window,text="*",command=lambda: ad("*"),width=5,font=("Times New Roman",14))
btn_times.grid(row=3,column=4)

btn_division=tk.Button(window,text="/",command=lambda: ad("/"),width=5,font=("Times New Roman",14))
btn_division.grid(row=2,column=4)

btn_clear=tk.Button(window,text="clear",command=lambda: clear(),width=5,font=("Times New Roman",14))
btn_clear.grid(row=5,column=3)

btn_decimal=tk.Button(window,text=".",command=lambda: ad("."),width=5,font=("Times New Roman",14))
btn_decimal.grid(row=5,column=2)

btn_open_parenthesis=tk.Button(window,text="(",command=lambda: ad("("),width=5,font=("Times New Roman",14))
btn_open_parenthesis.grid(row=6,column=1)

btn_close_pa=tk.Button(window,text=")",command=lambda: ad(")"),width=5,font=("Times New Roman",14))
btn_close_pa.grid(row=6,column=2)

btn_equal=tk.Button(window,text="=",command=lambda: calculate(),width=13,font=("Times New Roman",14))
btn_equal.grid(row=6,column=3,columnspan=2)

window.mainloop()
