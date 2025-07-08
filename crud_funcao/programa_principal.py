cadastro = []
from modulo import printdiferente, adicionar, remover, exibir, editar
while True:
    printdiferente('MENU PRINCIPAL')
    print('1-Adicionar cadastro')
    print('2-Remover cadastro')
    print('3-Exibir cadastro')
    print('4-Atualizar cadastro')
    print('5-Sair')

    try:  # verifica se o que o usuário digitou é um numero inteiro, coso não seja cai no except valor errado
        # aparece a mensagem exbindo que o numero está errado, e o continue faz com que o ele fique nesse looping
        # até digitar o um número inteiro.
        menu = int(input('digite a opção que deseja: '))
    except ValueError:
        print('O número que você digitou não está entre 1 e 5, tente novamente!')
        continue

    if menu == 1:
        adicionar(cadastro)

    elif menu == 2:
        remover(cadastro)

    elif menu == 3:
        exibir(cadastro)

    elif menu == 4:
        editar(cadastro)

    elif menu == 5:
        printdiferente('MUITO OBRIGADO!')
        break

    else:
        print('o número que você digitou não está entre 1 e 5, tente novamente!')


