from Piece import Piece 
from Pawn import Pawn
from Knight import Knight 
from Bishop import Bishop
from Rook import Rook 
from Queen import Queen
from King import King

global playAgain
playAgain = True
while playAgain:
  playAgain = "Hello"
  currentSide = "w"
  moveCount = 1
  previousMove = ""
  kingCheck = ""

  allPieces = []

  rows = [1, 2, 3, 4, 5, 6, 7, 8]
  cols = ["a", "b", "c", "d", "e", "f", "g", "h"]

  board = []

  for i in range(8):
      board.append(["  "] * 8)

  def print_board():
      print("\n")
      rowCount = 0
      for row in board:
          print(("    ".join(row)) + ("        " + str(rows[7 - rowCount])))
          print("\n")
          rowCount += 1
      print("     ".join(cols))
      print("\n")

  alphabet = "abcdefgh"
  numbers = "12345678"

  def convertSquare(square):
      coords = []
      coords.append(8 - int(square[1]))
      for i in range(len(alphabet)):
          if alphabet[i] == square[0]:
              coords.append(i)
      return coords

  def convertCoords(coordY, coordX):
      square = ""
      square += alphabet[coordX]
      square += str(8 - coordY)
      return square

  for i in range(8):
      allPieces.append(Pawn("P ", "w", 6, i))

  allPieces.extend(
      [Knight("N ", "w", 7, 1), Knight("N ", "w", 7, 6), Knight("N ", "b", 0, 1), Knight("N ", "b", 0, 6),
       Bishop("B ", "w", 7, 2), Bishop("B ", "w", 7, 5), Bishop("B ", "b", 0, 2), Bishop("B ", "b", 0, 5),
       Rook("R ", "w", 7, 0), Rook("R ", "w", 7, 7), Rook("R ", "b", 0, 0), Rook("R ", "b", 0, 7),
       Queen("Q ", "w", 7, 3), Queen("Q ", "b", 0, 3)])
  kings = [King("K ", "w", 7, 4), King("K ", "b", 0, 4)]
  for i in kings:
      allPieces.append(i)

  for i in range(8):
      allPieces.append(Pawn("P ", "b", 1, i))

  def createPM():
      for i in allPieces:
          i.createMoves()

  def choosePiece():
      global playAgain
      global alphabet
      global numbers
      global moveCount
      global currentSide
      global previousMove
      global kingCheck
      createPM()
      for i in kings:
          if i.color == currentSide:
              i.inCheck()
      createPM()
      isBreak = False
      print(previousMove)
      print("Move " + str(moveCount) + ": " + currentSide)
      if len(allPieces) == 2:
          print("Draw by insufficient material.")
          playAgain = input("Play again? Y/N")
          while True:
              try:
                  if playAgain == "Y":
                      playAgain = True
                  elif playAgain == "N":
                      playAgain = False
                  else:
                      0 / 0
                  break
              except:
                  print("I don't think you typed that right.")
                  playAgain = input("Play again? Y/N")
      if len(allPieces) == 3:
          for i in allPieces:
              if i.piece == "N " or i.piece == "B ":
                  print("Draw by insufficient material.")
                  playAgain = input("Play again? Y/N")
                  while True:
                      try:
                          if playAgain == "Y":
                              playAgain = True
                          elif playAgain == "N":
                              playAgain = False
                          else:
                              0 / 0
                          break
                      except:
                          print("I don't think you typed that right.")
                          playAgain = input("Play again? Y/N")
      if len(allPieces) == 4:
          cond = True
          for i in allPieces:
              if i.piece == "R " or i.piece == "P " or i.piece == "Q ":
                  cond = False
          if cond:
              print("Draw by insufficient material.")
              playAgain = input("Play again? Y/N")
              while True:
                  try:
                      if playAgain == "Y":
                          playAgain = True
                      elif playAgain == "N":
                          playAgain = False
                      else:
                          0 / 0
                      break
                  except:
                      print("I don't think you typed that right.")
                      playAgain = input("Play again? Y/N")
      checkmate = False
      if playAgain == "Hello":
          checkmate = True
      for i in allPieces:
          if i.color == currentSide and playAgain == "Hello":
              i.checkMoves()
              if len(i.checkMoves()) != 0:
                  print(i.piece + "on " + convertCoords(i.posY, i.posX))
                  print(i.checkMoves())
                  checkmate = False
      if checkmate == True and kingCheck == currentSide:
          print(currentSide + " loses in " + str(moveCount) + " moves by checkmate!")
          playAgain = input("Play again? Y/N")
          while True:
              try:
                  if playAgain == "Y":
                      playAgain = True
                  elif playAgain == "N":
                      playAgain = False
                  else:
                      0 / 0
                  break
              except:
                  print("I don't think you typed that right.")
                  playAgain = input("Play again? Y/N")
      if checkmate and not (kingCheck == currentSide):
          print("Draw in " + str(moveCount) + " moves by stalemate.")
          playAgain = input("Play again? Y/N")
          while True:
              try:
                  if playAgain == "Y":
                      playAgain = True
                  elif playAgain == "N":
                      playAgain = False
                  else:
                      0 / 0
                  break
              except:
                  print("I don't think you typed that right.")
                  playAgain = input("Play again? Y/N")
      if playAgain == "Hello" and playAgain is not True and playAgain is not False:
          whichPiece = input("Choose a piece to move (type in name as shown): ")
          while not isBreak:
              try:
                  for i in allPieces:
                      conv = convertSquare(whichPiece[5:7])
                      if len(whichPiece) == 7 and whichPiece[1:5] == " on " and i.posY == conv[0] and i.posX == conv[
                          1] and i.color == currentSide and i.piece == whichPiece[0:2]:
                          conv = convertSquare(whichPiece[5:7])
                          isBreak = True
              except:
                  whichPiece = input("Type in the name exactly as shown!")
              else:
                  if not isBreak:
                      whichPiece = input("Type in the name exactly as shown!")
          for i in allPieces:
              if conv[0] == i.posY and conv[1] == i.posX and playAgain == "Hello":
                  i.movePiece()
                  if currentSide == "w":
                      currentSide = "b"
                  else:
                      currentSide = "w"
                      moveCount += 1
                  choosePiece()

  print_board()
  choosePiece()
