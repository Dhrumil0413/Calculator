from flask import Flask, render_template, jsonify, request, redirect, url_for
from math import log10

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home_page():
    return render_template("index.html")

@app.route('/math', methods = ['POST'])
def math_operations():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']

        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
        else:
            return redirect(url_for('home_page'))



        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        elif operation == 'log':
            result = log10(num2) / log10(num1)

        result = "The " + operation + " on A " + str(num1) + " and B " + str(num2) + " is " + str(result)

    return render_template('results.html', result = result)




if __name__ == '__main__':
    app.run(host = 'localhost')