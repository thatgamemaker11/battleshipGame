import tkinter as tk

def disp():
    root = tk.Tk()
    root.configure(bg="black")
    root.title("Battleship")
    root.geometry("600x600")


    # var = tk.StringVar()
    # var.set("Welcome to battleship")
    # label = tk.Label(root, textvariable=var, font=("TkDefaultFont", 60), bg = "grey", fg="white")
    # label.place(x=500, y=90, anchor="center")


    def Row1():
        print("Row 1 button clicked!")
        # Add more actions for Row 1

    def Row2():
        print("Row 2 button clicked!")
        # Add more actions for Row 2

    def Row3():
        print("Row 3 button clicked!")
        # Add more actions for Row 3

    def Row4():
        print("Row 4 button clicked!")
        # Add more actions for Row 4

    def Row5():
        print("Row 5 button clicked!")
        # Add more actions for Row 5
    #========================================================
    def RowA():
        print("Button 'a' clicked!")

    def RowB():
        print("Button 'b' clicked!")

    def RowC():
        print("Button 'c' clicked!")

    def RowD():
        print("Button 'd' clicked!")

    def RowE():
        print("Button 'e' clicked!")
    a = tk.Button(root, text="a", command=RowA, font=("TkFixedFont", 20), bg="red", fg="white")
    a.place(x=100, y=0, anchor="nw")

    b = tk.Button(root, text="b", command=RowB, font=("TkFixedFont", 20), bg="red", fg="white")
    b.place(x=200, y=0, anchor="nw")

    c = tk.Button(root, text="c", command=RowC, font=("TkFixedFont", 20), bg="red", fg="white")
    c.place(x=300, y=0, anchor="nw")

    d = tk.Button(root, text="d", command=RowD, font=("TkFixedFont", 20), bg="red", fg="white")
    d.place(x=400, y=0, anchor="nw")

    e = tk.Button(root, text="e", command=RowE, font=("TkFixedFont", 20), bg="red", fg="white")
    e.place(x=500, y=0, anchor="nw")


    One = tk.Button(root, text="1", command=Row1 , font=(("TkFixedFont",20)), bg="red", fg="white")
    One.place(x=0, y=100, anchor="nw")

    Two = tk.Button(root, text="2", command=Row2 , font=(("TkFixedFont",20)), bg="red", fg="white")
    Two.place(x=0, y=200, anchor="nw")

    Three = tk.Button(root, text="3", command=Row3, font=("TkFixedFont", 20), bg="red", fg="white")
    Three.place(x=0, y=300, anchor="nw")

    Four = tk.Button(root, text="4", command=Row4, font=("TkFixedFont", 20), bg="red", fg="white")
    Four.place(x=0, y=400, anchor="nw")

    Five = tk.Button(root, text="5", command=Row5, font=("TkFixedFont", 20), bg="red", fg="white")
    Five.place(x=0, y=500, anchor="nw")
    #==========================================================================
    text = "ammo left:"+"[]"
    mTEXT = "misses:" + "[]"

    ammo = tk.StringVar()
    ammo.set(text)
    label = tk.Label(root, textvariable=ammo, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=450, y=300, anchor="center")

    misses = tk.StringVar()
    misses.set(mTEXT)
    label = tk.Label(root, textvariable=misses, font=("TkDefaultFont", 20), bg = "black", fg="white")
    label.place(x=450, y=350, anchor="center")




    root.mainloop()

disp()