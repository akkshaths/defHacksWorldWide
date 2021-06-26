import pandas as pd
import openpyxl
import time
from datetime import datetime


class editSchedule:
    def __init__(self):
        self.data = pd.read_excel('userData.xlsx', nrows = 100, keep_default_na=False)

        self.df = pd.DataFrame(self.data, columns= ['Time', 'Class/Club'])

    def addActivity(self, add, timing):
        #add is the names of the club as a list
        #timing is the times of the activities in a list in form ['8:30', '6:45']

        d = []
        for x in timing:
            d.append(datetime.strptime(x, '%H:%M').time())


        c = []
        for x in list(filter(None, list(self.df['Time']))):
            c.append(datetime.strptime(x, '%H:%M:%S').time())
        
        list1 = d + c
        listTime = sorted(list1)
        #return sorted(list1)
        list2 = add + list(self.df['Class/Club'])
        listAct = []

        for x in listTime:
            ind = list1.index(x)
            listAct.append(list2[ind])

        dictForSchedule = {
            'Time': listTime,
            'Class/Club': listAct
        }

        dataFrame = pd.DataFrame(dictForSchedule, columns=['Time', 'Class/Club'])
        dataFrame.to_excel('userData.xlsx', engine='openpyxl', index=False)





y = editSchedule()
y.addActivity(['Soccer','Economics','Finance'], ['10:30', '8:45', '6:30'])

