import streamlit as st
from langchain_handler import return_movie_suggestions
st.title("Need movie suggestions?")
time=st.sidebar.selectbox("Select time duration",('1 hour','1 hour 30 minutes','2 hours','2 hours 30 minutes','3 hours','More than 3 hours'))
genre=st.sidebar.selectbox("Select movie genre",('Action', 'Adventure','Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western'))

if(time and genre):
    if(st.button('Suggest movies')):
        with st.spinner("Finding movies for you..."):
            response=return_movie_suggestions(time,genre)
            if(response['error']):
                st.markdown('<h3 style="color:red">Free tier quota exhausted for api calls</h3>', unsafe_allow_html=True)
            
            for i in response['res'].split(';'):
                if '::' in i:
                    movie=i.split('::')
                    st.markdown('#### *'+movie[0].strip()+':*')
                    st.write(movie[1].strip())
     