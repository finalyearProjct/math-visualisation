from tkinter import *
import principal_component_analysis
import patient_object
from PIL import ImageTk, Image

class PCA_Window:


    def function(self):
        self.names = []
        self.names = self.name_input.get().split(" ")
        self.patients = []
        for i in range(0, len(self.names)):
            self.patients.append(patient_object.Patient(self.names[i]))
        object = principal_component_analysis.PCA(self.patients)
        object.start()
        self.name_input.delete(0, END)


    def __init__(self):
        self.window = Tk()
        self.window.title("Principal Component Analysis")
        self.window.geometry("800x600")
        self.window.configure(bg='black')

        self.heading = Label(self.window, text="Principal Component Analysis", font=("Helvetica 16"), bg="black", fg="cyan")
        self.frame1 = LabelFrame(self.window, text="What is Principal Component Analysis?", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
        self.describe = Label(self.frame1, bg="black", fg="cyan", text="PCA is used in data analysis and for making predictive models.\nIt is commonly used for dimensionality reduction\nby projecting each data point onto only the first few principal components\n while preserving as much of the data's variation as possible", font=("Helvetica", 11))

        self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
        self.step1 = Label(self.frame2, text="Step 1: We have used PCA to cluster patients with similarity.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step2 = Label(self.frame2, text="Step 2: Each of this object have many attributes indicators such as", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step3 = Label(self.frame2, text="in this the total number of attributes associated with a patient is seven", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step4 = Label(self.frame2, text="Step 3: So a patient can be seen as a vector in  5 dimensional space", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step5 = Label(self.frame2, text="Step 4: Using PCA we reduce this data into a 2 diamension.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step6 = Label(self.frame2, text="ie, we can represent the data with 2 axis with minimum loss", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step7 = Label(self.frame2, text="Step 5: From looking the data from PCA_1 and PCA_2 axis", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step8 = Label(self.frame2, text="we can observe the clusters in the patient space ", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step9 = Label(self.frame2, text="Step 4: This fraction will be proportional to  area(Circle)/area(Square).", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step10 = Label(self.frame2, text="Step 5: The area of square, a*a is known to us, hit_ratio is also available", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step11 = Label(self.frame2, text="to us. So by rearranging we can estimate the area of circle.", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step12 = Label(self.frame2, text="Step 6: The area of circle is pi*r*r, and we know the value of r.", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step13 = Label(self.frame2, text="Hence we can estimate the value pi. This is how it is done.", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step1 = Label(self.frame2, text="", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step1 = Label(self.frame2, text="", font=("Helvetica", 11), bg="black", fg="cyan")
        # self.step1 = Label(self.frame2, text="", font=("Helvetica", 11), bg="black", fg="cyan")

        # self.frame3 = LabelFrame(self.window, text="Enter the time interval", font=("Helvetica", 12), padx=5, pady=5, bg="black", fg="cyan")
        self.monte_text = Label(self.window, text="Enter the name of the patients: ", font=("Helvetica", 11), bg="black", fg="yellow")
        self.name_input = Entry(self.window, width=20, borderwidth=2)
        self.monte_button = Button(self.window, text="Animate", font=("Helvetica", 11), command=self.function, pady=10, bg="black", fg="yellow", width=15)

        self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=2, padx=30)
        self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=5, rowspan=2)
        self.describe.grid(row=1, column=0, sticky=W)
        self.frame2.grid(row=3, column=0, rowspan=8, columnspan=2, padx=30, pady=5, sticky=W)
        # self.label2.grid(row=3, column=0, padx=10, pady=10)
        self.step1.grid(row=3, column=0, sticky=W)
        self.step2.grid(row=4, column=0, sticky=W)
        self.step3.grid(row=5, column=0, sticky=W)
        self.step4.grid(row=6, column=0, sticky=W)
        self.step5.grid(row=7, column=0, sticky=W)
        self.step6.grid(row=8, column=0, sticky=W)
        self.step7.grid(row=9, column=0, sticky=W)
        self.step8.grid(row=10, column=0, sticky=W)

        self.monte_text.grid(row=1, column=2)
        self.name_input.grid(row=2, column=2, ipady=3)
        self.monte_button.grid(row=3, column=2)


        self.window.mainloop()

# object = PCA_Window()
