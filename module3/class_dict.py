class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

# show all the defined methods and attributes of the object
print(obj.__dict__)

# show all the defined methods and attributes of the class
print(Classy.__dict__)


print(Classy.__name__)
print(type(obj).__name__)