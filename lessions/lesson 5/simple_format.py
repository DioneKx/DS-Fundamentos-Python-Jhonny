wordGroup = []
wordInverse = []

for n in range(0, 3, +1):
    temp = str(input("Escreva uma (Única) palavra (Processo repetitivo): "))
    wordGroup.append(temp)
    
print(" ".join(wordGroup), len(wordGroup))

for n in range(0, len(wordGroup), +1):
    temp = wordGroup[n]
    ccount = int(len(temp)) - 1
    inverse = ""
    
    while ccount >= 0:
        inverse += temp[ccount]
        ccount -= 1
    
    
    if temp.lower() == inverse.lower():
        print("A palavra %s continua a mesma ao inverter" % (temp))
        wordInverse.append(inverse.capitalize())
    else:
        print("A palavra %s muda ao inverter" % (temp))
        wordInverse.append(inverse)
        

print(wordInverse)
    
    
