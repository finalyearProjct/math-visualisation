import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
import scipy.stats as ss

class ITS:
    def __init__(self):
        self.np_0 = np
        self.plt_0 = plt
        self.ss_0=ss
        self.mapped_list =list([])
        self.bin_list=list(self.np_0.linspace(-4,4,40))
        self.x_values=np.linspace(-4,4, 5000)
        self.y_values_0=ss.norm.cdf(self.x_values,0,1)
        self.figure, self.axes = self.plt_0.subplots(2)
        self.plt_0.suptitle("Inverse Transform Sampling - Demo")
        self.axes[0].set_ylim(0,1)
        self.axes[0].set_xlim(-4,4)
        self.axes[0].title.set_text('Sampling From CDF')
        self.y_values_1=self.ss_0.norm.pdf(self.x_values,0,1)
        self.axes[1].plot(self.x_values,self.y_values_1*50)
        self.axes[1].title.set_text('Generating Random numbers based on CDF')
        self.axes[1].set_ylim(0,50)
        self.axes[0].set_xlim(-4, 4)

    def animate(self,i):
        self.axes[0].plot(self.x_values, self.y_values_0,color='black')
        sample=self.np_0.random.uniform(0,1)
        self.axes[0].axhspan(sample-.01,sample+.01, color='pink', alpha=.2)
        inverse_value=self.ss_0.norm.ppf(sample)
        self.mapped_list.append(inverse_value)
        self.axes[0].axvspan(inverse_value - .01,inverse_value + .01, color='pink', alpha=.2)
        self.axes[1].hist(self.mapped_list,self.bin_list,color='black')

    def start(self):
        ani = anim.FuncAnimation(self.figure, self.animate, interval=1)
        self.plt_0.show()
