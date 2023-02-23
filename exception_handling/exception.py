

try:
    num = int(input("enter number: "))
except ValueError:
    print("invalid input")
except:
    print("an error occured")

