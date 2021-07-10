"""Monte_carlo object"""
class Monte_carlo:
    """
    parameters:

    time_interval(float)==
        time interval for the animation
    """

    def __init__(self,time_interval):

             # Constructor

        self.np_0=np

        # Creating instance of numpy object
        self.plt_0=plt
        # Creating instance of pyplot object
        self.time_gap=time_interval
        # saving the time gap in this variable
        self.radi=25
        # Setting radi of BIG circle
        self.ax_X_list = list([])
        # Creating a blank list for appending X value
        self.ax_Y_list = list([])
        # Creating a blank list for appending Y value
        self.ax_Y_pi = list([])
        # constant pi value list
        self.figure,self.axes =self.plt_0.subplots(2)
        # Creating subplots
        self.plt_0.suptitle("Monte Carlo simulation - Demo")
        # Creating a BIG title on the TOP part
        self.axes[0].set_ylim(0, 50)
        # Setting Y-Limit for the plot
        self.axes[0].set_xlim(0, 50)
        # Setting X-Limit for the plot
        self.axes[0].set_aspect(1)
        # Setting len to breadth ratio 1
        Drawing_colored_circle =self.plt_0.Circle((10, 10), 1.5)
        # Taking a sample
        Drawing_uncolored_circle =self.plt_0.Circle((25, 25), 25, fill=True, color='yellow')
        # Drawing the BIG circle
        self.axes[0].add_artist(Drawing_colored_circle)
        # Inserting the drawn circle into the plot
        self.axes[0].add_artist(Drawing_uncolored_circle)
        # Inserting the drawn circle into the plot
        self.axes[0].title.set_text('Sampling Process')
        # Setting the title for the first plot
        self.hit = 0

        self.total = 0
        # Total Picks

    def animate(self,i):
        """

        The animate function is the main part of this obj,it is called iteratively

        """
        self.total=self.total+1
        # Incrementing the total pick
        a=self.np_0.random.randint(0,50,2)
        # Choosing a random point
        Drawing_colored_circle =self.plt_0.Circle((a[0],a[1]), 1.5)
        # Drawing circle with center at that point
        mag=self.np_0.sqrt(self.np_0.square(a[0]-25)+self.np_0.square(a[1]-25))
        # Computing L-2 Norm
        if mag<self.radi:               # Checking of it is OUTSIDE or INSIDE
            self.hit=self.hit+1
            # If TRUE increment the hit
        value=self.hit*50*50/(self.total*self.np_0.square(self.radi))
        # Estimating Pi value from Area(Square),Area(Circle),Total hit,Total picks

        self.ax_Y_list.append(value)
        # Appending that to the list
        self.ax_X_list.append(self.total)
        # incrementing the  X list
        self.ax_Y_pi.append(3.14)
        # inserting 3.14 to draw straight line

        self.axes[0].add_artist(Drawing_colored_circle)
        # Inserting the drawn circle into the plot

        self.axes[1].clear()
        # Clearing the plot after each iteration
        self.axes[1].set_ylim(0,5)
        # Setting Y-LIMIT
        self.axes[1].set_xlim(0,self.total+2)
        # Re-Setting X-LIMIT
        self.plt_0.yticks(self.np_0.arange(0,5,.5))
        # Setting Y-TICKS
        self.axes[1].plot(self.ax_X_list,self.ax_Y_list,color='black',label ='Estimated value')
        # Plotting Estimated value
        self.axes[1].plot(self.ax_X_list, self.ax_Y_pi, color='red', marker="_",label ='Target value')
        # Plotting Reference value
        self.axes[1].set_ylabel('Estimation')
        # Setting Y-LABEL
        self.axes[1].set_xlabel('Samplng time')
        # Setting X-LABEL
        self.axes[1].title.set_text('Graphical Representation')
        # Setting TITLE for the plot
        self.axes[1].legend()
        # Displaying the Legend

    def start(self):
        """Used to start the animation


        """
        ani=anim.FuncAnimation(self.figure,self.animate,interval=self.time_gap*1000)
        """
    Creating animation function according to the TIME_GAP
        """
        self.plt_0.show()
        # Show the plot
