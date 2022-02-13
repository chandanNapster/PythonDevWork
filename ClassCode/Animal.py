class Animals:

    num_of_animals = 0
    animalList = [0]*2

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        #self.num_of_animals += 1

# def __init__(self,name):
##        self.name = name
##        self.num_of_animals +=1

    def getName(self):
        return self.name

    def getAge(self):
        return self.__age

    def __str__(self):
        # print(self.funck())
        # self.funckWhile()
        return "(" + str(self.getName()) + ", " + str(self.getAge()) + "" + ")"

    def funck(self):
        print(4 == 5)
        print(4 != 5)
        result = not(4 < 5)
        result2 = (4 < 5)
        if (result or result2):
            print("I a")
        return result

    def getNumofAnimals(self):
        return self.num_of_animals

    def addAnimals(self, name, age):
        self.num_of_animals += 1

    def funckWhile(self):
        i = 0
        while i < 10:
            print(i)
            i += 1

    def listAnimals(self, animal):
        # print("Here")
        if(len(self.getAnimalList()) == 2):
            # print("Hello")
            self.animalList[self.num_of_animals] = animal
            self.num_of_animals += 1
        else:
            doubleList = [0]*(len(self.animalList)*2)
            doubleList = self.getAnimalList
            self.animalList = doubleList
            print(len(self.animalList))

    def getAnimals(self):
        i = 0
        while i < self.num_of_animals:
            print(self.animalList[i])
            i += 1

    def getAnimalList(self):
        return self.animalList
