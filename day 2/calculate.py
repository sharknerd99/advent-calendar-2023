input = open('input.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    colon = line.find(':')
    games = line[colon + 1:-1].replace(" ", "").split(';')
    possible = True

    for game in games:
        colours = game.split(',')
        total = 0

        for colour in colours:
            if 'red' in colour and possible:
                if int(colour[:-3]) > 12:
                    possible = False
                    break
                total = total + int(colour[:-3])
            elif 'green' in colour and possible:
                if int(colour[:-5]) > 13:
                    possible = False
                    break 
                total = total + int(colour[:-5])
            elif 'blue' in colour and possible:
                if int(colour[:-4]) > 14:
                    possible = False
                    break 
                total = total + int(colour[:-4])
            else:
                possible = False
                break

        if total > 39:
            possible = False
            break

    if possible:
        sum = sum + int(line[5:colon])

input.close()
print(sum)
