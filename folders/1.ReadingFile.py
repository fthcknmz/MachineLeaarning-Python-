f = open("customer.txt")

# r: read a: append w:write x:create
for l in f:
    print(l)

f.close()

fileToAppend = open("students.txt", "a")
fileToAppend.write("Derin")
fileToAppend.write("\n")
fileToAppend.write("Salih")
fileToAppend.close()

import os

if os.path.exists("students.txt"):
    os.remove("students.txt")
