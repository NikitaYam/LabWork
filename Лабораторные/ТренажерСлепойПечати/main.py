import tkinter as tk
from tkinter.font import Font
import random as rd

class Worder(tk.Tk):

    def __init__(self):

        self.wrline = '...'

        self.colors = {True:'lime', False:'red', None:'yellow'}

        super().__init__()

        self.title('Тренажор Слепой Печати')
        self.configure(bg='black', borderwidth=10, border=10, relief='groove')
        self.geometry('500x250')

        self.write = tk.StringVar()
        self.text = tk.Text(self,bg='grey', width=45, height=1, fg='yellow', border=5, font=Font(family='Times', size=15))
        self.text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.text.bind('<KeyRelease>', self.check_line)

        self.newl_b = tk.Button(self, text='Новая строка', width=20, height=1, bg='grey', fg='yellow')
        self.newl_b.bind('<Button-1>', self.new_line)
        self.newl_b.place(relx=0.5, rely=0.7, anchor=tk.N)

        self.check_btn = tk.Button(self, text='Проверка', width=10, height=1, bg='grey', fg='yellow')
        self.check_btn.bind('<Button-1>', self.check_line)
        self.check_btn.place(relx=0.15, rely=0.7, anchor=tk.N)

        self.line = tk.Label(self, text=self.wrline, fg='yellow', bg='black', font=Font(family='Times', size=15))
        self.line.place(relx=0.5, rely=0.4, anchor=tk.S)

        self.author = tk.Label(self, text= 'by Terrapod', fg='yellow', bg='black', font=Font(family='Times', size=10))
        self.author.place(relx=0.155, rely=0.055, anchor=tk.E)


        self.mainloop()

    def new_line(self, event):
        sush = open('alf/sush', encoding='utf_8_sig').readline().split(' ')
        glag = open('alf/glag', encoding='utf_8_sig').readline().split(' ')
        pril = open('alf/pril', encoding='utf_8_sig').readline().split(' ')
        nare = open('alf/Nare', encoding='utf_8_sig').readline().split(' ')
        self.wrline = f'{pril[rd.randint(0, len(pril)-1)]} {sush[rd.randint(0, len(sush)-1)]} {nare[rd.randint(0, len(nare)-1)]} {glag[rd.randint(0, len(glag)-1)]}'
        self.line.configure(text = self.wrline)
        self.text.delete('1.0', tk.END)

    def check_line(self, event):
        if event.char == self.wrline[len(self.text.get('1.0', tk.END))]:
            # attach a tag (the character itself) if the character is in the colormap
            event.widget.tag_add(event.char, 'insert-1c')
            self.text.tag_config(event.char, foreground=self.colors[True])


window = Worder()
