#Type of App: Musing streaming
# Type of users: Users, Artist, Admin

from flask import Flask, render_template, request, redirect, url_for
from routes.common.landing_page import Landing_page
from routes.common.login import Login
from routes.common.signup import Signup

app = Flask(__name__)

Landing_page(app)
Login(app)
Signup(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

