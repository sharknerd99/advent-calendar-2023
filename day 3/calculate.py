input = open('input.txt', 'r')
lines = input.readlines()
x_max = len(lines[0]) - 1
y_max = len(lines)
sum = 0
y = 0

def full_num(line, x):
    while x + 1 < x_max:
        if not line[x + 1].isdigit():
            break
        x = x + 1
    return x

def check_part(x1, x2, y):
    while x1 <= x2:
        if x1 - 1 >= 0:
            if y - 1 >= 0 and not lines[y - 1][x1 - 1] == '.' and not lines[y - 1][x1 - 1].isdigit():
                return True
            if not lines[y][x1 - 1] == '.' and not lines[y][x1 - 1].isdigit():
                return True
            if y + 1 < y_max and not lines[y + 1][x1 - 1] == '.' and not lines[y + 1][x1 - 1].isdigit():
                return True

        if x1 + 1 < x_max:
            if y - 1 >= 0 and not lines[y - 1][x1 + 1] == '.' and not lines[y - 1][x1 + 1].isdigit():
                return True
            if not lines[y][x1 + 1] == '.' and not lines[y][x1 + 1].isdigit():
                return True
            if y + 1 < y_max and not lines[y + 1][x1 + 1] == '.' and not lines[y + 1][x1 + 1].isdigit():
                return True

        if y - 1 >= 0 and not lines[y - 1][x1] == '.' and not lines[y - 1][x1].isdigit():
            return True

        if y + 1 < y_max and not lines[y + 1][x1] == '.' and not lines[y + 1][x1].isdigit():
            return True

        x1 = x1 + 1
    
    return False

for line in lines:
    line = line[:-1]
    x = 0
    while x < x_max:
        if line[x].isdigit():
            x2 = full_num(line, x)
            if check_part(x, x2, y):
                #print(line[x:x2+1])
                sum = sum + int(line[x:x2+1])
            x = x2
        x = x + 1
    y = y + 1

print(sum)
input.close()