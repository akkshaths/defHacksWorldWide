import pandas as pd
import openpyxl

data = pd.read_excel('clubList.xlsx', nrows = 29)

df = pd.DataFrame(data, columns= ['Clubs','Address', 'Tag1','Tag2','Tag3'])

club = df['Clubs']
tag1 = df['Tag1']
tag2 = df['Tag2']
tag3 = df['Tag3']

class Filter:
    def __init__(self, interest):
        self.interest = interest

    def returnClubNames(self):
        set1 = set([])
        for x in range(0, len(club)):
            if tag1[x] in self.interest or tag2[x] in self.interest or tag3[x] in self.interest:
                set1.add(club[x])

        return set1


y = Filter(['Finance', 'Engineering', 'Medical'])
print(y.returnClubNames())