from flask import render_template, request, redirect, url_for
from models import *

def Dashbord(app):
    @app.route('/artist_dashbord', methods=["GET", "POST"])
    def artist_dashbord():
        if request.method == "GET":
            uid = request.args.get('username_id', '') 
            print(uid)

            user = artist.query.filter_by(id = uid).first()
            
        
            return render_template('artist_dashboard.html', session_user = user)