
fruits = ("apple", "banana", "orange")

# Iterating through indices and elements
for index, fruit in enumerate(fruits):
    print(f"{index} = {fruit}")

temperatures = (25, 30, 22, 35, 28)


max_temp = temperatures[0]
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
print(f"Maximum Temperature: {max_temp}")

scores = (90, 85, 95, 78, 88)

# Filtering elements greater than 90
high_scores = [score for score in scores if score > 90]
print("High Scores:", high_scores)

# Creating a tuple with elements squared
numbers = (1, 2, 3, 4, 5)
squared_numbers = tuple(num ** 2 for num in numbers)
print("Squared Numbers:", squared_numbers)

colors = ("red", "green", "blue", "yellow")

# Checking if a color exists in the tuple
color_to_check = "green"
exists = color_to_check in colors
print(f"{color_to_check} exists: {exists}")

# principal = 1000
# r = 0.05
# t = 5

# fam = principal*(1+r)**t
# print(fam)
import pandas as pd

data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
df = pd.DataFrame(data)


print(df.empty) 