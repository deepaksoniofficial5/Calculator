from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='grey')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=19, bg='#ccddff', font=('Times New Roman',28), textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text='(', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda:self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', font=('Times New Roman', 10), relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', font=('Times New Roman', 10), relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', font=('Times New Roman', 10), relief='flat', command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()