from tkinter import *
import monte_carlo
from PIL import ImageTk, Image

class Monte_Window:


    def monte_func(self):
        self.time_interval = int(self.monte_input.get())
        self.monte_obj = monte_carlo.Monte_carlo(self.time_interval)
        self.monte_obj.start()
        self.monte_input.delete(0, END)

    def __init__(self):
        self.window = Tk()
        self.window.title("Monte Carlo")
        self.window.geometry("800x600")
        self.window.configure(bg='black')

        self.heading = Label(self.window, text="Monte Carlo", font=("Helvetica 16"), bg="black", fg="cyan")
        self.frame1 = LabelFrame(self.window, text="What is Monte Carlo Simulation?", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
        self.describe = Label(self.frame1, bg="black", fg="cyan", text="Monte Carlo Simulation, also known as the Monte Carlo Method or\na multiple probability simulation, is a mathematical technique,\nwhich is used to estimate the possible outcomes of an uncertain event.", font=("Helvetica", 11))


        self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
        self.step1 = Label(self.frame2, text="Here monte carlo simulation is used to estimate the value of pi.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step2 = Label(self.frame2, text="This is done using some basic concepts of probabilities\n", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step3 = Label(self.frame2, text="Step 1: Here we take a square of side 10 units and", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step4 = Label(self.frame2, text="we place a circle at the center with a radi of 5 units.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step5 = Label(self.frame2, text="Step 2: If we sample some random points within the square", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step6 = Label(self.frame2, text="then surely some of the sampled points will be inside the circle.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step7 = Label(self.frame2, text="Step 3: So if the total number of sampling is x and number of ", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step8 = Label(self.frame2, text="hit is y, then fraction of success is (y/x).", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step9 = Label(self.frame2, text="Step 4: This fraction will be proportional to  area(Circle)/area(Square).", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step10 = Label(self.frame2, text="Step 5: The area of square, a*a is known to us, hit_ratio is also available", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step11 = Label(self.frame2, text="to us. So by rearranging we can estimate the area of circle.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step12 = Label(self.frame2, text="Step 6: The area of circle is pi*r*r, and we know the value of r.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step13 = Label(self.frame2, text="Hence we can estimate the value pi. This is how it is done.", font=("Helvetica", 11), bg="black", fg="cyan")


        self.monte_text = Label(self.window, text="Enter the time interval: ", font=("Helvetica", 11), bg="black", fg="yellow")
        self.monte_input = Entry(self.window, width=20, borderwidth=2)
        self.monte_button = Button(self.window, text="Animate", font=("Helvetica", 11), command=self.monte_func, pady=10, bg="black", fg="yellow", width=15)

        self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=2, padx=30)
        self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=5, rowspan=2)
        self.describe.grid(row=1, column=0, sticky=W)

        self.frame2.grid(row=3, column=0, rowspan=13, columnspan=2, padx=30, pady=5)
        self.step1.grid(row=3, column=0, sticky=W)
        self.step2.grid(row=4, column=0, sticky=W)
        self.step3.grid(row=5, column=0, sticky=W)
        self.step4.grid(row=6, column=0, sticky=W)
        self.step5.grid(row=7, column=0, sticky=W)
        self.step6.grid(row=8, column=0, sticky=W)
        self.step7.grid(row=9, column=0, sticky=W)
        self.step8.grid(row=10, column=0, sticky=W)
        self.step9.grid(row=11, column=0, sticky=W)
        self.step10.grid(row=12, column=0, sticky=W)
        self.step11.grid(row=13, column=0, sticky=W)
        self.step12.grid(row=14, column=0, sticky=W)
        self.step13.grid(row=15, column=0, sticky=W)

        self.monte_text.grid(row=1, column=2)
        self.monte_input.grid(row=2, column=2, ipady=3)
        self.monte_button.grid(row=3, column=2)


        self.window.mainloop()

# object = Monte_Window()
