from flask import render_template

def Landing_page(app):
    @app.route('/', methods=['GET']) 
    def landing_page():
        return render_template('landing_page.html')