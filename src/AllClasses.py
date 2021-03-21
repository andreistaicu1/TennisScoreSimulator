from src.HelpFunction import *


class Players:

    def __init__(self, name, first_percentage, double_fault, ace, first_serve_pts_won, second_serve_pts_won):
        self.firstPercentage = first_percentage
        self.doubleFault = double_fault
        self.ace = ace
        self.firstServePtsWon = first_serve_pts_won
        self.secondServePtsWon = second_serve_pts_won

        self.name = name


class Point:

    def __init__(self):

        self.winner = 0
        self.options = ['1', '2', 'q']
        self.data = []

        self.serving = True
        self.toText = {}

        self.made_serve = False
        self.ace = False
        self.double_fault = False

    def play_point(self, player1, player2, serving):

        self.serving = serving

        win_point = ''

        while win_point not in self.options:

            if serving:
                answer, self.made_serve, self.ace, self.double_fault = who_wins(player1)
            else:
                answer, self.made_serve, self.ace, self.double_fault = who_wins(player2)
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

        self.winner = data_of_point['winner']
        self.made_serve = data_of_point['made_serve']
        self.serving = data_of_point['serving']
        self.double_fault = data_of_point['double_fault']
        self.ace = data_of_point['ace']

    def result(self):

        return [int(self.winner)]

    def compile(self):

        self.toText['winner'] = self.winner
        self.toText['serving'] = self.serving
        self.toText['made_serve'] = self.made_serve
        self.toText['ace'] = self.ace
        self.toText['double_fault'] = self.double_fault


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


class Set:

    def __init__(self, set_length, player1, player2, ad, serving, will_breaker):

        self.set_length = set_length
        self.ad = ad
        self.player_array = [player1, player2]
        self.serving = serving

        self.will_breaker = will_breaker

        self.player1G = 0
        self.player2G = 0
        self.data = []

        self.winner = 0
        self.setOver = False
        self.tiebreaker = False

    def play_set(self):

        while not self.setOver:

            self.tiebreaker = self.player1G == self.player2G and self.player1G == self.set_length

            if self.tiebreaker and self.will_breaker:

                new_tiebreak = Tiebreak(self.player_array[0], self.player_array[1], True, 7)
                new_tiebreak.play_breaker()

                self.winner = new_tiebreak.winner

                if self.winner == 0:
                    self.setOver = True

                elif self.winner == 1:
                    self.player1G += 1

                else:
                    self.player2G += 1

                self.data.append(new_tiebreak)

                self.setOver = True

            else:

                new_game = Game(self.player_array[0], self.player_array[1], self.serving, self.ad)
                new_game.play_game()

                game_winner = new_game.winner

                if game_winner == 0:
                    self.setOver = True

                elif game_winner == 1:
                    self.player1G += 1

                else:
                    self.player2G += 1

                self.data.append(new_game)

                if self.player1G >= self.set_length or self.player2G >= self.set_length:

                    if self.player1G - self.player2G > 1:
                        self.winner = 1
                        self.setOver = True

                    elif self.player2G - self.player1G > 1:
                        self.winner = 2
                        self.setOver = True

                self.serving = not self.serving

    def iterate_set(self, current_game):
        pass


class Match:

    def __init__(self, player1, player2, to_win, serving, set_length, ad, final_set_breaker):

        self.serving = serving
        self.set_length = set_length
        self.to_win = to_win
        self.player_array = [player1, player2]
        self.ad = ad

        self.final_set_breaker = final_set_breaker
        self.final_set = False

        self.data = []
        self.winner = 0
        self.player1S = 0
        self.player2S = 0

        self.match_over = False

        self.Wimbledon = False
        self.Australian = False
        self.Miami = False
        self.Rome = False

    def play_match(self):

        while not self.match_over:

            if len(self.data) != 0:
                total_games = self.data[-1].player1G + self.data[-1].player2G

                if total_games % 2 == 1:
                    self.serving = not self.serving

            if len(self.data) == (self.to_win + self.to_win) - 2:
                self.final_set = True

            if self.final_set_breaker:
                new_set = Set(self.set_length, self.player_array[0], self.player_array[1], self.ad, self.serving, True)

            else:
                new_set = Set(self.set_length, self.player_array[0], self.player_array[1], self.ad, self.serving,
                              not self.final_set)

            new_set.play_set()

            self.iterate_match(new_set)

    def iterate_match(self, current_set):

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
