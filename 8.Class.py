class math_class:
    def __init__(self):
        print("constructer block")
    def addition(self, a, b):
        return a+b
    
    def multiplication(self, a, b):
        return a*b

    def division(self, a, b):
        return a/b

    def extraction(self, a, b):
        return a-b

math = math_class()
print(str(math.addition(2,28)))
