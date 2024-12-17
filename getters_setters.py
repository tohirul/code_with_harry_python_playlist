class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value: {self._value}")

    @property
    def truevalue(self):
        return self._value * 10

    @truevalue.setter
    def truevalue(self, value):
        self._value = value / 10


getValue = MyClass(130)
getValue.show()
getValue.truevalue = 150
print("Check: ", getValue.truevalue)
getValue.show()
