import pandas as pd
import openpyxl
import time
from datetime import time


class editSchedule:
    def __init__(self):
        self.data = pd.read_excel('userData.xlsx', nrows = 29)

        self.df = pd.DataFrame(self.data, columns= ['Time', 'Class/Club'])

    def addActivity(self, add, timing):
        #add is the names of the club as a list
        #timing is the times of the activities in a list
        
        list1 = timing + list(self.df['Time'])
        listTime = sorted(list1)

        list2 = add + list(self.df['Class/Club'])
        listAct = sorted(list2)

        dictForSchedule = {
            'Time': listTime,
            'Class/Club': listAct
        }

        dataFrame = pd.DataFrame(dictForSchedule, columns=['Time', 'Class/Club'])
        dataFrame.to_excel('userData.xlsx', engine='openpyxl')

        return ('sucess')



y = editSchedule()
timing = ['10:30', '8:45', '6:30']
c = []
for x in timing:
    c.append()
y.addActivity(['Soccer'], [])