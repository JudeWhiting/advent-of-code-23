answer = 0

with open('puzzle-input.txt', 'r') as file:
    
    lines = file.readlines()



for i in range(len(lines)):

    line = lines[i].replace(';', ',').replace(':', ',').split(',')
    biggest_red = 1
    biggest_green = 1
    biggest_blue = 1

    
    for x in range(1, len(line)):
        print(line[x])
        if 'red' in line[x] and biggest_red < int(line[x].split(' ')[1]):
            biggest_red = int(line[x].split(' ')[1])
        elif 'green' in line[x] and biggest_green < int(line[x].split(' ')[1]):
            biggest_green = int(line[x].split(' ')[1])
        elif 'blue' in line[x] and biggest_blue < int(line[x].split(' ')[1]):
            biggest_blue = int(line[x].split(' ')[1])

    answer += biggest_red * biggest_green * biggest_blue

    

print(answer)