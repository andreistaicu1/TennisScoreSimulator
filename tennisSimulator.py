import math
import sys
import random
import time


def whoWins(player):

    serving = True
    first = random.randint(0, 9999)
    firstServe = False
    ace = False
    double = False
    
    if (first / 9999) < player.firstPercentage:
        FirstServe = True
    
    forPoint = random.randint(0, 9999) / 10000
        
    if firstServe:
        if forPoint < player.ace:
            ace = True

        elif forPoint < player.firstServePtsWon:
            pass

        else:
            serving = not serving
    
    else:
        if forPoint < player.secondServePtsWon:
            pass

        elif forPoint > (1 - player.doubleFault):
            double = True
            serving = not serving

        else:
            serving = not serving
    
    return (serving, firstServe, ace, double)


class Point():

    def __init__(self):

        self.winner = 0
        self.options = ['1', '2', 'q']
        self.data = []

        self.serving = True
        self.toText = {}

        self.madeServe = False
        self.ace = False
        self.doubleFault = False

    
    def playPoint(self, player1, player2, serving):

        self.serving = serving

        winPoint = ''
        
        while winPoint not in self.options:

            if serving:
                answer, self.madeServe, self.ace, self.doubleFault = whoWins(player1)
            else:
                answer, self.madeServe, self.ace, self.doubleFault = whoWins(player2)
                answer = not answer

            if answer:
                winPoint = '1'
            else:
                winPoint = '2'
        
            if winPoint != 'q':
                self.winner = int(winPoint)
                self.data.append(self.winner)
            else:
                self.winner = 0
        
    def result(self):

        return [int(self.winner)]
    
    def compile(self):
        
        self.toText['winner'] = self.winner
        self.toText['serving'] = self.serving
        self.toText['madeServe'] = self.madeServe
        self.toText['ace'] = self.ace
        self.toText['doubleFault'] = self.doubleFault



class Game():

    def __init__(self, player1, player2, serving, ad):

        self.playerArray = [player1, player2]
        self.serving = serving
        self.ad = ad

        self.winner = 0
        self.data = []

        self.pointsP1 = 0
        self.pointsP2 = 0
        self.display = ['0', '15', '30', '40', '--', 'Ad']

        self.gameOver = False
        self.deuce = False
    
    def playGame(self):

        while not self.gameOver:

            newPoint = Point()
            newPoint.playPoint(self.playerArray[0], self.playerArray[1], self.serving)

            result = newPoint.result()
            self.data.append(newPoint)

            if result[0] == 0:
                self.gameOver = True
            
            elif result[0] == 1:
                self.pointsP1 += 1
            
            else:
                self.pointsP2 += 1
            
            if self.pointsP1 == 4 or self.pointsP2 == 4:

                if abs(self.pointsP1 - self.pointsP2) > 1 or not self.ad:
                    self.gameOver = True

                    if self.pointsP1 > self.pointsP2:
                        self.winner = 1
                    else:
                        self.winner = 2
                
                else:

                    self.deuce = True
                    self.pointsP1 -= 1
                    self.pointsP2 -= 1


class Tiebreak():

    def __init__(self, player1, player2, serving, tiebreakLength):

        self.tiebreakLength = tiebreakLength
        self.playerArray = [player1, player2]
        self.serving = serving

        self.player1P = 0
        self.player2P = 0
        self.data = []

        self.breakerOver = False
        self.winner = -1
    

    def playBreaker(self):

        while not self.breakerOver:

            newPoint = Point()
            newPoint.playPoint(self.playerArray[0], self.playerArray[1], self.serving)

            result = newPoint.result()
            self.data.append(newPoint)

            if result[0] == 0:
                self.breakerOver = True
            
            elif result[0] == 1:
                self.player1P += 1
            
            else:
                self.player2P += 1
            
            if self.player1P >= 7 or self.player2P >= 7:
                
                if self.player1P - self.player2P > 1:
                    self.breakerOver = True
                    self.winner = 1
                
                elif self.player2P - self.player1P > 1:
                    self.breakerOver = True
                    self.winner = 2
            
            if (self.player1P + self.player2P) % 2 == 1:
                self.serving = not self.serving



