from src.Classes.TennisSet import *


class TennisMatch:

    def __init__(self, player1, player2, to_win, serving, set_length, ad, final_set_breaker):
        """
        :param player1: Players object - representing player 1
        :param player2: Players object - representing player 2
        :param to_win: Int - must be greater than 0, how many sets to play in order to win
        :param serving: Boolean - True if player 1 serves first
        :param set_length: Int - what each set is played to between 1 and 10 (please)
        :param ad: Boolean - True if ads are played
        :param final_set_breaker: Boolean - True if a final set breaker is played, false if not
        """

        self.serving = serving
        self.set_length = set_length
        self.to_win = to_win
        self.player_array = [player1, player2]
        self.ad = ad

        self.final_set_breaker = final_set_breaker
        self.final_set = False

        self.toText = {}
        self.data = []
        self.winner = 0
        self.player1S = 0
        self.player2S = 0

        self.match_over = False

    def play_match(self):
        """
        Plays through an entire match
        :return: nothing
        """

        while not self.match_over:

            if len(self.data) != 0:
                total_games = self.data[-1].player1G + self.data[-1].player2G

                if total_games % 2 == 1:
                    self.serving = not self.serving

            if len(self.data) == (self.to_win + self.to_win) - 2:
                self.final_set = True

            if self.final_set_breaker:
                new_set = TennisSet(self.set_length, self.player_array[0], self.player_array[1], self.ad, self.serving,
                                    True)

            else:
                new_set = TennisSet(self.set_length, self.player_array[0], self.player_array[1], self.ad, self.serving,
                                    not self.final_set)

            new_set.play_set()

            self.iterate_match(new_set)

    def iterate_match(self, current_set):
        """
        Updates internal data based on result of the current_set
        :param current_set: TennisSet object - set to iterate on
        :return: nothing
        """

        self.data.append(current_set)
        result = current_set.winner

        if result == 0:
            return

        elif result == 1:
            self.player1S += 1

        else:
            self.player2S += 1

        if self.player1S == self.to_win:
            self.match_over = True
            self.winner = 1

        elif self.player2S == self.to_win:
            self.match_over = True
            self.winner = 2

    def compile(self):

        self.toText['set_length'] = self.set_length
        self.toText['serving'] = self.serving
        self.toText['to_win'] = self.to_win
        self.toText['ad'] = self.ad
        self.toText['final_set_breaker'] = self.final_set_breaker
