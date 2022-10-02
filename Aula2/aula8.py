"""
Entrada de dados
"""

nome= input("Qual é o seu nome ? ")
print(f'O usuário digitou {nome} e o tipo da variável é '
        f'{type(nome)}')

print()

nome= input("Qual é o seu nome ? ")
idade= input("Qual a sua idade ? ")

ano_nascimento = 2019 - int(idade)

print ()

print(f'{nome} tem {idade} anos. ')

print()

numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite um número ')
numero_2 = int(numero_2)

print(numero_1 + numero_2)



