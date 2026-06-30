from flask import render_template, request, redirect, url_for
from models import *

def Search(app):
    @app.route('/search', methods=["POST"])
    def search():
        search_query = request.form['user_query']
        songs_list = music_catalog.query.filter(music_catalog.title.like(f'{search_query}%')).all()
        return render_template('filter.html', songs =  songs_list)

