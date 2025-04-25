class Pot_Manager():
    def __init__(self):
        self.pot = 3
        self.stack_size = 19
    def update_pot(self, action, bet, state, player):
        if state == 'preflop':
            if action == 'call':
                self.pot += 1
                if player:
                    self.stack_size -= 1
        else:
            if action == 'bet' or action == 'raise' or action == 'call':
                self.pot += bet
                if player:
                    self.stack_size -= bet

    def reset_pot(self):
        self.pot = 3
