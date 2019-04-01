import pandas as pd
import numpy as np
doc_data=pd.DataFrame(pd.read_excel('Final_Train.xlsx'))
#print(doc_data)
Qualification=doc_data['Qualification']
#print(Qualification)
experience=doc_data['Experience']
#print(experience)
rating=doc_data['Rating']
#print(rating)
place=doc_data['Place']
#print(place)
profile=doc_data['Profile']
#print(profile)
other_info=doc_data['Miscellaneous_Info']
#print(other_info)
fees=doc_data['Fees']
#print(fees.head)
doc_data = doc_data.drop(['Fees','Rating'],axis = 1).copy()
#print(doc_data.head)

columns=doc_data.columns
print(columns)
for i in range(len(columns)):
  unique = (list(set(doc_data[columns[i]])))
  numUnique = []
  for j in range(0,len(unique)):
    numUnique.append(j)

  doc_data[columns[i]] = doc_data[columns[i]].replace(unique,numUnique)
#print(doc_data.head)  
from sklearn.linear_model import LinearRegression

reg = LinearRegression().fit(doc_data, fees)
from sklearn.metrics import accuracy_score

pred = reg.predict(doc_data)
#print(pred.shape)
def pred_acc(YPred,fees):
  mse = np.mean((YPred-fees)**2)
  totalErr = np.mean((fees)**2)
  print (100 - ((mse/totalErr)*100))

pred_acc(pred,fees)

