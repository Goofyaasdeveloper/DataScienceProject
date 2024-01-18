import streamlit as st 
import pickle
import pandas as pd

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies  = pd.DataFrame(movie_dict)

similarity= pickle.load(open('similarity.pkl','rb'))

def recommended(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances  = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[-1])[1:6]
    recommended_movies=[]
    
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title("Welcome to Movie Recommendation System")

options =st.selectbox("Enter the movie you want to search",movies['title'].values)

if st.button('Recommended'):
    recommendations  = recommended(options)
    for i in recommendations:
        st.write(i)

