class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print("I am driving")

    def printName(self):
        print(self.name)


c1 = Car("Honda")
c1.drive()
c1.printName()
