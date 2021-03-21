import random


def who_wins(player):
    serving = True
    first = random.randint(0, 9999)
    first_serve = False
    ace = False
    double = False

    if (first / 9999) < player.firstPercentage:
        first_serve = True

    for_point = random.randint(0, 9999) / 10000

    if first_serve:
        if for_point < player.ace:
            ace = True

        elif for_point < player.firstServePtsWon:
            pass

        else:
            serving = not serving

    else:
        if for_point < player.secondServePtsWon:
            pass

        elif for_point > (1 - player.doubleFault):
            double = True
            serving = not serving

        else:
            serving = not serving

    return serving, first_serve, ace, double


# Count the number of break points (create new game, copy points into game)
# Or just copy code from
def break_point_counter(match):
    pass


def match_point_counter(match):
    pass


# How badly were they losing (in games, tiebreaks, matches)
def comeback_adjustor(match):
    pass


def match_value(match):
    pass
