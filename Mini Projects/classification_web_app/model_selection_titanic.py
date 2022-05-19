from encoder import encode
from sklearn.preprocessing import StandardScaler
import pandas as pd

def features():
    data = pd.read_csv("./dataset/titanic_survival.csv")
    data = encode(data)
    feature_selection = ["Age","SibSp","Sex","Cabin"]
    X = data[feature_selection]
    sc = StandardScaler()
    X = sc.fit_transform(X)
    return X