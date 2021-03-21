from src.Classes.Point import *


class Game:

    def __init__(self, player1, player2, serving, ad):

        self.playerArray = [player1, player2]
        self.serving = serving
        self.ad = ad

        self.winner = 0
        self.data = []

        self.pointsP1 = 0
        self.pointsP2 = 0
        self.display = ['0', '15', '30', '40', '--', 'Ad']

        self.gameOver = False
        self.deuce = False

    def play_game(self):

        while not self.gameOver:
            new_point = Point()
            new_point.play_point(self.playerArray[0], self.playerArray[1], self.serving)

            self.iterate_game(new_point)

    def iterate_game(self, current_point):

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