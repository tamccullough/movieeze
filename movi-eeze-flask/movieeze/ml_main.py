#movie recommender
import pandas as pd
import numpy as np
import heapq
import pickle
import os

os_path = os.path.join(os.path.expanduser('~'))
PATH = os_path+'/mldl/models/'

filename = PATH+'movielens_light_recommender_model.sav'
ml_model = pickle.load(open(filename, 'rb'))

genres = ['Action','Adventure','Animation',
          'Children','Comedy','Crime',
          'Documentary','Drama','Fantasy',
          'Film-Noir','Horror','Musical',
          'Mystery','Romance','Sci-Fi',
          'Thriller','War','Western']

movies = pd.read_csv('movieeze/datasets/movies.csv')
ratings = pd.read_csv('movieeze/datasets/ratings.csv')
users = pd.read_csv('movieeze/datasets/users.csv')

def get_r(user_id):
    # Select which system to use. Due to memory constraints, item based is the only viable option
    recommender_system = ml_model
    # N will represent how many items to recommend
    N = 2000

    # The setting to a set and back to list is a failsafe.
    rated_items = list(set(ratings.loc[ratings['userid'] == user_id]['movieid'].tolist()))
    ratings_list = movies['movieid'].values.tolist()
    reduced_ratings = ratings.loc[ratings['movieid'].isin(ratings_list)].copy()

    # Self explanitory name
    all_item_ids = list(set(reduced_ratings['movieid'].tolist()))

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
    recommended_df = movies.loc[movies['movieid'].isin(recommended_ids)].copy()
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
        j = cap_str(i)
        str_ = f'(?=.*{j})'
        s_ += str_
    s_
    f_list = f_list[f_list['genres'].str.contains(fr'^\b{s_}\b',regex=True)]
    return f_list

def set_up_ml(user_id,genre_list):
    f_list = get_r(user_id)
    items = genre_list.split(',')
    f_list = reg_frame(f_list,items)
    f_list.pop('movieid')
    f_list.pop('pred_rating')
    f_list = f_list.reset_index(drop=True)
    f_list = f_list.T.reset_index(drop=True).T
    #f_list = f_list.head(10)
    return f_list


# JUST KEEP IT HERE SAFELY
def set_up_back(user_id,genre_list):
    ml_list = get_r(user_id)
    cols = ml_list.columns
    f_list = pd.DataFrame(columns = cols)
    items = genre_list.split(',')
    s_ = ''
    for i in items:
        j = cap_str(i)
        str_ = f'(?=.*{j})'
        s_ += str_
    s_
    f_list = ml_list.copy()
    f_list = f_list[f_list['genres'].str.contains(fr'^\b{s_}\b',regex=True)]
    f_list.pop('movieid')
    f_list.pop('pred_rating')
    f_list = f_list.reset_index(drop=True)
    f_list = f_list.T.reset_index(drop=True).T
    f_list = f_list.head(10)
    return f_list
