# Name: William W
# Period 6
# Dice Rolling Simulator

import random

rollnums = [0, 0, 0, 0, 0, 0]

# main code
number = int(input("How many rolls? "))

for i in range(number):
    roll = random.randint(1, 6)
    print(str(i + 1) + ": Rolled " + str(roll))
    rollnums[roll - 1] += 1

print("Total Rolls: " + str(number + 1))

for i in range(6):
    print(str(i + 1) + ": " + str(rollnums[i]))

print("\nPercentages:")
for i in range(6):
    print(str(i + 1) + ": " + str(rollnums[i] / 10 * 100))