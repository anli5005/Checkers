import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        red_sqr = 'red4'
        black_sqr = 'black'
        self.loadimage = tk.PhotoImage(file="Red_Circle.png")
        self.loadimage2 = tk.PhotoImage(file='greycircle.png')

        self.a1 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=0, sticky=tk.W)
        self.a2 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=0, column=1, sticky=tk.W)
        self.a3 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=2, sticky=tk.W)
        self.a4 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=0, column=3, sticky=tk.W)
        self.a5 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=4, sticky=tk.W)
        self.a6 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=0, column=5, sticky=tk.W)
        self.a7 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=6, sticky=tk.W)
        self.a8 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=0, column=7, sticky=tk.W)
        self.b1 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=1, column=0, sticky=tk.W)
        self.b2 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=1, sticky=tk.W)
        self.b3 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=1, column=2, sticky=tk.W)
        self.b4 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=3, sticky=tk.W)
        self.b5 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=1, column=4, sticky=tk.W)
        self.b6 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=5, sticky=tk.W)
        self.b7 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=1, column=6, sticky=tk.W)
        self.b8 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=7, sticky=tk.W)
        self.c1 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=0, sticky=tk.W)
        self.c2 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=2, column=1, sticky=tk.W)
        self.c3 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=2, sticky=tk.W)
        self.c4 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=2, column=3, sticky=tk.W)
        self.c5 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=4, sticky=tk.W)
        self.a6 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=2, column=5, sticky=tk.W)
        self.c7 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=6, sticky=tk.W)
        self.c8 = tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=2, column=7, sticky=tk.W)
        self.d1 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=3, column=0, sticky=tk.W)
        self.d2 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=3, column=1, sticky=tk.W)
        self.d3 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=3, column=2, sticky=tk.W)
        self.d4 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=3, column=3, sticky=tk.W)
        self.d5 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=3, column=4, sticky=tk.W)
        self.d6 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=3, column=5, sticky=tk.W)
        self.d7 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=3, column=6, sticky=tk.W)
        self.d8 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=3, column=7, sticky=tk.W)
        self.e1 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=4, column=0, sticky=tk.W)
        self.e2 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=4, column=1, sticky=tk.W)
        self.e3 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=4, column=2, sticky=tk.W)
        self.e4 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=4, column=3, sticky=tk.W)
        self.e5 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=4, column=4, sticky=tk.W)
        self.e6 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=4, column=5, sticky=tk.W)
        self.e7 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=4, column=6, sticky=tk.W)
        self.e8 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=4, column=7, sticky=tk.W)
        self.f1 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=5, column=0, sticky=tk.W)
        self.f2 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=1, sticky=tk.W)
        self.f3 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=5, column=2, sticky=tk.W)
        self.f4 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=3, sticky=tk.W)
        self.f5 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=5, column=4, sticky=tk.W)
        self.f6 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=5, sticky=tk.W)
        self.f7 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=5, column=6, sticky=tk.W)
        self.f8 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=7, sticky=tk.W)
        self.g1 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=0, sticky=tk.W)
        self.g2 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=6, column=1, sticky=tk.W)
        self.g3 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=2, sticky=tk.W)
        self.g4 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=6, column=3, sticky=tk.W)
        self.g5 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=4, sticky=tk.W)
        self.g6 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=6, column=5, sticky=tk.W)
        self.g7 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=6, sticky=tk.W)
        self.g8 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=6, column=7, sticky=tk.W)
        self.h1 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=7, column=0, sticky=tk.W)
        self.h2 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=1, sticky=tk.W)
        self.h3 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=7, column=2, sticky=tk.W)
        self.h4 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=3, sticky=tk.W)
        self.h5 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=7, column=4, sticky=tk.W)
        self.h6 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=5, sticky=tk.W)
        self.h7 = tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=7, column=6, sticky=tk.W)
        self.h8 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=7, sticky=tk.W)

    def moveRed(self):





root = tk.Tk()
root.title("Mad Libs")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
