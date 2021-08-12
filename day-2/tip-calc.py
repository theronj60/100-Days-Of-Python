print("Welcome to the Python Tip Calculator")
bill_total = float(input("What was the total of the bill?\n$"))
percentage = float(input("What percentage would you like to tip? 10, 12, or 15?\n")) / 100
total_people = float(input("How many people are splitting the bill?\n"))
tip = bill_total * percentage
split = round(tip / total_people, 2)
total = print(f"Each person needs to pay: ${split}")
