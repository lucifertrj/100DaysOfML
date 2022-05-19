import streamlit
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB

import model_selection_titanic, model_selection_hospital

def features():
    params = dict()
    if clf_name == "Logistic Regression":
        slider_lr_c = streamlit.slider("c",min_value=0.2,max_value=1.0,step=0.1)
        params['C'] = slider_lr_c
        slider_lr_max_iter = streamlit.slider("max_iter",min_value=100,max_value=1500,step=100)
        params['max_iter'] = slider_lr_max_iter

    elif clf_name == "Decision Tree Classifier":
        slider_dc = streamlit.slider("max_depth",min_value=3,max_value=15,step=1)
        params['max_depth'] = slider_dc
        slider_dc_nodes = streamlit.slider("max_leaf_nodes",min_value=10,max_value=50,step=5)
        params['max_leaf_nodes'] = slider_dc_nodes

    elif clf_name == "Naive Bayes":
        slider_nb_alpha = streamlit.slider("alpha",min_value=0.0,max_value=1.0,step=0.1)
        params['alpha'] = slider_nb_alpha

    elif clf_name == "KNN":
        slider_k_value = streamlit.slider("n_neighbors",min_value=3,max_value=25,step=2)
        params['n_neighbors'] = slider_k_value

    else:
        slider_rf_n = streamlit.slider("n_estimators",min_value=100,max_value=1300,step=100)
        params['n_estimators'] = slider_rf_n
        slider_dc = streamlit.slider("max_depth",min_value=3,max_value=15,step=1)
        params['max_depth'] = slider_dc
    return params

def predict_ml(model):
    model = model.fit(x_train,y_train)
    predict = model.predict(x_test)
    streamlit.markdown("Accuracy Score: `{}`".format(accuracy_score(predict,y_test)))
    conf_matrix = confusion_matrix(y_test,predict)
    streamlit.markdown("**`Confusion Matrix`**")
    fig10, ax = plt.subplots()
    sns.heatmap(conf_matrix/np.sum(conf_matrix), annot=True,fmt='.2%', cmap='CMRmap')
    streamlit.pyplot(fig10)


streamlit.title("Classification Web App")
streamlit.subheader("Choose the below dataset and Algorithm")

streamlit.sidebar.markdown("Creator: [Tarun Jain](https://twitter.com/TRJ_0751)")
streamlit.sidebar.markdown("Learn ML: [100DaysOfML](https://github.com/lucifertrj/100DaysOfML)")
streamlit.sidebar.markdown("Blogs ML: [Anime Vyuh](https://animevyuh.org/category/machine-learning)")

dataset = streamlit.selectbox(label="Choose Dataset:",options=['Titanic Survival','Heart Disease'])
clf_name = streamlit.selectbox(label="Choose Classifier ML Model:",options=['Decision Tree Classifier','KNN','Logistic Regression','Random Forest Classifier','Naive Bayes'])

re_format = dataset.lower().replace(' ','_')+'.csv'
read_dataset = pd.read_csv(f"./dataset/{re_format}")

streamlit.subheader("Displaying 20 Sample Data")
streamlit.dataframe(read_dataset.sample(20))

fig1,axes1 = plt.subplots()
if dataset.lower().startswith('heart'):
    sns.countplot(x="Survived_1_year",data=read_dataset)
    X = model_selection_hospital.features()
    Y = read_dataset['Survived_1_year']
else:
    sns.countplot(x="Survived",data=read_dataset)
    X = model_selection_titanic.features()
    Y = read_dataset['Survived']

streamlit.subheader("Label of the Dataset")
streamlit.pyplot(fig1)

streamlit.subheader("Correlation")
fig3,axes3 = plt.subplots()
sns.heatmap(read_dataset.corr(),annot=True,linewidths=1)
streamlit.pyplot(fig3)

streamlit.subheader("Choose your desire Test-dataset size")
test_case = streamlit.slider("test_size_to_fit_model",min_value=0.15,max_value=0.35,step=0.02)
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=test_case)

streamlit.subheader(f"You have choosen: {clf_name}, vary Hyperparameters:")
model_features = features()


def main():
    if clf_name=="Decision Tree Classifier":
        model=DecisionTreeClassifier(max_depth=model_features['max_depth'],max_leaf_nodes=model_features['max_leaf_nodes'])
        predict_ml(model)

    elif clf_name=="Logistic Regression":
        model=LogisticRegression(C=model_features['C'],max_iter=model_features['max_iter'])
        predict_ml(model)

    elif clf_name=="KNN":
        model=KNeighborsClassifier(n_neighbors=model_features['n_neighbors'])
        predict_ml(model)

    elif clf_name=="Random Forest Classifier":
        model=RandomForestClassifier(max_depth=model_features['max_depth'],n_estimators=model_features['n_estimators'])
        predict_ml(model)

    else:
        model = MultinomialNB(alpha=model_features['alpha'])
        predict_ml(model)

if __name__ == '__main__':
    main()
