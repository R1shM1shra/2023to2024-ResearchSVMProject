# importing packages
import pandas as pd
from sklearn.svm import SVC

# importing data
data = pd.read_csv(r"C:\Users\894054\Downloads\cumulative.csv\cumulative.csv")

# assigning data to variables
y = data['classdata']
x = data[drop'correlatingvar2']

# build SVM model
SVM_Model = SVC('linear')
SVM_Model.fit(x,y)

print(f'Accuracy - : {SVM_Model.score(x,y):.3f}')
