input = open('input.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    first = 0
    last = 0

    for char in line:
        if char.isdigit():
            if first == 0:
                first = char
            last = char

    sum = sum + int(first + last)

input.close()
print(sum)
