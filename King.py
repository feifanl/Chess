from Piece import Piece

class King(Piece):
  def createMoves(self):
      global allPieces
      global alphabet
      global numbers
      self.possibleMoves.clear()
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      alpha = alphabet.index(nextMove[0])
      if alpha != 7:
          alpha += 1
          nextMove = ""
          nextMove += alphabet[alpha]
          nextMove += convertCoords(self.posY, self.posX)[1]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
  
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      alpha = alphabet.index(nextMove[0])
      if alpha != 0:
          alpha -= 1
          nextMove = ""
          nextMove += alphabet[alpha]
          nextMove += convertCoords(self.posY, self.posX)[1]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      num = numbers.index(nextMove[1])
      if num != 7:
          num += 1
          nextMove = ""
          nextMove += convertCoords(self.posY, self.posX)[0]
          nextMove += numbers[num]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      num = numbers.index(nextMove[1])
      if num != 0:
          num -= 1
          nextMove = ""
          nextMove += convertCoords(self.posY, self.posX)[0]
          nextMove += numbers[num]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      alpha = alphabet.index(nextMove[0])
      num = numbers.index(nextMove[1])
      if alpha != 7 and num != 7:
          alpha += 1
          num += 1
          nextMove = ""
          nextMove += alphabet[alpha]
          nextMove += numbers[num]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      alpha = alphabet.index(nextMove[0])
      num = numbers.index(nextMove[1])
      if alpha != 7 and num != 0:
          alpha += 1
          num -= 1
          nextMove = ""
          nextMove += alphabet[alpha]
          nextMove += numbers[num]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      alpha = alphabet.index(nextMove[0])
      num = numbers.index(nextMove[1])
      if alpha != 0 and num != 7:
          alpha -= 1
          num += 1
          nextMove = ""
          nextMove += alphabet[alpha]
          nextMove += numbers[num]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
      nextMove = convertCoords(self.posY, self.posX)
      isBreak = False
      alpha = alphabet.index(nextMove[0])
      num = numbers.index(nextMove[1])
      if alpha != 0 and num != 0:
          alpha -= 1
          num -= 1
          nextMove = ""
          nextMove += alphabet[alpha]
          nextMove += numbers[num]
          for i in allPieces:
              if i.color != self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      self.possibleMoves.append(nextMove)
                      isBreak = True
                      continue
          for i in allPieces:
              if i.color == self.color:
                  if i.posY == convertSquare(nextMove)[0] and i.posX == convertSquare(nextMove)[1]:
                      isBreak = True
                      continue
          if isBreak == False:
              self.possibleMoves.append(nextMove)
      self.inCheck()
      if kingCheck != self.color:
          if self.hasMoved == False:
              for i in allPieces:
                  if i.piece == "R " and i.hasMoved == False and i.color == self.color:
                      isCastle = True
                      if abs(i.posX - self.posX) == 4:
                          if board[self.posY][self.posX - 1] == "  " and board[self.posY][
                              self.posX - 2] == "  " and board[self.posY][self.posX - 3] == "  ":
                              oldX = self.posX
                              self.posX -= 1
                              self.inCheck()
                              if kingCheck == self.color:
                                  isCastle = False
                              self.posX = oldX
                              self.inCheck()
                              self.posX -= 2
                              self.inCheck()
                              if kingCheck == self.color:
                                  isCastle = False
                              self.posX = oldX
                              self.inCheck()
                              if isCastle:
                                  self.posX = oldX
                                  self.possibleMoves.append("0-0-0")
                      isCastle = True
                      if abs(i.posX - self.posX) == 3:
                          if board[self.posY][self.posX + 1] == "  " and board[self.posY][self.posX + 2] == "  ":
                              oldX = self.posX
                              self.posX += 1
                              self.inCheck()
                              if kingCheck == self.color:
                                  isCastle = False
                              self.posX = oldX
                              self.inCheck()
                              self.posX += 2
                              self.inCheck()
                              if kingCheck == self.color:
                                  isCastle = False
                              self.posX = oldX
                              self.inCheck()
                              if isCastle:
                                  self.posX = oldX
                                  self.possibleMoves.append("0-0")
              return self.possibleMoves
  
  def inCheck(self):
      var = False
      global kingCheck
      for i in allPieces:
          if i.color != self.color:
              for j in i.possibleMoves:
                  try:
                      convertCoords(self.posY, self.posX)
                  except:
                      pass
                  else:
                      if j == convertCoords(self.posY, self.posX):
                          var = True
  
              if var == False:
                  kingCheck = ""
              else:
                  kingCheck = currentSide
