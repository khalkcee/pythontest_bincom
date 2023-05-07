import random
import psycopg2
from collections import Counter
from statistics import mode
import numpy as np

colors = [
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE",
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE",
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"
]
#------------------
# 1 the mean color: 
mean_color = Counter(colors).most_common()[0][0]
print("Mean color:", mean_color)

# 2 Calculate the most common color by finding the mode
most_common_color = mode(colors)
print("Most common color:", most_common_color)


# 3 median
sorted_colors = sorted(colors)
num_colors = len(sorted_colors)
if num_colors % 2 == 0:
    median_color_1 = sorted_colors[num_colors // 2 - 1]
    median_color_2 = sorted_colors[num_colors // 2]
    median_color = f"{median_color_1}/{median_color_2}"
else:
    median_color = sorted_colors[num_colors // 2]
print("Median color:", median_color)


#4 BONUS if a colour is chosen at random, 
# what is the probability that the color is red?


# count of number of times red appears
red_count = colors.count('red')

#total number of colors
total_colors = len(colors)

#probability calculation
probability = red_count / total_colors

print("The probability of selecting red color at random is:", probability)

#5 
colors = [c.lower() for c in colors]
# frequencies of each color
color_freq = {}
for color in colors:
    if color in color_freq:
        color_freq[color] += 1
    else:
        color_freq[color] = 1

# Get the mean of the colors
mean_color = np.mean(list(color_freq.values()))

# Get the variance of the colors
variance_color = sum(
    [(freq - mean_color) ** 2 for freq in color_freq.values()]) / len(colors)

print(f"The variance of the colors is {variance_color:.2f}")


#6 
# connect to  database 
conn = psycopg2.connect(
    database="mydatabase", user="myusername", password="mypassword", host="localhost", port="5432"
)

# create a cursor object
cur = conn.cursor()

# create the table
cur.execute("CREATE TABLE colors (color VARCHAR(255), frequency INT)")

# loop through the colors and count the frequency
for color in set(colors):
    frequency = colors.count(color)
    cur.execute(
        f"INSERT INTO colors (color, frequency) VALUES ('{color}', {frequency})")

# commit the changes and close the connection
conn.commit()
conn.close()

print("Colors and their frequencies have been saved to the database.")


# QUESTION 7
# a recursive searching 
# algorithm to search for a number entered by 
# the user in a list of numbers:
def recursive_search(lst, num_to_find, index=0):
    if len(lst) == 0:
        return -1
    elif lst[0] == num_to_find:
        return index
    else:
        return recursive_search(lst[1:], num_to_find, index+1)


# Take input from user
num_to_find = int(input("Enter the number to search: "))

# Test the function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = recursive_search(lst, num_to_find)
if index == -1:
    print("Number not found in list")
else:
    print(f"Number found at index: {index}")


# 8

# Generate random 4-digit binary number
binary_num = ''.join(str(random.randint(0, 1)) for _ in range(4))

# Convert binary to decimal
decimal_num = int(binary_num, 2)

# Print results
print("Binary number:", binary_num)
print("Decimal number:", decimal_num)





#9
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


sum = 0
for i in range(1, 51):
    sum += fibonacci(i)

print("Sum of first 50 Fibonacci numbers:", sum)
