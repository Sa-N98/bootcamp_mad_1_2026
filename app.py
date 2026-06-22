from  flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET']) # / == http://10.235.72.35:5001
def landing_page():
    return render_template('landing_page.html', user_name="Kevin")

@app.route('/sum', methods=['GET'])
def get_sum():
    a = 2
    b = 7
    return str(a + b)   # str() converts int → string

# EXAMPLE 3 — Dynamic URL (variable in the URL)
# <name> captures whatever the user types in the URL
# Visit: http://localhost:5001/greet/Kevin
# Visit: http://localhost:5001/greet/Priya
# -------------------------------------------------------
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}! Welcome to Flask."

# EXAMPLE 4 — URL Calculator (two numbers in the URL)
# <int:a> tells Flask to only accept whole numbers
# Visit: http://localhost:5001/add/10/25
# Visit: http://localhost:5001/multiply/6/7
# Visit: http://localhost:5001/power/2/10
# -------------------------------------------------------
@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    return f"{a} + {b} = {a + b}"
 
@app.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a, b):
    return f"{a} x {b} = {a * b}"
 
@app.route('/power/<int:base>/<int:exp>', methods=['GET'])
def power(base, exp):
    return f"{base}^{exp} = {base ** exp}"


# EXAMPLE 5 — JSON response (how real APIs work)
# jsonify() converts a Python dict into JSON
# Visit: http://localhost:5001/api/student/Kevin
# Visit: http://localhost:5001/api/status
# -------------------------------------------------------
@app.route('/api/student/<name>', methods=['GET'])
def get_student(name):
    data = {
        "name":   name,
        "course": "Mobile App Dev",
        "year":   2,
        "passed": True
    }
    return jsonify(data)

# EXAMPLE 6 - Check if a number is prime or not 
@app.route('/isprime/<int:n>', methods=['GET'])
def is_prime(n):
    if n < 2:
        return f"{n} is NOT prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is NOT prime"
    return f"{n} IS prime"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

