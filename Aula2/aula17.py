"""
Formatando valores com modificadores
:s - Texto (string)
:d - Inteiros (int)
:f - Número de ponto flutuante (float)
:. - (NÚMERO)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s , d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2
print(divisao)
print('{:.2f}'.format(divisao) )
print(f'{divisao:.2f}')

nome = 'Gilberto Neri Godoy'
print(f'{nome:s}')

num_3 = 25
print(f'{num_3:0>10}')
print(f'{num_3:0<10}')
print(f'{num_3:0^10}')
print(f'{num_3:0.2f}')

nome1 ='Gilberto Neri Godoy'
#nome_formatado = '{:@>35}'.format(nome1)
nome_formatado = '{n:!>35}'.format(n=nome1)
print(nome_formatado)

nome2 = 'Neri Godoy'
print(nome2.lower())# tudo minusculo
print(nome2.upper())# tudo maiusculo
print(nome2.title())# primeiras letras maiusculo