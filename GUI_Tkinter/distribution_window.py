from tkinter import *
import distribution

class Dist_Window:

    def uniform_func(self):
        self.lower = int(self.lower_input.get())
        self.upper = int(self.upper_input.get())
        self.uniform_obj = distribution.Uni_dist(self.lower, self.upper)
        self.dist_obj1 = distribution.Animated_histo(self.uniform_obj)
        self.dist_obj1.start()
        self.lower_input.delete(0, END)
        self.upper_input.delete(0, END)

    def exp_func(self):
        self.power = int(self.exp_input.get())
        self.exp_obj = distribution.Exp_dist(self.power)
        self.dist_obj2 = distribution.Animated_histo(self.exp_obj)
        self.dist_obj2.start()
        self.exp_input.delete(0, END)

    def __init__(self, dist):
        self.dist = dist
        self.window = Tk()


        if self.dist == 1:
            self.window.title("Uniform Distribution")
            self.window.geometry("820x600")
            self.window.configure(bg='black')

            self.heading = Label(self.window, text="Uniform Distribution", pady=10, font=("Helvetica", 16), bg="black", fg="cyan")
            self.frame1 = LabelFrame(self.window, text="What is Continuous Uniform Distribution?", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
            self.describe = Label(self.frame1, bg="black", fg="cyan", text="The uniform distribution is a continuous probability distribution and is concerned with \nevents that are equally likely to occur. The continuous random variable X is said to be \nuniformly distributed, or having rectangular distribution on the interval [a,b]. We write \nX∼U(a,b), if its probability density function equals f(x)=1/b−a,x∈[a,b] and 0 elsewhere", font=("Helvetica", 11))

            self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
            self.step1 = Label(self.frame2, text="To plot Uniform Distribution, there is a parent class named Distribution.", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step2 = Label(self.frame2, text="And there is a child class named 'Uniform_Distribution'.\n", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step3 = Label(self.frame2, text="Step 1: Input the lower and upper limits of the interval", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step4 = Label(self.frame2, text="Step 2: Uniform_Distribution child class passes the list of randomly generated", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step5 = Label(self.frame2, text="intervals of continuous values to the Distribution parent class.", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step6 = Label(self.frame2, text="Step 3: Then these intervals that are equally probable are plotted\n", font=("Helvetica", 11), bg="black", fg="cyan")

            self.upper_label = Label(self.window, text="Enter the upper limit", font=("Helvetica", 11), bg="black", fg="yellow")
            self.upper_input = Entry(self.window, width=15)
            self.lower_label = Label(self.window, text="Enter the lower limit", font=("Helvetica", 11), bg="black", fg="yellow")
            self.lower_input = Entry(self.window, width=15)
            self.uniform_button = Button(self.window, text="Animate", command=self.uniform_func, padx=10, pady=10, font=("Helvetica", 11), width=10, bg="black", fg="yellow")

            self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=4, padx=30)
            self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=10, rowspan=3)
            self.describe.grid(row=1, column=0, sticky=W)

            self.frame2.grid(row=4, column=0, rowspan=7, columnspan=4, padx=30, pady=5, sticky=W)
            self.step1.grid(row=5, column=0, sticky=W)
            self.step2.grid(row=6, column=0, sticky=W)
            self.step3.grid(row=7, column=0, sticky=W)
            self.step4.grid(row=8, column=0, sticky=W)
            self.step5.grid(row=9, column=0, sticky=W)
            self.step6.grid(row=10, column=0, sticky=W)


            self.lower_label.grid(row=1, column=5, pady=5)
            self.lower_input.grid(row=2, column=5, ipady=2, pady=5)
            self.upper_label.grid(row=3, column=5, pady=5)
            self.upper_input.grid(row=4, column=5, ipady=2, pady=5)
            self.uniform_button.grid(row=5, column=5, pady=5)

        elif self.dist == 2:
            self.window.title("Exponential Distribution")
            self.window.geometry("820x600")
            self.window.configure(bg='black')

            self.heading = Label(self.window, text="Exponential Distribution", pady=10, font=("Helvetica", 16), bg="black", fg="cyan")
            self.frame1 = LabelFrame(self.window, text="What is Continuous Exponential Distribution?", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
            self.describe = Label(self.frame1, bg="black", fg="cyan", text="The exponential distribution is a continuous probability distribution used to model the   \ntime we need to wait before a given event occurs. Sometimes it is also called negative \nexponential distribution. The probability distribution function f(x) = λexp(-λx) for all x>=0.", font=("Helvetica", 11))

            self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
            self.step1 = Label(self.frame2, text="To plot Exponential Distribution, there is a parent class named Distribution.", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step2 = Label(self.frame2, text="And a child class named 'Exponential_Distribution'.\n", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step3 = Label(self.frame2, text="Step 1: Input the lambda 'λ' value. λ = 1/E(X), where X is the continuous random", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step4 = Label(self.frame2, text="variable and E(X) is the mean value of the distribution", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step5 = Label(self.frame2, text="Step 2: The x value is given as λ+10", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step6 = Label(self.frame2, text="Step 3: The value returned by the child class Exponential_Distribution", font=("Helvetica", 11), bg="black", fg="cyan")
            self.step7 = Label(self.frame2, text="is passed to the parent class Distribution to plot exponential distribution", font=("Helvetica", 11), bg="black", fg="cyan")

            self.exp_label = Label(self.window, text="Enter the limit", font=("Helvetica", 11), bg="black", fg="yellow")
            self.exp_input = Entry(self.window, width=18)
            self.exp_button = Button(self.window, text="Animate", width=10, command=self.exp_func, padx=10, pady=10, font=("Helvetica", 11), bg="black", fg="yellow")

            self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=2, padx=30)
            self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=10, rowspan=2)
            self.describe.grid(row=1, column=0, sticky=W)

            self.frame2.grid(row=3, column=0, rowspan=7, padx=30, pady=5, sticky=W, columnspan=2)
            self.step1.grid(row=3, column=0, sticky=W)
            self.step2.grid(row=4, column=0, sticky=W)
            self.step3.grid(row=5, column=0, sticky=W)
            self.step4.grid(row=6, column=0, sticky=W)
            self.step5.grid(row=7, column=0, sticky=W)
            self.step6.grid(row=8, column=0, sticky=W)
            self.step6.grid(row=9, column=0, sticky=W)
            self.step7.grid(row=10, column=0, sticky=W)

            self.exp_label.grid(row=1, column=3, pady=5, padx=10)
            self.exp_input.grid(row=2, column=3, pady=5, ipady=2, padx=10)
            self.exp_button.grid(row=3, column=3, pady=5, padx=10)

        self.window.mainloop()


# object = Dist_Window(2)
