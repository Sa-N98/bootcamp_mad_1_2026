from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class credentials(db.Model):
    __tablename__ = "credentials"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    cretential_type = db.Column(db.String)

class artist(db.Model):
    __tablename__ = "artist"
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String)

class customers(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    user_playlist = db.relationship('playlist', secondary='playlist_user_map', backref='customers')
    user_favourits = db.relationship('favourits', secondary='favourits_user_map', backref='customers')


class playlist(db.Model):
    __tablename__ = "playlist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    song_list = db.Column(db.String)

class favourits(db.Model):
    __tablename__ = "favourits"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    song_list = db.Column(db.String)

class playlist_user_map(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey(customers.id), nullable = False, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(playlist.id), nullable = False, primary_key=True)

class favourits_user_map(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey(customers.id), nullable = False, primary_key=True)
    favourits_id = db.Column(db.Integer, db.ForeignKey(favourits.id), nullable = False, primary_key=True)

class music_catalog(db.Model):
    __tablename__ = "music_catalog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String,unique=True)
    file_path = db.Column(db.String)
    artist = db.Column(db.String)
    total_favourits = db.Column(db.Integer)
    
