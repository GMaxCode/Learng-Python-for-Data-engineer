# aprendendo usar o for para acessar dados em Dicionarios ou listas.


chocolate = {'produto': 'chocolate',
            'preco': 2.50,
            'quantidade': 20,
            'custo': 1.20
              }

pao = {'produto': 'pao',
      'preco': 6.50,
      'quantidade': 20,
      'custo': 4.20
        }

produtos = [chocolate,pao]

faturamento = chocolate['preco'] * chocolate['quantidade']


for produto in produtos:
    print(f'produto: {produto["produto"]} - preço: {produto["preco"]}')

for produto in produtos:
    faturamento = produto['preco'] * produto['quantidade']
    custo_total = produto['custo'] * produto['quantidade']
    lucro = faturamento - custo_total
    
    print(f'produto: {produto["produto"]}')
    print(f'seu faturamento: {faturamento:.2f}')
    print(f'seu custo total: {custo_total:.2f}')
    print(f'seu lucro: {lucro:.2f}')   