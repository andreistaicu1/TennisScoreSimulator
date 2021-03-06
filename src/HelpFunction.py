import random


def who_wins(player_serving, player_returning):
    """
    Given a player it computes who wins the specific point
    Uses the statistics on the Players object given
    :param player_serving: Players object of serving player
    :param player_returning: Player object of returning player
    :return: Tuple (serving, first_serve, ace, double_fault)
        serving: Boolean - True if player won point
        first_serve: Boolean - True if player made first serve
        ace: Boolean - True if player hit an ace
        double_fault: Boolean - True if player double faulted
    """
    serving = True
    first = random.randint(0, 9999)
    first_serve = False
    ace = False
    double = False

    first_won_pts = (player_serving.first_serve_pts_won + (1 - player_returning.first_return_pts_won)) / 2
    second_won_pts = (player_serving.second_serve_pts_won + (1 - player_returning.second_return_pts_won)) / 2

    if (first / 9999) < player_serving.first_percentage:
        first_serve = True

    for_point = random.randint(0, 9999) / 10000

    if first_serve:
        if for_point < player_serving.ace:
            ace = True

        elif for_point < first_won_pts:
            pass

        else:
            serving = not serving

    else:
        if for_point < second_won_pts:
            pass

        elif for_point > (1 - player_serving.double_fault):
            double = True
            serving = not serving

        else:
            serving = not serving

    return serving, first_serve, ace, double


def save_score_match(match):
    """
    Given a match it prints out the score of it to the terminal
     as in: (6-1, 6-2, 6-3)
    :param match: TennisMatch object
    :return: nothing
    """
    first = 0
    second = 0

    if match.winner == 1:
        first = 0
        second = 1

    elif match.winner == 2:
        first = 1
        second = 0

    score = ''

    for j in match.data:
        new_array = [j.player1G, j.player2G]
        tie = -1

        if abs(new_array[first] - new_array[second]) == 1:
            if j.data[-1].player1P > j.data[-1].player2P:
                tie = j.data[-1].player2P
            if j.data[-1].player1P < j.data[-1].player2P:
                tie = j.data[-1].player1P

        score = score + str(new_array[first]) + ' - ' + str(new_array[second])

        if tie != -1:
            score = score + ' (' + str(tie) + '), '
        else:
            score = score + ', '

    return score


def print_score_match(match):

    print(match.player_array[match.winner - 1].name + ' wins: ')
    print(save_score_match(match))

    print('\n')

