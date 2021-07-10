import numpy as np
from matplotlib import pyplot as plt


class SVD:
    """Constructor is a matrix A"""
    def __init__(self, A):
        self.A=A
        self.fig, self.axs = plt.subplots(2)

        plt.suptitle("SVD - Visualizer", color='white', fontweight="bold", size=30)
        self.fig.canvas.set_window_title('SVD - Visualizer')
        self.fig.set_figheight(8)
        self.fig.set_figwidth(14)
        self.fig.patch.set_facecolor('black')

        self.Plot_maker()

        xvals = np.linspace(-4, 4, 9)
        yvals = np.linspace(-3, 3, 7)
        self.xygrid = np.column_stack([[x, y] for x in xvals for y in yvals])
        """Mapping based on the colorizer light fuction"""
        self.colors = list(map(self.colorizer_light, self.xygrid[0], self.xygrid[1]))

    def Plot_maker(self):
        """just for formatting purpose"""
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
    def Sigmoid_mapping(self,x):
        """A mathematical function to map any number between 0 and 1"""
        return 1 / (1 + np.exp(-x))
    def colorizer_dark(self, x, y):
        """This uses Sigmoid function for coloring purpose

        Map x-y coordinates to a rgb color


        """
        r =self.Sigmoid_mapping(x - 2)
        g =self.Sigmoid_mapping(y - 2)
        b =self.Sigmoid_mapping(x - 2)
        return (r, g, b)
    def colorizer_light(self,x, y):
        """
        Map x-y coordinates to a rgb color
        """
        r = min(1, 1 - y / 3)
        g = min(1, 1 + y / 3)
        b = 1 / 4 + x / 16
        return (r, g, b)
    def start(self):
        """Function to start Animation"""

        u,sigma,v=np.linalg.svd(self.A)
        """SVD decompostion"""
        SIGMA=np.diag(sigma)

        self.ax0.scatter(self.xygrid[0],self.xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax0.set_title('Reference XY Grid', fontweight="bold", size=15, color='yellow')
        self.ax0.axis([-7, 7, -7, 7])
        self.ax0.set_aspect(1)


        trans_xygrid=np.matmul(self.A,self.xygrid)
        """Applying the trasformation"""


        self.ax1.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax1.set_title(' On Applying Transformation', fontweight="bold", size=15, color='yellow')
        self.ax1.axis([-20, 20, -20, 20])
        self.ax1.set_aspect(1)

        trans_xygrid=np.matmul(u , self.xygrid)
        """the rotated space grid"""

        self.ax2.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax2.set_title('Rotation', fontweight="bold", size=15, color='yellow')
        self.ax2.axis([-7, 7, -7, 7])
        self.ax2.set_aspect(1)

        trans_xygrid=np.matmul(SIGMA,self.xygrid)

        self.ax3.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax3.set_title('Scaling', fontweight="bold", size=15, color='yellow')
        self.ax3.axis([-20,20, -20, 20])
        self.ax3.set_aspect(1)

        trans_xygrid=np.matmul(v,self.xygrid)

        self.ax4.scatter(trans_xygrid[0],trans_xygrid[1], s=40, color=self.colors, edgecolor="none")
        self.ax4.set_title('Rotation', fontweight="bold", size=15, color='yellow')
        self.ax4.axis([-7,7, -7, 7])
        self.ax4.set_aspect(1)


        plt.tight_layout()
        plt.show()

# A = [[1, 2],
#      [3, 4]]
# m=SVD(A)
# m.start()
