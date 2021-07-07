import numpy as np


class Patient:
    def __init__(self,a_name):
        self.name=a_name
        self.body_temp=np.random.normal(36.51,1.78)
        self.systolic_bp=np.random.normal(138.7,35.6)
        self.diastolic_bp=np.random.normal(75.5, 21.0)
        self.heart_rate=np.random.normal(100.5,24.8)
        self.breath_rate =np.random.normal(19.66,5.875)
    def get_Values(self):
        return list([self.body_temp,self.systolic_bp,self.diastolic_bp,self.heart_rate,self.breath_rate])
    def get_Attributes(self):
        return ['Body temperature','Systolic B.P','Diastolic B.P','Heart rate','Breath Rate']
    def Update(self):
        self.body_temp = np.random.normal(36.51, 1.78)
        self.systolic_bp = np.random.normal(138.7, 35.6)
        self.diastolic_bp = np.random.normal(75.5, 21.0)
        self.heart_rate = np.random.normal(100.5, 24.8)
        self.breath_rate = np.random.normal(19.66, 5.875)
