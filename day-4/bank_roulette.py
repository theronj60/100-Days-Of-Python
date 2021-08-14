import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

rand_name_index = random.randint(0, len(names))

print(names[rand_name_index])
