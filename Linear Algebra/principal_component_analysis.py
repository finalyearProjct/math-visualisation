import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
import patient_object

class PCA:
    def __init__(self,patient_object_list,dimension=2):
        self.np_0=np
        self.plt_0=plt

        self.f=self.plt_0.figure("Patient Correlation Analysis",facecolor='yellow')
        self.f.set_figheight(10)
        self.f.set_figwidth(15)

        self.list_patient=patient_object_list
        self.number_dimension=dimension
        self.list_patient_names=list(np.arange(len(self.list_patient)))
        self.list_attributes=self.list_patient[0].get_Attributes()
        self.X=list([])
        self.Computational_part()
        self.boot_induvidual_plot()
    def boot_induvidual_plot(self):
        self.plot_traits = list([self.plt_0.subplot2grid((2, 5), (0, 0)), self.plt_0.subplot2grid((2, 5), (0, 1)),
                                 self.plt_0.subplot2grid((2, 5), (0, 2)), self.plt_0.subplot2grid((2, 5), (0, 3)),
                                 self.plt_0.subplot2grid((2, 5), (0, 4))])

        for x in range(len(self.X_transp)):

            present=self.plot_traits[x]
            present.set_facecolor('orange')
            present.scatter(self.np_0.arange(len(self.list_patient_names)),self.X_transp[x],c='blue')

            present.xaxis.set_major_locator(plt.MultipleLocator(1))

            present.set_xlabel('Patient ID', fontweight='bold')
            present.set_ylabel(self.list_attributes[x], fontweight='bold')
            present.title.set_text(self.list_attributes[x]+"  Variation")

            present = self.plt_0.subplot2grid((2, 5), (1, 0), colspan=5)
            print(self.X_reduced_transp[0])
            present.scatter(self.X_reduced_transp[0], self.X_reduced_transp[1], c='red')
                    #present.title.set_text("Patient Similarity Chart")

            present.set_xlabel("Principle Component -1", fontweight='bold')
            present.set_ylabel("Principle Component -2", fontweight='bold')

            for x in range(len(self.list_patient_names)):
                self.list_patient_names[x] = "Patient " + str(x)
            for i, txt in enumerate(self.list_patient_names):
                present.annotate(txt, (self.X_reduced_transp[0][i] + 1, self.X_reduced_transp[1][i]), fontsize=10, c='black')
    def Computational_part(self):
        self.X=list([])
        for x in self.list_patient:
            self.X.append(x.get_Values())
            # self.list_patient_names.append(x.name)

        self.X_transp = np.transpose(self.X)

        ##### Computation Part  ########

        # # mean Centering the data
        self.X_meaned = self.X - self.np_0.mean(self.X, axis=0)

        ## Covariance matrix calculation
        self.cov_mat = self.np_0.cov(self.X_meaned, rowvar=False)

        # # Eigen calculations
        eigen_values, eigen_vectors = self.np_0.linalg.eigh(self.cov_mat)

        # Reverse the array
        sorted_index = self.np_0.argsort(eigen_values)[::-1]

        # Reverse the array
        self.sorted_eigenvalue = eigen_values[sorted_index]
        self.sorted_eigenvectors = eigen_vectors[:, sorted_index]

        # making subsets

        self.eigenvector_subset = self.sorted_eigenvectors[:, 0:self.number_dimension]

        self.X_reduced = self.np_0.dot(self.eigenvector_subset.transpose(), self.X_meaned.transpose()).transpose()

        self.X_reduced_transp = np.transpose(self.X_reduced)


    def animate(self,i):
        for x in self.list_patient:
            x.Update()
        self.Computational_part()
        self.boot_induvidual_plot()


    def start(self):
        ani = anim.FuncAnimation(self.f, self.animate, interval=1000)
        self.plt_0.tight_layout()
        self.plt_0.show()
