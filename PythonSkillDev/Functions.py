from collections import namedtuple
# DECLARE THE STRUCTURE OF THE BOX DATA STRUCTURE
Box = namedtuple("Box", "color weight content_breakable")

# INITIALIZE SOME BOXES
b1 = Box("Red", 10, False)
b2 = Box("Blue", 20, True)
b3 = Box("Green", 40, False)

# CREATE A BOXES LIST AND POPULATE IT WITH SOME VAUES
Boxes = []
Boxes.append(Box("Red", 8, True))
Boxes.append(Box("Blue", 11, True))
Boxes.append(Box("Green", 15, False))
Boxes.append(Box("Yellow", 16, True))
Boxes.append(Box("Red", 29, False))
Boxes.append(Box("Blue", 56, True))
Boxes.append(Box("Red", 5, False))
Boxes.append(b1)
Boxes.append(b2)
Boxes.append(b3)


def addBoxes(boxes):
    Boxes.append(boxes)


def createBox(color, weight, isBreakable):
    return Box(color, weight, isBreakable)


b = createBox("Yellow", 4, False)
addBoxes(b)

addBoxes(createBox("Red", 23, True))


# print(Boxes)


def findBoxes(color):
    colorBoxes = []
    num_of_boxes = 0
    print(color)
    for box in Boxes:
        if box.color.casefold() == color.casefold():
            colorBoxes.append(box)
            num_of_boxes += 1
    return colorBoxes, num_of_boxes


def userInputSearchBoxes():
    color = input("Enter the color of box or press q to quit :")
    while color.casefold() != 'q':
        print(findBoxes(color))
        color = input("Enter the color of box or press q to quit :")


colDict = {}


def findMultipleBoxes(**param):
    for color in param.values():
        print(findBoxes(color))


def createABoxDict(color, index):
    col = 'col' + str(index)
    colDict[col] = color
    return colDict


def userInputSearchMultipleBoxes():
    userInput = input("Press any key to continue or press q to quit :")
    dict_index = 0
    while userInput.casefold() != 'q':
        color = input(
            "Enter box color you wish to search for or press q to stop :")
        if color.casefold() != 'q':
            createABoxDict(color, dict_index)
        dict_index += 1
        userInput = color
    findMultipleBoxes(**colDict)


# userInputSearchBoxes()
# findMultipleBoxes(**colDict)
userInputSearchMultipleBoxes()
# print(colDict)
# print(createABoxDict('Red', 3))


def testArg(*list):
    for item in list:
        print(item)


listA = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

testArg(1, 2)
testArg(1, 2, 3, 4)
