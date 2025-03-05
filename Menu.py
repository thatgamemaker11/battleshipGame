import tkinter as tk


import info


def welcome():
    root = tk.Tk()
    root.configure(bg="grey")
    root.title("Welcome")
    root.geometry("1000x600")


    var = tk.StringVar()
    var.set("Welcome to battleship")
    label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 60), bg = "grey", fg="white")
    label.place(x=500, y=90, anchor="center")

    def diff1():
        global diff
        diff = 1
        root.destroy()
        import game
        info.info(1)

    def diff2():
        global diff
        diff = 2
        root.destroy()
        import game
        info.info(2)

    def diff3():
        global diff
        diff = 3
        root.destroy()
        import game
        info.info(3)





    One = tk.Button(root, text="Easy", command=diff1 , font=(("TkFixedFont",44)), bg="orange", fg="white")
    One.place(x=200, y=300, anchor="center")

    Two = tk.Button(root, text="Medium", command=diff2, font=(("TkFixedFont", 44)), bg="orange", fg="white")
    Two.place(x=500, y=300, anchor="center")

    Thr = tk.Button(root, text="Hard", command=diff2, font=(("TkFixedFont", 44)), bg="orange", fg="white")
    Thr.place(x=800, y=300, anchor="center")





    root.mainloop()

