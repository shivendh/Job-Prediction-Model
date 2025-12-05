import joblib
import pandas as pd
import numpy as np
from sklearn import decomposition
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Normalizer

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier


dataset = pd.read_csv("roo_data.csv")

# get the feature columns from the dataset
data = dataset.iloc[:,:-1].values

# get the label
label = dataset.iloc[:,-1].values
print(len(data[0]))

# encode the rows 14 -> 38
labelencoder = LabelEncoder()
for i in range(14,38):
    data[:,i] = labelencoder.fit_transform(data[:,i])
print(data[:5])


# normalize values in the rows 0-14
data1=data[:,:14]

normalized_data = Normalizer().fit_transform(data1)
print(normalized_data.shape)

data2=data[:,14:]
data2.shape

# create a new DF using new encoded and normalized values
df1 = np.append(normalized_data,data2,axis=1)

X1 = pd.DataFrame(df1,columns=['Acedamic percentage in Operating Systems', 'percentage in Algorithms',
       'Percentage in Programming Concepts',
       'Percentage in Software Engineering', 'Percentage in Computer Networks',
       'Percentage in Electronics Subjects',
       'Percentage in Computer Architecture', 'Percentage in Mathematics',
       'Percentage in Communication skills', 'Hours working per day',
       'Logical quotient rating', 'hackathons', 'coding skills rating',
       'public speaking points', 'can work long time before system?',
       'self-learning capability?', 'Extra-courses did', 'certifications',
       'workshops', 'talenttests taken?', 'olympiads',
       'reading and writing skills', 'memory capability score',
       'Interested subjects', 'interested career area ', 'Job/Higher Studies?',
       'Type of company want to settle in?',
       'Taken inputs from seniors or elders', 'interested in games',
       'Interested Type of Books', 'Salary Range Expected',
       'In a Realtionship?', 'Gentle or Tuff behaviour?',
       'Management or Technical', 'Salary/work', 'hard/smart worker',
       'worked in teams ever?', 'Introvert'])



# encode the labels
label = labelencoder.fit_transform(label)
print(len(label))

# create a labels' DataFrame
y=pd.DataFrame(label,columns=["Suggested Job Role"])
print(y.head())

# xgboost

# split training and testing data
X_train,X_test,y_train,y_test=train_test_split(X1,y,test_size=0.3,random_state=10)

# reshape the training data
X_train=pd.to_numeric(X_train.values.flatten())
X_train=X_train.reshape((14000,38))


# Fit the model
model = XGBClassifier()
model.fit(X_train, y_train)

# save the model
with open('model.joblib', 'wb') as f:
    joblib.dump(model, f)
