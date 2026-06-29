from flask import render_template, request, redirect, url_for
from models import *

def Login(app):
    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            message = request.args.get('message', '') 
            return render_template('login.html',  signup_message = message)
        elif request.method == "POST":
            from_email = request.form['e_mail']
            from_password = request.form['p_word']

            query_output = credentials.query.filter_by(email = from_email, password =  from_password).first()

            # print(f'query_output {type(query_output)}')

            if query_output:
                # print(f'query_output_email {query_output.email}')
                # print(f'query_output_username {query_output.username}')
                # print(f'query_output_type {query_output.cretential_type}')

                if query_output.cretential_type == 'user':  
                    return redirect(url_for('user_dashbord', username_id = query_output.id))
                elif query_output.cretential_type == 'artist':
                    return render_template('artist_dashboard.html', username_id = query_output.id)

            else:
            
                return redirect(url_for('signup', message = 'No Account found with this email or password. Please Create an account'))