import numpy as np 
import pandas as pd
from scholarly import scholarly
import xlsxwriter

df = pd.read_excel("prof.xlsx","Sheet1")

professors_names = df["Professor name:"].values.tolist()

number_of_professors = len(professors_names)
citations_list = []
print("Total Number of Professors" + str(number_of_professors))

for i in range(number_of_professors):

    try:
        scholar = next(scholarly.search_author(str(professors_names[i])))
        print(scholar)
        citations_list.append(scholar["citedby"])
    except StopIteration:
        citations_list.append(0)
    print(i)
    

#print(citations_list)

finaldata = pd.DataFrame({'citedby':citations_list})
datatoexcel = pd.ExcelWriter("out.xlsx", engine = 'xlsxwriter')
finaldata.to_excel(datatoexcel,sheet_name='Sheet1')

datatoexcel.save()
