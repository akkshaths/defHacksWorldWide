import pandas as pd
import openpyxl

data = pd.read_excel('clubList.xlsx', nrows = 29)

df = pd.DataFrame(data, columns= ['Clubs','Address', 'Tag1','Tag2','Tag3', 'Social Media Links', 'Website Link'])

club = df['Clubs']
tag1 = df['Tag1']
tag2 = df['Tag2']
tag3 = df['Tag3']
address = df['Address']
social = df['Social Media Links']
link = df['Website Link']

class Filter:
    def __init__(self, interest):
        self.interest = interest

    def returnClubNames(self):
        dict1 = {
            'Club Name': [],
            'Social Media': [],
            'Address': [],
            'Link': []
        }
        for x in range(0, len(club)):
            if tag1[x] in self.interest or tag2[x] in self.interest or tag3[x] in self.interest:
                dict1['Club Name'].append(club[x])
                dict1['Address'].append(address[x])
                dict1['Link'].append(link[x])
                dict1['Social Media'].append(social[x])

        dataFrame = pd.DataFrame.from_dict(dict1)
        return dataFrame



y = Filter(['Finance', 'Engineering', 'Medical'])
print(y.returnClubNames())