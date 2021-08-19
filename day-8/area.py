import math

def paint_calc(height, width, cover):
    cans = (height * width) / cover
    cans = math.ceil(cans)
    print(f"You need {cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
