def printdiferente(txt):
    """
    função que recebe uma string e fica em == ==
    """
    print('='*30)
    print(txt)
    print('='*30)


def adicionar(lista):
    """
    função criada para adicionar cadastros ela recebe uma lista como parametro
    e é adicionado dentro dessa lista um dicionario
    """
    while True:
        dic = {}
        dic['nome'] = str(input('nome: ')).strip().lower()
        dic['idade'] = int(input('idade: '))
        dic['cpf'] = int(input('cpf: '))
        lista.append(dic)
        print(f'cadastro foi adicionado com sucesso!')

        opcao = str(input('Deseja adicionar outro cadastro?[s-sim][n-não] ')).strip().lower()[0]

        if opcao == 'n':
            break

def remover(lista):
    """
    função criada para remover cadastro em uma lista, ela recebe uma lista como parametro é o cadastro
    é removido caso o nome digitado seja igual ao nome cadastrodo.
    """
    while True:
        if not lista:
            print('nenhum cadastro foi inserido')
        else:
            nome_remover = str(input('digite o nome que deseja remover: ')).strip().lower()
            removido = False
            for c in lista:
                if c['nome'] == nome_remover:
                    removido = True
                    lista.remove(c)
                    print('cadastro removido com sucesso')

            if not removido:
                print('nome que você digitou não foi encontrado, tente novamente!')

        opcao = str(input('Deseja remover outro cadastro?[s-sim][n-não] ')).strip().lower()[0]

        if opcao == 'n':
            break

def exibir(lista):
    """
    função criada para exibir os itens em uma lista, ela recebe uma lista como parametro e o nomes
    são exibidos, caso nao haja nenhum cadastro aparece a mensagem
    """
    if not lista:
        print('nenhum cadastro foi inserido')
    else:
        for c in lista:
            print(f'nome:{c["nome"]}')
            print(f'idade:{c["idade"]}')
            print(f'cpf: {c["cpf"]}')
            print('='*30)

def editar(lista):
    """
    função criada para editar algum cadastro dentro da lista, caso nao tem nenhum cadastro na lista
    aparece a mensagem "nenhum cadastro foi inserido".
    """
    while True:
        if not lista:
            print('nenhum cadastro foi inserido')
        else:
            nome_editar = str(input('digite o nome do cadastro que deseja editar: ')).strip().lower()
            editado = False
            for c in lista:
                if c['nome'] == nome_editar:
                    editado = True
                    print('cadastro encontrado!')
                    printdiferente('MENU EDITAR')
                    print('1-modificar nome')
                    print('2-modificar idade')
                    print('3-modificar cpf')
                    print('4-Sair')

                    try:
                        opcao = int(input('digite a opção que deseja'))
                    except ValueError:
                        print('o valor que você digitou não está entre 1 e 4')
                        continue

                    if opcao == 1:
                        nome_novo = str(input('digite o novo nome: ')).strip().lower()
                        c['nome'] = nome_novo

                    elif opcao == 2:
                        nova_idade = int(input('digite a nova idade: '))
                        c['idade'] = nova_idade

                    elif opcao == 3:
                        novo_cpf = int(input('digite a seu novo cpf: '))
                        c['cpf'] = novo_cpf

                    elif opcao == 4:
                        break

                    else:
                        print('o numero que você digitou não foi identificado')

            if not editado:
                print('o nome que você digitou não foi encotrado tente novamente')

        opcao = str(input('Deseja editar outro cadastro?[s-sim][n-não] ')).strip().lower()[0]

        if opcao == 'n':
            break
