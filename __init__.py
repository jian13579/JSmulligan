from flask import jsonify
from shuffler import *
from simulator import *
import json

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
        result = []
        sim = simulator()
        sim.simulate_mulligan(deckcode)

	    return jsonify(result)
    except Exception as e:
        return str(e)
