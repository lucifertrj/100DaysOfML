from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le = LabelEncoder()
def encode(data):
    data.fillna(method="ffill",inplace=True)
    for feature in data.columns:
        if data[feature].dtype == 'O':
            data[feature] = le.fit_transform(data[feature])
    return data