def mostrar_menu():
    print('--- menu ---')
    print('1 - Ver mensagem ')
    print('2 - Sair')

def mostrar_mensagem():
    print('bem-vindo')

mostrar_menu()

opcao = input('escolha: ')

if opcao == '1':
    mostrar_mensagem()

    if opcao == '0':
        print('encerrado...')
else:
    print('Opção invalida!')