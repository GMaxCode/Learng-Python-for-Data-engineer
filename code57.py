# trabalhando com Dicionarios e Listas

# listas >> [0,2,3,4,5,6]

precos = ['3.50','6.00','2.30','5.33']

# Dicionários >> CHAVE and VALOR, Para acessar algum valor do dicionario basta usar ['nome da chave']

chocolate = {'produto': 'chocolate',
            'preco': 2.50,
            'quantidade': 20,
            'custo': 1.20
              }

pao = {'produto': 'pao',
      'preco': 6.50,
      'quantidade': 20,
      'custo': 1.20
        }

produtos = [chocolate,pao]

for pao in produtos:
    print(pao['produto'])
    print(pao['preco'])

faturamento = chocolate['quantidade'] * chocolate['preco']
custo_total = chocolate['custo'] * chocolate['quantidade']
lucro = faturamento - custo_total

# print(produtos[0]['preco'])
print(f'seu FAT: {faturamento:.2f}')
print(f'seu CUST_TOT: {custo_total:.2f}')
print(f'seu LUCRO: {lucro:.2f}')