from flask import Flask
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import ml_main
from datetime import date
today = date.today()
current_year = date.today().strftime('%Y')

import numpy as np
import pandas as pd
import random

users = pd.read_csv('datasets/users.csv')
users = users.users.values

genres = ['Action','Adventure','Animation',
          'Children','Comedy','Crime',
          'Documentary','Drama','Fantasy',
          'Film-Noir','Horror','Musical',
          'Mystery','Romance','Sci-Fi',
          'Thriller','War','Western']

movieeze = Flask(__name__)

theme, tfont, bfont = 'dark', ['Pacifico','cursive'],  ['Roboto','sans-serif']

@movieeze.route('/')
def index():
    #get the genres and search
    genres_choices = ', '.join(genres)

    return render_template('index.html', genres = genres_choices,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/movies', methods=['POST'])
#@login_required
def movies():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = request.form['Genres']

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/comedy')
#@login_required
def comedy():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'Comedy'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/horror')
#@login_required
def horror():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'Horror'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/drama')
#@login_required
def drama():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'Drama'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/romance')
#@login_required
def romance():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'Romance'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/scifi')
#@login_required
def scifi():
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'sci-fi'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/fantasy')
#@login_required
def fantasy():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'Fantasy'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/action')
#@login_required
def action():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'Action'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

@movieeze.route('/animation')
#@login_required
def animation():
    #posting the results
    user_1 = random.choice(users)
    user_2 = random.choice(users)
    user_3 = random.choice(users)
    genres_list = 'Animation'

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list,
    theme = theme,  tfont = tfont, bfont = bfont)

if __name__ == "__main__":
    movieeze.run()
