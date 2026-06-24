from flask import render_template, request, redirect, url_for

def Signup(app):
    @app.route('/signup', methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            return render_template('signup.html')
        
        elif request.method == "POST":
            username = request.form['u_name']
            email = request.form['e_mail']
            password = request.form['p_word']

            print(f"\n\n username: {username} ,  email: {email}, password: {password} \n\n")
            return redirect(url_for('login', message = 'Signup Successful!!!'))