from tkinter import *
from tkinter import ttk
import linear_transformation

class Linear_Transform_Window:

    def linear_func(self):
        self.degree = linear_transformation.rotation(int(self.degree_input.get()))
        self.text = str(self.text_input.get())
        self.eye = linear_transformation.eye
        linear_obj = linear_transformation.Linear_transformation(self.text, [self.degree, 2*self.eye])
        linear_obj.start()
        self.degree_input.delete(0, END)
        self.text_input.delete(0, END)


    def __init__(self):
        self.window = Tk()
        self.window.title("Linear Transformation")
        self.window.geometry("890x600")
        self.window.configure(bg='black')

        self.heading = Label(self.window, text="Linear Transformation", font=("Helvetica 16"), bg="black", fg="cyan")
        self.frame1 = LabelFrame(self.window, text="What is Linear Transformation?", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
        self.describe = Label(self.frame1, bg="black", fg="cyan", text="A linear transformation is a function from one vector space to another that respects the \nunderlying (linear) structure of each vector space. The range of the transformation may \nbe the same as the domain and the two vector spaces must have the same underlying \nfield. The defining characteristic of a linear transformation T:V→W is that, for any vectors \nv1 and v2 in V and scalars a and b of the underlying field, T(av1+bv2)=aT(v1)+bT(v2) \n and T(cu)= cT(u).", font=("Helvetica", 11))



        self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
        self.step1 = Label(self.frame2, text="Here when we multiply a column vector by a 2*2 matrix, we are actually", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step2 = Label(self.frame2, text="mapping that vector to some other point in 2D.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step3 = Label(self.frame2, text="So indirectly when we multiply we are actually doing this mapping", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step4 = Label(self.frame2, text="process, or we are manipulating the whole grid space.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step5 = Label(self.frame2, text="Step 1: Input any word in all captial letters and provide any", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step6 = Label(self.frame2, text="transformation you would like to apply on the text.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step7 = Label(self.frame2, text="Step 2: Matrices such as Rotation, Reflection, Permutation, etc ", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step8 = Label(self.frame2, text="are predefined in the code. T", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step9 = Label(self.frame2, text="Step 3: The text would be multiplied by the respective predefined", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step10 = Label(self.frame2, text="matrix and you can see what happens to the space.", font=("Helvetica", 11), bg="black", fg="cyan")



        self.degree_label = Label(self.window, text="Enter the degree of rotation", font=("Helvetica", 11), bg="black", fg="yellow")
        self.degree_input = Entry(self.window, width=20)
        self.text_label = Label(self.window, text="Enter the text", font=("Helvetica", 11), bg="black", fg="yellow")
        self.text_input = Entry(self.window, width=20)
        self.button = Button(self.window, text="Animate", width=10, command=self.linear_func, padx=10, pady=10, font=("Helvetica",11), bg="black", fg="yellow")

        self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=2, padx=30)
        self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=5, rowspan=6)
        self.describe.grid(row=1, column=0, sticky=W)

        self.frame2.grid(row=7, column=0, rowspan=10, columnspan=2, padx=30, pady=5, sticky=W)
        self.step1.grid(row=7, column=0, sticky=W)
        self.step2.grid(row=8, column=0, sticky=W)
        self.step3.grid(row=9, column=0, sticky=W)
        self.step4.grid(row=10, column=0, sticky=W)
        self.step5.grid(row=11, column=0, sticky=W)
        self.step6.grid(row=12, column=0, sticky=W)
        self.step7.grid(row=13, column=0, sticky=W)
        self.step8.grid(row=14, column=0, sticky=W)
        self.step9.grid(row=15, column=0, sticky=W)
        self.step10.grid(row=16, column=0, sticky=W)



        self.degree_label.grid(row=1, column=3, pady=5)
        self.degree_input.grid(row=2, column=3, ipady=2)
        self.text_label.grid(row=4, column=3)
        self.text_input.grid(row=5, column=3, ipady=2)
        self.button.grid(row=7, column=3)


        self.window.mainloop()


# object = Linear_Transform_Window()
