from flask import Flask
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import ml_main
from datetime import date
today = date.today()
current_year = date.today().strftime('%Y')

import numpy as np
import pandas as pd

movieeze = Flask(__name__)


movieeze.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'movieeze.sqlite'))

@movieeze.route('/')
def index():
    #get the ingredients and search
    return render_template('/index.html')#, posts=posts)

@movieeze.route('/movies', methods=['POST'])
#@login_required
def movies():
    #posting the results
    user_id = g.user['username']
    genres_list = request.form['genres']
    movies_list = ml_main.set_up_ml(user_id,genres_list)
    #movies_list = ml_main.set_test()
    num_ = movies_list.shape[0]
    return render_template('/movies.html',movies_table = movies_list,g_list = genres_list)


if __name__ == "__main__":
    movieeze.run()
