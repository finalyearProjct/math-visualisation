import numpy as np
from matplotlib import pyplot as plt


class Matched_filter:
    def __init__(self,S):
        self.S=S

        self.fig,self.axs = plt.subplots(3)
        plt.suptitle("Matched Filter-Interactive",color='black',fontweight="bold", size=20)
        self.fig.canvas.set_window_title('Matched Filter-Interactive')
        self.fig.set_figheight(8)
        self.fig.set_figwidth(14)
        self.fig.patch.set_facecolor('white')

        self.ax_K=plt.axes([0.3, 0.02, 0.5, 0.04])
        self.slider_K=plt.Slider(self.ax_K, 'Slider',-len(S),len(S),0,color='red')
        self.slider_K.label.set_color('black')
        self.slider_K.label.set_size(15)

        self.counter=0
        self.axis_correlation=[0]
        self.value_correlation=[1]

        self.ax0 = plt.subplot2grid((3, 1), (0, 0))
        self.ax1 = plt.subplot2grid((3, 1), (1, 0))
        self.ax2 = plt.subplot2grid((3, 1), (2, 0))

        self.MakeupPlots()

        self.A = np.append(np.append(np.zeros(len(self.S) + 1), self.S), np.zeros(len(self.S)))
        self.rot_A=self.A
        self.axis = np.arange(-(len(self.S) + 1), len(self.S) + len(self.S), 1)
        self.ax0.stem(self.axis, self.A, linefmt='white')

        print(len(self.axis))
        print(len(self.rot_A))

        self.slider_K.on_changed(self.update)


    def MakeupPlots(self):

        self.ax0.set_facecolor('black')
        self.ax1.set_facecolor('black')
        self.ax2.set_facecolor('black')

        self.ax2.set_ylim(0, 1)


    def update(self,val):

        self.counter=self.counter+1
        self.axis_correlation.append(self.counter)
        k = int(self.slider_K.val)
        self.A_rot=self.rotate(self.A,k)
        self.ax1.clear()
        self.ax1.stem(self.axis,self.A_rot,linefmt ='white')
        self.ax2.clear()
        self.value_correlation.append(self.similarity(self.A,self.A_rot))
        self.ax2.plot(self.axis_correlation,self.value_correlation,color ='white')
        self.ax2.set_yticks(np.linspace(0,1,5))
        self.ax2.set_ylabel('Similarity')

    def rotate(self,A,n):
        k=(-n+len(self.A))%len(self.A)
        slice_0,slice_1=self.A[0:k],self.A[k:len(A)]
        return np.append(slice_1,slice_0)

    def similarity(self,A,rot_A):
        mag_A=np.linalg.norm(A)
        mag_rot_A=np.linalg.norm(rot_A)
        similarity=np.dot(A,rot_A)/(mag_A*mag_rot_A)
        return similarity

    def start(self):
        self.ax1.stem(self.axis,self.rot_A)
        plt.show()

# A=np.array([1,2,3,4,5])
# M=Matched_filter(A)
# M.start()
