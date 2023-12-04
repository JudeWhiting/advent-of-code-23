with open('puzzle-input.txt', 'r') as file:
    lines = file.readlines()
    
answer = 0

for i in range(len(lines)):
     lines[i] = lines[i].replace('one', 'o1e')
     lines[i] = lines[i].replace('two','t2o')
     lines[i] = lines[i].replace('three','t3e')
     lines[i] = lines[i].replace('four','f4r')
     lines[i] = lines[i].replace('five','f5e')
     lines[i] = lines[i].replace('six','s6x')
     lines[i] = lines[i].replace('seven','s7n')
     lines[i] = lines[i].replace('eight','e8t')
     lines[i] = lines[i].replace('nine','n9e')
     lines[i] = lines[i].replace('zero','z0o')
    

print(lines[2])

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


