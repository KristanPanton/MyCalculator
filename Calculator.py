from tkinter import *
from tkinter.ttk import *
import math


class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("MyCalc")
        master.geometry()

        # self.bgcolor = "#232235"
        self.bgcolor = "#111218"

        # self.fgcolor = "#1F8FAA"
        # self.fgcolor = "#FE4A49"
        self.fgcolor = "#7699E5"

        # self.bgsecondary = "#327DFF"
        # self.bgsecondary = "#092B34"
        self.bgsecondary = "#2C3858"

        self.master = master
        self.master.bind('<Return>', self.equals)
        # Modifies the background color of the window
        self.master.configure(bg=self.fgcolor)

        self.result = 0
        self.expression = ""
        self.newtext = ""
        self.hasCalculated = False
        self.invalidInStr = "Invalid Input!"

        self.btn_style = Style()
        self.entry_style = Style()

        self.btn_style.theme_use("clam")
        self.btn_style.configure("TButton", font=("calibri", 18, "bold"), foreground=self.fgcolor,
                                 background=self.bgcolor,
                                 relief="flat",
                                 padding=[0, 20]
                                 )
        self.btn_style.map("TButton",
                           foreground=[("pressed", self.fgcolor), ("active", self.bgcolor)],
                           background=[("pressed", "!disabled", self.bgsecondary), ("active", self.fgcolor)],
                           )

        self.entry_style.configure("TEntry",
                                   background=self.bgcolor,
                                   foreground=self.fgcolor,
                                   fieldbackground="#111218",
                                   selectbackground=self.fgcolor,
                                   selectforeground="#111218",
                                   borderwidth=0
                                   )

        self.e = Entry(self.master, style="TEntry", justify=RIGHT, width=22, font=("calibri", 30))
        self.e.grid(row=0, column=0, columnspan=6, sticky="ew")
        self.e.focus_set()

        self.create_buttons()

    def insert_character(self, arg):
        """Inserts the corresponding pressed button's character into the text box"""
        if self.invalidInStr in self.e.get():
            self.e.delete(0, END)
        if self.e.get() == "" and arg == ".":
            arg = "0."
        if arg not in "+-x÷%.()" and self.hasCalculated:
            self.e.delete(0, END)

        self.hasCalculated = False
        self.e.insert(END, arg)

    def square(self):
        self.replace_character()
        try:
            self.result = eval("math.pow(" + self.newtext + ", 2)")
            self.hasCalculated = True
        except SyntaxError or NameError or TypeError:
            self.e.delete(0, END)
            self.e.insert(END, self.invalidInStr)
        else:
            self.e.delete(0, END)
            self.e.insert(END, self.result)
            print("Entries:", self.newtext, "=", self.result)

    def square_root(self):
        self.replace_character()
        try:
            self.result = eval("math.sqrt(" + self.newtext + ")")
            self.hasCalculated = True
        except SyntaxError or NameError or TypeError:
            self.e.delete(0, END)
            self.e.insert(END, self.invalidInStr)
        else:
            self.e.delete(0, END)
            self.e.insert(END, self.result)
            print("Entries:", self.newtext, "=", self.result)

    def replace_character(self):
        """Replaces division and multiplication operators."""
        self.expression = self.e.get()
        self.newtext = self.expression.replace("x", "*")
        self.newtext = self.newtext.replace("÷", "/")
        self.newtext = self.newtext.replace("²", "**2")

    def equals(self, e=None):
        self.replace_character()
        try:
            self.result = eval(self.newtext)
            self.hasCalculated = True
        except SyntaxError or NameError or TypeError:
            self.e.delete(0, END)
            self.e.insert(END, self.invalidInStr)
        else:
            self.e.delete(0, END)
            self.e.insert(END, self.result)
            print("Entries:", self.newtext, "=", self.result)

    def delete_character(self):
        """Deletes last character from the text box"""

        # Get text
        text = self.e.get()

        # Clear text box
        self.e.delete(0, END)

        if self.invalidInStr == text:
            return

        # Reinsert text - last character
        self.e.insert(END, text[:-1])

    def clear_entry(self):
        """Clears the textbox"""
        self.e.delete(0, END)
        self.hasCalculated = False

    def create_buttons(self):
        """Generates buttons"""
        Button(self.master, text="=",
               style="TButton",
               command=self.equals).grid(
            row=4, column=4, columnspan=2, sticky="ew")

        Button(self.master, text="AC", width=5,
               style="TButton",
               command=self.clear_entry).grid(row=1, column=4, sticky="ew")

        Button(self.master, text="DEL", width=5,
               style="TButton",
               command=self.delete_character).grid(row=1, column=5, sticky="ew")

        Button(self.master, text="+", width=5,
               style="TButton",
               command=lambda: self.insert_character("+")).grid(row=4, column=3, sticky="ew")

        Button(self.master, text="x", width=5,
               style="TButton",
               command=lambda: self.insert_character("x")).grid(row=2, column=3, sticky="ew")

        Button(self.master, text="-", width=5,
               style="TButton",
               command=lambda: self.insert_character("-")).grid(row=3, column=3, sticky="ew")

        Button(self.master, text="÷", width=5,
               style="TButton",
               command=lambda: self.insert_character("÷")).grid(row=1, column=3, sticky="ew")

        Button(self.master, text="%", width=5,
               style="TButton",
               command=lambda: self.insert_character("%")).grid(row=4, column=2, sticky="ew")

        Button(self.master, text="7", width=5,
               style="TButton",
               command=lambda: self.insert_character("7")).grid(row=1, column=0, sticky="ew")

        Button(self.master, text="8", width=5,
               style="TButton",
               command=lambda: self.insert_character("8")).grid(row=1, column=1, sticky="ew")

        Button(self.master, text="9", width=5,
               style="TButton",
               command=lambda: self.insert_character("9")).grid(row=1, column=2, sticky="ew")

        Button(self.master, text="4", width=5,
               style="TButton",
               command=lambda: self.insert_character("4")).grid(row=2, column=0, sticky="ew")

        Button(self.master, text="5", width=5,
               style="TButton",
               command=lambda: self.insert_character("5")).grid(row=2, column=1, sticky="ew")

        Button(self.master, text="6", width=5,
               style="TButton",
               command=lambda: self.insert_character("6")).grid(row=2, column=2, sticky="ew")

        Button(self.master, text="1", width=5,
               style="TButton",
               command=lambda: self.insert_character("1")).grid(row=3, column=0, sticky="ew")

        Button(self.master, text="2", width=5,
               style="TButton",
               command=lambda: self.insert_character("2")).grid(row=3, column=1, sticky="ew")

        Button(self.master, text="3", width=5,
               style="TButton",
               command=lambda: self.insert_character("3")).grid(row=3, column=2, sticky="ew")

        Button(self.master, text="0", width=5,
               style="TButton",
               command=lambda: self.insert_character("0")).grid(row=4, column=0, sticky="ew")

        Button(self.master, text=".", width=5,
               style="TButton",
               command=lambda: self.insert_character(".")).grid(row=4, column=1, sticky="ew")

        Button(self.master, text="(", width=5,
               style="TButton",
               command=lambda: self.insert_character("(")).grid(row=2, column=4, sticky="ew")

        Button(self.master, text=")", width=5,
               style="TButton",
               command=lambda: self.insert_character(")")).grid(row=2, column=5, sticky="ew")

        Button(self.master, text="√", width=5,
               style="TButton",
               command=self.square_root).grid(row=3, column=4, sticky="ew")

        Button(self.master, text="x²", width=5,
               style="TButton",
               command=self.square).grid(row=3, column=5, sticky="ew")


root = Tk()

# Instantiates Calculator
app = Calculator(master=root)

# Updates winfo width and height
root.update()
# Changes the minimum size of the window
root.minsize(root.winfo_width(), root.winfo_height() + 4)
root.resizable(0, 0)

app.mainloop()
