class Image_Compression:
    """class for image compression using SVD"""
    def __init__(self, file):           ## Constructor is the file name
        self.file = file        ## This is the file name
        self.plt = plt
        self.img = img
        self.np = np

        # just for formatting purpose
        self.fig, self.axs = self.plt.subplots(2)
        self.plt.suptitle("Image compression using SVD",color='white',fontweight="bold", size=20)
        self.fig.canvas.set_window_title('Image compression using SVD')
        self.fig.set_figheight(8)
        self.fig.set_figwidth(14)
        self.fig.patch.set_facecolor('black')

        # making subplots
        self.ax0 = self.plt.subplot2grid((1, 2), (0,0))
        self.ax1 = self.plt.subplot2grid((1, 2), (0,1))

        #placing a slider in th window
        self.ax_K=self.plt.axes([0.3, 0.05, 0.5, 0.04])
        self.slider_K = self.plt.Slider(self.ax_K, 'Image Size Tuner', 0,200,20,color='red')
        self.slider_K.label.set_color('white')
        self.slider_K.label.set_size(15)

        self.imag=None
        self.imag_approx=None


        self.processing()
        """This is the method responsible for Approximating the image using SVD for the first time"""
        ## attaching the event with the slider
        self.slider_K.on_changed(self.update)
        self.ax1.axis('off')

        # function to show the figure on the image
        self.plt.show()

    def processing(self):
        """Function responsible for approximating the total image to first k rank pieces"""
        self.A = self.img.imread(self.file)

        # This line of code just collapse the RGB value to a single grey scale value
        self.X = self.np.mean(self.A,-1)
        ## for showing the gray scale image
        self.imag = self.ax0.imshow(self.X)
        self.imag.set_cmap('gray')
        # just formatting
        self.ax0.set_title('Original Image', fontweight="bold", size=15, color='yellow')
        self.ax0.axis('off')


        ## computational part ##########
        self.u, self.sigma, self.v = self.np.linalg.svd(self.X,full_matrices=False)

        # constructing the diagonal matrix

        self.SIGMA = self.np.diag(self.sigma)

        self.k=20      ##  setting the sample value

        ## Choosing only the first k rank to construct the image
        self.X_approx = self.u[:,:self.k]@self.SIGMA[0:self.k,:self.k]@self.v[:self.k,:]
        ## drawing the approx image
        self.imag_approx = self.ax1.imshow(self.X_approx)
        self.imag_approx.set_cmap('gray')



    def update(self, val):
        """The slider is binded to this function upodate"""
        ## The change event will invoke this method
        self.k =int(self.slider_K.val)

        ## Choosing only the first k rank to construct the image
        self.X_approx = self.u[:, :self.k] @ self.SIGMA[0:self.k, :self.k] @ self.v[:self.k, :]
        self.imag_approx=self.ax1.imshow(self.X_approx)
        self.imag_approx.set_cmap('gray')


        self.ax1.set_title('Compressed Image for K value of  '+str(self.k), fontweight="bold", size=15, color='yellow')
        """
    Displaying the present value of k
        """
