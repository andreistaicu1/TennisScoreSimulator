from src.Classes.TennisPoint import *


class TennisGame:

    def __init__(self, player1, player2, serving, ad):
        """
        :param player1: Players object - representing player 1
        :param player2: Players object - representing player 2
        :param serving: Boolean - True if player 1 serving, False if not
        :param ad: Boolean - True if ads are played
        """

        self.player_array = [player1, player2]
        self.serving = serving
        self.ad = ad

        self.winner = 0
        self.data = []
        self.toText = {}

        self.pointsP1 = 0
        self.pointsP2 = 0
        self.display = ['0', '15', '30', '40', '--', 'Ad']

        self.gameOver = False
        self.deuce = False

    def play_game(self):
        """
        Begins loop that plays out this current game until the game is over
        :return: Nothing
        """

        while not self.gameOver:
            new_point = TennisPoint()
            new_point.play_point(self.player_array[0], self.player_array[1], self.serving)

            self.iterate_game(new_point)

    def iterate_game(self, current_point):
        """
        Updates internal data characteristics after being given a point
        :param current_point: TennisPoint object - point to be added to game.data
        :return: Nothing
        """

        result = current_point.result()
        self.data.append(current_point)

        if result[0] == 0:
            self.gameOver = True

        elif result[0] == 1:
            self.pointsP1 += 1

        else:
            self.pointsP2 += 1

        if self.pointsP1 == 4 or self.pointsP2 == 4:

            if abs(self.pointsP1 - self.pointsP2) > 1 or not self.ad:
                self.gameOver = True

                if self.pointsP1 > self.pointsP2:
                    self.winner = 1
                else:
                    self.winner = 2

            else:

                self.deuce = True
                self.pointsP1 -= 1
                self.pointsP2 -= 1

    def compile(self):
        """
        Creates a dict of data unique to TennisGame class (tbh kinda pointless)
        :return:
        """
        self.toText['serving'] = self.serving

    def equals(self, another_game):
        pass
