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

        root.after(1000, countdown)


def check(event):
    global start_writing

    if start_writing:
        reset_timer()

    else:
        start_writing = True
        countdown()


def reset_timer():
    global timer
    timer = 0


def delete():
    text.delete("1.0", tk.END)
    reset_timer()


root = tk.Tk()
root.title("Disappearing Text Writing App")
root.geometry("1000x600")

label = tk.Label(root, text="Disappearing Text App", font=("Arial", 24))
label.pack(pady=20)


text = tk.Text(root, font=("Arial", 16), wrap="word", height=20, width=80)
text.pack(padx=20, pady=20)

text.bind("<KeyPress>", check)


root.mainloop()
