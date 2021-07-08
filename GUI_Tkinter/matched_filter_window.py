from tkinter import *
import matched_filter


class Matched_Filter_Window:

    def function(self):
        self.number = StringVar()
        self.number = self.input.get()
        self.list = []
        self.list = list(map(int, self.number.strip().split()))
        self.object = matched_filter.Matched_filter(self.list)
        self.object.start()
        self.input.delete(0, END)

        # a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
    def __init__(self):
        self.window = Tk()
        self.window.title("Matched Filter")
        self.window.geometry("850x600")
        self.window.configure(bg="black")

        self.heading = Label(self.window, text="Matched Filter", font=("Helvetica", 16), bg="black", fg="cyan")

        self.frame1 = LabelFrame(self.window, text="What is Matched Filter?",  font=("Helvetica", 12), padx=5, pady=5, bg="black", fg="yellow")
        self.describe = Label(self.frame1, text="In signal processing, a matched filter is obtained by correlating a known delayed \nsignal, or template, with an unknown signal to detect the presence of the template \nin the unknown signal. This is equivalent to convolving the unknown signal with a\n conjugated time-reversed version of the template. The matched filter is the optimal \nlinear filter for maximizing the signal-to-noise ratio (SNR) in the presence of additive \nstochastic noise.",font=("Helvetica", 11), bg="black", fg="cyan")






        self.frame2 = LabelFrame(self.window, text="How is it done?", font="Helvetica 12", padx=5, pady=5, bg="black", fg="yellow")
        self.step1 = Label(self.frame2, text="Matched Filter or Correlative filter, is tool which is used to detect", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step2 = Label(self.frame2, text="a particular signal from a collection of signals.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step3 = Label(self.frame2, text="The basis of matched filter is the concept of Dot product between two vectors.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step4 = Label(self.frame2, text="Step 1: Here we are overlapping the translated version of input signal", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step5 = Label(self.frame2, text="(given signal) over the parent signal.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step6 = Label(self.frame2, text="Step 2: Maximum similarity will happen when there is a perfect overlap.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step7 = Label(self.frame2, text="Step 3: There is a slider to move/translate the signal to and fro.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step8 = Label(self.frame2, text="Step 4: Here similarity means the cosine of angle between original signal,", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step9 = Label(self.frame2, text="Step 4: This fraction will be proportional to  area(Circle)/area(Square).", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step10 = Label(self.frame2, text="and translated version of original signal.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step11 = Label(self.frame2, text="Step 5: This is how a matched/correlative filter works.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step12 = Label(self.frame2, text="Note: White entering the list of numbers, enter them in this form 1 2 3 4 5", font=("Helvetica", 11), bg="black", fg="cyan")




        self.label = Label(self.window, text="Enter a list of numbers", font=("Helvetica", 11), bg="black", fg="yellow")
        self.input = Entry(self.window, width=20)
        self.button = Button(self.window, text="Animate", command=self.function, padx=10, pady=10, bg="black", fg="yellow", width=10, font=("Helvetica", 11))

        self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=2, padx=30)

        self.frame1.grid(row=1, column=0, sticky=W, padx=30, rowspan=4)
        self.describe.grid(row=1, column=0, sticky=W, padx=5)

        self.frame2.grid(row=5, column=0, sticky=W, padx=30, pady=10, rowspan=12, columnspan=2)
        self.step1.grid(row=5, column=0, sticky=W)
        self.step2.grid(row=6, column=0, sticky=W)
        self.step3.grid(row=7, column=0, sticky=W)
        self.step4.grid(row=8, column=0, sticky=W)
        self.step5.grid(row=9, column=0, sticky=W)
        self.step6.grid(row=10, column=0, sticky=W)
        self.step7.grid(row=11, column=0, sticky=W)
        self.step8.grid(row=12, column=0, sticky=W)
        self.step9.grid(row=13, column=0, sticky=W)
        self.step10.grid(row=14, column=0, sticky=W)
        self.step11.grid(row=15, column=0, sticky=W)
        self.step12.grid(row=16, column=0, sticky=W)

        # self.instruct.grid(row=1, column=3, pady=5)
        self.label.grid(row=1, column=3, pady=5)
        self.input.grid(row=2, column=3, pady=5, ipady=3)
        self.button.grid(row=4, column=3, pady=5)

        self.window.mainloop()


# object = Matched_Filter_Window()
