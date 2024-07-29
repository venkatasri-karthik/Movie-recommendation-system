import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=791df835d9f1bcdda477cf9587ac61a0&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w185/"+data['poster_path']
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations_list = []
    recommended_posters=[]
    for i in movies_list:
        movie_id=movies_df.iloc[i[0]].movie_id
        recommendations_list.append(movies_df.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommendations_list,recommended_posters

st.title("Movie Recommendation system")
movies_data=pickle.load(open("movies.pkl", "rb"))
movies_df=pd.DataFrame(movies_data)
similarity=pickle.load(open("similarity.pkl", "rb"))
selected_movie_name=st.selectbox("Select your option",movies_df['title'].values)

if st.button("Recommend"):
    recommendations,posters=recommend(selected_movie_name)
    col1, col2, col3, col4,col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])