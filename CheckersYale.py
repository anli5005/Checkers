import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.red_sqr = 'red4'
        self.black_sqr = 'black'
        self.loadimage = tk.PhotoImage(file="Red_Circle.png")
        self.loadimage2 = tk.PhotoImage(file='greycircle2.png')
        self.loadimage3 = tk.PhotoImage(file='transparent.png')

        self.a1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=0, column=0, sticky=tk.W)
        self.a2 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr)
        self.a2.grid(row=0, column=1, sticky=tk.W)
        self.a3 = tk.Button(self, width=4, height=2, background=self.red_sqr)
        self.a3.grid(row=0, column=2, sticky=tk.W)
        self.a4 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr)
        self.a4.grid(row=0, column=3, sticky=tk.W)
        self.a5 = tk.Button(self, width=4, height=2, background=self.red_sqr)
        self.a5.grid(row=0, column=4, sticky=tk.W)
        self.a6 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr)
        self.a6.grid(row=0, column=5, sticky=tk.W)
        self.a7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=0, column=6, sticky=tk.W)
        self.a8 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr)
        self.a8.grid(row=0, column=7, sticky=tk.W)
        self.b1 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr).grid(row=1, column=0, sticky=tk.W)
        self.b2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=1, sticky=tk.W)
        self.b3 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr).grid(row=1, column=2, sticky=tk.W)
        self.b4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=3, sticky=tk.W)
        self.b5 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr).grid(row=1, column=4, sticky=tk.W)
        self.b6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=5, sticky=tk.W)
        self.b7 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr).grid(row=1, column=6, sticky=tk.W)
        self.b8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=7, sticky=tk.W)
        self.c1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=0, sticky=tk.W)
        self.c2 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr, command=self.movec2)
        self.c2.grid(row=2, column=1, sticky=tk.W)
        self.c3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=2, sticky=tk.W)
        self.c4 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr, command=self.movec4)
        self.c4.grid(row=2, column=3, sticky=tk.W)
        self.c5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=4, sticky=tk.W)
        self.c6 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr)
        self.c6.grid(row=2, column=5, sticky=tk.W)
        self.c7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=6, sticky=tk.W)
        self.c8 = tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr)
        self.c8.grid(row=2, column=7, sticky=tk.W)
        self.d1 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=3, column=0, sticky=tk.W)
        self.d2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=1, sticky=tk.W)
        self.d3 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=3, column=2, sticky=tk.W)
        self.d4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=3, sticky=tk.W)
        self.d5 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=3, column=4, sticky=tk.W)
        self.d6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=5, sticky=tk.W)
        self.d7 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=3, column=6, sticky=tk.W)
        self.d8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=7, sticky=tk.W)
        self.e1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=0, sticky=tk.W)
        self.e2 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=4, column=1, sticky=tk.W)
        self.e3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=2, sticky=tk.W)
        self.e4 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=4, column=3, sticky=tk.W)
        self.e5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=4, sticky=tk.W)
        self.e6 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=4, column=5, sticky=tk.W)
        self.e7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=6, sticky=tk.W)
        self.e8 = tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=4, column=7, sticky=tk.W)
        self.f1 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=5, column=0, sticky=tk.W)
        self.f2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=1, sticky=tk.W)
        self.f3 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=5, column=2, sticky=tk.W)
        self.f4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=3, sticky=tk.W)
        self.f5 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=5, column=4, sticky=tk.W)
        self.f6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=5, sticky=tk.W)
        self.f7 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=5, column=6, sticky=tk.W)
        self.f8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=7, sticky=tk.W)
        self.g1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=0, sticky=tk.W)
        self.g2 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=6, column=1, sticky=tk.W)
        self.g3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=2, sticky=tk.W)
        self.g4 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=6, column=3, sticky=tk.W)
        self.g5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=4, sticky=tk.W)
        self.g6 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=6, column=5, sticky=tk.W)
        self.g7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=6, sticky=tk.W)
        self.g8 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=6, column=7, sticky=tk.W)
        self.h1 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=7, column=0, sticky=tk.W)
        self.h2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=1, sticky=tk.W)
        self.h3 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=7, column=2, sticky=tk.W)
        self.h4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=3, sticky=tk.W)
        self.h5 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=7, column=4, sticky=tk.W)
        self.h6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=5, sticky=tk.W)
        self.h7 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr).grid(row=7, column=6, sticky=tk.W)
        self.h8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=7, sticky=tk.W)

    def movec2(self):
        if self.c2['image'] == 'Red_Circle.png':
            self.c2.configure(image=self.loadimage2)
        elif self.c2['image'] == 'greycircle2.png':
            self.c2.configure(image=self.loadimage)
        else:
            self.c2.configure(image=self.loadimage3)

    def movec4(self):
        if self.c4['image'] == 'Red_Circle.png':
            self.c4.configure(image=self.loadimage2)
        elif self.c4['image'] == 'greycircle2.png':
            self.c4.configure(image=self.loadimage)
        else:
            self.c4.configure(image=self.loadimage3)



root = tk.Tk()
root.title("Checkers")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
