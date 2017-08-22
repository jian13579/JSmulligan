# A mulligan app developed for Vicious Syndicate

from flask import Flask, render_template, request, jsonify
from shuffler import *
from simulator import *

app = Flask(__name__)

@app.route('/_simulate', methods=['POST'])
def simulate():
    """Takes the deckcode and executes the mulligan function"""

    #exampledeckcode "AAECAf0ECE3FBJAH7Ae%2FCIivAqG3ApbHAgvAAbsClQOrBO0ElgWjtgLXtgLpugLBwQKYxAIA"

    deckcode = request.form.get('deckcode', 0, type=str)
    sim = simulator()
    sim.simulate_mulligan(deckcode)
    result = sim.results
    if result:
        return jsonify({result})

    return jsonify({'error': 'Bad Deckstring!'})

##Testing the case where we do not have a dynamic code to check for the response between the server and the webpage
@app.route('/_smallsim')
def testsim():
    sim = simulator()
    sim.simulate_mulligan("AAECAf0ECE3FBJAH7Ae%2FCIivAqG3ApbHAgvAAbsClQOrBO0ElgWjtgLXtgLpugLBwQKYxAIA")
    result = sim.results["hand_url"]
    return jsonify(result)

##Example for adding numbers serverside
@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/mulligan')
def mulligan():
    return render_template("mulligan.html")


##Example for adding numbers server side
@app.route('/example')
def example():
    return render_template("example.html")

##Still using GETjson Requests to test mulligan
@app.route('/smalltest')
def smalltest():
    return render_template("smalltest.html")

##First time using AJAX request to test mulligan
@app.route('/tests')
def test():
    return render_template("tests.html")


##More testing below here
@app.route('/supertest')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	email = request.form['email']
	name = request.form['name']

	if name and email:
		newName = name[::-1]

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})

if __name__ == "__main__":
    app.run()
