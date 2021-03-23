from src.PrintToTerminalReplay import *


federer = Players('Federer', .621, .0647, 0.163, .7734, .5683, .3254, .5094)
nadal = Players('Nadal', .683, .0708, .0634, .7207, .5746, .3423, .5534)
djokovic = Players('Djokovic', .649, .078, .114, .7365, .5547, .3362, .5514)
thiem = Players('Thiem', .603, .0880, .1228, .741, .532, .303, .502)
medvedev = Players('Medvedev', .596, .110, .1665, .747, .520, .300, .531)

all_matches = []

for i in range(1):
    new_match = TennisMatch(medvedev, thiem, 3, bool(random.getrandbits(1)), 6, True, False)
    new_match.play_match()
    all_matches.append(new_match)

# FOLLOWING RUNS PRINT_MATCH FUNCTION
# TESTS PRINT TO TERMINAL REPLAY
p1 = 0
p2 = 0

for match in all_matches:
    print_match(match)

    if match.winner == 1:
        p1 += 1
    else:
        p2 += 1

print(f'Medvedev won {p1} out of {p1 + p2} matches so {100 * p1 / (p1 + p2)}%')
print(f'Thiem won {p2} out of {p1 + p2} matches so {100 * p2 / (p1 + p2)}%')
