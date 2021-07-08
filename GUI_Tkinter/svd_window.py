from tkinter import *
import singular_value_decomposition


class SVD_Window():

    def __init__(self):
        self.window = Tk()
        self.window.title("SINGULAR VALUE DECOMPOSITION")
        self.window.geometry("900x600")
        self.window.configure(bg="black")

        self.heading = Label(self.window, text="SINGULAR VALUE DECOMPOSITION", font=("Helvetica", 16), bg="black", fg="cyan")

        self.frame1 = LabelFrame(self.window, text="What is Singular Value Decomposition", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
        self.describe = Label(self.frame1, text="In linear algebra, the Singular Value Decomposition (SVD) of a matrix is a factorization \nof that matrix into three matrices. It has some interesting algebraic properties and \nconveys important geometrical and theoretical insights about linear transformations.", bg="black", font=("Helvetica", 11), fg="cyan")

        self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
        self.step1 = Label(self.frame2, text="Singular value decomposition is used to decompose an arbitary matrix", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step2 = Label(self.frame2, text="into the product of rotation, scaling, rotation matrices.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step3 = Label(self.frame2, text="This has many application in various fields.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step4 = Label(self.frame2, text="Here second column is, made to see how the space is getting manipulated as a whole.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step5 = Label(self.frame2, text="Then in the third column it shows the  manipulated decomposed space i.e. how the ", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step6 = Label(self.frame2, text="individual pieces(Rotation_1, scaling_1, Rotation_2) transform the normal grid space.\n", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step7 = Label(self.frame2, text="Note: To enter matrix [4, 2], the input should be given as ----> 4 2. The matrix is 2D.", font=("Helvetica", 11), bg="black", fg="cyan")


        # self.instruct1 = Label(self.window, text="The input should be in this form\n\n4 2", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.instruct2 = Label(self.window, text="Enter a 2x2 matrix", font=("Helvetica", 11), bg="black", fg="cyan")
        self.first_row_label = Label(self.window, text="Enter the first row", font=("Helvetica", 11), bg="black", fg="yellow")
        self.first_row_input = Entry(self.window, width=20)
        self.second_row_label = Label(self.window, text="Enter the second row", font=("Helvetica", 11), bg="black", fg="yellow")
        self.second_row_input = Entry(self.window, width=20)
        self.button = Button(self.window, width=10, text="Animate", bg="black", fg="yellow", command=self.function, padx=10, pady=10, font=("Helvetica", 11))

        self.heading.grid(row=0, column=0, sticky=W, pady=20, padx=30)
        self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=5, rowspan=2)
        self.describe.grid(row=1, column=0, sticky=W)

        self.frame2.grid(row=3, column=0, sticky=W, padx=30, pady=5, rowspan=7)
        self.step1.grid(row=3, column=0, sticky=W)
        self.step2.grid(row=4, column=0, sticky=W)
        self.step3.grid(row=5, column=0, sticky=W)
        self.step4.grid(row=6, column=0, sticky=W)
        self.step5.grid(row=7, column=0, sticky=W)
        self.step6.grid(row=8, column=0, sticky=W)
        self.step7.grid(row=9, column=0, sticky=W)

        # self.instruct1.grid(row=1, column=3)
        # self.instruct2.grid(row=2, column=3)
        self.first_row_label.grid(row=1, column=3, padx=5)
        self.first_row_input.grid(row=2, column=3, ipady=2, padx=5)
        self.second_row_label.grid(row=3, column=3, padx=5)
        self.second_row_input.grid(row=4, column=3, ipady=2, padx=5)
        self.button.grid(row=5, column=3, padx=5)

        self.window.mainloop()


    def function(self):
        self.list = []
        self.first = list(map(int, self.first_row_input.get().strip().split()))
        self.second = list(map(int, self.second_row_input.get().strip().split()))
        self.list = [self.first, self.second]
        object = singular_value_decomposition.SVD(self.list)
        object.start()
        self.first_row_input.delete(0, END)
        self.second_row_input.delete(0, END)


# object = SVD_Window()
