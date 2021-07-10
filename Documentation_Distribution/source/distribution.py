"""class for animating a distriution"""
class animated_histo:
    """
    parameters:

    a_ddist(float)==
    discrete distriution
    """



    def __init__(self,a_ddist):   # Constructor with DDist object as input
        self.ddist=a_ddist
                # These are for plotting related things
        self.plt=plt
        self.anim=anim
        self.fig, self.ax = self.plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)
        self.ax.set_ylim(0,50)
        self.bin_division=15        # number of division for the histogram
        self.bins=np.linspace(self.ddist.min_limit,self.ddist.max_limit,self.bin_division)
        self.holder=list([])            # The container
        self.holder.append(self.ddist.Draw())       # taking a sample


    def animate(self,i):
        """

        The animate function is the main part of this object. it is called iteratively

        """
        self.ax.hist(self.holder,self.bins, color="blue", ec="blue")
        self.holder.append(self.ddist.Draw())   # Drawing a  sample


    def start(self):
        """Used to start the animation


        """
        ani= anim.FuncAnimation(self.fig,self.animate, interval=200) # Initaites the animation
        """
        Intiates the animation
        """
        self.plt.show() # plot the figure on the screen
