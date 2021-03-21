from src.Classes.Point import *


class Tiebreak:

    def __init__(self, player1, player2, serving, tiebreak_length):

        self.tiebreak_length = tiebreak_length
        self.playerArray = [player1, player2]
        self.serving = serving

        self.player1P = 0
        self.player2P = 0
        self.data = []

        self.breaker_over = False
        self.winner = -1

    def play_breaker(self):

        while not self.breaker_over:

            new_point = Point()
            new_point.play_point(self.playerArray[0], self.playerArray[1], self.serving)

            self.iterate_breaker(new_point)

            if (self.player1P + self.player2P) % 2 == 1:
                self.serving = not self.serving

    def iterate_breaker(self, current_point):

        result = current_point.result()
        self.data.append(current_point)

        if result[0] == 0:
            self.breaker_over = True

        elif result[0] == 1:
            self.player1P += 1

        else:
            self.player2P += 1

        if self.player1P >= 7 or self.player2P >= 7:

            if self.player1P - self.player2P > 1:
                self.breaker_over = True
                self.winner = 1

            elif self.player2P - self.player1P > 1:
                self.breaker_over = True
                self.winner = 2
