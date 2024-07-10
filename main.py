import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
from tkinter import *
from math import *
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label.config(text= "TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    label3.config(text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_rest = SHORT_BREAK_MIN * 60
    long_rest = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_rest)
        label.config(text = "BREAK", fg= RED)
    if reps % 2 == 0:
        count_down(short_rest)
        label.config(text = "BREAK", fg= PINK)
    else:
        count_down(work_sec)
        label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    timer_min = floor(count / 60)
    timer_sec= count % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"

    canvas.itemconfig(timer_text, text= f"{timer_min}:{timer_sec}")
    if count > 0:
        global timer
        timer= window.after(1000, count_down, count -1)
    else:
        start_timer()
        check = ""
        math_session = math.floor(reps/2)
        for i in range(math_session):
            check += "✔️"
            label3.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
canvas = Canvas(height= 200, width= 223, bg= YELLOW, highlightthickness= 0)
window.title("Pomodoro")
window.config(padx= 150, pady= 100, bg= YELLOW)
image_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 87, image= image_png)
timer_text =canvas.create_text(100, 110, text= "00:00", font= (FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)
#Timer heading
fg= GREEN
label = Label(text= "Timer", fg= GREEN,bg= YELLOW,  font= (FONT_NAME, 35, "bold"))
label.grid(row=0, column=1)
#start button
button = Button(text= "START", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command= start_timer)
button.grid(row= 4, column=0)
#reset button
button2 = Button(text= "RESET", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command= reset_timer)
button2.grid(row=4, column=2)
#checkmark label
label3= Label(bg=YELLOW, fg= GREEN, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
label3.grid(row=5, column=1)














window.mainloop()