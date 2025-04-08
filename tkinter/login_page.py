import tkinter as tk
win=tk.Tk()
win.title("login page")
win.geometry("400x300")
your_username="admin"
your_passwoed="1234"
def check():
    if your_username==username.get() and your_passwoed==password.get():
        sresult=tk.Label(win, text="You sucssesfully logged in", fg="green", font=("Cooper black",14,"bold")).place(x=80,y=220)    
    else:
        fresult=tk.Label(win, text="username or password is incorrect", fg="red", font=("Cooper black",12,"bold")).place(x=70,y=220)
wellcome=tk.Label(win, text="login page", fg="purple", font=("Pristina",22,"bold")).place(x=150,y=25)
username_text=tk.Label(win, text="Username:", fg="black", font=("Cooper black",10,"bold")).place(x=100,y=90)
password_text=tk.Label(win, text="Password:", fg="black", font=("Cooper black",10,"bold")).place(x=100,y=120)
username=tk.Entry(win)
username.place(x=200,y=92.5)
password=tk.Entry(win)
password.place(x=200,y=122.5)
login_btn=tk.Button(win, text="login", bg="purple", fg="white", font=("Cooper black",12), width=7, command=check).place(x=165,y=160)
win.mainloop()