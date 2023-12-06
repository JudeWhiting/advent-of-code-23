with open('puzzle-input.txt', 'r') as file:

    lines = file.readlines()
    #lines = [line.strip() for line in file.readlines()]
    
text = []

for line in lines:
    text += line.replace('\n','N')
text += 'N'



numbers = ['0','1','2','3','4','5','6','7','8','9']
check = numbers + ['.','N']
symbols = set()
valid_numbers = []
line_length = 141



for char in text:
    if char not in check:
        symbols.add(char)
symbols = list(symbols)



def check_for_numbers(text, numbers, i):
    valid_numbers = []

    if text[i + 1] in numbers:

        if text[i + 3] in numbers:
            valid_numbers += [text[i+1] + text[i+2] + text[i+3]]
        else:
            valid_numbers += [text[i+1] + text[i+2]]

    return valid_numbers



for i in range(len(text)):


    if text[i] in symbols:


        if text[i + 1] in numbers:

            if text[i + 3] in numbers:
                valid_numbers += [text[i+1] + text[i+2] + text[i+3]]
                text[i+1] = 'N'
                text[i+2] = 'N'
                text[i+3] = 'N'
            else:
                valid_numbers += [text[i+1] + text[i+2]]
                text[i+1] = 'N'
                text[i+2] = 'N'


        if text[i - 1] in numbers:

            if text[i - 3] in numbers:
                valid_numbers += [text[i-3] + text[i-2] + text[i-1]]
                text[i-3] = 'N'
                text[i-2] = 'N'
                text[i-1] = 'N'
            else:
                valid_numbers += [text[i-2] + text[i-1]]
                text[i-2] = 'N'
                text[i-1] = 'N'

        


print(valid_numbers)
