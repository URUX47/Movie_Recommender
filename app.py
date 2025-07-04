import streamlit as st
import pandas as pd
import pickle
import requests
def recommend (movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
     new = []
     recommend_poster = []
     for i in movies_list:
         movie_id = movies.iloc[i[0]].id
         new.append(movies.iloc[i[0]].title)
         recommend_poster.append(fetch_poster(movie_id))
     return new, recommend_poster

movies_dict = pickle.load(open('dict_mov.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

option = st.selectbox(
"How would you like to be contacted?",
 movies['title'].values)

if st.button('Recommend'):
   re, movie_poster = recommend(option)
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
       st.text(re[0])
       st.image(movie_poster[0])
   with col2:
       st.text(re[1])
       st.image(movie_poster[1])
   with col3:
       st.text(re[2])
       st.image(movie_poster[2])
   with col4:
       st.text(re[3])
       st.image(movie_poster[3])
   with col5:
       st.text(re[4])
       st.image(movie_poster[4])
#   with col5:
 #      st.text(re[5])

#   for i in re:
 #       st.write(i)
#st.image(r"C:\Users\suraj\PycharmProjects\movies_recommender\mo.jpg")