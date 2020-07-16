# bounce.py
#
# Exercise 1.5

height = 100
bounches = 10

while bounches > 0:
    height *= 0.6
    print(round(height, 4))
    bounches -= 1