nCandidatos = int(input('Informe o número de candidatos participantes: '))
candidatos = []
cedula = []

verification = False
wait = []


for n in range (nCandidatos):
    temp = str(input("Informe o nome do candidato: "))
    candidatos.append(temp)
    cedula.append(int(0))

print(candidatos)
    
totalVotos = int(input("Informe o número total de votos (Válidos) a serem contados: "))

while totalVotos > 0:
    temp = str(input("Informe o nome do candidato escolhido: "))
    verify = False
    
    for n in range(nCandidatos):
        if temp == candidatos[n]:
            print("Voto considerado válido.")
            cedula[n] += 1
            totalVotos -= 1
            verify = True
            break
        
    if verify == False:
        print('Voto considerado invalido. Refaça a votação e...')


for n in range(nCandidatos):
    msg = f"{candidatos[n]} recebeu: {cedula[n]} votos."
    print(msg)
    
    
maximum = max(cedula)
while verification == False:
    try:
        y = cedula.index(maximum)
        cedula[y] = 0
        wait.append(y)
    except:
       verification = True

print(wait)

if len(wait) == 1:
    print(f"O vencedor é {candidatos[wait[0]]}")
elif len(wait) > 1:
    msg = "Empate entre os candidatos:"
    for n in range(len(wait)):
        msg += f" {candidatos[wait[n]]},"
    print(f"{msg} cada um com o total de {maximum} de pontos")
            