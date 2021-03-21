import random


def who_wins(player):
    serving = True
    first = random.randint(0, 9999)
    first_serve = False
    ace = False
    double = False

    if (first / 9999) < player.first_percentage:
        first_serve = True

    for_point = random.randint(0, 9999) / 10000

    if first_serve:
        if for_point < player.ace:
            ace = True

        elif for_point < player.first_serve_pts_won:
            pass

        else:
            serving = not serving

    else:
        if for_point < player.second_serve_pts_won:
            pass

        elif for_point > (1 - player.double_fault):
            double = True
            serving = not serving

        else:
            serving = not serving

    return serving, first_serve, ace, double


def print_score_match(match):
    first = 0
    second = 0

    if match.winner == 1:
        first = 0
        second = 1

    elif match.winner == 2:
        first = 1
        second = 0

    print(match.playerArray[match.winner - 1].name + ' wins: ')

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

    print(score)

    print('\n')