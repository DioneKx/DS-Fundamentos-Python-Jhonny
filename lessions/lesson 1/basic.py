numero = int(input("Informe um número: ")) # O input de python sempre retorna em string, por isso, quando se trata de numero, faça a conversão
numero2 = float(input("Informe um número: ")) # O tipo que tem maior quantidade de dados p/armazenar prevalece ao efetuar uma equação
soma = numero + numero2 # Caso não tivesse convertido, essa var estaria concatenando as outras duas
vt = "Valor Total"

print(type(soma)) # type retorna o tipo da var dentro dos () 
print(vt, "da soma", soma) # Para concatenar, por exemplo, em print, utilize "," após as aspas do texto ou a var (Pode-se usar tambem "+", porém deve converter os numeros para String)