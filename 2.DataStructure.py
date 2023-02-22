#List
names = ["fethi", "ibrahim", "feyyaz"]

print("names: ", names)
names.append("ahmet")
print("names: ", names)
names[1] = "veli"
print("names: ", names)

print("names.count('fethi'): ", names.count("fethi"))
names.pop(1)
print("names.pop(1)->names: ", names)
names.reverse()
print("names.reverse()->names: ", names)
names_copy = names.copy()
print("names.clear(): ", names.clear())
print("names_copy: ", names_copy)
print()

#Tuple
my_tuple = (2,4,6,8)
print("my_tuple: ", my_tuple)
print("cant change: my_tuple[0] = 10")
print("my_tuple[1]: ", my_tuple[1])
print("my_tuple[-1]: ", my_tuple[-1])
print()

#Set
my_set = {"fethi", "ibrahim", "feyyaz"}
print("my_set: ", my_set)

for name in my_set:
    print("name: ", name)

my_set.add("ali")
print("my_set.add('ali')->my_set: ", my_set)
my_set.update(["merve", "özge", "sinem"])
print("my_set.update(['merve', 'özge', 'sinem'])->my_set: ", my_set)
print()

numbers = {1,2,3,4,3,5,6,5}
numbers2 = {1,2,7}
print("numbers: ", numbers)
print("numbers | numbers2", numbers | numbers2)
print("numbers & numbers2", numbers & numbers2)
print("numbers - numbers2", numbers - numbers2)
print("numbers ^ numbers2", numbers ^ numbers2)
print()

#dictinory
my_dict = {"book": "kitap", "table": "masa"}
print(my_dict)