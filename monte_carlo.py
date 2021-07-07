import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
from tkinter import *

class Monte_carlo:
    def __init__(self,time_interval):
        self.np_0=np
        self.plt_0=plt
        self.time_gap=time_interval
        self.radi=25
        self.ax_X_list = list([])
        self.ax_Y_list = list([])
        self.ax_Y_pi = list([])
        self.figure,self.axes =self.plt_0.subplots(2)
        self.plt_0.suptitle("Monte Carlo simulation - Demo")
        self.axes[0].set_ylim(0, 50)
        self.axes[0].set_xlim(0, 50)
        self.axes[0].set_aspect(1)
        Drawing_colored_circle =self.plt_0.Circle((10, 10), 1.5)
        Drawing_uncolored_circle =self.plt_0.Circle((25, 25), 25, fill=True, color='yellow')
        self.axes[0].add_artist(Drawing_colored_circle)
        self.axes[0].add_artist(Drawing_uncolored_circle)
        self.axes[0].title.set_text('Sampling Process')
        self.hit = 0
        self.total = 0



    def animate(self,i):
        self.total=self.total+1
        a=self.np_0.random.randint(0,50,2)
        Drawing_colored_circle =self.plt_0.Circle((a[0],a[1]), 1.5)
        mag=self.np_0.sqrt(self.np_0.square(a[0]-25)+self.np_0.square(a[1]-25))
        if mag<self.radi:
            self.hit=self.hit+1
        value=self.hit*50*50/(self.total*self.np_0.square(self.radi))
        self.ax_Y_list.append(value)
        self.ax_X_list.append(self.total)
        self.ax_Y_pi.append(3.14)
        self.axes[0].add_artist(Drawing_colored_circle)
        self.axes[1].clear()
        self.axes[1].set_ylim(0,5)
        self.axes[1].set_xlim(0,self.total+2)
        self.plt_0.yticks(self.np_0.arange(0,5,.5))
        self.axes[1].plot(self.ax_X_list,self.ax_Y_list,color='black',label ='Estimated value')
        self.axes[1].plot(self.ax_X_list, self.ax_Y_pi, color='red', marker="_",label ='Target value')
        self.axes[1].set_ylabel('Estimation')
        self.axes[1].set_xlabel('Sampling time')
        # self.axes[1].title.set_text('Graphical Representation')
        self.axes[1].legend()


    def start(self):
        ani=anim.FuncAnimation(self.figure,self.animate,interval=self.time_gap*1000)
        self.plt_0.show()
