from src.DataHandling.DataCollector import *
from src.DataHandling.ReadingData import *
from src.PrintToTerminalReplay import *

specialMatches = []
allMatches = []

federer = Players('Federer', .621, .0647, 0.163, .7734, .5683, .3254, .5094)
nadal = Players('Nadal', .683, .0708, .0634, .7207, .5746, .3423, .5534)

for i in range(1):
    new_match = TennisMatch(federer, nadal, 1, True, 3, True, True)
    new_match.play_match()
    allMatches.append(new_match)
    print('done')

print(len(specialMatches))

for i in allMatches:
    save_match(i, '../data/matchdata.txt', federer, nadal)

# NEXT LINES DO NOT WORK BY THE WAY
matches = pull_data('../data/matchdata.txt')
print(len(matches))

for i in matches:
    print_match(i)
