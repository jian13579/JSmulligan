##This file will take in a deck list copy string and with the assistance of the hearthstims decklist reader,
##return 3 or 4 cards based on the coin
from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType
from matchingdbfid import *
from matchingdbfidtoid import *
from matchingidtourls import *
import random
import sys
#import numpy

def isFirst():
    """
    does a coin flip between two booleans, where true is first, and false is second
    """
    return random.choice([True, False])

def opponent_selection(vector = ('Druid', 'Hunter', 'Mage', 'Paladin', 'Priest', 'Rogue', 'Shaman','Warlock', 'Warrior')):
    """
    takes in a vector of 9 different probabilities based on the percentages of each
    class that appears in the meta currently. In the future we want to look for
    distinguishments in the meta based on rank differences (i.e. legends, 1-5, and 5+)
    Vector form should be in (druid, hunter, mage, paladin, priest, rogue, shaman, warlock, warrior)
    in order to match the probabilities based on the VS data reaper live.
    """
    ## As we move on to include the classes and a full probability distribution,
    ## the numpy.choice function will encompass all of that
    ## we want to be able to pull probabilities from the google doc
    return random.choice(vector)


def fulldecklist(deckcode):
    """
    This function takes in the deckcode, and deciphers the deckcode into the complete list of cards
    where the tuples (x,y) are separated into a list [x] y times.
    """
    ##First imports the deckcode as a deck
    ##Example Mage Deck we will be using ("AAECAf0ECO0Fcem6AoivAuwHobcCxQS/CAuBsgKVA8HBApYF17YCmMQCqwTAAbC8ArsCo7YCAA==")

    deck = Deck.from_deckstring(str(deckcode))
    complete_deck = []
    for card,copy in deck.cards:
      l = [card] * copy
      complete_deck.extend(l)
    return complete_deck

def initial_draw(decklist, isFirst):
    """
    takes in the code of the decklist, and then shuffles the decklist, and based on random we draw 3 or 4 cards(elements of the list)
    """

    ##First imports the deckcode as a deck
    ##Example Mage Deck we will be using ("AAECAf0ECO0Fcem6AoivAuwHobcCxQS/CAuBsgKVA8HBApYF17YCmMQCqwTAAbC8ArsCo7YCAA==")
    #deck = Deck.from_deckstring(str(deckcode))

    ## from this deck we are able to create the hero, format, and decklist
    ## we first generate the list of tuples which tell the amount, and the cardID for each card
    ## In order for this program to be more efficient, we can implement the id to name only when the cards are drawn
    ## and shown to the players
    ## An example of the list of cards is a list of tuples showing (cardID, #of cards in deck)
    ## [(749, 1), (113, 1), (40297, 1), (38792, 1), (1004, 1), (39841, 1), (581, 1),
    ## (1087, 1), (39169, 2), (405, 2), (41153, 2), (662, 2), (39767, 2), (41496, 2), (555, 2),
    ## (192, 2), (40496, 2), (315, 2), (39715, 2)]

    ## Turns the decklist into a list that is shufflable
    #decklist = fulldecklist(decklist)

    ##randomizes the decklists and then returns the first 3 cards
    #print(decklist)
    random.shuffle(decklist)
    #print(decklist)
    if isFirst:
      cardone = decklist.pop()
      cardtwo = decklist.pop()
      cardthree = decklist.pop()
      #print(cardone, cardtwo, cardthree)
      #cardone = matchdbfid(str(cardone))
      #cardtwo = matchdbfid(str(cardtwo))
      #cardthree = matchdbfid(str(cardthree))
      #print(cardone, cardtwo, cardthree)
      return [cardone, cardtwo, cardthree]

    else:
      cardone = decklist.pop()
      cardtwo = decklist.pop()
      cardthree = decklist.pop()
      cardfour = decklist.pop()
      #print(cardone, cardtwo, cardthree, cardfour)
      #cardone = matchdbfid(str(cardone))
      #cardtwo = matchdbfid(str(cardtwo))
      #cardthree = matchdbfid(str(cardthree))
      #cardfour = matchdbfid(str(cardfour))
      #print(cardone, cardtwo, cardthree, cardfour)
      return [cardone, cardtwo, cardthree, cardfour]

def final_draw(decklist, number_tossed):
  """
  Takes the decklist and draws the number of cards mulliganed away from it
  """
  new_cards = []
  while number_tossed > 0:
    new_cards.append(decklist.pop())
    number_tossed -= 1
  return new_cards
