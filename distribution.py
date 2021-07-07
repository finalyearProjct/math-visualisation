import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as anim


class Animated_histo:
    def __init__(self,a_ddist):
        self.ddist=a_ddist
        self.plt=plt
        self.anim=anim
        self.fig, self.ax = self.plt.subplots(1, 1, figsize=(6, 5), tight_layout=True)
        self.ax.set_ylim(0,50)
        self.bin_division=15
        self.bins=np.linspace(self.ddist.min_limit,self.ddist.max_limit,self.bin_division)
        self.holder=list([])
        self.holder.append(self.ddist.Draw())
    def animate(self,i):
        self.ax.hist(self.holder,self.bins, color="blue", ec="blue")
        self.holder.append(self.ddist.Draw())
    def start(self):
        ani= anim.FuncAnimation(self.fig,self.animate, interval=200)
        self.plt.show()

class Exp_dist:
    def __init__(self,a_lamda):
        self.lamda=a_lamda
        self.np=np
        self.max_limit=a_lamda+10
        self.min_limit=0
    def Draw(self):
        return self.np.random.exponential(self.lamda)
    def Run(self, count):
        a = list([])
        for x in range(count):
            a.append(self.Draw())
        return a

class Uni_dist:
    def __init__(self, l_limit, u_limit):
        self.a=l_limit
        self.b=u_limit
        self.max_limit=u_limit
        self.min_limit=l_limit
        self.np=np
    def Draw(self):
        return self.np.random.uniform(self.a,self.b)
    def Run(self,count):
        a=list([])
        for x in range(count):
            a.append(self.Draw())
        return a

#obj1 = exp_dist(1)
#obj2 = animated_histo(obj1)
#obj2.start()
