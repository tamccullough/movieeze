from flask import Flask
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import ml_main
from datetime import date
today = date.today()
current_year = date.today().strftime('%Y')

import numpy as np
import pandas as pd
import random

ratings = pd.read_csv('datasets/ratings_2010.csv')
users = ratings.userId.unique()

genres = ['Action','Adventure','Animation',
          'Children','Comedy','Crime',
          'Documentary','Drama','Fantasy',
          'Film-Noir','Horror','Musical',
          'Mystery','Romance','Sci-Fi',
          'Thriller','War','Western']

movieeze = Flask(__name__)

@movieeze.route('/index')
def index():
    #get the ingredients and search
    genres_list = ', '.join(genres)
    return render_template('index.html', genres = genres_list)

@movieeze.route('/movies', methods=['POST'])
#@login_required
def movies():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = request.form['Genres']

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/comedy')
#@login_required
def comedy():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'comedy'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/horror')
#@login_required
def horror():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'horror'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/drama')
#@login_required
def drama():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'drama'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/romance')
#@login_required
def romance():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'romance'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/sci-fi')
#@login_required
def scifi():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'sci-fi'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/fantasy')
#@login_required
def fantasy():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'fantasy'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/action')
#@login_required
def action():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'fantasy'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

@movieeze.route('/animation')
#@login_required
def animation():
    #posting the results
    user_1 = random.choice(users)#123711 # user with a medium amount of ratings
    user_2 = random.choice(users)#15078 # user with the lowest number of ratings
    user_3 = random.choice(users)#72315 # user with a lot of ratings
    genres_list = 'fantasy'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)

if __name__ == "__main__":
    movieeze.run()
