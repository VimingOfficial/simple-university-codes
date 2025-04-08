import tkinter as tk
import random
from PIL import Image, ImageTk

win=tk.Tk()
win.title("stone paper scissors game")
win.geometry("450x600")

#image for buttons
stone_orginal=Image.open("stone.png")
stone_resized_b=stone_orginal.resize((80,80))
stone_resized_r=stone_orginal.resize((120,120))
stone_b=ImageTk.PhotoImage(stone_resized_b)
stone_r=ImageTk.PhotoImage(stone_resized_r)

paper_orginal=Image.open("paper.png")
paper_resized_b=paper_orginal.resize((80,80))
paper_resized_r=paper_orginal.resize((120,120))
paper_b=ImageTk.PhotoImage(paper_resized_b)
paper_r=ImageTk.PhotoImage(paper_resized_r)

sus_orginal=Image.open("sus.png")
sus_resized_b=sus_orginal.resize((80,80))
sus_resized_r=sus_orginal.resize((120,120))
sus_b=ImageTk.PhotoImage(sus_resized_b)
sus_r=ImageTk.PhotoImage(sus_resized_r)

original_image = Image.open("static.jpg")
resized_image = original_image.resize((120,120))
static = ImageTk.PhotoImage(resized_image)
static_lbl1=tk.Label(win, image=static)
static_lbl1.place(x=50,y=50)
static_lbl2=tk.Label(win, image=static)
static_lbl2.place(x=275,y=50)

user_static_txt=tk.Label(win,text="User:",fg="green",font=("Cooper black",12,"bold")).place(x=50,y=25)
com_static_txt=tk.Label(win,text="Computer:",fg="orange",font=("Cooper black",12,"bold")).place(x=275,y=25)

image_path=[stone_r,paper_r,sus_r]
com_result=None
com_score=0
user_score=0

def computer_choose():
    global com_result
    rand=random.choice(image_path)
    com_result=rand
    com_result_lbl=tk.Label(win, image=com_result)
    com_result_lbl.place(x=275,y=50)
    return com_result

def stone():
    global com_score,user_score
    computer_choose()
    stone_static=tk.Label(win,image=stone_r)
    stone_static.place(x=50,y=50)
    if com_result==stone_r:
        status_lbl.config(text="Draw",fg="black",font=("Cooper black",23,"bold"))
    elif com_result==paper_r:
        status_lbl.config(text="Lose",fg="red",font=("Cooper black",24,"bold"))
        com_score+=1
    else:
        status_lbl.config(text=" Win",fg="green",font=("Cooper black",24,"bold"))
        user_score+=1
    user_score_lbl.config(text=user_score)
    com_score_lbl.config(text=com_score)

def paper():
    global com_score,user_score
    computer_choose()
    paper_static=tk.Label(win,image=paper_r)
    paper_static.place(x=50,y=50)
    if com_result==stone_r:
        status_lbl.config(text=" Win",fg="green",font=("Cooper black",24,"bold"))
        user_score+=1
    elif com_result==paper_r:
        status_lbl.config(text="Draw",fg="black",font=("Cooper black",23,"bold"))
    else:
        status_lbl.config(text="Lose",fg="red",font=("Cooper black",24,"bold"))
        com_score+=1
    user_score_lbl.config(text=user_score)
    com_score_lbl.config(text=com_score)

def sus():
    global com_score,user_score
    computer_choose()
    sus_static=tk.Label(win,image=sus_r)
    sus_static.place(x=50,y=50)
    if com_result==stone_r:
        status_lbl.config(text="Lose",fg="red",font=("Cooper black",24,"bold"))
        com_score+=1
    elif com_result==paper_r:
        status_lbl.config(text=" Win",fg="green",font=("Cooper black",24,"bold"))
        user_score+=1
    else:
        status_lbl.config(text="Draw",fg="black",font=("Cooper black",23,"bold"))
    user_score_lbl.config(text=user_score)
    com_score_lbl.config(text=com_score)

status_lbl=tk.Label(win,text="----",fg="black",font=("Cooper black",40,"bold"))
status_lbl.place(x=182,y=320)
score_text_lbl=tk.Label(win,text="Scores",fg="black",font=("Cooper black",18,"bold"))
score_text_lbl.place(x=180,y=400)
user_text_lbl=tk.Label(win,text="user:",fg="green",font=("Cooper black",14,"bold"))
user_text_lbl.place(x=68,y=450)
com_text_lbl=tk.Label(win,text="computer:",fg="orange",font=("Cooper black",14,"bold"))
com_text_lbl.place(x=310,y=450)
user_score_lbl=tk.Label(win,text="0",fg="black",font=("Cooper black",40,"bold"))
user_score_lbl.place(x=72,y=495)
com_score_lbl=tk.Label(win,text="0",fg="black",font=("Cooper black",40,"bold"))
com_score_lbl.place(x=340,y=495)
# 3 btn
stone_btn=tk.Button(win,image=stone_b,command=stone)
stone_btn.place(x=50,y=210)
paper_btn=tk.Button(win,image=paper_b, command=paper)
paper_btn.place(x=180,y=210)
sus_btn=tk.Button(win,image=sus_b, command=sus)
sus_btn.place(x=310,y=210)
win.mainloop()