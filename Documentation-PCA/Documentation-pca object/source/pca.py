"""
 Patient Object for PCA constructor
 """
class patient:
    """
    parameter: a_name
            Seting a name
    """
    def __init__(self,a_name):  # Constructor
        self.name=a_name        # Setting name

        self.body_temp=np.random.normal(36.51,1.78)  # Initialising body_temp
        self.systolic_bp=np.random.normal(138.7,35.6)  # systolic_bp
        self.diastolic_bp=np.random.normal(75.5, 21.0)  # Initialising diastolic_bp
        self.heart_rate=np.random.normal(100.5,24.8)    # Initialising heart_rate
        self.breath_rate =np.random.normal(19.66,5.875)   # Initialising breath_rate

    def get_Values(self):
        """
        Get the parameters as a list
        return the List
        """
        return list([self.body_temp,self.systolic_bp,self.diastolic_bp,self.heart_rate,self.breath_rate])
    def get_Attributes(self):
        """
         Get the Attributes of the patient
         return the list
        """
        return ['Body temperature','Systolic B.P','Diastolic B.P','Heart rate','Breath Rate']
    def Update(self):
        """
        Re assign all the attributes of the patient
        Using Normal Distribution re assign the attribute values
        """
        self.body_temp = np.random.normal(36.51, 1.78)
        self.systolic_bp = np.random.normal(138.7, 35.6)
        self.diastolic_bp = np.random.normal(75.5, 21.0)
        self.heart_rate = np.random.normal(100.5, 24.8)
        self.breath_rate = np.random.normal(19.66, 5.875)
