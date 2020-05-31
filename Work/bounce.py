# bounce.py
#
# Exercise 1.5

height = 100 # drop height in meters

factor = 3/5

for i in range(1, 11):
    height = height * factor
    print(i, round(height, 4))
