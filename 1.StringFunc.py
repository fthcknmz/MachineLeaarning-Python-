message = "Hello World"

#substring
print("message[1:10]: ", message[1:10])

#length
print("len(message): ", len(message))

#lower / upper
print("message.upper(): ", message.upper())
print("message.lower(): ", message.lower())

# replace
message = "dünya"
print("message.replace('ü','u'): ",message.replace("ü","u"))
print("message.replace('a','e'): ",message.replace("a","e"))

# split
info = "Fethi Çekinmez Istanbul"
print("info.split(): ",info.split())
info = "Fethi;Çekinmez;Istanbul"
print("info.split(';'): ",info.split(";"))

# input 
name = input("name?")
print("name: ", name)