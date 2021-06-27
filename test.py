import pandas as pd
import os

df = pd.DataFrame({'Fruit':['apples','oranges','pears','avocados'],'Price':[0.50, 1.12,0.85,1.90], 'Weight': [3.2, 5.6, 2.2, 3.1] })
df2 = df.to_html()

for i in range(df.shape[0]):
    for j in range(df.shape[1]): 
        print (i,j)

def create_html_table(x):
    
    row_data = ''

    for i in range(x.shape[0]):

        for j in range(x.shape[1]):        
            if ((i % 2) != 0) & (j == 0): #not an even row and the start of a new row
                row_data += '\n<tr style="background-color:#f2f2f2"> \n <td class = "text_column">'+str(x.iloc[i,j])+'</td>'

            elif j == 0: #The first column
                row_data += '\n<tr> \n <td class = "text_column">'+str(x.iloc[i,j])+'</td>'
            
            elif j == 1: #second column
                row_data += '\n <td class = "number_column">'+str(x.iloc[i,j])+'</td>'
            
            elif j == 2: #third column and our last column in my example
                row_data += ' <td class = "number_column">'+str(x.iloc[i,j])+'</td> \n </tr>'

            else:
                row_data += '\n <td class = "number_column">'+str(x.iloc[i,j])+'</td>'
                
    return row_data



print(create_html_table(df))