from tennisSimulator import *

# Count the number of break points (create new game, copy points into game)
# Or just copy code from 
def breakPointCounter(match):
    pass


# How badly were they losing (in games, tiebreaks, matches)
def comebackAdjustor(match):
    pass

def printScoreMatch(match):

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

    for i in match.data:
        newArray = [i.player1G, i.player2G]
        tie = -1

        if abs(newArray[first] - newArray[second]) == 1:
            if i.data[-1].player1P > i.data[-1].player2P:
                tie = i.data[-1].player2P
            if i.data[-1].player1P < i.data[-1].player2P:
                tie = i.data[-1].player1P

        score = score + str(newArray[first]) + ' - ' + str(newArray[second])

        if tie != -1:
            score = score + ' (' + str(tie) + '), '
        else:
            score = score + ', '

    print(score)

    print('\n')


def saveMatch(match, filename, player1, player2):

    matchesFile = open(filename, 'w')

    matchesFile.write('New Match:\n')
    matchesFile.write('\n')

    if match.winner == 1:
        matchesFile.write(player1.name + ' won the match.\n')
    else:
        matchesFile.write(player2.name + ' won the match.\n')

    scoreOne = ''
    scoreTwo = ''

    for i in match.data:
        scoreOne += str(i.player1G) + '  '
        scoreTwo += str(i.player2G) + '  '
    
    matchesFile.write(player1.name + '\n')
    matchesFile.write(f'{scoreOne}\n')
    matchesFile.write(f'{scoreTwo}\n')
    matchesFile.write(player2.name + '\n')

    matchesFile.write('\n')

    for setPlayed in match.data:

        oneWon = 0
        twoWon = 0
        
        for game in setPlayed.data:

            matchesFile.write('\n')

            matchesFile.write('Current Game Score:\n')
            matchesFile.write(f'{player1.name} {str(oneWon)} - {str(twoWon)} {player2.name}\n')

            matchesFile.write('\n')

            for point in game.data:
                
                point.compile()

                matchesFile.write('\n')

                if point.winner == 1:
                    matchesFile.write(player1.name + ' won the point.\n')
                else:
                    matchesFile.write(player2.name + ' won the point.\n')
                
                matchesFile.write('\n')

                for item in point.toText:

                    matchesFile.write(f'{item} - {point.toText[item]}\n')
            
            if game.winner == 1:
                oneWon += 1
            else:
                twoWon += 1
        
        matchesFile.write('\n')

        if point.winner == 1:
            matchesFile.write(player1.name + ' won the set.\n')
        else:
            matchesFile.write(player2.name + ' won the set.\n')
        
        matchesFile.write(f'{player1.name} {str(oneWon)} - {str(twoWon)} {player2.name}\n')

        matchesFile.write('\n')
    
    matchesFile.write('-----------------------------------------------------------\n')
    matchesFile.write('\n')
    matchesFile.close()


allMatches = []

federer = Players('Federer', .621, .0647, 0.163, .7155, .5075)
nadal = Players('Nadal', .683, .0708, .0634, .6975, .5425)

for i in range(50):
    newMatch = Match(federer, nadal, 2, True, 6, True, True)
    newMatch.playMatch()
    allMatches.append(newMatch)

for i in allMatches:
    saveMatch(i, 'matchdata.txt', federer, nadal)