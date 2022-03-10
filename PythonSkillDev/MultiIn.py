class Box(object):
    def __init__(self, color, **kwarg):
        super().__init__(**kwarg)
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return ("The box [ " + str(self.getColor()) + " ]")


class BreakableItems(object):
    def __init__(self, isBreakable, **kwarg):
        super().__init__(**kwarg)
        self.isBreakable = isBreakable

    def isBreakable(self):
        return self.isBreakable

    def __str__(self):
        return ("Is breakable [ " + str(self.isBreakable()) + " ]")


class RedBreakableBox(Box, BreakableItems):
    def __init__(self, weight):
        super().__init__(isBreakable=True, color="Red")
        self.__weight = weight

    def __str__(self):
        return ("[" + "The Box is of " + str(super().getColor()) + " color" +
                "\n The Box " + ("is " if (super().isBreakable()) else "is not ") + "breakable" +
                "\n The weight of the box is " + str(self.__weight) + " Kg" + "]")


if __name__ == '__main__':

    RedBreakableBox1 = RedBreakableBox(34)
    print(RedBreakableBox1)
    box1 = Box(color="Green")
    print(box1)
    box2 = Box("Red")
    print(box2)
