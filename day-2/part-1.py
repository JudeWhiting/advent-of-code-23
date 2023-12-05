
answer = 0

with open('puzzle-input.txt', 'r') as file:
    
    lines = file.readlines()


for i in range(len(lines)):

    line = lines[i].replace(';', ',').replace(':', ',').split(',')
    game_number = int(line[0].replace('Game ', ''))

    
    for x in range(1, len(line)):
        if 'red' in line[x] and int(line[x].split(' ')[1]) > 12:
            game_number = 0
        elif 'green' in line[x] and int(line[x].split(' ')[1]) > 13:
            game_number = 0
        elif 'blue' in line[x] and int(line[x].split(' ')[1]) > 14:
            game_number = 0

    answer += game_number

    

print(answer)
