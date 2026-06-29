from flask import render_template, request, redirect, url_for
from models import *

def Dashbord(app):
    @app.route('/user_dashbord', methods=["GET", "POST"])
    def user_dashbord():
        if request.method == "GET":
            uid = request.args.get('username_id', '') 

            user = customers.query.filter_by(id = uid).first()
            all_musics = music_catalog.query.order_by(music_catalog.total_favourits.desc()).all()
            top_5_songs = all_musics[:5]

           

            return render_template('user_dashboard.html', session_user = user, top_5= top_5_songs)