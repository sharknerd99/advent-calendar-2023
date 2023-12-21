input = open('input.txt', 'r')
lines = input.readlines()
x_max = len(lines[0]) - 1
y_max = len(lines)
sum = 0
y = 0
gears = []
gears_nums = []

def full_num(line, x):
    while x + 1 < x_max:
        if not line[x + 1].isdigit():
            break
        x = x + 1
    return x

def check_part(x1, x2, y):
    while x1 <= x2:
        if x1 - 1 >= 0:
            if y - 1 >= 0 and lines[y - 1][x1 - 1] == '*':
                return (True, x1 - 1, y - 1)
            if lines[y][x1 - 1] == '*':
                return (True, x1 - 1, y)
            if y + 1 < y_max and lines[y + 1][x1 - 1] == '*':
                return (True, x1 - 1, y + 1)

        if x1 + 1 < x_max:
            if y - 1 >= 0 and lines[y - 1][x1 + 1] == '*':
                return (True, x1 + 1, y - 1)
            if lines[y][x1 + 1] == '*':
                return (True, x1 + 1, y)
            if y + 1 < y_max and lines[y + 1][x1 + 1] == '*':
                return (True, x1 + 1, y + 1)

        if y - 1 >= 0 and lines[y - 1][x1] == '*':
            return (True, x1, y - 1)

        if y + 1 < y_max and lines[y + 1][x1] == '*':
            return (True, x1, y + 1)

        x1 = x1 + 1
    
    return (False, 0, 0)

def check_duplicate(gear, num):
    if gear in gears:
        index = gears.index(gear)
        return gears_nums[index] * num
    else:
        gears.append(gear)
        gears_nums.append(num)
        return 0

for line in lines:
    line = line[:-1]
    x = 0
    while x < x_max:
        if line[x].isdigit():
            x2 = full_num(line, x)
            gear = check_part(x, x2, y)

            if gear[0]:
                sum = sum + check_duplicate(gear, int(line[x:x2+1]))
            
            x = x2
        x = x + 1
    y = y + 1

print(sum)
input.close()