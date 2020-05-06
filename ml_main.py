#movie recommender
import pandas as pd
import numpy as np
import heapq
import pickle
import os

filename = 'model/moviEeze_recommender_model_2010_up.sav'
ml_model = pickle.load(open(filename, 'rb'))

genres = ['Action','Adventure','Animation',
          'Children','Comedy','Crime',
          'Documentary','Drama','Fantasy',
          'Film-Noir','Horror','Musical',
          'Mystery','Romance','Sci-Fi',
          'Thriller','War','Western']

movies = pd.read_csv('datasets/movies_2010.csv')
ratings = pd.read_csv('datasets/ratings_2010.csv')
links = pd.read_csv('datasets/links_2010.csv')
genre_image_list = pd.read_csv('datasets/genre_image_list.csv')
def get_r(user_id):
    # Select which system to use. Due to memory constraints, item based is the only viable option
    recommender_system = ml_model
    # N will represent how many items to recommend
    N = 2000

    # The setting to a set and back to list is a failsafe.
    rated_items = list(set(ratings.loc[ratings['userId'] == user_id]['movieId'].tolist()))
    ratings_list = movies['movieId'].values.tolist()
    reduced_ratings = ratings.loc[ratings['movieId'].isin(ratings_list)].copy()

    # Self explanitory name
    all_item_ids = list(set(reduced_ratings['movieId'].tolist()))

    # New_items just represents all the items not rated by the user
    new_items = [x for x in all_item_ids if x not in rated_items]

    # Estimate ratings for all unrated items
    predicted_ratings = {}
    for item_id in new_items:
        predicted_ratings[item_id] = recommender_system.predict(user_id, item_id).est
        pass

    # Get the item_ids for the top ratings
    recommended_ids = heapq.nlargest(N, predicted_ratings, key=predicted_ratings.get)
    recommended_ids = sorted(recommended_ids)

    # predicted_ratings
    recommended_df = movies.loc[movies['movieId'].isin(recommended_ids)].copy()
    #recommended_df.insert(1, 'pred_rating', np.zeros(len(recommended_ids)))
    recommended_df.insert(1, 'pred_rating', 0)

    # recommended_df = movies.copy()
    for idx,item_id in enumerate(recommended_ids):
        recommended_df.iloc[idx, recommended_df.columns.get_loc('pred_rating')] = int(predicted_ratings[item_id])
        pass
    return recommended_df.head(N).sort_values('pred_rating', ascending=False)

def cap_str(item):
    string = item
    return string.capitalize()

def reg_frame(f_list,items):
    s_ = ''
    for i in items:
        j = i.strip()
        if j == 'sci-fi':
            j = 'Sci-Fi'
        if j == 'film-noir':
            j = 'Film-Noir'
        else:
            j = cap_str(j)
        str_ = f'(?=.*{j})'
        s_ += str_
    s_
    f_list = f_list[f_list['genres'].str.contains(fr'^\b{s_}\b',regex=True)]
    return f_list

def set_up_ml(user_id,genre_list):
    film_list = get_r(user_id)
    items = genre_list.split(',')
    film_list = reg_frame(film_list,items)
    film_list.pop('date')
    return film_list

def get_final_recommendation(list_1,list_2,list_3): # combine all recommendations
    film_recommendation = pd.DataFrame()
    film_recommendation = pd.concat([list_1,list_2,list_3]) # concat lists
    film_recommendation = film_recommendation.sort_values('pred_rating',ascending=False) # sort by predicted rating
    film_recommendation.pop('pred_rating') # drop the rating column
    film_recommendation = film_recommendation.reset_index()
    film_recommendation.pop('index') # reset and pop the old index
    a = []
    b = []
    for i in range(0,film_recommendation.shape[0]): # iterate through the dataframe and get the appropriate link for each movie
        link = links[links['movieId'] == film_recommendation.iloc[i]['movieId']]
        link = 'https://www.themoviedb.org/movie/' + str(int(link.iloc[0][2])) # append the link to the array
        a.append(link)
        genres = film_recommendation.iloc[i]['genres']
        genres = genres.split('|')
        if len(genres) == 1:
            genre1 = genres[0]
            genre = genre1.lower()
        else:
            genre1 = genres[0]
            genre2 = genres[1]
            genre = genre1.lower() + genre2.lower()
        #if genre.isin()
        b.append(genre)
    film_recommendation['link'] = a # add the array to the dataframe
    film_recommendation['image'] = b
    film_recommendation.pop('movieId')
    if film_recommendation['image'].isin(genre_image_list['genre']).any():
        a = []
        for i in range(0,film_recommendation.shape[0]):
            image = genre_image_list[genre_image_list['genre'] == film_recommendation.iloc[i]['image'] ]
            if image.empty:
                image = film_recommendation.iloc[i]['genres']
                image = image.split('|')
                image = image[0]+ '.jpg'
                image = image.lower()
                a.append(image)
            else:
                image = image.reset_index()
                image.pop('index')
                image = image.iloc[0]['image']
                a.append(image)
    film_recommendation['image'] = a
    film_recommendation = film_recommendation.drop_duplicates() # drop recommended duplicates of films
    return film_recommendation
