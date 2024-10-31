import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_movie(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc68578a4281b1822f54a450532d40d8' .format(movie_id))
    data = response.json()
    #print(data)
    return 'https://tmdb.org/t/p/w500' + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similiarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_movie(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similiarity = pickle.load(open('similiarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender')

selected_movie = st.selectbox(
    "Select a Movie:",
   movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
