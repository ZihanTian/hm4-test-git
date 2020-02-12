import hw4_cards as cards
class Hand:
    '''a hand for playing card

    Class Attributes
    ----------------
    None

    Instance Attributes
    -------------------
    init_card: list
        a list of cards

    '''
    def __init__(self, init_cards):
        self.cards = init_cards 
        

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand

        Parameters  
        -------------------
        card: instance
            a card to add

        Returns
        -------
        None

        '''
        for c in self.cards:
            if c.suit_name == card.suit_name and c.rank == card.rank:
                break
        self.cards.append(card)
        

    def remove_card(self, card):
        '''remove a card from the hand

        Parameters  
        -------------------
        card: instance
            a card to remove

        Returns
        -------
        the card, or None if the card was not in the Hand

        '''
        for ind,c in enumerate(self.cards):
            if c.suit_name == card.suit_name and c.rank == card.rank:
                card_out = self.cards.pop(0) 
                return card_out
        return None 
        
 
    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card

        Parameters  
        -------------------
        deck: instance
            a deck from which to draw

        Returns
        -------
        None

        '''
        draw_card = deck.deal_card()
        self.add_card(draw_card)
#hand = Hand([#ard()])
#print(len(hand.cards) )       