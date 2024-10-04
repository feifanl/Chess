from Piece import Piece

class Pawn(Piece):
  def createMoves(self):
      global previousMove
      global alphabet
      global numbers
      self.possibleMoves.clear()
      nextMove = convertCoords(self.posY, self.posX)
      num = numbers.index(nextMove[1])
      isBreak = False
      if self.color == "w":
          if num != 7:
              nextMove = ""
              nextMove += convertCoords(self.posY, self.posX)[0]
              nextMove += numbers[num + 1]
              for i in allPieces:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
              if isBreak == False:
                  self.possibleMoves.append(nextMove)
              isBreak = False
              if num == 1:
                  nextMove = ""
                  nextMove += convertCoords(self.posY, self.posX)[0]
                  nextMove += numbers[num + 2]
                  for i in allPieces:
                      if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1] or i.posY == \
                              convertSquare(nextMove)[0] + 1 and i.posX == convertSquare(nextMove)[1]:
                          isBreak = True
                          continue
                  if isBreak == False:
                      self.possibleMoves.append(nextMove)
          else:
              return
          for i in allPieces:
              if i.posY == (self.posY - 1) and i.posX == (self.posX - 1) and i.color != self.color:
                  self.possibleMoves.append(convertCoords(i.posY, i.posX))
              if i.posY == (self.posY - 1) and i.posX == (self.posX + 1) and i.color != self.color:
                  self.possibleMoves.append(convertCoords(i.posY, i.posX))
          if previousMove != "" and previousMove[0] == "P" and previousMove[6] == "7" and previousMove[
              12] == "5" and (self.posX + 1) == alphabet.index(previousMove[11]) and self.posY == 3:
              self.possibleMoves.append(convertCoords(self.posY - 1, self.posX + 1))
          if previousMove != "" and previousMove[0] == "P" and previousMove[6] == "7" and previousMove[
              12] == "5" and (self.posX - 1) == alphabet.index(previousMove[11]) and self.posY == 3:
              self.possibleMoves.append(convertCoords(self.posY - 1, self.posX - 1))
      nextMove = convertCoords(self.posY, self.posX)
      num = numbers.index(nextMove[1])
      isBreak = False
      if self.color == "b":
          if num != 0:
              nextMove = ""
              nextMove += convertCoords(self.posY, self.posX)[0]
              nextMove += numbers[num - 1]
              for i in allPieces:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
              if isBreak == False:
                  self.possibleMoves.append(nextMove)
              isBreak = False
              if num == 6:
                  nextMove = ""
                  nextMove += convertCoords(self.posY, self.posX)[0]
                  nextMove += numbers[num - 2]
                  for i in allPieces:
                      if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1] or i.posY == \
                              convertSquare(nextMove)[0] - 1 and i.posX == convertSquare(nextMove)[1]:
                          isBreak = True
                          continue
                  if isBreak == False:
                      self.possibleMoves.append(nextMove)
          else:
              return
          for i in allPieces:
              if i.posY == (self.posY + 1) and i.posX == (self.posX - 1) and i.color != self.color:
                  self.possibleMoves.append(convertCoords(i.posY, i.posX))
              if i.posY == (self.posY + 1) and i.posX == (self.posX + 1) and i.color != self.color:
                  self.possibleMoves.append(convertCoords(i.posY, i.posX))
          if previousMove != "" and previousMove[0] == "P" and previousMove[6] == "2" and previousMove[
              12] == "4" and (self.posX + 1) == alphabet.index(previousMove[11]) and self.posY == 4:
              self.possibleMoves.append(convertCoords(self.posY + 1, self.posX + 1))
          if previousMove != "" and previousMove[0] == "P" and previousMove[6] == "2" and previousMove[
              12] == "4" and (self.posX - 1) == alphabet.index(previousMove[11]) and self.posY == 4:
              self.possibleMoves.append(convertCoords(self.posY + 1, self.posX - 1))
