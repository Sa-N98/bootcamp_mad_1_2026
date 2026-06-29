from flask import render_template, request, redirect, url_for
from models import *

def Explore(app):
    @app.route('/explore/<uid>', methods=["GET", "POST"])
    def explore(uid):
        if request.method == "GET":
            all_songs = music_catalog.query.all()
            return render_template('explore.html', session_user_id=uid, songs= all_songs)