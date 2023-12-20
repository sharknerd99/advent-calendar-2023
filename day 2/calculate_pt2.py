input = open('input.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    colon = line.find(':')
    games = line[colon + 1:-1].replace(" ", "").split(';')
    min_red = 0
    min_green = 0
    min_blue = 0

    for game in games:
        colours = game.split(',')

        for colour in colours:
            if 'red' in colour:
                if int(colour[:-3]) > min_red:
                    min_red = int(colour[:-3])
            elif 'green' in colour:
                if int(colour[:-5]) > min_green:
                    min_green = int(colour[:-5])
            elif 'blue' in colour:
                if int(colour[:-4]) > min_blue:
                    min_blue = int(colour[:-4])

    sum = sum + (min_red * min_green * min_blue)

input.close()
print(sum)
