


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
