"""
OPERADORES RELACIONAIS

== { ESTÁ PERGUNTANDO SE SÃO IGUAIS
!= { SE É DIFERENTE
"""

var_1 = 'Luiz'
var_2 = 'Otávio'

expressão = (var_1 == var_2)

print(expressão)

nome= input('Qual é o seu nome')
idade= input('Qual é a sua idade ?')

idade = int(idade)
# limite par pegar empréstimo

idade_limite= 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} Não pode pegar empréstimo. ')

# limite par pegar empréstimo

idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade_maior <= idade:
    print(f'{nome} pode está autorizado a pegar o empréstimo. ')
else:
    print(f'{nome} Não poderá pegar empréstimo. ')



