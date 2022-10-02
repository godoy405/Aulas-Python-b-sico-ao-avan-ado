usuario = input('Nome do usuário: ')
senha = input('Senha do usuário:')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado')
else:
    print('Senha ou usário inválidos')