with open('puzzle-input.txt', 'r') as file:
    lines = file.readlines()
    
answer = 0

for line in lines:
        
    for char in line:
            try:
                digit1 = int(char)
                break
            except:
                pass
    for char in reversed(line):
            try:
                digit2 = int(char)
                break
            except:
                pass
              
    answer += digit1 * 10 + digit2
    
print(answer)


