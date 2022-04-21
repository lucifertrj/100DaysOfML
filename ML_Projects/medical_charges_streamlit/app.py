import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

st.title("Predict Medical Charges")
st.header("Machine Learning: Regression")
st.write("Provided Medical Charges dataset, we shall predict price using Regression ML Algorithms")

st.sidebar.markdown("[Anime Vyuh](https://animevyuh.org/)")
st.sidebar.markdown("[Check Tutorial](https://animevyuh.org/build-machine-learning-model-using-streamlit/)")

st.header("Analyse The Data")
data = pd.read_csv('medical.csv')
st.write("100 Sample Data:")
st.dataframe(data.sample(100))

st.markdown("### Description Of Data")
st.write(data.describe())

st.markdown("### Check for Empty Data")
st.write(data.isnull().sum())

st.markdown("### Correlation Of Features Based on Label(charges)")
st.write(data.corr()['charges'].sort_values())
st.write("Here age,bmi, children are numeric feature")
st.write("We shall later encode the category(object) data type")

st.header("Visualize The Data")

fig = px.histogram(data,marginal='box',x="age",color="smoker")
fig.update_layout(bargap=0.3)
st.plotly_chart(fig)

fig,axes = plt.subplots()
sb.heatmap(data.corr(),annot=True)
st.pyplot(fig)

fig2,axes2 = plt.subplots()
plt.pie(data['region'].value_counts(),labels=['southwest','southeast','northwest','northeast'],autopct="%0.2f%%",colors=["purple","blue",'green','red'],explode=[0.01,0.02,0,0])
st.pyplot(fig2)

from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error,mean_squared_error

st.header("Prediction Of Our Model")
features = ['age','bmi','smoker']
x = data[features]

category = list()
numerical = list()
for features in x.columns:
    if x[features].dtype == 'O':
        category.append(features)
    else:
        numerical.append(features)

scale = MinMaxScaler()
x[numerical] = scale.fit_transform(x[numerical])

encode = LabelEncoder()
x[category] = encode.fit_transform(x[category])

x = x[numerical+category]
y = data['charges']

st.markdown("### After scaling, encoding and Feature Selection")
st.markdown("#### Features")
st.dataframe(x)

st.markdown("#### Label")
st.dataframe(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

st.markdown("#### Change Learning Rate And Notice the Error And Score")
lr = st.slider("Learning rate",min_value=0.03,max_value=0.1,step=0.01)
model = AdaBoostRegressor(n_estimators=1000,random_state=42,learning_rate=lr)
model = model.fit(x_train,y_train)
predict = model.predict(x_test)

st.write(f"MAE: {mean_absolute_error(predict,y_test)}")
st.write(f"RMSE: {mean_squared_error(predict,y_test,squared=False)}")
st.write(f"Score:{model.score(x_train,y_train)*100}%")

st.markdown("<h1 style='text-align: center; color: red;'>Thank You</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color:blue;'><a href='https://www.buymeacoffee.com/trjtarun'>Contribute</a></h3>", unsafe_allow_html=True)
