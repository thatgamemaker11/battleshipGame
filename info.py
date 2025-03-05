import tkinter as tk

def info(diff):
    root = tk.Tk()
    root.configure(bg="black")
    root.title("Battleship")
    root.geometry("600x600")


    def cont():
        root.destroy()
        import game
        game.main()

        # Add more actions for Row 1

    cont = tk.Button(root, text="Continue", command=cont, font=("TkFixedFont", 20), bg="red", fg="white")
    cont.place(x=300, y=500, anchor="center")

    #==========================================================================
    text1 = "Welcome to battleship"
    text2 = "The Submarine takes 3 hits to sink"
    text3 = "Red = HIT     White = MISS"
    text4 = "Once you have"
    text5 = "[]"
    text6 = "Misses the game is over"


    var = tk.StringVar()
    var.set(text1)
    label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=300, y=100, anchor="center")

    var = tk.StringVar()
    var.set(text2)
    label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=300, y=150, anchor="center")

    var = tk.StringVar()
    var.set(text3)
    label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=300, y=220, anchor="center")

    var = tk.StringVar()
    var.set(text4)
    label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=300, y=300, anchor="center")

    var = tk.StringVar()
    var.set(text5)
    label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=300, y=350, anchor="center")

    var = tk.StringVar()
    var.set(text6)
    label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=300, y=400, anchor="center")


    root.mainloop()

