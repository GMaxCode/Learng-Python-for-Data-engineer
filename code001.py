# usando váriaveis para guardar dados
# entrada tratamento e saida para reutilizar os dados saidos que foram tratados.

nome = 'joao'
produto = 'chocolate amargo'
quantidade = 40
preco = 2.50
custo = 1.20
custo_total = quantidade * custo
faturamento = quantidade * preco
lucro = faturamento - custo_total

print(f'seu faturamento diario foi: {faturamento:.2f} ')
print(f'seu lucro Total: {lucro:.2f}')
print(f'seu custo total por 40 chocolates: {custo_total:.2f}')