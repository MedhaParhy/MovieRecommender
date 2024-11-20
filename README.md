# Movie Recommender System  

This project is a **Movie Recommendation Site** created by following [this tutorial](https://www.youtube.com/watch?v=4WPD9GuFfOI). The site provides movie recommendations based on various features such as overview, genre, keywords, actors, and director.  

---

## **Features**  
- **Data Preprocessing:**  
  - Utilized the [tmdb_5000_movies dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) for training.  
  - Preprocessed data using a Bag-of-Words model (`CountVectorizer`) to vectorize movie metadata.  

- **Recommendation Algorithm:**  
  - Computed pairwise **cosine similarity** to identify the most similar movies based on selected features.  

- **API Integration:**  
  - Sent HTTP requests using the `requests` library to fetch movie details and posters via [The Movie Database (TMDB) API](https://developers.themoviedb.org/3).  
  - Parsed JSON responses to extract key details, including movie posters and titles.  

- **Frontend Development:**  
  - Built an interactive web interface using **Streamlit** for seamless user interaction and dynamic visualization of results.  

---
# Acknowledgments

Dataset: [Kaggle TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

API: [TMDB API](https://developers.themoviedb.org/3).

Tutorial: [YouTube](https://www.youtube.com/watch?v=4WPD9GuFfOI).

![Screenshot 2024-11-20 095443](https://github.com/user-attachments/assets/d9fdcb70-d986-4869-9efc-05b3f00ee435)
![Screenshot 2024-11-20 095507](https://github.com/user-attachments/assets/fe585070-52aa-4ba3-8081-3e792901139e)
![Screenshot 2024-11-20 095525](https://github.com/user-attachments/assets/dc7d84f8-ea93-4671-88ff-9f1f17ee1692)
