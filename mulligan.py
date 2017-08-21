# A mulligan app developed for Vicious Syndicate

from flask import Flask, render_template, request, jsonify
from shuffler import *
from simulator import *

app = Flask(__name__)

@app.route('/_simulate')
def simulate():
    """Takes the deckcode and executes the mulligan function"""

    #exampledeckcode "AAECAf0ECE3FBJAH7Ae%2FCIivAqG3ApbHAgvAAbsClQOrBO0ElgWjtgLXtgLpugLBwQKYxAIA"
    try:
        deckcode = request.args.get('deckcode', 0, type=str)
        sim = simulator()
        sim.simulate_mulligan(deckcode)
        result = sim.results
        return jsonify(result)
    except Exception as e:
        return str(e)

##Testing the case where we do not have a dynamic code to check for the response between the server and the webpage
@app.route('/_smallsim')
def testsim():
    sim = simulator()
    sim.simulate_mulligan("AAECAf0ECE3FBJAH7Ae%2FCIivAqG3ApbHAgvAAbsClQOrBO0ElgWjtgLXtgLpugLBwQKYxAIA")
    result = sim.results["hand_url"]
    return jsonify(result)

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

@app.route('/example')
def example():
    return render_template("example.html")

@app.route('/smalltest')
def smalltest():
    return render_template("smalltest.html")

if __name__ == "__main__":
    app.run()
