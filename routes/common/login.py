from flask import render_template, request, redirect

def Login(app):
    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            message = request.args.get('message', '') 
            return render_template('login.html',  signup_message = message)
        elif request.method == "POST":
            email = request.form['e_mail']
            password = request.form['p_word']

            print(f"\n\n email: {email}, password: {password} \n\n")

            return "Login Successful"