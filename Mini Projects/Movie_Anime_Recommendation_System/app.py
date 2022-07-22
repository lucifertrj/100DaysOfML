import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS

import warnings
warnings.filterwarnings("ignore")

st.title("Anime Recommendation System")

st.markdown("[Read Article for Step-by-step guide](https://animevyuh.org/movie-recommendation-system)")
st.markdown("Download Dataset: [Anime World: Kaggle Dataset](https://www.kaggle.com/datasets/tarundalal/anime-dataset)")

data = pd.read_csv("AnimeWorld.csv")
anime_data = data[['Anime','Genre','Description','Studio']]
anime_data.fillna(method="ffill",inplace=True)
st.header("Anime Dataset")
st.dataframe(anime_data)

def filter_genre(data):
    if data[0]=='[':
        return data.strip('[]').replace(' ','').replace("'",'')
    else:
        return data

anime_data['Genre'] = anime_data['Genre'].apply(filter_genre)

def WC_generate(col,size,words):
    plt.figure(figsize=(15,15))
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color = 'black', width = size,  height = size, max_words = words)
    wordcloud.generate(' '.join(anime_data[col].astype(str)))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(f"{col}.jpg")
    st.image(f"{col}.jpg")

if st.button("Show Word Cloud"):
    st.header("Anime Name")
    WC_generate('Anime',1050,150)

    st.header("Anime Studio")
    WC_generate('Studio',1000,100)

    st.header("Anime Genre")
    WC_generate('Genre',500,50)

choice = st.selectbox('On what basis would you like to be Recommended?',('Genre','Studio', 'Description'))

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(anime_data[choice])

cosine_sim = cosine_similarity(tfidf_matrix,tfidf_matrix)
index_sim = pd.Series(anime_data.index, index=anime_data['Anime']).drop_duplicates()

def get_recommendations(title):
    idx = index_sim[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return list(anime_data['Anime'].iloc[movie_indices].values)

choice2 = st.selectbox(f'Pick Anime for similar recommendation based on {choice}',sorted(anime_data['Anime']))

if st.button("Recommend Similar Anime"):
    st.header("Here are your 10 Recommendation")
    for index,anime_name in enumerate(get_recommendations(choice2),start=1):
        st.write(f"{index}: {anime_name}")


st.markdown("[Support Anime Vyuh]()")