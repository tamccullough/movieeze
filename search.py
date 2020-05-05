import pandas as pd
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from movieeze.auth import login_required
from movieeze.db import get_db
from movieeze import ml_main

bp = Blueprint('search', __name__)

@bp.route('/')
def index():
    #get the ingredients and search
    return render_template('search/index.html')#, posts=posts)

@bp.route('/movies', methods=['POST'])
#@login_required
def movies():
    #posting the results
    user_id = g.user['username']
    genres_list = request.form['genres']
    movies_list = ml_main.set_up_ml(user_id,genres_list)
    #movies_list = ml_main.set_test()
    num_ = movies_list.shape[0]
    return render_template('search/movies.html',movies_table = movies_list,g_list = genres_list)
