import os

f = open(os.getcwd() + "/2020/9/input.txt", "r")
Lines = f.readlines()


# does any two numbers in the list sums up to num?
def sums_to_number(my_list, num):
    my_list.sort()
    found = False
    first = 0
    last = len(my_list) - 1

    while not found and first != last:
        found = (my_list[first] + my_list[last] == num)

        first += 1
        if last == first:
            last -= 1
            first = 0

    return found

def sums_to_number_set(my_list, num):
    found = False
    first = 0
    last = len(my_list) - 1

    while not found and first != last:
        found = sum(my_list[first : last + 1]) == num

        if found:
            return True, first, last

        if my_list[last] > num:
            last -= 1

        first += 1
        if last == first:
            last -= 1
            first = 0

    return False, -1, -1


# part 1

magic_number = 25
numbers = []
for i, value in enumerate(Lines):
    numbers.append(int(value))
    
    if i >= magic_number:
        found = sums_to_number(numbers[i - magic_number : i], numbers[i])
        
        if not found:
            break

print("part 1: " + str(numbers[-1]))


# part 2

number_to_be_found = numbers[-1]
numbers = list((int(i) for i in Lines))
x, f, l = sums_to_number_set(numbers, number_to_be_found)

my_min = min(numbers[f:l+1])
my_max = max(numbers[f:l+1])

if x:
    print("part 2: " + str(my_min + my_max))
else:
    print("not exists")