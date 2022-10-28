"""Exemplo:
Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.
Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:
A) Qual foi o faturamento de IPhone no dia 20/08/2020?
B) Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?
"""
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]
produto_mais_vendido = ''
qtde_produto_mais_vendido = 0

for item in vendas:
    data, produto, cor, armazenamento, unidades, valor = item

    if produto == 'iphone x' and data == '20/08/2020':
        faturamento = 0
        faturamento += unidades * valor

    if unidades > qtde_produto_mais_vendido and data == '21/08/2020':
        produto_mais_vendido = produto
        qtde_produto_mais_vendido = unidades

print(f'O faturamento foi de: {faturamento}. \n'
      f'O produto mais vendido foi {produto_mais_vendido}')
