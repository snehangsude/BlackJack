from dealer import Dealer


class CardBrain(Dealer):
    """Initializes the CardBrain class which inherits from the Dealer class"""

    def __init__(self):
        self.user = [self.assign_cards() for _ in range(2)]
        self.comp = [self.assign_cards() for _ in range(2)]
        self.choice = ""

    def request_card(self):
        """Requests a single card if the user asks to deal a card. Calls the dealer to generate a random card.
        Additionally, checks if there is ACE in the hand and replaces it depending on the current sum"""
        if self.choice == 'y':
            self.user.append(self.assign_cards())
            self.comp.append(self.assign_cards())
        elif self.choice == 'n':
            if sum(self.comp) < 17:
                self.comp.append(self.assign_cards())

        # Replacing ACE if it exceeds sum of 21
        if 11 in self.user:
            if sum(self.user) > 21:
                self.user[self.user.index(11)] = 1
        if 11 in self.comp:
            if sum(self.comp) > 21:
                self.comp[self.comp.index(11)] = 1

    def check_score(self):
        """Checks all possible outcomes based on the card at hand and returns the result"""
        if sum(self.comp) == 21 and len(self.comp) == 2:
            return 'BlackJack!'
        elif sum(self.user) == 21 and len(self.user) == 2:
            return 'BlackJack!'
        elif sum(self.user) == 21 and sum(self.comp) == 21:
            return "It's a draw!"
        elif sum(self.comp) == 21:
            return 'You lose!'
        elif sum(self.user) == 21:
            return 'You win!'
        elif sum(self.user) > 21:
            return 'You lose!'
        elif sum(self.comp) > 21:
            return 'You win!'
        elif sum(self.user) > sum(self.comp) and self.choice == 'n':
            return 'You win!'
        elif sum(self.user) < sum(self.comp) and self.choice == 'n':
            return 'You lose!'
        elif sum(self.user) == sum(self.comp) and self.choice == 'n':
            return "It's a draw!"
