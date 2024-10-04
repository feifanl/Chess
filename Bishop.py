from Piece import Piece

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
