from src.AllClasses import *


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


def save_match(match, filename, player1, player2):
    matches_file = open(filename, 'a')

    matches_file.write('New Match:\n')
    matches_file.write('\n')

    if match.winner == 1:
        matches_file.write(player1.name + ' won the match.\n')
    else:
        matches_file.write(player2.name + ' won the match.\n')

    score_one = ''
    score_two = ''

    for k in match.data:
        score_one += str(k.player1G) + '  '
        score_two += str(k.player2G) + '  '

    matches_file.write(player1.name + '\n')
    matches_file.write(f'{score_one}\n')
    matches_file.write(f'{score_two}\n')
    matches_file.write(player2.name + '\n')

    matches_file.write('\n')

    for set_played in match.data:

        one_won = 0
        two_won = 0

        for game in set_played.data:

            matches_file.write('\n')

            matches_file.write('Current Game Score:\n')
            matches_file.write(f'{player1.name} {str(one_won)} - {str(two_won)} {player2.name}\n')

            matches_file.write('\n')

            for point in game.data:

                point.compile()

                matches_file.write('\n')

                if point.winner == 1:
                    matches_file.write(player1.name + ' won the point.\n')
                else:
                    matches_file.write(player2.name + ' won the point.\n')

                matches_file.write('\n')

                for item in point.toText:
                    matches_file.write(f'{item} - {point.toText[item]}\n')

            if game.winner == 1:
                one_won += 1
            else:
                two_won += 1

        matches_file.write('\n')

        if set_played.winner == 1:
            matches_file.write(player1.name + ' won the set.\n')
        else:
            matches_file.write(player2.name + ' won the set.\n')

        matches_file.write(f'{player1.name} {str(one_won)} - {str(two_won)} {player2.name}\n')

        matches_file.write('\n')

    matches_file.write('-----------------------------------------------------------\n')
    matches_file.write('\n')
    matches_file.close()


allMatches = []

federer = Players('Federer', .621, .0647, 0.163, .7155, .5075)
nadal = Players('Nadal', .683, .0708, .0634, .6975, .5425)


for i in range(5):
    newMatch = Match(federer, nadal, 2, True, 6, True, True)
    newMatch.play_match()
    print('done')
    allMatches.append(newMatch)

for i in allMatches:
    save_match(i, '../data/matchdata.txt', federer, nadal)