class Set():

    def __init__(self, setLength, player1, player2, ad, serving, willBreaker):

        self.setLength = setLength
        self.ad = ad
        self.playerArray = [player1, player2]
        self.serving = serving

        self.willBreaker = willBreaker

        self.player1G = 0
        self.player2G = 0
        self.data = []

        self.winner = 0
        self.setOver = False
        self.tiebreaker = False

    
    def playSet(self):

        while not self.setOver:

            self.tiebreaker = self.player1G == self.player2G and self.player1G == self.setLength

            if self.tiebreaker and self.willBreaker:

                newTiebreak = Tiebreak(self.playerArray[0], self.playerArray[1], True, 7)
                newTiebreak.playBreaker()
                result = newTiebreak.data

                self.winner = newTiebreak.winner

                if self.winner == 0:
                    self.setOver = True

                elif self.winner == 1:
                    self.player1G += 1

                else:
                    self.player2G += 1
                

                self.data.append(newTiebreak)

                self.setOver = True

            else:

                newGame = Game(self.playerArray[0], self.playerArray[1], self.serving, self.ad)
                newGame.playGame()
                result = newGame.data

                gameWinner = newGame.winner

                if gameWinner == 0:
                    self.setOver = True

                elif gameWinner == 1:
                    self.player1G += 1
                
                else:
                    self.player2G += 1

                self.data.append(newGame)

                if self.player1G >= self.setLength or self.player2G >= self.setLength:

                    if self.player1G - self.player2G > 1:
                        self.winner = 1
                        self.setOver = True

                    elif self.player2G - self.player1G > 1:
                        self.winner = 2
                        self.setOver = True

                self.serving = not self.serving

    
class Match():

    def __init__(self, player1, player2, toWin, serving, setLength, ad, finalSetBreaker):

        self.serving = serving
        self.setLength = setLength
        self.toWin = toWin
        self.playerArray = [player1, player2]
        self.ad = ad

        self.finalSetBreaker = finalSetBreaker
        self.finalSet = False

        self.data = []
        self.winner = 0
        self.player1S = 0
        self.player2S = 0

        self.matchOver = False

        self.Wimbledon = False
        self.Australian = False
        self.Miami = False
        self.Rome = False
    
    def playMatch(self):

        while not self.matchOver:

            if len(self.data) != 0:
                totalGames = self.data[-1].player1G + self.data[-1].player2G

                if totalGames % 2 == 1:
                    self.serving = not self.serving
            
            if len(self.data) == (self.toWin + self.toWin) - 2:
                    self.finalSet = True

            if self.finalSetBreaker:
                newSet = Set(self.setLength, self.playerArray[0], self.playerArray[1], self.ad, self.serving, True)
            
            else:
                newSet = Set(self.setLength, self.playerArray[0], self.playerArray[1], self.ad, self.serving, not self.finalSet)
            
            newSet.playSet()

            self.data.append(newSet)
            result = newSet.winner

            if result == 0:
                return
            
            elif result == 1:
                self.player1S += 1

            else:
                self.player2S += 1
            
            if self.player1S == self.toWin:
                self.matchOver = True
                self.winner = 1
            
            elif self.player2S == self.toWin:
                self.matchOver = True
                self.winner = 2

class Players():

    def __init__(self, name, firstPercentage, doubleFault, ace, firstServePtsWon, secondServePtsWon):

        self.firstPercentage = firstPercentage
        self.doubleFault = doubleFault
        self.ace = ace
        self.firstServePtsWon = firstServePtsWon
        self.secondServePtsWon = secondServePtsWon

        self.name = name