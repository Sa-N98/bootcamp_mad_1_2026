from flask import render_template, request, redirect, url_for
from models import *

def Favourits(app):
    @app.route('/add_favourits', methods=["POST"])
    def add_favourits():
        u_id = request.form['user_id']
        s_id = request.form['song_id']

        check = favourits_user_map.query.filter_by(customer_id = u_id).first()
        if check:
                user_favourits = favourits.query.filter_by(id = check.favourits_id).first()
                user_favourits.song_list = user_favourits.song_list + f",{s_id}"
                db.session.commit()

                return "Favourit added"

        else:
            new_favourits = favourits(
                name = "Favourits",
                song_list = s_id
            )

            db.session.add(new_favourits)
            db.session.flush()

            new_map = favourits_user_map(
                customer_id = u_id,
                favourits_id = new_favourits.id
                )
            db.session.add(new_map)
            db.session.commit()
            return "Favourit added"

    @app.route('/favorites/<uid>', methods=["GET"])
    def get_favourits(uid):
        user = customers.query.filter_by(id= uid).first()
        user_favourits = user.user_favourits[0]
        song_id = user_favourits.song_list.split(',')

        fav_songs = []
        for sid in song_id:
             song = music_catalog.query.filter_by(id= sid).first()
             fav_songs.append(song)

        return render_template('user_favourits.html', songs = fav_songs)