# with open("test.txt") as file:
#     contents = file.read()
#     print(contents)

with open("test.txt", mode="a") as file:
    file.write("\nNext Line.")
