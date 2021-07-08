from tkinter import *
import mixer_matrix_multiplication
from tkinter import filedialog


class Mixer_Window():
    def openTrack1(self):
        self.window.trackname1 = filedialog.askopenfilename(initialdir="/", title="Select the file", filetypes=(("WAV files", "*.wav"), ("All files", "*.*")))
        self.track1 = StringVar()
        self.track1 = self.window.trackname1
        self.tracks.append(self.track1)
        print(self.tracks[0])

    def openTrack2(self):
        self.window.trackname2 = filedialog.askopenfilename(initialdir="/", title="Select the file", filetypes=(("WAV files", "*.wav"), ("All files", "*.*")))
        self.track2 = StringVar()
        self.track2 = self.window.trackname2
        self.tracks.append(self.track2)
        print(self.tracks[1])

    def openTrack3(self):
        self.window.trackname3 = filedialog.askopenfilename(initialdir="/", title="Select the file", filetypes=(("WAV files", "*.wav"), ("All files", "*.*")))
        self.track3 = StringVar()
        self.track3 = self.window.trackname3
        self.tracks.append(self.track3)
        print(self.tracks[2])

    def function(self):
        object = mixer_matrix_multiplication.Mixer(self.tracks)

    def __init__(self):
        self.window = Tk()
        self.window.title("MATRIX MIXER")
        self.window.geometry("850x600")
        self.window.configure(bg='black')

        self.tracks = []

        self.heading = Label(self.window, text="Matrix Mixer", font=("Helvetica 16"), bg="black", fg="cyan")
        self.frame1 = LabelFrame(self.window, text="What is Matrix Mixer?", bg="black", font=("Helvetica", 12), fg="yellow", padx=5, pady=5)
        self.describe = Label(self.frame1, bg="black", fg="cyan", text="Matrix Mixer routes multiple input audio signals to a single output channel. It \nusually employs level controls such as potentiometers/sliders to determine \nhow much of each input is going to the output. Matrix mixer is actuallly an    \nelectronic device. But here we have developed a program that does the       \nsame job.", font=("Helvetica", 11))

        self.frame2 = LabelFrame(self.window, text="How is it done?", bg="black", fg="yellow", font=("Helvetica", 11), padx=5, pady=5)
        self.step1 = Label(self.frame2, text="Step 1: In this mixer we have 3 tracks in .wav format.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step2 = Label(self.frame2, text="Step 2: They are first trimmed to a common size. ", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step3 = Label(self.frame2, text="Step 3: Now by adjusting the slider, we alter the weight associated with each track.", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step4 = Label(self.frame2, text="Step 4: When we click on mix we take the linear combination of these tracks.\n", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step5 = Label(self.frame2, text="i.e  f = (a*track_0)+(b*track_1)+(c*track_2)\n", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step6 = Label(self.frame2, text="Step 5: Here each track is a column vector of specific size and we are multiplying", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step7 = Label(self.frame2, text="it with the weight (another column matrix) that is given to them using the slider ", font=("Helvetica", 11), bg="black", fg="cyan")
        self.step8 = Label(self.frame2, text="Step 6: Output of the mixer is the mixed version of the songs.", font=("Helvetica", 11), bg="black", fg="cyan")

        self.opent1_button = Button(self.window, text="Track 1", font=("Helvetica", 11), command=self.openTrack1, pady=10, bg="black", fg="cyan", width=15)
        self.opent2_button = Button(self.window, text="Track 2", font=("Helvetica", 11), command=self.openTrack2, pady=10, bg="black", fg="cyan", width=15)
        self.opent3_button = Button(self.window, text="Track 3", font=("Helvetica", 11), command=self.openTrack2, pady=10, bg="black", fg="cyan", width=15)
        self.mix_button = Button(self.window, text="Sound Mixer", font=("Helvetica", 11), command=self.function, pady=10, bg="black", fg="yellow", width=20)

        self.heading.grid(row=0, column=0, sticky=W, pady=20, columnspan=2, padx=30)
        self.frame1.grid(row=1, column=0, sticky=W, padx=30, pady=5, rowspan=2)
        self.describe.grid(row=1, column=0, sticky=W)

        self.frame2.grid(row=3, column=0, rowspan=11, columnspan=2, padx=30, pady=5, sticky=W)
        self.step1.grid(row=3, column=0, sticky=W)
        self.step2.grid(row=4, column=0, sticky=W)
        self.step3.grid(row=5, column=0, sticky=W)
        self.step4.grid(row=6, column=0, sticky=W)
        self.step5.grid(row=7, column=0,)
        self.step6.grid(row=8, column=0, sticky=W)
        self.step7.grid(row=9, column=0, sticky=W)
        self.step8.grid(row=10, column=0, sticky=W)

        self.opent1_button.grid(row=1, column=2)
        self.opent2_button.grid(row=2, column=2)
        self.opent3_button.grid(row=3, column=2)
        self.mix_button.grid(row=4, column=2)



        self.window.mainloop()


# object = Mixer_Window()
