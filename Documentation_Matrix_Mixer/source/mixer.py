
import tkinter as tk
import soundfile as sf
import sounddevice as sd

class Mixer:
    """
    mixer class
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Matrix Multiplication")
        self.root.geometry("600x200")

        self.fs=44100
        """
        Setting sampling Rate
        """

        self.track_0_name="vettah-bgm_0.wav"
        self.track_1_name="vocal.wav"               # These are the  audio files for mixing
        self.track_2_name="bg_0.wav"


        y, fs = sf.read(self.track_0_name, dtype='float32')
        self.track_0_audio=y[slice(0,5*fs,1)]           ## Converting to an array
        
        y, fs = sf.read(self.track_1_name, dtype='float32')
        self.track_1_audio=y[slice(0,5*fs,1)]           ## Converting to an array

        y, fs = sf.read(self.track_2_name, dtype='float32')
        self.track_2_audio=y[slice(0,5*fs,1)]/3                 ## Converting to an array


        # creating string variable in Tkinter

        self.x =0
        self.y =0
        self.z =0


        # First label-scale pair

        self.label_track_0 = tk.Label(self.root, text="Track 0",width=10,font=("Courier",20))
        self.scale_0=tk.Scale(self.root, from_=0, to=10, orient=tk.HORIZONTAL,command=self.Get_x,activebackground='yellow',bd=3,bg='red')
        self.button_0_play = tk.Button(self.root, text="Play",width=10,font=("Courier",10),bd=3,command=self.Play_track_0)

        # Second label-scale pair

        self.label_track_1 = tk.Label(self.root, text="Track 1",width=10,font=("Courier",20))
        self.scale_1 = tk.Scale(self.root, from_=0, to=10, orient=tk.HORIZONTAL,command=self.Get_y,activebackground='yellow',bd=3,bg='green')
        self.button_1_play=tk.Button(self.root,text="Play",width=10,font=("Courier",10),bd=3,command=self.Play_track_1)

        # Third label-scale pair

        self.label_track_2 = tk.Label(self.root, text="Track 2",width=10,font=("Courier",20))
        self.scale_2 = tk.Scale(self.root, from_=0, to=10, orient=tk.HORIZONTAL,command=self.Get_z,activebackground='yellow',bd=3,bg='blue')
        self.button_2_play = tk.Button(self.root, text="Play",width=10,font=("Courier",10),bd=3,command=self.Play_track_2)

        # Packing Widgets in tkinter window

        self.button_mix=tk.Button(self.root,text="Mix",width=15,font=("Courier",15),command=self.Mix)
        self.button_quit=tk.Button(self.root,text="Quit",width=15,font=("Courier",15),command=self.root.quit)

        self.label_track_0.grid(row=0,column=0)
        self.scale_0.grid(row=0,column=1)
        self.button_0_play.grid(row=0,column=2)

        self.label_track_1.grid(row=1, column=0)
        self.scale_1.grid(row=1, column=1)
        self.button_1_play.grid(row=1, column=2)

        self.label_track_2.grid(row=2, column=0)
        self.scale_2.grid(row=2, column=1)
        self.button_2_play.grid(row=2, column=2)

        self.button_mix.grid(row=3,column=1)
        self.button_quit.grid(row=3, column=2)


        self.root.mainloop()        ## calling the main loop


    def Get_x(self,event):      ## Function to reset the X  variable value
        """
        Function to reset the X  variable value
        """
        self.x=self.scale_0.get()
    def Get_y(self,val):        ## Function to reset the Y  variable value
        """
        Function to reset the Y  variable value
        """
        self.y=self.scale_1.get()
    def Get_z(self,event):      ## Function to reset the Z variable value
        """
        Function to reset the Z variable value
        """
        self.z=self.scale_2.get()
    def Play_track_0(self):         ## Function to play the track 0
        """
        Function to play the track 0
        """
        sd.play(self.track_0_audio,self.fs)         ## for playing the respective track
        sd.wait()       ## Disable all other interrupts
    def Play_track_1(self):         ## Function to play the track 1
        """
        Function to play the track 1
        """
        sd.play(self.track_1_audio, self.fs)## for playing the respective track
        sd.wait()           ## Disable all other interrupts
    def Play_track_2(self):     ## Function to play the track 2
        """
        Function to play the track 2
        """
        sd.play(self.track_2_audio, self.fs)## for playing the respective track
        sd.wait()               ## Disable all other interrupts
    def Mix(self):   ## Function to play the linearly combined track
        """
        Function to play the linearly combined track
        """
        sd.play((self.x*self.track_0_audio)+(self.y*self.track_1_audio)+(self.z*self.track_2_audio), self.fs)
        sd.wait()
