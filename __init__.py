from flask import jsonify, Flask
from shuffler import *
from simulator import *
import json

app = Flask(__name__)

@app.route('/mulligan/')
def mulligan():
	return ender_template('mulligan.html')


"""
This function takes the deckstring from the button, and then runs the mulligan
function returning a JSON that contains the urls of the cards drawn
"""
@app.route('/execution/')
def execution():
    try:
        deckcode = request.args.get('deckcode', 0, type=str)
        sim = simulator()
        sim.simulate_mulligan(deckcode)
        result = sim.results
        return jsonify(result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
        app.run()
