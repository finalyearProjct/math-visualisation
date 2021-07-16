class ITS:
    """
    Inverse transform sampling class ,here we are using uniform distrubution to generate a Normal distribution. Inverse transform is the basis for such a technique. This is made for just a demonstration  purpose."""
    def __init__(self):# Nothing is given in the constructor
        self.np_0 = np
        self.plt_0 = plt
        self.ss_0=ss        # This is the  statistics module,which is used for plotting the shape of normal distribution.
        self.mapped_list =list([])
        self.bin_list=list(self.np_0.linspace(-4,4,40))
        self.x_values=np.linspace(-4,4, 5000)
        self.y_values_0=ss.norm.cdf(self.x_values,0,1) # For plotting the cumulative distribution function.

        self.figure, self.axes = self.plt_0.subplots(2)         # Just for formatting purpose title,colour ect.
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
        """
        This function is the main function,which is responsible for sampling from uniform distribution then use inverse of the CDF of gaussian ditsribution to generate normal distribution."""

        self.axes[0].plot(self.x_values, self.y_values_0,color='black')
        sample=self.np_0.random.uniform(0,1)## sampling process
        self.axes[0].axhspan(sample-.01,sample+.01, color='pink', alpha=.2)
        inverse_value=self.ss_0.norm.ppf(sample)## Mapping with the help of inverse CDF.
        self.mapped_list.append(inverse_value)
        self.axes[0].axvspan(inverse_value - .01,inverse_value + .01, color='pink', alpha=.2)
        self.axes[1].hist(self.mapped_list,self.bin_list,color='black')

    def start(self):
        '''The function that is used to trigger the start of ITS  simulation. '''
        ani = anim.FuncAnimation(self.figure, self.animate, interval=1)
        self.plt_0.show()
