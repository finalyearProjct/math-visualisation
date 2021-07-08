import matplotlib.image as img
import numpy as np
from matplotlib import pyplot as plt


class Image_Compression:
    def __init__(self, file):
        self.file = file
        self.plt = plt
        self.fig, self.axs = self.plt.subplots(2)
        self.img = img
        self.np = np
        self.plt.suptitle("Image compression using SVD",color='white',fontweight="bold", size=20)
        self.fig.canvas.set_window_title('Image compression using SVD')
        self.fig.set_figheight(8)
        self.fig.set_figwidth(14)
        self.fig.patch.set_facecolor('black')

        self.ax0 = self.plt.subplot2grid((1, 2), (0,0))
        self.ax1 = self.plt.subplot2grid((1, 2), (0,1))

        self.ax_K=self.plt.axes([0.3, 0.05, 0.5, 0.04])
        # ax_K.set_facecolor('red')
        self.slider_K = self.plt.Slider(self.ax_K, 'Image Size Tuner', 0,200,20,color='red')
        self.slider_K.label.set_color('white')
        self.slider_K.label.set_size(15)

        # self.A = self.img.imread('images/equation_image.png')
        self.A = self.img.imread(self.file)
        self.X = self.np.mean(self.A,-1)
        self.imag = self.ax0.imshow(self.X)
        self.imag.set_cmap('gray')
        self.ax0.set_title('Original Image', fontweight="bold", size=15, color='yellow')
        self.ax0.axis('off')

        self.u, self.sigma, self.v = self.np.linalg.svd(self.X,full_matrices=False)
        self.SIGMA = self.np.diag(self.sigma)
        self.k=20
        self.X_approx = self.u[:,:self.k]@self.SIGMA[0:self.k,:self.k]@self.v[:self.k,:]
        self.imag_approx = self.ax1.imshow(self.X_approx)
        self.imag_approx.set_cmap('gray')

        self.slider_K.on_changed(self.update)
        self.ax1.axis('off')

        self.plt.show()


    def update(self, val):
        # global u
        # global v
        # global SIGMA
        self.k =int(self.slider_K.val)
        self.X_approx = self.u[:, :self.k] @ self.SIGMA[0:self.k, :self.k] @ self.v[:self.k, :]
        self.imag_approx=self.ax1.imshow(self.X_approx)
        self.imag_approx.set_cmap('gray')
        self.ax1.set_title('Compressed Image for K value of  '+str(self.k), fontweight="bold", size=15, color='yellow')
