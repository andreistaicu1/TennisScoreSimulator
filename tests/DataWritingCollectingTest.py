from src.DataHandling.DataCollector import *
from src.DataHandling.ReadingData import *
from src.PrintToTerminalReplay import *

specialMatches = []
allMatches = []

federer = Players('Federer', .621, .0647, 0.163, .7734, .5683, .3254, .5094)
nadal = Players('Nadal', .683, .0708, .0634, .7207, .5746, .3423, .5534)

for i in range(100):
    new_match = TennisMatch(federer, nadal, 3, True, 6, True, False)
    new_match.play_match()
    allMatches.append(new_match)

matches_file = open('../data/matchdata.txt', 'w')
matches_file.close()

for i in allMatches:
    save_match(i, '../data/matchdata.txt', federer, nadal)


matches = pull_data('../data/matchdata.txt')


# DONE
for i in range(len(matches)):
    a = save_score_match(matches[i])
    b = save_score_match(allMatches[i])
    print(a)
    print(b)
    assert a == b

