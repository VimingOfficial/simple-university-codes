import tkinter as tk
from tkinter import messagebox
import math

win=tk.Tk()
win.title("calculator")
win.geometry("300x370")
win.configure(background="black")

calculator_lbl=tk.Label(win,text="Calculator",fg="black",font=("cooperblack",14,"bold"),bg="light green")
calculator_lbl.pack()




result_lbl=tk.Entry(win,text="0",fg="black",font=("Cooperblack",14,"bold"))
result_lbl.place(x=150,y=54,anchor="center",height=35)

def num_entry(a):
    result_lbl.insert(tk.END,a)

def delete():
    result_lbl.delete(0,tk.END)

def calcute(event=None):
    try:
        res = result_lbl.get()
        f_res = eval(res)
        result_lbl.delete(0, tk.END)
        result_lbl.insert(0, f_res)
    except ZeroDivisionError:
        messagebox.showerror(title="Erorr", message="can't divide by zero")
    except:
        messagebox.showerror(title="Erorr", message="Please enter number")

win.bind("<Return>", calcute)

num1_btn=tk.Button(win,text="1",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(1))
num1_btn.place(x=39,y=230,height=50,width=50)
num2_btn=tk.Button(win,text="2",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(2))
num2_btn.place(x=89,y=230,height=50,width=50)
num3_btn=tk.Button(win,text="3",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(3))
num3_btn.place(x=139,y=230,height=50,width=50)
num4_btn=tk.Button(win,text="4",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(4))
num4_btn.place(x=39,y=180,height=50,width=50)
num5_btn=tk.Button(win,text="5",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(5))
num5_btn.place(x=89,y=180,height=50,width=50)
num6_btn=tk.Button(win,text="6",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(6))
num6_btn.place(x=139,y=180,height=50,width=50)
num7_btn=tk.Button(win,text="7",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(7))
num7_btn.place(x=39,y=130,height=50,width=50)
num8_btn=tk.Button(win,text="8",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(8))
num8_btn.place(x=89,y=130,height=50,width=50)
num9_btn=tk.Button(win,text="9",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(9))
num9_btn.place(x=139,y=130,height=50,width=50)
num0_btn=tk.Button(win,text="0",font=("Cooper black",14,"bold"),bg="grey",command=lambda: num_entry(0))
num0_btn.place(x=89,y=280,height=50,width=50)

sin_btn=tk.Button(win, text="sin", font=("Cooper black", 12, "bold"),bg="orange",command=lambda: num_entry("math.sin(")).place(x=39,y=78,height=50,width=50)
cos_btn=tk.Button(win, text="cos", font=("Cooper black", 12, "bold"),bg="orange",command=lambda: num_entry("math.cos(")).place(x=89,y=78,height=50,width=50)
tan_btn=tk.Button(win, text="tan", font=("Cooper black", 12, "bold"),bg="orange",command=lambda: num_entry("math.tan(")).place(x=139,y=78,height=50,width=50)
parantez1_btn=tk.Button(win, text="(", font=("Cooper black", 12, "bold"),bg="orange",command=lambda: num_entry("(")).place(x=192,y=78,height=50,width=35)
parantez2_btn=tk.Button(win, text=")", font=("Cooper black", 12, "bold"),bg="orange",command=lambda: num_entry(")")).place(x=227,y=78,height=50,width=35)


calcute_btn=tk.Button(win,text="=",font=("Cooper black",14,"bold"),bg="orange",command=lambda: calcute())
calcute_btn.place(x=139,y=280,height=50,width=50)
clear_btn=tk.Button(win,text="C",font=("Cooper black",14,"bold"),bg="orange",command=lambda:delete())
clear_btn.place(x=39,y=280,height=50,width=50)

zarb_btn=tk.Button(win,text="×",font=("Cooper black",14,"bold"),bg="orange",command=lambda : num_entry("*"))
zarb_btn.place(x=192,y=130,height=50,width=70)
taghsim_btn=tk.Button(win,text="÷",font=("Cooper black",14,"bold"),bg="orange",command=lambda : num_entry("/"))
taghsim_btn.place(x=192,y=180,height=50,width=70)
jam_btn=tk.Button(win,text="+",font=("Cooper black",14,"bold"),bg="orange",command=lambda : num_entry("+"))
jam_btn.place(x=192,y=230,height=50,width=70)
tafrigh_btn=tk.Button(win,text="-",font=("Cooper black",14,"bold"),bg="orange",command=lambda : num_entry("-"))
tafrigh_btn.place(x=192,y=280,height=50,width=70)

win.mainloop()