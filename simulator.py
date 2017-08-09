from shuffler import *
from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType



class simulator:

    def __init__(self):
        """
        Information to be written in the database
        """
        self.decklist = []
        self.order = None
        self.originaldecklist = None
        self.deck = None
        self.opponent = ""
        self.hand = []
        self.deckcode = None
        self.user_selection = None
        self.urls = []
        self.hand_names = []
        self.result = {}
        self.nextfourdraws = []

    def simulate_mulligan(self, deckcode):
        #determine order & draw initial cards

        self.deckcode = str(deckcode)
        self.order = isFirst()
        self.deck = Deck.from_deckstring(self.deckcode)
        self.decklist = fulldecklist(self.deckcode)
        self.originaldecklist = self.decklist
        random.shuffle(self.decklist)
        self.opponent = opponent_selection()
        self.hand = initial_draw(self.decklist, self.order)
        self.hand_names = self.display_cards(self.hand)
        self.display_cards_ID(self.hand)
        self.urls = self.ID_to_url(self.hand)

        #creates the next four possible draws for the next mulligan. In this case, top card starts from the index 0
        self.nextfourdraws = [self.decklist.pop(), self.decklist.pop(), self.decklist.pop(), self.decklist.pop()]
        self.nextfourdraws = self.ID_to_url(self.nextfourdraws)

        self.results.update({"order":self.order, "hand_url":self.urls,
        "opponent": self.opponent, "decklist": self.originaldecklist,
        "smalldeck":self.nextfourdraws, "deckcode":self.deckcode,
        "hand_names": self.hand_names})

    def display_cards(self, cards):
        """
        matches the dbfids to the numbers outputted by the strings in everysingle card
        """
        to_display = []
        for card in cards:
            to_display.append(matchdbfid(str(card)))
        print(to_display)

    def display_cards_ID(self, cards):
        """
        matches the dbfids to the ids of the cards and then to the images
        """
        CardIDs = []
        for card in cards:
            CardIDs.append(matchdbfidtoid(str(card)))
        print(CardIDs)
        return CardIDs

    def ID_to_url(self, cards):
        """
        matches the ids to the urls of the card images
        """
        Cardurls = []
        for card in cards:
            CardIDs.append(matchidtourl(str(card)))
        return Cardurls

"""
    def replace_cards(self):

        Choosing an index to replace what ever card is at the index that one decides

        self.user_selection = input("Which cards would you like to keep (0 for keep & 1 for toss, space separated):")
        self.user_selection = self.user_selection.split()
        trash = [position for position, choice in enumerate(self.user_selection) if choice == '1']
        for hand_index in trash:
            self.hand.insert(hand_index, self.decklist.pop())
            del self.hand[hand_index + 1]
        return self.hand

    def reset(self):

        choice to restart with same deck, enter a new deck, or exit the simulation.
        we do not need to include an else, since we will turn this to click based
        upon interface creation

        choice = input("To simulate the same deck press 1, to simulate a new decklist press 2, to exit the simulation press 3:")
        if choice == '1':
            self.simulate_mulligan(self.deckcode)

        if choice == '2':
            newdeckcode = str(input("Enter the deckcode of the deck you wish to practice:"))
            self.simulate_mulligan(newdeckcode)

        if choice == '3':
            print("Thanks for playing")
            return False
"""
