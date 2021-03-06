## this function matches the ids generateed to the urls given in the package

import json

def matchidtourl(cardid):
    """
    Takes in the dbfid, and the dictionary of cards that was generated by parsing
    through the hearthsims API which has a list of all the json files of each card
    """
    with open("finalmatchedurls.json", "r") as fin:
        data = json.loads(fin.read())
        d = dict(data)
        url = d[cardid]
    return url
