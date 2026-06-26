from flask import render_template, request, redirect, url_for
from models import *

def Signup(app):
    @app.route('/signup', methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            message = request.args.get('message', '')
            return render_template('signup.html', ligin_fail_message = message)
        
        elif request.method == "POST":
            from_username = request.form['u_name']
            from_email = request.form['e_mail']
            from_password = request.form['p_word']
            from_type = request.form['u_type']

            query_output = credentials.query.filter_by(email = from_email).all()

            if query_output:
                 return "An account with this email already exists. Please try a different one."
            else:
                new_credentials = credentials(
                    username = from_username,
                    email = from_email,
                    password = from_password,
                    cretential_type = from_type
                )
                db.session.add(new_credentials)
                db.session.commit()

            return redirect(url_for('login', message = 'Signup Successful!!!'))