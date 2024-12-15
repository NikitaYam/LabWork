import tkinter as tk

class Proga(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Записная книжка')
        self.geometry("700x700")
        self.configure(background='black')

        self.dela = []

        self.text = tk.Text(self, background='grey', height=20, width=75, borderwidth=10)
        self.text.anchor(tk.CENTER)
        self.text.pack()

        self.btn_show = tk.Button(self, text='Показать')
        self.btn_show.anchor(tk.CENTER)
        self.btn_show.place(x=50, y=600)

    def dob(self, a:str):
        self.dela.append(a)

    def ubr(self, a:int):
        self.dela.pop(a-1)

    def show(self):
        for i in range(0, len(self.dela)):
            print(i+1, self.dela[i])

    def reshow(self):
        a = ''
        for i in range(0, len(self.dela)):
            a+=f'{i} {self.dela[i]} {'\n'}'
        self.text.edit(a)

a = Proga()
a.mainloop()