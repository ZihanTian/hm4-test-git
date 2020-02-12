#########################################
##### Name:      <ZihanTian>        #####
##### Uniqname:         <zti>       #####
#########################################
import unittest
import hw4_cards as mycard
import hm4_cards_ec1 as hands


class TestHand(unittest.TestCase):
    

    def test_1_initial(self):
        # test the hand is correctly initialized with some cards
        card1 = mycard.Card(0,1)
        card2 = mycard.Card(0,2)
        card3 = mycard.Card(0,3)
        init_list = [card1,card2,card3]
        my_hand = hands.Hand(init_list)
        for instance in my_hand.cards:
            self.assertIsInstance(instance,mycard.Card)

    def test_2_AddAndRemove(self):
        card1 = mycard.Card(0,1)
        my_hand = hands.Hand([card1])
        card_toadd = mycard.Card(0,6)
        my_hand.add_card(card_toadd)
        self.assertEqual(my_hand.cards[-1],card_toadd)
        card_removed = my_hand.remove_card(card1)
        self.assertEqual(card_removed,card1)

    def test_3_draw(self):
        my_deck = mycard.Deck()
        my_hand = hands.Hand([])
        num1 = len(my_deck.cards)
        my_hand.draw(my_deck)
        card_draw = my_hand.cards[-1]
        num2 = len(my_deck.cards)
        # check side effect of deck
        self.assertEqual(num1-1,num2)
        self.assertIsInstance(card_draw,mycard.Card)





if __name__ == "__main__":
    unittest.main()
