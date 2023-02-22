def greetings(name):
    print("Hello, " + name + ". WELCOME!")

nm = input()

greetings(nm)
print("***********************")


def calculate_area(a, b):
    return a*b/2

area = calculate_area(3,4)
print(area)
print("***********************")


calculate_area2 = lambda a,b : a*b/2
print(calculate_area2(3,6))
print("***********************")

print(type(calculate_area2))
print(type(calculate_area))