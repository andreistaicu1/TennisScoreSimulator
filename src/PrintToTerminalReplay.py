"""
Proof of concept that we can replay matches from an existing match object
"""
from src.DataHandling.ReadingData import *
import time

federer = Players('Federer', .621, .0647, 0.163, .7155, .5075)
nadal = Players('Nadal', .683, .0708, .0634, .6975, .5425)


def print_game(current_game, one, two):
    """
    For each point in the game this prints out the current score
    :param current_game: TennisGame object
    :param one: Int - current game score for player 1
    :param two: Int - current game score for player 2
    :return: nothing
    """
    player_1p = 0
    player_2p = 0
    game_over = False
    deuce = False

    print(f'{current_game.player_array[0].name} {one} - {two} {current_game.player_array[1].name}')
    print('\n')

    for point in current_game.data:

        # TIME BOY
        time.sleep(.3)

        if point.winner == 1:
            player_1p += 1

        else:
            player_2p += 1

        if player_1p == 4 or player_2p == 4:
            if abs(player_1p - player_2p) > 1 or not current_game.ad:
                game_over = True
            else:
                deuce = True
                player_1p -= 1
                player_2p -= 1

        if not game_over:

            if current_game.serving:
                first = player_1p
                second = player_2p
            else:
                first = player_2p
                second = player_1p

            if not deuce:
                print(f'{current_game.display[first]} - {current_game.display[second]}')
            else:
                print(f'{current_game.display[first + 2]} - {current_game.display[second + 2]}')
                deuce = False

    print('\n')


def print_tiebreak(current_breaker):
    """
    Prints out the score of the breaker point by point
    :param current_breaker: Current breaker score
    :return: nothing
    """
    player_1p = 0
    player_2p = 0

    for point in current_breaker.data:

        # TIME BOY
        time.sleep(.3)

        if point.winner == 1:
            player_1p += 1
        else:
            player_2p += 1

        print(f'{current_breaker.player_array[0].name} {player_1p} - {player_2p}'
              f' {current_breaker.player_array[1].name}')

    print('\n')


def print_set(current_set, set_num):
    """
    Given a set it prints out the contents of the tet
    :param current_set: TennisSet object
    :param set_num: which set number is this
    :return: nothing
    """
    cur_score_one = 0
    cur_score_two = 0

    for game in current_set.data:

        if type(game) == TennisGame:
            if game.serving:
                print(f'{game.player_array[0].name} is serving')
            else:
                print(f'{game.player_array[1].name} is serving')
            print_game(game, cur_score_one, cur_score_two)

        else:
            print_tiebreak(game)

        if game.winner == 1:
            cur_score_one += 1
        else:
            cur_score_two += 1

    print(f'Set # {set_num}')
    print(f'{current_set.player_array[0].name} {current_set.player1G} - {current_set.player2G}'
          f' {current_set.player_array[1].name}')

    print('\n')


def print_match(current_match):
    """
    Given a match it prints out the contents of the match point by point
    :param current_match: TennisMatch object
    :return: nothing
    """
    index_m = 1
    for set_ in current_match.data:
        print_set(set_, index_m)
        index_m += 1

    print('\n')
    print_score_match(current_match)


all_matches = []

for i in range(5):
    new_match = TennisMatch(federer, nadal, 2, True, 6, True, True)
    new_match.play_match()
    all_matches.append(new_match)

for match in all_matches:
    print_match(match)
