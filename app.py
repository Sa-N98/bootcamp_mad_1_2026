from  flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET']) # / == http://10.235.72.35:5001
def landing_page():
    return render_template('landing_page.html', user_name="Kevin")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

