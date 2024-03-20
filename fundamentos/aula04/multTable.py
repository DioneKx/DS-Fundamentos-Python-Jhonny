# names = ["Larissa", "Lulinha", "Amenic", "Gustavo", "Henri", "Enzo"]

# for i in range(10): #Syntax Default do for em python (Define o i como 0 e adiciona o incremento de forma automática)
#     print(i)
    
# for i in range(10,0,-1): #Syntax do for: for <var> in range(<N. da var>, <Limite>, <Incremento || Decremento>): <Conteúdo>
#     print(i)

# for n in names: #O for pega o tamanho do array e passa por cd index, transferindo o conteudo pra var (Basicamente um ForEach)
#     print(n)
    
number = int(input("Digite um número (INT): "))
operation = input("Digite (Apenas) o sinal de uma operação(*, /, +, -): ")

for n in range(1, 11, +1):
    if operation == "/":
        print(f"Divisão ({number} / {n}): " + str(number / n))
    if operation == "*":
        print(f"Multiplicação ({number} * {n}): " + str(number * n))
    if operation == "-":
        print(f"Subtração ({number} - {n}): " + str(number - n))
    if operation == "+":
        print(f"Soma ({number} + {n}): " + str(number + n))