from tkinter import *
import inverse_transform_sampling


class Inverse_Window():
    def function(self):
        object = inverse_transform_sampling.ITS()
        object.start()


    def __init__(self):
        self.window = Tk()
        self.window.title("Inverse Transform Sampling")
        self.window.geometry("810x600")
        self.window.configure(bg="black")

        self.heading = Label(self.window, text="Inverse Transform Sampling", padx=5, pady=10, font=("Helvetica 16"), bg="black", fg="cyan")

        self.frame1 = LabelFrame(self.window, text="What is Inverse Sampling Transform?", font=("Helvetica 13"), padx=10, pady=10, bg="black", fg="yellow")
        self.describe = Label(self.frame1, text="Inverse transform sampling (also known as Inversion Sampling) is a basic method \nfor pseudo-random number sampling, i.e., for generating sample numbers at           \nrandom from any probability distribution given its cumulative distribution function.     \nThe cumulative distribution for a random variable X is FX(x)=P(X≤x).                         ", font=("Helvetica", 11), bg="black", fg="cyan")

        self.frame2 = LabelFrame(self.window, text="How is it done?", padx=5, pady=5, font=("Helvetica", 11), bg="black", fg="yellow")
        self.step1 = Label(self.frame2, text="Step 1: First, independent realizations of a randow variable is generated.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step2 = Label(self.frame2, text="Step 2: We are randomly choosing a proportion of the area under the curve", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step3 = Label(self.frame2, text="and returning the number in the domain such that exactly this proportion", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step4 = Label(self.frame2, text="of the area occurs to the left of that number.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step5 = Label(self.frame2, text="Step 3: Intuitively, we are unlikely to choose a number in the far end ", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step6 = Label(self.frame2, text="of tails because there is very little area in them which would", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step7 = Label(self.frame2, text="require choosing a number very close to zero or one. ", font=("Helvetica", 11), bg="black", fg="cyan")

        self.button = Button(self.window, text="Animate", width=13, command=self.function, pady=10, bg="black", fg="yellow", font=("Helvetica 11"))


        self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=2, padx=30)
        self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=10)
        self.describe.grid(row=1, column=0, sticky=W, pady=10)

        self.frame2.grid(row=3, column=0, rowspan=13, columnspan=2, padx=30, pady=5, sticky=W)
        self.step1.grid(row=3, column=0, sticky=W)
        self.step2.grid(row=4, column=0, sticky=W)
        self.step3.grid(row=5, column=0, sticky=W)
        self.step4.grid(row=6, column=0, sticky=W)
        self.step5.grid(row=7, column=0, sticky=W)
        self.step6.grid(row=8, column=0, sticky=W)
        self.step7.grid(row=9, column=0, sticky=W)

        self.button.grid(row=1, column=3, padx=20, pady=10)


        self.window.mainloop()


# object = Inverse_Window()
