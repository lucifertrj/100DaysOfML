from encoder import encode
import pandas as pd
from sklearn.preprocessing import StandardScaler

def features():
    data = pd.read_csv("./dataset/hospital_survival.csv")
    data = encode(data)
    feature_selection = ["Treated_with_drugs","Patient_Age",'Patient_Body_Mass_Index','Patient_Smoker','Patient_mental_condition','Number_of_prev_cond']
    X = data[feature_selection]
    sc = StandardScaler()
    X = sc.fit_transform(X)
    return X