from src.DataHandling.DataCollector import *
from src.DataHandling.ReadingData import *

specialMatches = []
allMatches = []

federer = Players('Federer', .621, .0647, 0.163, .7155, .5075)
nadal = Players('Nadal', .683, .0708, .0634, .6975, .5425)

for i in range(5):
    new_match = TennisMatch(federer, nadal, 3, True, 6, True, True)
    new_match.play_match()
    allMatches.append(new_match)
    print('done')

print(len(specialMatches))

for i in allMatches:
    save_match(i, '../data/matchdata.txt', federer, nadal)

# NEXT LINES DO NOT WORK BY THE WAY
matches = pull_data('../data/matchdata.txt')
print(len(matches))
