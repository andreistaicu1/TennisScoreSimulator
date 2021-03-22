from src.Classes.TennisGame import *
from src.Classes.TennisTiebreak import *


class TennisSet:

    def __init__(self, set_length, player1, player2, ad, serving, will_breaker):

        self.set_length = set_length
        self.ad = ad
        self.player_array = [player1, player2]
        self.serving = serving
        self.will_breaker = will_breaker

        self.player1G = 0
        self.player2G = 0
        self.data = []
        self.toText = {}

        self.winner = 0
        self.setOver = False
        self.tiebreaker = False

    def play_set(self):

        while not self.setOver:

            self.tiebreaker = self.player1G == self.player2G and self.player1G == self.set_length

            if self.tiebreaker and self.will_breaker:

                new_tiebreak = TennisTiebreak(self.player_array[0], self.player_array[1], True, 7)
                new_tiebreak.play_breaker()

                self.iterate_set_breaker(new_tiebreak)

            else:

                new_game = TennisGame(self.player_array[0], self.player_array[1], self.serving, self.ad)
                new_game.play_game()

                self.iterate_set_game(new_game)

                self.serving = not self.serving

    def iterate_set_game(self, current_game):

        if self.tiebreaker and self.will_breaker:
            return

        game_winner = current_game.winner

        if game_winner == 0:
            self.setOver = True

        elif game_winner == 1:
            self.player1G += 1

        else:
            self.player2G += 1

        self.data.append(current_game)

        if self.player1G >= self.set_length or self.player2G >= self.set_length:

            if self.player1G - self.player2G > 1:
                self.winner = 1
                self.setOver = True

            elif self.player2G - self.player1G > 1:
                self.winner = 2
                self.setOver = True

    def iterate_set_breaker(self, current_breaker):

        if self.tiebreaker and self.will_breaker:

            self.winner = current_breaker.winner

            if self.winner == 0:
                self.setOver = True

            elif self.winner == 1:
                self.player1G += 1

            else:
                self.player2G += 1

            self.data.append(current_breaker)

            self.setOver = True

        else:
            return False

    def compile(self):

        self.toText['serving'] = self.serving
        self.toText['will_breaker'] = self.will_breaker
