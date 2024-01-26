import sys
import joblib
import csv
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import mean_squared_error 


def label_encoding(df_feature):
    le = LabelEncoder()
    out = pd.DataFrame(df_feature.copy())  
    out['condition'] = le.fit_transform(df_feature)
    #out = out.drop('condition',axis=1)
    return out

def concating(df_1,df_2):
    df_out = pd.concat([df_1,df_2],axis=1)
    return df_out


df = pd.read_csv(sys.argv[1])

#Making the suitable input data
condition = label_encoding(df['condition'])
input = df.drop(['uuid','condition','datasetId','SDRR_RMSSD'],axis=1)
input = concating(input,condition)

uuid=df['uuid'].to_list()

#Predicting based on the model trained
model=joblib.load("ai_cures.pkl")
prediction=model.predict(input)


#Storing the predicted HR to results.csv
csvfile=open('results.csv','w',newline='')
#Writing to results.csv
row=[]
csvwriter=csv.writer(csvfile)
csvwriter.writerow(['uuid','HR'])
for i in range(len(prediction)):
    row.append(uuid[i])
    row.append(prediction[i])
    csvwriter.writerow(row)
    row=[]

# x_tgt=pd.read_csv("sample_output_generated.csv")
# y_pred=model.predict(input)
# print(mean_squared_error(x_tgt['HR'],y_pred))