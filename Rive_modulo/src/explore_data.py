#Learning ML
#13/05/2026
#Reading and understanding data in CSV Files

import pandas as pd #pandas is a tool to read data

#Imported 21/05/2026
from sklearn.preprocessing import LabelEncoder #This is done in order to turn the labels in text into readable material for the model, i.e. numbers

from sklearn.model_selection import train_test_split # automatically divides data into training and testing groups

from sklearn.ensemble import RandomForestClassifier #a machine learning classifcation algorithm, meaning, it's an AI pattern detector

import numpy as np
from sklearn.metrics import accuracy_score


#File Loading

df= pd.read_csv("C:/Users/ACER/OneDrive/Desktop/isdb/2026/1_Semestre/Seguranca de Sistemas/Detector-de-Intrus-es\Rive_modulo/Dados/dataset1.csv") #pointing which file to read

# print(df.head()) #SHows first 5 rows
# print(df.shape) #Prints the size of the dataset
# print(df.columns) #Prints column labels

#File loading ends

#Cleaning up the data
#here, unnecessary spaces are cleaned off of column labels
df.columns= df.columns.str.strip()
#print(df.columns)
#cleaning ends

# Modifying date: 21/05/2026
#Feature/Label split
X= df.drop("Label", axis= 1) #creates a new dataset without the label colum:The model won't see the snwer while learning; In here, Label is what is being removed, and axis=1 means columns
y= df["Label"] #This gives the answers for the training
 
# print(X.head()) #This should show all columns but the label column
# print(y.head()) #This should show the resuts, meaning, just the labels

#split ends

#encoding
encoder= LabelEncoder()
y_encoded= encoder.fit_transform(y)

#print(y.head())
#print(y_encoded[:5])

X = X.replace([np.inf, -np.inf], np.nan)
valid_rows= X.notna().all(axis=1)
X= X[valid_rows]
y_encoded= y_encoded[valid_rows]

X_train, X_test, y_train, y_test= train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# print(X_train.shape) #prints the number of rows and columns meant for training
# print(X_test.shape) #prints the number of rows and columns meant for testing; This is data the model has never seen before

#encoding ends


#Training model
#model= RandomForestClassifier() :this creates an empty AI model, as in, it knows nothing yet

print("start training")
model = RandomForestClassifier(n_estimators=10)
model.fit(X_train, y_train) #this line gives the model learning data

print("Model trained successfully") 

#Training ends

#Testing model

y_pred= model.predict(X_test)

accuracy= accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

#testing ends
