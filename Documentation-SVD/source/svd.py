"""
Singular value decomposition

This object creates an animation of Singular value decomposition
"""
import numpy as np
from matplotlib import pyplot as plt
class SVD:
    """Parameters:
    
        A= a matrix is passed
    """
    def __init__(self,A):  # Constructor is a matrix A
        self.A=A
        self.fig, self.axs = plt.subplots(2)

        plt.suptitle("SVD - Visualizer", color='white', fontweight="bold", size=30)
        self.fig.canvas.set_window_title('SVD - Visualizer')
        self.fig.set_figheight(8)
        self.fig.set_figwidth(14)       # For Formatting  purpose
        self.fig.patch.set_facecolor('black')

        self.Plot_maker()       ## For formatting purpose

        xvals = np.linspace(-4, 4, 9)   # making 1-D array
        yvals = np.linspace(-3, 3, 7)       # making 1-D array
        self.xygrid = np.column_stack([[x, y] for x in xvals for y in yvals])  # used to create a XY grid space

        self.colors = list(map(self.colorizer_light, self.xygrid[0], self.xygrid[1]))
        ## Mapping based on the colorizer light fuction

    def Plot_maker(self):  ## just for formatting purpose
        """ For formatting the plot"""
        self.ax0 = plt.subplot2grid((3, 3), (0, 0), rowspan=3)
        self.ax1 = plt.subplot2grid((3, 3), (0, 1), rowspan=3)
        self.ax2 = plt.subplot2grid((3, 3), (0, 2), colspan=1)
        self.ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1)
        self.ax4 = plt.subplot2grid((3, 3), (2, 2), colspan=1)

        self.ax0.set_facecolor('black')
        self.ax1.set_facecolor('black')
        self.ax2.set_facecolor('black')
        self.ax3.set_facecolor('black')
        self.ax4.set_facecolor('black')
    def Sigmoid_mapping(self,x):        ## A mathematical function to map any number between 0 and 1
        """
        A mathematical function to map any number between 0 and 1
        """
        return 1 / (1 + np.exp(-x))
    def colorizer_dark(self, x, y):    ##  This uses Sigmoid function for coloring purpose
        """
        Map x-y coordinates to a rgb color
        """
        r =self.Sigmoid_mapping(x - 2)
        g =self.Sigmoid_mapping(y - 2)
        b =self.Sigmoid_mapping(x - 2)
        return (r, g, b)
    def colorizer_light(self,x, y):  ##  Another beautiful mapping RULE
        """
        Map x-y coordinates to a rgb color
        """
        r = min(1, 1 - y / 3)
        g = min(1, 1 + y / 3)
        b = 1 / 4 + x / 16
        return (r, g, b)
    def start(self):        ## Triggers the start
        """
        Function for triggering the start
        """

        u,sigma,v=np.linalg.svd(A)      ## SVD decompostion
        SIGMA=np.diag(sigma)

        ##  plotting the non transformed space
        self.ax0.scatter(self.xygrid[0],self.xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax0.set_title('Reference XY Grid', fontweight="bold", size=15, color='yellow')
        self.ax0.axis([-7, 7, -7, 7])
        self.ax0.set_aspect(1)

        ## Applying the trasformation
        trans_xygrid=np.matmul(self.A,self.xygrid)


        ## plotting the transformed grid space
        self.ax1.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax1.set_title(' On Applying Transformation', fontweight="bold", size=15, color='yellow')
        self.ax1.axis([-20, 20, -20, 20])
        self.ax1.set_aspect(1)

        ## now we care aout the Decomposed trasformations

        ## the rotated space grid
        trans_xygrid=np.matmul(u , self.xygrid)

        self.ax2.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax2.set_title('Rotation', fontweight="bold", size=15, color='yellow')
        self.ax2.axis([-7, 7, -7, 7])
        self.ax2.set_aspect(1)

        ## Scaling applied on the grid space

        trans_xygrid=np.matmul(SIGMA,self.xygrid)

        self.ax3.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax3.set_title('Scaling', fontweight="bold", size=15, color='yellow')
        self.ax3.axis([-20,20, -20, 20])
        self.ax3.set_aspect(1)

        ## Rotation applied on the grid space
        trans_xygrid=np.matmul(v,self.xygrid)

        self.ax4.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax4.set_title('Rotation', fontweight="bold", size=15, color='yellow')
        self.ax4.axis([-7,7, -7, 7])
        self.ax4.set_aspect(1)


        ## For plotting purpose
        plt.tight_layout()
        plt.show()
