from src.HelpFunction import *


class TennisPoint:

    def __init__(self):
        """
        Instantiates data to generic data
        """

        self.winner = 0
        self.options = ['1', '2', 'q']
        self.data = []

        self.serving = True
        self.toText = {}

        self.made_serve = False
        self.ace = False
        self.double_fault = False

    def play_point(self, player1, player2, serving):
        """
        Iterates through a point based on player characteristics
        :param player1: Players object - representing player 1
        :param player2: Players object - representing player 2
        :param serving: Boolean - is player 1 serving?
        :return: nothing
        """

        self.serving = serving

        win_point = ''

        while win_point not in self.options:

            if serving:
                answer, self.made_serve, self.ace, self.double_fault = who_wins(player1, player2)
            else:
                answer, self.made_serve, self.ace, self.double_fault = who_wins(player2, player1)
                answer = not answer

            if answer:
                win_point = '1'
            else:
                win_point = '2'

            if win_point != 'q':
                self.winner = int(win_point)
                self.data.append(self.winner)
            else:
                self.winner = 0

    def iterate_point(self, data_of_point):

        self.winner = int(data_of_point['winner'])

        if data_of_point['made_serve'] == 'True':
            self.made_serve = True
        else:
            self.made_serve = False

        if data_of_point['serving'] == 'True':
            self.serving = True
        else:
            self.serving = False

        if data_of_point['double_fault'] == 'True':
            self.double_fault = True
        else:
            self.double_fault = False

        if data_of_point['ace'] == 'True':
            self.ace = True
        else:
            self.ace = False

    def result(self):
        """
        Pointless
        :return: int - 1 if player 1 won the point, 2 if player 2 did, 0 if no one did
        """

        return [int(self.winner)]

    def compile(self):
        """
        Consolidates internal data in a dictionary that can be easily printed to a text file
        :return: nothing
        """

        self.toText['winner'] = self.winner
        self.toText['serving'] = self.serving
        self.toText['made_serve'] = self.made_serve
        self.toText['ace'] = self.ace
        self.toText['double_fault'] = self.double_fault

    def equals(self, another_point):

        self.compile()
        another_point.compile()

        for item in self.toText:
            if self.toText[item] != another_point.toText[item]:
                return False

        return True
