import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # heyyyyyy gang so mr. respass told me  to work on figuring out how to get
        # an image onto a button. i worked on it all hour but, like a fool, i can't figure it out. This is the code he
        # recommended,,,, didn't really work but it was the best I could get. sorry
        # he also mentioned that we should work on compiling this whole thing into a for loop so we don't have to
        # hard code every tiny thing
        # btw - I KNOW THE CODE I DID IS A FAILURE. I REALLY DID TRY THOUGH AND AT LEAST IT'S NOT AN ERROR MESSAGE
        red_sqr = 'red4'
        black_sqr = 'black'
        self.a1 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=0, sticky=tk.W)
        picture = tk.PhotoImage(file="Red_Circle.png")
        self.a2 = tk.Label(self, image=picture, width=4, height=2, background=black_sqr)
        self.a2.photo = picture
        self.a2.grid(row=0, column=1, sticky=tk.W)
        self.a3 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=2, sticky=tk.W)
        self.a4 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=0, column=3, sticky=tk.W)
        self.a5 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=4, sticky=tk.W)
        self.a6 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=0, column=5, sticky=tk.W)
        self.a7 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=0, column=6, sticky=tk.W)
        self.a8 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=0, column=7, sticky=tk.W)
        self.b1 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=1, column=0, sticky=tk.W)
        self.b2 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=1, sticky=tk.W)
        self.b3 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=1, column=2, sticky=tk.W)
        self.b4 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=3, sticky=tk.W)
        self.b5 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=1, column=4, sticky=tk.W)
        self.b6 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=5, sticky=tk.W)
        self.b7 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=1, column=6, sticky=tk.W)
        self.b8 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=1, column=7, sticky=tk.W)
        self.c1 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=0, sticky=tk.W)
        self.c2 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=2, column=1, sticky=tk.W)
        self.c3 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=2, sticky=tk.W)
        self.c4 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=2, column=3, sticky=tk.W)
        self.c5 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=4, sticky=tk.W)
        self.c6 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=2, column=5, sticky=tk.W)
        self.c7 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=2, column=6, sticky=tk.W)
        self.c8 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=2, column=7, sticky=tk.W)
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
        self.f1 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=5, column=0, sticky=tk.W)
        self.f2 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=1, sticky=tk.W)
        self.f3 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=5, column=2, sticky=tk.W)
        self.f4 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=3, sticky=tk.W)
        self.f5 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=5, column=4, sticky=tk.W)
        self.f6 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=5, sticky=tk.W)
        self.f7 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=5, column=6, sticky=tk.W)
        self.f8 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=5, column=7, sticky=tk.W)
        self.g1 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=0, sticky=tk.W)
        self.g2 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=6, column=1, sticky=tk.W)
        self.g3 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=2, sticky=tk.W)
        self.g4 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=6, column=3, sticky=tk.W)
        self.g5 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=4, sticky=tk.W)
        self.g6 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=6, column=5, sticky=tk.W)
        self.g7 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=6, column=6, sticky=tk.W)
        self.g8 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=6, column=7, sticky=tk.W)
        self.h1 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=7, column=0, sticky=tk.W)
        self.h2 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=1, sticky=tk.W)
        self.h3 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=7, column=2, sticky=tk.W)
        self.h4 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=3, sticky=tk.W)
        self.h5 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=7, column=4, sticky=tk.W)
        self.h6 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=5, sticky=tk.W)
        self.h7 = tk.Button(self, width=4, height=2, background=black_sqr).grid(row=7, column=6, sticky=tk.W)
        self.h8 = tk.Button(self, width=4, height=2, background=red_sqr).grid(row=7, column=7, sticky=tk.W)


root = tk.Tk()
root.title("Mad Libs")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
