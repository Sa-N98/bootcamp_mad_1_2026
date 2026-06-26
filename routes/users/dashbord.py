from flask import render_template, request, redirect, url_for
from models import *

def Dashbord(app):
    @app.route('/user_dashbord', methods=["GET", "POST"])
    def user_dashbord():
        if request.method == "GET":
            output = request.args.get('username', '') 
            all_musics = music_catalog.query.order_by(music_catalog.total_favourits.desc()).all()

            top_5_songs = all_musics[:5]

            print(top_5_songs)

            return render_template('user_dashboard.html', username = output, top_5= top_5_songs)