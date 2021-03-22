from src.PrintToTerminalReplay import *


federer = Players('Federer', .621, .0647, 0.163, .7155, .5075)
nadal = Players('Nadal', .683, .0708, .0634, .6975, .5425)

all_matches = []

for i in range(5):
    new_match = TennisMatch(federer, nadal, 2, True, 6, True, True)
    new_match.play_match()
    all_matches.append(new_match)

# FOLLOWING RUNS PRINT_MATCH FUNCTION
# TESTS PRINT TO TERMINAL REPLAY
for match in all_matches:
    print_match(match)
