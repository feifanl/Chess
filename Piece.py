class Piece:
  def __init__(self, piece, color, posY, posX):
      self.piece = piece
      self.color = color
      self.posY = posY
      self.posX = posX
      self.possibleMoves = []
      self.hasMoved = False
      board[self.posY][self.posX] = self.piece

  def movePiece(self):
      global previousMove
      for i in self.checkMoves():
          print(i)
      move = input("Choose a move: ")
      while True:
          if not (move in self.possibleMoves):
              move = input("Please enter a valid move: ")
          else:
              if move == "0-0" or move == "0-0-0":
                  if move == "0-0":
                      board[self.posY][self.posX] = "  "
                      self.posX += 2
                      board[self.posY][self.posX] = self.piece
                      self.hasMoved = True
                      for i in allPieces:
                          if i.piece == "R " and i.posX == 7 and i.color == currentSide:
                              board[i.posY][i.posX] = "  "
                              i.posX -= 2
                              board[i.posY][i.posX] = i.piece
                              i.hasMoved = True
                  if move == "0-0-0":
                      board[self.posY][self.posX] = "  "
                      self.posX -= 2
                      board[self.posY][self.posX] = self.piece
                      self.hasMoved = True
                      for i in allPieces:
                          if i.piece == "R " and i.posX == 0 and i.color == currentSide:
                              board[i.posY][i.posX] = "  "
                              i.posX += 3
                              board[i.posY][i.posX] = i.piece
                              i.hasMoved = True
                  previousMove = ""
                  previousMove += move
                  print_board()
                  break
              if self.piece == "P " and (
                      (self.color == "w" and move[1] == "8") or (self.color == "b" and move[1] == "1")):
                  promotion = input("Choose a piece to promote to (Q, R, B, N): ")
                  while True:
                      if promotion != "Q" and promotion != "R" and promotion != "B" and promotion != "N":
                          promotion = input("That isn't valid. Try again.")
                      else:
                          previousMove = ""
                          previousMove += self.piece + "promoted to " + promotion + " on " + move
                          board[self.posY][self.posX] = "  "
                          self.posY = convertSquare(move)[0]
                          self.posX = convertSquare(move)[1]
                          allPieces.remove(self)
                          if promotion == "Q":
                              allPieces.append(Queen("Q ", self.color, self.posY, self.posX))
                          if promotion == "R":
                              allPieces.append(Rook("R ", self.color, self.posY, self.posX))
                          if promotion == "B":
                              allPieces.append(Bishop("B ", self.color, self.posY, self.posX))
                          if promotion == "N":
                              allPieces.append(Knight("N ", self.color, self.posY, self.posX))
                          print_board()
                          return
              else:
                  for i in allPieces:
                      if i.posY == convertSquare(move)[0] and i.posX == convertSquare(move)[1]:
                          allPieces.remove(i)
                      if self.color == "w":
                          if self.piece == "P " and move == self.possibleMoves[len(self.possibleMoves) - 1] and \
                                  move[
                                      0] != convertCoords(self.posY, self.posX)[0] and \
                                  board[convertSquare(move)[0]][
                                      convertSquare(move)[1]] == "  " and (int(move[1]) - 1) == int(
                              convertCoords(i.posY, i.posX)[1]) and move[0] == convertCoords(i.posY, i.posX)[
                              0] and i.piece == "P ":
                              board[i.posY][i.posX] = "  "
                              allPieces.remove(i)
                      if self.color == "b":
                          if self.piece == "P " and move == self.possibleMoves[len(self.possibleMoves) - 1] and \
                                  move[
                                      0] != convertCoords(self.posY, self.posX)[0] and \
                                  board[convertSquare(move)[0]][
                                      convertSquare(move)[1]] == "  " and (int(move[1]) + 1) == int(
                              convertCoords(i.posY, i.posX)[1]) and move[0] == convertCoords(i.posY, i.posX)[
                              0] and i.piece == "P ":
                              board[i.posY][i.posX] = "  "
                              allPieces.remove(i)
                  previousMove = ""
                  previousMove += self.piece + "on " + convertCoords(self.posY, self.posX) + " to " + move
                  board[self.posY][self.posX] = "  "
                  self.posY = convertSquare(move)[0]
                  self.posX = convertSquare(move)[1]
                  board[self.posY][self.posX] = self.piece
                  print_board()
                  break

  def checkMoves(self):
      oldMoves = list(self.possibleMoves)
      possible_moves = []
      for m in oldMoves:
          oldposY = self.posY
          oldposX = self.posX
          if len(m) == 2:
              self.posY = convertSquare(m)[0]
              self.posX = convertSquare(m)[1]
              createPM()
              for i in allPieces:
                  if convertCoords(i.posY, i.posX) == m:
                      i.possibleMoves.clear()
              for king in kings:
                  if king.color == self.color:
                      king.inCheck()
              if kingCheck == self.color:
                  self.posY = oldposY
                  self.posX = oldposX
                  for king in kings:
                      if king.color == self.color:
                          king.inCheck()
                  createPM()
              elif kingCheck == "":
                  self.posY = oldposY
                  self.posX = oldposX
                  for king in kings:
                      if king.color == self.color:
                          king.inCheck()
                  createPM()
                  possible_moves.append(m)
          else:
              possible_moves.append(m)
      self.possibleMoves.clear()
      self.possibleMoves = possible_moves
      return self.possibleMoves
