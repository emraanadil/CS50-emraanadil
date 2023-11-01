# program to determine the nof of coins
from cs50 import get_float

# getting user input
while True:
    dollars = get_float("No of dollars: ")
    if (dollars > 0):
        break
# calculating the change
cents = int(round(dollars * 100))
cents_25 = 0
cents_10 = 0
cents_5 = 0
cents_1 = 0
# looping for coins

while (cents > 0):
    while (cents >= 25):
        cents_25 += 1
        cents -= 25
    while (cents >= 10):
        cents_10 += 1
        cents -= 10
    while (cents >= 5):
        cents_5 += 1
        cents -= 5
    while (cents >= 1):
        cents_1 += 1
        cents -= 1

#   print the not of cents;
add = cents_25 + cents_10 + cents_5 + cents_1
print(add)
