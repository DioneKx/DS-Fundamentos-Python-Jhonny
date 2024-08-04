course = "Python" # String (%s)
year = 2024 # Inteiro (%d)
valor = 1500.00 # Float (%f)

msg = f"O curso de {course} possui o valor de R$ {valor}, no ano de {year}"
#É possível criar um texto dessa forma ao utilizar "f" antes da string

# msg = "O curso de " + course + " possui o valor de R$" + str(valor) + ", no ano de " + str(year)
#Para guardar diferentes tipos de variaveis em uma outra var, trasnforme tudo em um unico tipo (String acima)

''' Concatenação com virgula abaixo '''

# print("O curso de", course, "possui o valor de R$", valor, "no ano de ", year)

''' Concatenação utilizando identificadores '''

# print("O curso de %s possui o valor de R$%.2f, no ano de %d" % (course, valor, year))
#Para alterar a qntd de casas decimais do float, segue %.<N>f

''' É necessário escolher os identificadores certos p/determinados tipos de var. '''

print("Tipo da Var:", type(msg), msg)