from src.Classes.TennisPoint import *


class TennisTiebreak:

    def __init__(self, player1, player2, serving, tiebreak_length):
        """
        :param player1: Players object - player 1
        :param player2: Players object - player 2
        :param serving: Boolean - True if player 1 starts serving first
        :param tiebreak_length: Int - what the tiebreak is played to
        """

        self.tiebreak_length = tiebreak_length
        self.player_array = [player1, player2]
        self.serving = serving

        self.player1P = 0
        self.player2P = 0
        self.data = []
        self.toText = {}

        self.breaker_over = False
        self.winner = -1

    def play_breaker(self):
        """
        Runs the tiebreaker on its own
        :return: nothing
        """

        while not self.breaker_over:

            new_point = TennisPoint()
            new_point.play_point(self.player_array[0], self.player_array[1], self.serving)

            self.iterate_breaker(new_point)

            if (self.player1P + self.player2P) % 2 == 1:
                self.serving = not self.serving

    def iterate_breaker(self, current_point):
        """
        Given a point it updates internal data of the tiebreaker
        :param current_point: TennisPoint object - to be added to the data
        :return: nothing
        """

        result = current_point.result()
        self.data.append(current_point)

        if result[0] == 0:
            self.breaker_over = True

        elif result[0] == 1:
            self.player1P += 1

        else:
            self.player2P += 1

        if self.player1P >= self.tiebreak_length or self.player2P >= self.tiebreak_length:

            if self.player1P - self.player2P > 1:
                self.breaker_over = True
                self.winner = 1

            elif self.player2P - self.player1P > 1:
                self.breaker_over = True
                self.winner = 2

    def compile(self):
        """
        Consolidates internal data in a dictionary that can be easily printed to a text file
        :return: nothing
        """
        self.toText['tiebreak_length'] = self.tiebreak_length
        self.toText['serving'] = self.serving

    def equals(self, another_tiebreak):
        return True
