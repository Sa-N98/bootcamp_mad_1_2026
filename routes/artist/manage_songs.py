from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from models import *

def Song_manager(app):
    @app.route('/upload_song', methods=["POST"])
    def upload_song():
        form_title = request.form['title']
        audio_file = request.files['file_path']
        form_artist = request.form['artist']

        if audio_file:
            filename = secure_filename(audio_file.filename)
            upload_path = os.path.join('static/songs_lib', filename)
            audio_file.save(upload_path)
            
            new_song = music_catalog(
                title = form_title,
                file_path = f'songs_lib/{filename}',
                artist = form_artist,
                total_favourits = 0
            )
            db.session.add(new_song)
            db.session.commit()

            return "Song uploaded successfully"

        return "No file uploaded", 400
