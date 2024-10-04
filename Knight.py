from Piece import Piece

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
