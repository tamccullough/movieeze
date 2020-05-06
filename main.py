from flask import Flask
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import ml_main
from datetime import date
today = date.today()
current_year = date.today().strftime('%Y')

import numpy as np
import pandas as pd

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
    return render_template('index.html', genres = genres)

@movieeze.route('/movies', methods=['POST'])
#@login_required
def movies():
    #posting the results
    user_1 = 123711 # user with a medium amount of ratings
    user_2 = 15078 # user with the lowest number of ratings
    user_3 = 72315 # user with a lot of ratings
    genres_list = request.form['Genres']

    recommended_list_1 = ml_main.set_up_ml(user_1,genres_list) # generate a list of recommendations for each user
    recommended_list_2 = ml_main.set_up_ml(user_2,genres_list)
    recommended_list_3 = ml_main.set_up_ml(user_3,genres_list)

    final_recommendation = ml_main.get_final_recommendation(recommended_list_1,recommended_list_2,recommended_list_3)
    return render_template('movies.html',movies_table = final_recommendation,genres = genres_list)


if __name__ == "__main__":
    movieeze.run()
