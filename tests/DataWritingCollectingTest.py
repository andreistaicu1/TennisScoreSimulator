from src.DataHandling.DataCollector import *
from src.DataHandling.ReadingData import *
from src.PrintToTerminalReplay import *

special_matches = []
all_matches = []

federer = Players('Federer', .621, .0647, 0.163, .7734, .5683, .3254, .5094)
nadal = Players('Nadal', .683, .0708, .0634, .7207, .5746, .3423, .5534)

for i in range(1000):
    new_match = TennisMatch(federer, nadal, 3, True, 6, True, False)
    new_match.play_match()
    all_matches.append(new_match)

matches_file = open('../data/matchdata.txt', 'w')
matches_file.close()

for i in all_matches:
    save_match(i, '../data/matchdata.txt', federer, nadal)


matches = pull_data('../data/matchdata.txt')


# DONE
for i in range(len(matches)):
    a = save_score_match(matches[i])
    b = save_score_match(all_matches[i])
    print(a)
    print(b)

    for j in range(len(matches[i].data)):
        for k in range(len(matches[i].data[j].data)):
            for l in range(len(matches[i].data[j].data[k].data)):
                assert matches[i].data[j].data[k].data[l].winner == all_matches[i].data[j].data[k].data[l].winner

    assert a == b

