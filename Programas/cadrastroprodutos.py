listaprodutos = []

def cadastra_produto(produto_para_cadastrar: dict):
    listaprodutos.append(produto_para_cadastrar)
    return
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

print('|','__'* 10,'|') 
print('         MENU')
print('|','__'* 10,'|')
print('1 - Cadrastrar um novo produto:')
print('2 - lista dos produtos cadastrado:')
print('3 - Sair')

opcao = valida_int('Digite a opção desejada :', 1, 3)

while opcao == 1:
    produto_novo = {}

    produto_novo['codigo'] = int(input('Digite o código do produto: '))


    if produto_novo['codigo'] == 0:
        print('Código 0, encerrando cadastro de produtos.')
        break

    
    produto_novo['estoque'] = int(input('Digite a quantidade em estoque: '))
    produto_novo['minimo'] = int(input('Digite a quantidade mínima do estoque: '))
    
    cadastra_produto(produto_novo)
    opcao = valida_int('Digite a opção desejada :', 1, 3)
    
while opcao == 2:
    print(listaprodutos)
    break


while opcao == 3:
    print('encerrando o progama')
    break

if len(listaprodutos) > 0:
    print('Lista com os codigos dos produtos:')
    print("Código".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))

    for produto in sorted(listaprodutos, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))
else:
    print('Lista vazia.')