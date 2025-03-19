
dicionario = {}


def adicionar_item():
    item = input('Digite o item que deseja adicionar: ').lower().strip()
    qtd = int(input(f'Digite a quantidade de {item}: '))
    if item in dicionario:
        print('Esse item já existe')
    else:
        dicionario[item] = qtd
        print(f'Item: {item} adicionado! Quantidade do item: {qtd}')
    
def remover_item():
    item_removido = input('Digite o item que deseja remover: ').lower().strip()
    if item_removido in dicionario:
        del dicionario[item_removido]
        print(f'Item: {item_removido} foi removido!')
    else:
        print('Item não existe no estoque')

def exibir_estoque():
    if not dicionario:
        print('Estoque vazio!')
    else:
        print('Itens em estoque:')
        for item, qtd in dicionario.items():
            print(f'{item}: {qtd} Unidades ')

while True:

    try:
        opcoes = int(input('Escolha um opção:\n '
        '1 - Adicionar item \n '
        '2 - Remover item \n '
        '3 - Exibir estoque\n '
        '4 - Sair\n'))

        if opcoes == 1:
            adicionar_item()
        elif opcoes == 2:
            remover_item()
        elif opcoes == 3:
            exibir_estoque()
        elif opcoes == 4:
            break
        else:
            print('Digite uma opção válida!')
        
    except ValueError:
        print('Digite uma opção válida!')




        


