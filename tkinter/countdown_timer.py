import tkinter as tk
win=tk.Tk()
win.title("countdown timer")
win.geometry("300x300")
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer.config(text=time_left)
        win.after(1000, countdown)
    else:
        timer.config(text="Time's up!", fg="red", font=("cooperblack",20))
def start():
    global time_left
    time_left = int(time_input.get())
    if time_left > 0:
        countdown()
time_input=tk.Entry(win, width=20)
time_input.place(x=60,y=20)
start_btn=tk.Button(win, text="Start",command=start).place(x=200,y=16.5)
remaining_time=tk.Label(win, text="Remaining time:", fg="black", font=("Cooper black",10,"bold")).place(x=92,y=70)
timer=tk.Label(win, text="0", fg="black", font=("Cooper black",45,"bold"))
timer.place(x=130,y=120)
win.mainloop()