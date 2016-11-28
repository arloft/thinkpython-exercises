#def drawGrid(numberOfRows, numberOfColumns):
#    if numberOfRows == 1 and numberOfColumns == 1:

def draw2x2Grid(count):
    print((("+ " + "- " * 4) * count) + "+")
    print((("| " + " " * 8) * count) + "|")
    print((("+ " + "- " * 4) * count) + "+")

draw2x2Grid(4)