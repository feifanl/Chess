from utils import *

def print_board():
    print("\n")
    rowCount = 0
    for row in board:
        print(("    ".join(row)) + ("        " + str(rows[7 - rowCount])))
        print("\n")
        rowCount += 1
    print("     ".join(cols))
    print("\n")

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

    class Knight(Piece):
        def createMoves(self):
            global alphabet
            global numbers
            self.possibleMoves.clear()
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            if nextMove[0] != "h" and int(nextMove[1]) < 7:
                nextMove = ""
                nextMove += alphabet[alpha + 1]
                nextMove += numbers[num + 2]
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
            if nextMove[0] != "a" and int(nextMove[1]) < 7:
                nextMove = ""
                nextMove += alphabet[alpha - 1]
                nextMove += numbers[num + 2]
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
            if nextMove[0] != "g" and nextMove[0] != "h" and int(nextMove[1]) < 8:
                nextMove = ""
                nextMove += alphabet[alpha + 2]
                nextMove += numbers[num + 1]
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
            if nextMove[0] != "g" and nextMove[0] != "h" and int(nextMove[1]) > 1:
                nextMove = ""
                nextMove += alphabet[alpha + 2]
                nextMove += numbers[num - 1]
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
            if nextMove[0] != "a" and nextMove[0] != "b" and int(nextMove[1]) < 8:
                nextMove = ""
                nextMove += alphabet[alpha - 2]
                nextMove += numbers[num + 1]
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
            if nextMove != "a" and nextMove[0] != "b" and int(nextMove[1]) > 1:
                nextMove = ""
                nextMove += alphabet[alpha - 2]
                nextMove += numbers[num - 1]
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
            if nextMove[0] != "h" and int(nextMove[1]) > 2:
                nextMove = ""
                nextMove += alphabet[alpha + 1]
                nextMove += numbers[num - 2]
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
            if nextMove[0] != "a" and int(nextMove[1]) > 2:
                nextMove = ""
                nextMove += alphabet[alpha - 1]
                nextMove += numbers[num - 2]
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

    class Bishop(Piece):
        def createMoves(self):
            global alphabet
            global numbers
            self.possibleMoves.clear()
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break

    class Rook(Piece):
        def createMoves(self):
            global alphabet
            global numbers
            self.possibleMoves.clear()
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break

    class Queen(Piece):
        def createMoves(self):
            global alphabet
            global numbers
            self.possibleMoves.clear()
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break
            nextMove = convertCoords(self.posY, self.posX)
            isBreak = False
            alpha = alphabet.index(nextMove[0])
            num = numbers.index(nextMove[1])
            while isBreak == False:
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
                else:
                    break

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
                    assert (playAgain == "Y" or playAgain == "N")
                    if playAgain == "Y":
                        playAgain = True
                    elif playAgain == "N":
                        playAgain = False
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
                            assert (playAgain == "Y" or playAgain == "N")
                            if playAgain == "Y":
                                playAgain = True
                            elif playAgain == "N":
                                playAgain = False
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
                        assert (playAgain == "Y" or playAgain == "N")
                        if playAgain == "Y":
                            playAgain = True
                        elif playAgain == "N":
                            playAgain = False
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
        if checkmate and kingCheck == currentSide:
            print(currentSide + " loses in " + str(moveCount) + " moves by checkmate!")
            playAgain = input("Play again? Y/N")
            while True:
                try:
                    assert (playAgain == "Y" or playAgain == "N")
                    if playAgain == "Y":
                        playAgain = True
                    elif playAgain == "N":
                        playAgain = False
                    break
                except:
                    print("I don't think you typed that right.")
                    playAgain = input("Play again? Y/N")
        if checkmate and not (kingCheck == currentSide):
            print("Draw in " + str(moveCount) + " moves by stalemate.")
            playAgain = input("Play again? Y/N")
            while True:
                try:
                    assert (playAgain == "Y" or playAgain == "N")
                    if playAgain == "Y":
                        playAgain = True
                    elif playAgain == "N":
                        playAgain = False
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
