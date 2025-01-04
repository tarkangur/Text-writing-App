import tkinter as tk


timer = 0
start_writing = False


def countdown():
    global start_writing

    if start_writing:
        global timer

        timer += 1

        if timer > 5:
            delete()
            start_writing = False

        tk.Tk.after(1000, countdown)


def reset_timer():
    global timer
    timer = 0


def delete():
    text.delete("1.0", tk.END)
    reset_timer()


root = tk.Tk()
root.title("Disappearing Text Writing App")
root.geometry("1000x600")

label = tk.Label()
label.config(text="Start", font=50)
label.pack()


text = tk.Text(font=50)
text.pack()


root.mainloop()
