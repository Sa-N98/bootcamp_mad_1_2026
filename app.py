#Type of App: Musing streaming
# Type of users: Users, Artist, Admin

from flask import Flask, send_from_directory
from models import *
from routes.common.landing_page import Landing_page
from routes.common.login import Login
from routes.common.signup import Signup
from routes.users.dashbord import Dashbord as uDashbord
from routes.users.explore import Explore
from routes.users.favourits import Favourits
from routes.artist.manage_songs import Song_manager
from routes.artist.dashbord import Dashbord as aDashbord
from routes.common.search import Search
import os

app = Flask(__name__)

current_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(current_dir, "appDB.sqlite3")

db.init_app(app)
app.app_context().push()

Landing_page(app)
Login(app)
Signup(app)
uDashbord(app)
aDashbord(app)
Explore(app)
Favourits(app)
Song_manager(app)
Search(app)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5001)

