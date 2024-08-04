nameP = str(input("Digite seu nome: "))
valorP = float(input("Digite quanto pesa (00.00): "))
valorA = float(input("Digite sua altura (00.00): "))

valorImc = valorP / (valorA ** 2)

def imc():
    if valorImc <= 18.5:
        classification = "Abaixo do peso padrão."
    elif valorImc > 18.5 and valorImc < 25:
        classification = "Peso ideal (Parábens)."
    elif valorImc >= 25 and valorImc < 30:
        classification = "Levemento acima do peso padrão."
    elif valorImc >= 30 and valorImc < 35:
        classification = "Obesidade grau I."
    elif valorImc >= 35 and valorImc <= 40:
        classification = "Obesidade grau II (Severa)."
    else:
        classification = "Obesidade grau III (Mórbida)."
    
    return classification

print("%s pesa %.2f, com altura de %.2fm, totalizando um imc de: %.2f, sendo classificado em: %s" % (nameP, valorP, valorA, valorImc, imc()))
    