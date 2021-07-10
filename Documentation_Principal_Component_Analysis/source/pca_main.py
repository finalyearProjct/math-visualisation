class PCA:
    """Principal Component Analysis Object

    Parameters:
    
    patient_object_list ==  Patient object list form the patient class

    dimension == number of dimension to be reduced

    """
    def __init__(self,patient_object_list,dimension=2): # Constructor

        # This accepts patient obj list and number of dimension to be reduced
        self.np_0=np
        # Creating an instance of numpy obj
        self.plt_0=plt
        # Creating an instance of pyplot object

        self.f=self.plt_0.figure("Patient Correlation Analysis",facecolor='yellow')
        # Creating a figure object
        self.f.set_figheight(10)
        # Setting height
        self.f.set_figwidth(15)
        # Setting width

        self.list_patient=patient_object_list
        # Re assigning parsed value to object's attribute
        self.number_dimension=dimension
        # Re assigning parsed value to object's attribute

        self.list_patient_names=list(np.arange(len(self.list_patient)))
        # creating ID for patient
        self.list_attributes=self.list_patient[0].get_Attributes()
        # Getting attributes from a patient obj
        self.X=list([])
        # creating an empty list
        self.Computational_part()
        # calling the object's function
        self.boot_induvidual_plot()
        # calling the object's function

    def boot_induvidual_plot(self):     # Setting up induvidual plots
        """
        Setting up induvidual plots
        """
        self.plot_traits = list([self.plt_0.subplot2grid((2, 5), (0, 0)), self.plt_0.subplot2grid((2, 5), (0, 1)),
                                 self.plt_0.subplot2grid((2, 5), (0, 2)), self.plt_0.subplot2grid((2, 5), (0, 3)),
                                 self.plt_0.subplot2grid((2, 5), (0, 4))])

        # creatng list of  plot objects

        for x in range(len(self.X_transp)):   # Iterating over each attributes patient

            present=self.plot_traits[x]
            # Selecting a particular plot object
            present.set_facecolor('orange')
            # setting face color
            present.scatter(self.np_0.arange(len(self.list_patient_names)),self.X_transp[x],c='blue')
            # drawing a scatter plot of this attribute

            present.xaxis.set_major_locator(plt.MultipleLocator(1))

            present.set_xlabel('Patient ID', fontweight='bold')
            # setting X-LABEL
            present.set_ylabel(self.list_attributes[x], fontweight='bold')
            # setting Y-LABEL
            present.title.set_text(self.list_attributes[x]+"  Variation")
            # setting Title

            present = self.plt_0.subplot2grid((2, 5), (1, 0), colspan=5)
            # to plot the present's status
            present.scatter(self.X_reduced_transp[0], self.X_reduced_transp[1], c='red')
            # plotting in the BOTTOM-PLOT

            present.set_xlabel("Principle Component -1", fontweight='bold')
            # setting X-LABEL
            present.set_ylabel("Principle Component -2", fontweight='bold')
            # setting Y-LABEL

            for x in range(len(self.list_patient_names)):   # Naming each patient with ID
                self.list_patient_names[x] = "Patient " + str(x)
                # Eg: Patient 0,Patient 1...
            for i, txt in enumerate(self.list_patient_names):   # This is used to enumerate the scatter plots label
                present.annotate(txt, (self.X_reduced_transp[0][i] + 1, self.X_reduced_transp[1][i]), fontsize=10, c='black')
                # Coonecting with present
    def Computational_part(self):
        """
        Computational part
        """

        self.X=list([])
        # creating an empty list
        for x in self.list_patient:
            self.X.append(x.get_Values())
            # Accessing the values and appending this to the created list

        self.X_transp = np.transpose(self.X)  # Transposing the vector

        # Computation Part

        #  mean Centering the data
        self.X_meaned = self.X - self.np_0.mean(self.X, axis=0)

        # Covariance matrix calculation
        self.cov_mat = self.np_0.cov(self.X_meaned, rowvar=False)

        # Eigen calculations
        eigen_values, eigen_vectors = self.np_0.linalg.eigh(self.cov_mat)

        # Reverse the array
        sorted_index = self.np_0.argsort(eigen_values)[::-1]

        # Reverse the array
        self.sorted_eigenvalue = eigen_values[sorted_index]
        self.sorted_eigenvectors = eigen_vectors[:, sorted_index]

        # making subsets

        self.eigenvector_subset = self.sorted_eigenvectors[:, 0:self.number_dimension]

        self.X_reduced = self.np_0.dot(self.eigenvector_subset.transpose(), self.X_meaned.transpose()).transpose()

        # This is the final reduced Vector

        self.X_reduced_transp = np.transpose(self.X_reduced)
    def animate(self,i):   # Animate function is called iteratively
        """
        Animate function is called iteratively
        """

        for x in self.list_patient:  # Traversing through each patient
            x.Update()
            # updating each
        self.Computational_part()
        # invoking obj's function
        self.boot_induvidual_plot()
        # invoking obj's function
    def Start(self):   # this is used to start the object
        """
        This is used to start the object
        """
        ani = anim.FuncAnimation(self.f, self.animate, interval=1000)
        # animating object wth 1 sec gap
        self.plt_0.tight_layout()
        self.plt_0.show()
        # showing the plot
