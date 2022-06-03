"""
- A Machine Learning model is undone if it just remains in Jupyter Notebook. 
- Streamlit provides a faster way to build and share data web apps. 
- It turns Jupyter Notebook Python Scripts into a great-looking Web App. 
- And still, it just takes a few minutes. 
- The only pre-requisites to build machine learning model using Streamlit is Python Programming. 

And we got you covered. Check the detailed Anime Vyuh Python Tutorials Series[https://animevyuh.org/category/python-tutorials], Python made easy.
"""
# install: pip install streamlit
#import the necessary modules
#to run the program run the following command:
#streamlit run file_name.py in our case it is [streamlit run ml_with_streamlit_1.py]

import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px
from io import StringIO

# Widgets
#1. Title

st.title("First Streamlit Web App")

#2. Header

st.header("Sub heading")

#3. Write

st.write("I just print normal sentences/paragraphs")

#4. Markdown
st.markdown("### I am H3 Heading")
st.markdown("**I am Bold Text**")
st.markdown("[I am HyperLink](https://animevyuh.org/)") #syntax: [text](link)

#5. Sidebar

st.sidebar.markdown("[Anime Vyuh](https://animevyuh.org/)")

st.sidebar.markdown("[Check Tutorial](https://animevyuh.org/build-machine-learning-model-using-streamlit/)")

#6. DataFrame

data = pd.read_csv('../Day11: Linear Regression/medical.csv')
st.write("100 Sample Data:")
st.dataframe(data.sample(100))

#7. Visualize the Data

#To plot Plotly graph on Streamlit Web app:

fig = px.histogram(data,marginal='box',x="age",color="smoker")
fig.update_layout(bargap=0.3)
st.plotly_chart(fig)

#Next, you can now plot seaborn plot on the Streamlit web app.

fig,axes = plt.subplots()
sb.heatmap(data.corr(),annot=True)
st.pyplot(fig)

#Last but not least Matplotlib can also be implemented on Streamlit web app.

fig2,axes2 = plt.subplots()
plt.pie(data['region'].value_counts(),labels=['southwest','southeast','northwest','northeast'],autopct="%0.2f%%",colors=["purple","blue",'green','red'],explode=[0.01,0.02,0,0])

st.pyplot(fig2)

#8. Slider Widget

#Syntax for Slider widget:
#st.slider("text",min_value=<numeric>,max_value=<numeric>,step=<numeric>) 
#Note: min_value<max_value

st.markdown("#### Move the Slider")
value = st.slider("Some Value",min_value=1,max_value=100,step=5)

#9. Check box

ask = st.checkbox('Are you Human?') #returns bool type

if ask:
    st.write('Hello human')

#10. Radio Buttons

best_anime = st.radio("What's your favorite Anime?",
     ('One Piece', 'Attack On Titan', 'Gintama',"Naruto","Hunter X Hunter"))

if best_anime == 'One Piece':
    st.write('Peak Fiction: Best Worldbuilding')
elif best_anime == "Attack On Titan":
    st.write("Best Story and Perfect Ending")
elif best_anime == "Gintama":
    st.write("Best Comedy")
elif best_anime == "Naruto":
    st.write("Best Influencing Anime")
elif best_anime == "Hunter X Hunter":
    st.write("One of the best in terms of character build up")
else:
    st.write("Select an option")

#11. User input

user_input = st.text_input('Enter something')
if user_input:
    st.write("You entered:",user_input)
else:
    st.write("Type something in text box")

uploaded_file = st.file_uploader("Choose a .csv file")
print(uploaded_file)
if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        st.write("Valid CSV file")
    else:
        st.write("Invalid File")
else:
    st.write("No Files Selected")
