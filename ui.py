from tkinter import *
from card_brain import CardBrain

THEME = "#444444"


class Interface:

    def __init__(self):
        """Initializes the Interface along with the the CardBrain class. Call this method to start the game."""
        self.card = CardBrain()
        self.window = Tk()
        self.window.title("BlackJack")
        self.window.config(bg=THEME, padx=30, pady=30)

        # Creates the Canvas where the cards are displayed
        self.canvas = Canvas(width=400, height=300, bg="#F2E1C1", bd=-2)
        self.comp_deck = self.canvas.create_text(200, 60,
                                                 text=f"{self.card.comp[0]}",
                                                 font=("Bernard MT Condensed", 30,))
        self.user_deck = self.canvas.create_text(200, 240, text=f"{self.card.user}",
                                                 font=("Bernard MT Condensed", 30,))
        self.canvas.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        # Generates the Buttons
        self.hit = Button(bd=-2, highlightthickness=0, text="DEAL", bg=THEME, padx=10, pady=10,
                          font=("Helvetica Neue", 17, "bold"), fg="#FFC947", command=self.deal, )
        self.hit.grid(row=4, column=1)

        self.stand = Button(bd=-2, highlightthickness=0, text="HOLD", bg=THEME, padx=10, pady=10,
                            font=("Helvetica Neue", 17, "bold"), fg="#D54C4C", command=self.hold, )
        self.stand.grid(row=4, column=2)

        self.start_b = Button(bd=-2, width=25, highlightthickness=0, text="RESTART", bg=THEME, padx=10, pady=2,
                              font=("Tahoma", 18, "bold"), fg="#50CB93", command=self.start, state='disabled')
        self.start_b.grid(row=5, column=1, columnspan=2)

        # Shows the Score of User and Computer
        self.user_score = Label(text=f"Your total: {sum(self.card.user)}", font=("Tw Cen MT", 14, "bold"),
                                bg=THEME,
                                fg="white")
        self.user_score.grid(row=3, column=1, columnspan=2)

        self.comp_score = Label(text="", font=("Tw Cen MT", 14, "bold"), bg=THEME,
                                fg="white")
        self.comp_score.grid(row=1, column=1, columnspan=2)

        # Game state for sharing the result
        self.result = Label(text="", font=("Matura MT Script Capitals", 30,), bg=THEME,
                            fg="#F48B29")
        self.result.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        self.blackjack_check()
        self.window.mainloop()

    def deal(self):
        """Related action with the 'DEAL' button and helps to increase a card when pressed"""
        self.card.choice = 'y'
        self.card.request_card()
        self.canvas.itemconfig(self.user_deck, text=f"{self.card.user}")
        self.user_score.config(text=f"Your total: {sum(self.card.user)}")
        result = self.card.check_score()
        self.result.config(text=result)
        if result == 'You lose!' or result == 'You win!':
            self.canvas.itemconfig(self.comp_deck, text=f"{self.card.comp}")
            self.comp_score.config(text=f"Computer's total: {sum(self.card.comp)}")
            self.start_b.config(state='normal')
            self.hit.config(state='disabled')
            self.stand.config(state='disabled')

    def hold(self):
        """Related action with the 'HOLD' button - Once pressed the 'DEAL' & 'HOLD' would be disabled.
        As the computer would be playing alone"""
        self.card.choice = 'n'
        self.hit.config(state='disabled')
        self.stand.config(state='disabled')
        self.card.request_card()
        if sum(self.card.comp) >= 17:
            result = self.card.check_score()
            self.result.config(text=result)
            self.canvas.itemconfig(self.comp_deck, text=f"{self.card.comp}")
            self.comp_score.config(text=f"Computer's total: {sum(self.card.comp)}")
            self.start_b.config(state='normal')
        else:
            self.hold()

    def blackjack_check(self):
        """Initial check if there is a BlackJack when two cards are dealt"""
        result = self.card.check_score()
        if result == 'BlackJack!':
            self.result.config(text=result)
            self.canvas.itemconfig(self.comp_deck, text=f"{self.card.comp}")
            self.comp_score.config(text=f"Computer's total: {sum(self.card.comp)}")
            self.start_b.config(state='normal')
            self.hit.config(state='disabled')
            self.stand.config(state='disabled')

    def start(self):
        """Destroys and recreates the Interface to restart the game"""
        self.window.destroy()
        Interface()
