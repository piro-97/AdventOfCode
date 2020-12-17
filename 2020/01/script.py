import os


# part 1

numbers = []

f = open(os.getcwd() + "/2020/1/input.txt", "r")
lines = f.readlines()

for line in lines:
    numbers.append(int(line))

for num1 in numbers:
    for num2 in numbers:
        if (num1 + num2 == 2020):
            print("part 1: " + str(num1 * num2))



# part 2

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if (num1 + num2 + num3 == 2020):
                print("part 2: " + str(num1 * num2 * num3))
