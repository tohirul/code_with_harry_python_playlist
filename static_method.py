
class Math:
    def __init__(self, num):
        self.num = num

    def addition(self, n):
        self.num += n

    @staticmethod
    def add(a, b):
        return a + b


result = Math(8)
print(result.num)

result.addition(10)
print(result.num)
