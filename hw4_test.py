
#########################################
##### Name:      <ZihanTian>        #####
##### Uniqname:         <zti>       #####
#########################################
import unittest
import hw4_cards as cards


# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card1 = cards.Card(rank=12)
        self.assertEqual(card1.rank_name,"Queen")

    def test_2_clubs(self):
        card2 = cards.Card(suit=1)
        self.assertEqual(card2.suit_name,"Clubs")

    def test_3_string(self):
        card3 = cards.Card(3,13)
        self.assertEqual(card3.__str__(),"King of Spades")
    
    def test_4_cards(self):
        deck1 = cards.Deck()
        self.assertEqual(len(deck1.cards),52)

    def test_5_return_card(self):
        deck2 = cards.Deck()
        self.assertIsInstance(deck2.deal_card(),cards.Card)
    
    def test_6_one_fewer(self):
        deck3 = cards.Deck()
        num1 = len(deck3.cards)
        a_card = deck3.deal_card()
        num2 = len(deck3.cards)
        self.assertEqual(num1-1,num2)

    def test_7_one_more(self):
        deck4 = cards.Deck()
        a_card = deck4.deal_card()
        num1 = len(deck4.cards)
        deck4.replace_card(a_card)
        num2 = len(deck4.cards)
        self.assertEqual(num1+1,num2)

    def test_8_not_effected(self):
        my_card = cards.Card()
        deck5 = cards.Deck()
        num_cards_initial = len(deck5.cards)
        deck5.replace_card(my_card)
        num_cards = len(deck5.cards)
        self.assertEqual(num_cards_initial,num_cards)







        





############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
