

import numpy as np

from matplotlib import pyplot as plt
def rotation(a_degree):     ## Function to rotate a vector bu=y some angle in a plane
    """
    Function to rotate a vector bu=y some angle in a plane
    """
    theta=np.deg2rad(a_degree)  ## converting degree to radian
    rotation_matrix = np.column_stack([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
    # Constructing the rotation matrix
    return rotation_matrix      # returning the matrix

## List of Some standard matrices

reflection=np.column_stack([[1,0],[0,-1]])
shear=np.column_stack([[1,0],[1,1]])
permutation=np.column_stack([[0,1],[1,0]])
project_x=np.column_stack([[1,0],[0,0]])
project_y=np.column_stack([[0,0],[0,1]])
eye=np.column_stack([[1,0],[0,1]])
class Linear_transformation:
    """
    Constructor is the text which we want to get tranformed and the list of transformations
        Parameters:
            a_text: text to transform

            a_transform_list: list of transformation
    """


    def __init__(self,a_text,a_transform_list):

        ## constructor is the text which we want to get tranformed and the list of transformations

        # create a subplot and do all the neccessary formatting
        self.fig,self.axs = plt.subplots(2)
        plt.suptitle("Linear Transformation - Visualizer",color='black',fontweight="bold", size=30)
        self.fig.canvas.set_window_title('Linear Transformation - Visualizer')
        self.fig.set_figheight(8)
        self.fig.set_figwidth(14)
        self.fig.patch.set_facecolor('red')

        ## just sett the plots facecolor
        self.axs[0].set_facecolor('black')
        self.axs[1].set_facecolor('yellow')

        #This is the TEXT-PIXEL mapping dictionary

        self.data_base=dict(
    {'A':[0,5,10,16,22,18,14,9,4,11,12,13],
     'B':[1,6,11,16,21,22,23,19,13,12,9,3,2],
     'C':[3,2,6,11,16,22,23,24,4],
     'D':[3,2,1,6,11,16,21,22,23,19,14,9],
     'E':[4,3,2,1,6,11,16,21,22,23,24,12,13,14],
     'F':[1,6,11,12,13,16,21,22,23,24],
     'G':[24,23,22,21,20,15,10,5,0,1,2,7,12,13,14,9,4],
     'H':[20,15,10,5,0,11,12,13,14,19,24,9,4],
     'I':[1,2,3,7,12,17,22,21,23],
     'J':[5,1,2,3,8,13,18,23,22],
     'K':[20,15,10,5,0,11,12,18,24,8,4],
     'L':[21,16,11,6,1,2,3,4],
     'M':[0,5,10,15,20,16,12,18,24,19,14,9,4],
     'N':[0,5,10,15,20,16,12,8,4,9,14,19,24],
     'O':[1,5,10,15,21,22,23,19,14,9,3,2],
     'P':[1,6,11,16,21,22,23,19,13,12],
     'Q':[1,5,10,15,21,22,23,19,14,9,3,2,12,8,4],
     'R':[1,6,11,16,21,22,23,19,13,12,8,4],
     'S':[24,23,22,21,15,11,12,13,9,3,2,1,0],
     'T':[2,7,12,17,22,21,20,23,24],
     'U':[20,15,10,5,1,2,3,9,14,19,24],
     'V':[20,15,10,6,2,8,14,19,24],
     'W':[20,15,10,5,0,6,12,8,4,9,14,19,24],
     'X':[20,16,12,6,0,18,24,8,4],
     'Y':[20,16,12,7,2,18,24],
     'Z':[20,21,22,23,24,18,12,6,0,1,2,3,4]

     })

        ## creating the grid space
        xvals = np.linspace(-4, 4, 9)
        yvals = np.linspace(-3, 3, 7)
        self.xygrid = np.column_stack([[x, y] for x in xvals for y in yvals])

        ## Applying the transformations in a cascaded manner one by one
        self.transform_list =a_transform_list
        self.net_transform=np.eye(2)
        for x in self.transform_list:
            self.net_transform = np.matmul(self.net_transform, x)


        self.text=a_text
        ## Number of steps to reach the final step
        self.steps=30

        ## creating the color map object
        self.colors = list(map(self.colorizer_light,self.xygrid[0],self.xygrid[1]))
        ## This is for storing the list of intermediate tranformed vector
        self.trans_xygrid=self.stepwise_transform(self.net_transform,self.xygrid,30)

        ## just for setting the len-breadth of the plot
        n=len(self.text)
        self.x_peak = n * 10
        self.y_peak = 15
        ## this is the main function for the whole TEXT
        self.m,self.c =self.ApplyTransform(self.text,self.net_transform, numsteps=self.steps, a_increamenter=15, a_origin_x=-10 - 5 * n)
        ## just creating tick points in the plot in x and y directions
        self.x_marks = np.arange(-self.x_peak,self.x_peak, 15)
        self.y_marks = np.arange(-self.y_peak,self.y_peak, 15)

    def colorizer_light(self,x, y):## function for Converting x and y value to a color map
        """
        Map x-y coordinates to a rgb color and the mapping is more lighter
        """
        r = min(1, 1 - y / 3)
        g = min(1, 1 + y / 3)
        b = 1 / 4 + x / 16
        return (r, g, b)
    def Sigmoid_mapping(self,x): ## function for converting any number to a number which lies in (0,1)
        """
        function for converting any number to a number which lies in (0,1)
        """
        return 1 / (1 + np.exp(-x))
    def colorizer_dark(self,x, y):## function for Converting x and y value to a color map
        """
        Map x-y coordinates to a rgb color and the mapping is more darker
        """
        r =self.Sigmoid_mapping(x - 2)
        g =self.Sigmoid_mapping(y - 2)
        b =self.Sigmoid_mapping(x - 2)
        return (r, g, b)

    def Symbol2DotArray(self,symbol='A'): ## The function to convert a charecter to a DOT ARRAY
        """
        The function to convert a charecter to a DOT ARRAY
        """

        ## input is the character
        list_points =self.data_base.get(symbol)
        list_vector = list([])
        for x in list_points:## for converting a sequence of numbers to list of positions
            cord_x = x % 5
            cord_y = (x - cord_x) / 5
            list_vector.append([cord_x, cord_y])
        list_vector = np.array(list_vector)
        list_vector = (np.transpose(list_vector)) - 2
        return list_vector
    def stepwise_transform(self,a, points, nsteps=30):  ## Function to get the list of transformed space
        """
        Function to get the list of transformed space
        where a: MATRIX
        where points: set of points who should get transformed
        where  nsteps: number of steps
        """
        # where a: MATRIX
        # where points: set of points who should get transformed
        #where  nsteps: number of steps

        transgrid = np.zeros((nsteps + 1,) + np.shape(points))

        # compute intermediate transforms
        for j in range(nsteps + 1):
            intermediate = np.eye(2) + j / nsteps * (a - np.eye(2))
            transgrid[j] = np.dot(intermediate, points)  # apply intermediate matrix transformation
        return transgrid

    def ApplyTransform(self,text, transform, numsteps=30, a_origin_x=-20, a_origin_y=0, a_increamenter=10):
        """
        This is the main fuction:

        where text:
        the text on which we need to apply these transformations

        where transform:
        is the NET TRANSFORMATION

        where numsteps:
        default value is 30

        where a_origin_x :
        the point from where the text starts along the X axis

        where a_origin_x :
        the point from where the text starts along the Y axis

        where a_increamenter:
        sets the distance between two characters//
        """
        origin_x = a_origin_x
        origin_y = a_origin_y
        increamenter = a_increamenter

        list_color = list([])
        list_dot_matrix = list([])
        list_transformed = list([])

        ## Whole transformed grid space is generated here..
        for x in text:
            m =self.Symbol2DotArray(x)
            list_dot_matrix.append(m)
            list_color.append(list(map(self.colorizer_dark, m[0], m[1])))
        for x in range(len(list_dot_matrix)):
            m =self.stepwise_transform(transform, list_dot_matrix[x], nsteps=numsteps)
            list_transformed.append(m)
        ## for all the above the transformation are applied with reference
        # to that particular charecter's center of mass...
        ## Now we are translating the characters to their respective positions
        for x in list_transformed:
            origin_x = origin_x + increamenter
            for y in x:
                y[0] = y[0] + origin_x
                y[1] = y[1] + origin_y

        return list_transformed, list_color
    def animate(self,i):                ##the function responsible for the animation effect
        """
        The function responsible for the animation effect
        """
        # just formatting
        self.axs[0].clear()
        self.axs[1].clear()

        ## Just converting any i value to a lower number
        x = i % 30


        ## Plotting everything by iterating by going through the loop-Specific to each move
        for y in range(len(self.m)):
            self.axs[1].set_title('Transformation Applied to the given TEXT', fontweight="bold", size=20,color='yellow')
            self.axs[1].scatter(self.m[y][x][0],self.m[y][x][1], s=120, color=self.c[y], edgecolor="none")
            self.axs[1].axis([-self.x_peak,self.x_peak, -self.y_peak, self.y_peak])
            self.axs[1].set_xticks(self.x_marks)
            self.axs[1].set_yticks(self.y_marks)
        ### Setting the general settings
        self.axs[0].scatter(self.trans_xygrid[x][0],self.trans_xygrid[x][1], s=40, color=self.colors, edgecolor="none")
        self.axs[0].set_title('Transformation Applied to the  XY Grid', fontweight="bold", size=20,color='yellow')
        self.axs[0].axis([-10, 10, -10, 10])
        self.axs[0].set_aspect(1)
    def start(self):## Function to start  or trigger the animation function
        """
        Function to start  or trigger the animation function
        """
        ani = anim.FuncAnimation(self.fig, self.animate, interval=10)       ## calling with a gap of 10 msec
        plt.show()
