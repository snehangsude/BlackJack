import random

K, Q, J, A = 10, 10, 10, 11
CARDS = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, K, Q, J]


class Dealer:
    """Initializes the Dealer class, helps to deal a card"""

    def assign_cards(self):
        """Call this method to deal a single random card from the list CARDS"""
        card = random.choice(CARDS)
        return card
