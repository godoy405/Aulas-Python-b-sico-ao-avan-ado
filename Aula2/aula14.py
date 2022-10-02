usuario = input('Digite seu usário: ')

qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa cadastrar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema')

