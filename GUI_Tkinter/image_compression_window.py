from tkinter import *
import image_compression
from tkinter import filedialog


class Image_Compression_Window:
    def open(self):
        self.window.imagename = filedialog.askopenfilename(initialdir="/", title="Select the file", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
        self.image = StringVar()
        self.image = self.window.imagename
        image_obj = image_compression.Image_Compression(self.image)
    def __init__(self):
             self.window = Tk()
             self.window.title("Monte Carlo")
             self.window.geometry("860x600")
             self.window.configure(bg='black')

             self.heading = Label(self.window, text="Image Compression", font=("Helvetica 16"), bg="black", fg="cyan")
             self.frame1 = LabelFrame(self.window, text="What is Image Compression?", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
             self.describe = Label(self.frame1, bg="black", fg="cyan", text="Image compression is a type of data compression applied to digital images without \ndegrading the quality of the image to an unacceptable level, to reduce their cost for \nstorage or transmission. The reduction in file size allows more images to be stored \nin a given amount of disk or memory space.", font=("Helvetica", 11))

             self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
             self.step1 = Label(self.frame2, text="Image compression is a classic use of SVD. We consider each image as a matrix", font=("Helvetica", 11), bg="black", fg="cyan")
             self.step2 = Label(self.frame2, text="Step 1: After calculating SVD we will get a set of vectors which can be considered as axises.", font=("Helvetica", 11), bg="black", fg="cyan")
             self.step3 = Label(self.frame2, text="Step 2: We can represent the image with respect to each axis", font=("Helvetica", 11), bg="black", fg="cyan")
             self.step4 = Label(self.frame2, text="Step 3: Each axis has its own weightage. The primary axis contains maximum information", font=("Helvetica", 11), bg="black", fg="cyan")
             self.step5 = Label(self.frame2, text="maximum information. And the amount of information decreases on every axis", font=("Helvetica", 11), bg="black", fg="cyan")



             self.image_text = Label(self.window, text="Select the image file", font=("Helvetica", 11), bg="black", fg="yellow")
             self.image_button = Button(self.window, text="Open Image", font=("Helvetica", 11), command=self.open, pady=10, bg="black", fg="yellow", width=15)

             self.heading.grid(row=0, column=0, sticky=W, padx=25, columnspan=2, pady=20)
             self.frame1.grid(row=1, column=0, sticky=W, padx=25, pady=10, rowspan=2)
             self.describe.grid(row=1, column=0, sticky=W)

             self.frame2.grid(row=3, column=0, rowspan=13, columnspan=2, padx=25, pady=5, sticky=W)
             self.step1.grid(row=3, column=0, sticky=W)
             self.step2.grid(row=4, column=0, sticky=W)
             self.step3.grid(row=5, column=0, sticky=W)
             self.step4.grid(row=6, column=0, sticky=W)
             self.step5.grid(row=7, column=0, sticky=W)

             self.image_text.grid(row=1, column=2)
             self.image_button.grid(row=2, column=2)


             self.window.mainloop()



# object = Image_Compression_Window()
