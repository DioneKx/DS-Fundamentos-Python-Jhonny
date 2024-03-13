nht = float(input("Digite o número de horas trabalhadas (00.00): "))
vph = float(input("Digite o valor pago por hora: "))

sb = vph * nht

def income(): #Funcão do python
    if sb < 1000.00:
        sl = sb - (sb * 0.05)
    elif sb >= 1000.00 and sb <= 2000.00:
        sl = sb - (sb * 0.10)
    else:
        sl = sb - (sb * 0.15)
    return sl

print("Seu salario (Liquido): %.2f" % (income()))