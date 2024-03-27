qntd = int(input("Digite a quantia de numeros p/determinar m: "))
result = 0
nwhile = 1

while nwhile <= qntd:
    result += int(input("Digite um número para a média: "))
    nwhile += 1
    
print("Sua média: %.2f" % ((result / qntd)))
    