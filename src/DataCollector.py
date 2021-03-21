from src.Classes.Match import *
from src.Classes.Players import *


def save_match(match, filename, player1, player2):
    matches_file = open(filename, 'a')
    player_array = [player1, player2]

    for player in player_array:
        matches_file.write('_')
        player.compile()

        for var in player.toText:
            matches_file.write(f'{var} - {player.toText[var]}')

    for set_played in match.data:
        for game in set_played.data:
            for point in game.data:

                point.compile()

                for item in point.toText:
                    matches_file.write(f'{item} - {point.toText[item]}\n')

                matches_file.write('-\n')
            matches_file.write('--\n')
        matches_file.write('---\n')
    matches_file.write('----\n')

    matches_file.close()


specialMatches = []
allMatches = []

federer = Players('Federer', .621, .0647, 0.163, .7155, .5075)
nadal = Players('Nadal', .683, .0708, .0634, .6975, .5425)

for i in range(5):
    new_match = Match(federer, nadal, 2, True, 6, True, True)
    new_match.play_match()
    allMatches.append(new_match)
    print('done')

print(len(specialMatches))

for i in allMatches:
    save_match(i, '../data/matchdata.txt', federer, nadal)
