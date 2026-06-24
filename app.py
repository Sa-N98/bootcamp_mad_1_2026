from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET']) 
def landing_page():
    return render_template('landing_page.html')

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
 



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

