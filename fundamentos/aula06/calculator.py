nTotal = int(input("Informe o total de números a serem considerados na expressão: "))

while nTotal <= 1:
    nTotal = int(input("Informe o total de númeroS a serem considerados na expressão: "))

global numbers #definindo uma variavel como global (Vinculada ao nome inserido)
numbers = []
expression = str(input("Informe a expressão correspondente ( + || - || * || / ): "))

for n in range(nTotal):
    numbers.append(float(input("Informe o número a ser considerado na expressão: ")))

def addition():
    temp = 0
    for n in range(nTotal):
        temp += numbers[n]
        
    return temp

def subtraction():
    temp = 0
    for n in range(nTotal):
        if temp == 0:
            temp = numbers[n]
        else:
            temp -= numbers[n]
            
    return temp

def multiplication():
    temp = 1
    for n in range(nTotal):
        temp = temp * numbers[n]
        
    return temp

def division():
    temp = 0
    for n in range(nTotal):
        if temp == 0:
            temp = numbers[n]
        else:
            temp = temp / numbers[n]
        
    return temp

if expression == "+":
    res = addition()
elif expression == "-":
    res = subtraction()
elif expression == "*":
    res = multiplication()
elif expression == "/":
    res = division()
else:
    print("Expressão inválida")

print("%.1f" % res)
