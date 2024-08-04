# Segue lista do "+ leve" pro "+ pesado": 
# 1.constatnes / 2.variavéis / 3.vetores/arrays / 4.matrizes (conjunto de arrays) / 5.dicionário (Var -> outras Var.) / 6.objeto/instância

subTotal = 0
vocal = ["a", "e", "i", "o", "u"]
word = str(input('Escreva uma (Única) palavra: '))

for n in range(0, 4, +1):
    subTotal += word.count(vocal[n])

print("A palavra escrita tem um total de:", len(word), "letras")
print(f"Um total de {subTotal} vocais")