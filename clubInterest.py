import pandas as pd
import openpyxl
from IPython.display import display

class Filter:
    def __init__(self):
        self.data = pd.read_excel('TCNJ.xlsx', nrows = 29)

        self.df = pd.DataFrame(self.data, columns= ['Clubs','Address', 'Tag1','Tag2','Tag3', 'Social Media Links', 'Link'])

        self.club = self.df['Clubs']
        self.tag1 = self.df['Tag1']
        self.tag2 = self.df['Tag2']
        self.tag3 = self.df['Tag3']
        self.address = self.df['Address']
        self.social = self.df['Social Media Links']
        self.link = self.df['Link']
        

    def returnClubNames(self, interest):
        dict1 = {
            'Club Name': [],
            'Address': [],
            'Social Media': [],
            'Link': []
        }
        for x in range(0, len(self.club)):
            if self.tag1[x] in interest or self.tag2[x] in interest or self.tag3[x] in interest:
                dict1['Club Name'].append(self.club[x])
                dict1['Address'].append(self.address[x])
                dict1['Link'].append(self.link[x])
                dict1['Social Media'].append(self.social[x])

        dataFrame = pd.DataFrame.from_dict(dict1)
        return dataFrame.to_html()

    def searchFor(self, query):
        dict2 = {
            'Club Name': [],
            'Address': [],
            'Social Media': [],
            'Link': []
        }
        if query in list(self.club):
            x = list(self.club).index(query)
            dict2['Club Name'].append(self.club[x])
            dict2['Address'].append(self.address[x])
            dict2['Link'].append(self.link[x])
            dict2['Social Media'].append(self.social[x])
        dataFrame = pd.DataFrame.from_dict(dict2)
        return dataFrame.to_string()

    def printting(self):
        dict1 = {
            'Club Name': self.club,
            'Address': self.address,
            'Social Media': self.social,
            'Link': self.link,
            'Tag1': self.tag1,
            'Tag2': self.tag2,
            'Tag3': self.tag3
        }
        dataFrame = pd.DataFrame.from_dict(dict1)
        tabHTML = dataFrame.to_html(index=False)
        return tabHTML

y = Filter()
#print(y.printting())
data = y.printting()
print(data)

# ansh = list(y.printting())
# if 'Economics Club' in ansh:
#     print('success')
