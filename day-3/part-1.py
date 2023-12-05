with open('puzzle-input.txt', 'r') as file:

    lines = [line.strip() for line in file.readlines()]
    

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['*','$','#','=','-','/','%','@','&','+']
number = ''
validnumbers = []
skipcount = 0

for linecount in range(len(lines)):

    for charcount in range(len(lines[linecount])):

        if skipcount > 0:
            continue

        if lines[linecount][charcount] in numbers:

            number += lines[linecount][charcount]
            number += lines[linecount][charcount + 1]
            skipcount += 1

            if lines[linecount][charcount + 2] in numbers:
                number += lines[linecount][charcount + 2]
                skipcount += 1
            

        if lines[linecount][charcount - 1] in symbols:
            validnumbers.append(int(number))
        elif lines[linecount][charcount + len(number)]:
            validnumbers.append(int(number))