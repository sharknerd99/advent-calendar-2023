def checkFirst(line):
    index = 9999
    count = 1
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digit = '0'

    for num in nums:
        ind1 = line.find(num)
        ind2 = line.find(str(count))

        if ind1 != -1 and ind1 < index:
            index = ind1
            digit = str(count)

        if ind2 != -1 and ind2 < index:
            index = ind2
            digit = str(count)

        count = count + 1

    return digit

def checkLast(line):
    index = -9999
    count = 1
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digit = '0'
    
    for num in nums:
        ind1 = line.rfind(num)
        ind2 = line.rfind(str(count))
        
        if ind1 != -1 and ind1 > index:
            index = ind1
            digit = str(count)
        
        if ind2 != -1 and ind2 > index:
            index = ind2
            digit = str(count)
        
        count = count + 1
    
    return digit

input = open('input.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    first = checkFirst(line)
    last = checkLast(line)

    sum = sum + int(first + last)

input.close()
print(sum)
