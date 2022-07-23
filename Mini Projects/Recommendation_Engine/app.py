import tkinter as tk
import pygame
import time
import tkinter.messagebox as msg

def main_clock(total_minutes,heading,message):
    total_secs = int(total_minutes * 60)
    while True:
        sec = total_secs%60
        min = total_secs//60
        #min, sec = divmod(total_secs,60)
        time.sleep(1)
        label_time.config(text=f"{min}:{sec}")
        total_secs = total_secs-1
        if total_secs < 0:
            pygame.mixer.music.play(1)
            msg.showinfo(heading, message)
            break
        root.update()

def work_clock():
    main_clock(25,"Take a Break", "Click the break button to start the break timer")

def break_clock():
    main_clock(5,"Go back to work", "Click the work button to start the work timer")

try:
    pygame.mixer.init()
    pygame.mixer.music.load("sound.ogg")
except pygame.error:
    print("Download sound.ogg or add any .ogg music file")

root = tk.Tk()
root.geometry("300x300+470+180")
root.resizable(False, False)
root.title("Pomodoro")

canvas = tk.Canvas(bg="red")
canvas.place(x=-1, y=-1, width=330, height=330)

label_time = tk.Label(text="25:00",font=("arial",80,"bold"))
label_time.pack(fill="y",pady=20,padx=6)

work = tk.Button(text="Work", command=work_clock,bg="blue",fg="white",bd=4,font=("arial",18,"bold")).place(x=50, y=220)
take_a_break = tk.Button(text="Break", command=break_clock,bg="blue",fg="white",bd=4,font=("arial",18,"bold")).place(x=160, y=220)

root.mainloop()