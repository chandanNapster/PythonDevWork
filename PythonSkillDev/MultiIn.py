class Box:
    def __init__(self, color, **kwarg):
        super().__init__(**kwarg)
        self.color = color

    def getColor(self):
        return self.color


class BreakableItems:
    def __init__(self, isBreakable, **kwarg):
        super().__init__(**kwarg)
        self.isBreakable = isBreakable

    def isBreakable(self):
        return self.isBreakable


class RedBreakableBox(Box, BreakableItems):
    def __init__(self, weight):
        super().__init__(color="Red", isBreakable=True)
        self.__weight = weight

    def __str__(self):
        return ("[" + "The Box is of " + str(super().getColor()) + " color" +
                "\n The Box " + ("is " if (super().isBreakable()) else "is not ") + "breakable" +
                "\n The weight of the box is " + str(self.__weight) + " Kg" + "]")


if __name__ == '__main__':

    RedBreakableBox1 = RedBreakableBox(34)
    print(RedBreakableBox1)
