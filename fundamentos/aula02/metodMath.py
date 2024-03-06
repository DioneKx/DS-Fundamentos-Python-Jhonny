import math

valorInt = int(input("Digite um Valor (Inteiro): "))
valorOther= int(input("Digite um outro Valor (Inteiro): "))

# print ('Raiz quadrada de 49:', math.sqrt(49))
# print ('Cosseno de 180 graus:', math.cos(180))
# print ('Seno de 360 graus:', math.sin(360))
# print ('Tangente de 180 graus:', math.tan(180))
# print ('Angulo de 90 graus:', math.radians(90), 'radianos')
# print ('PI:', math.pi)
# print ('Hipotenusa de 4 e 8:', math.hypot(4, 8))
# print ('Arredonda o valor para cima de de 5.854:', math.ceil(5.854))

print ('Raiz quadrada de', valorInt,':', math.sqrt(valorInt))
print ('Cosseno de', valorInt, 'graus:', math.cos(valorInt))
print ('Seno de', valorInt, 'graus:', math.sin(valorInt))
print ('Tangente de', valorInt, 'graus:', math.tan(valorInt))
print ('Angulo de', valorInt, 'graus:', math.radians(valorInt), 'radianos')
print ('PI:', math.pi)
print ('Hipotenusa de', valorInt, 'e', valorOther, ':', math.hypot(valorInt, valorOther))

valorFloat = float(input("Digite um Valor Quebrado: "))
print ('Arredonda o valor para cima de', valorFloat,':', math.ceil(valorFloat))