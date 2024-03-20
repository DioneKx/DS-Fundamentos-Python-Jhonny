qntd = int(input("Digite a quantia de numeros p/determinar m: "))
result = 0

for i in range(0, qntd, +1):
    result += int(input("Digite um número para a média: "))
    
print("Sua média: %.2f" % ((result / qntd)))
    