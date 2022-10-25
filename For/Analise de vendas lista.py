"""1. Análise de Vendas
Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam."""
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
for item in vendas:
    if item[1] >= meta:
        print('vendedor {} bateu a mata.Fez R$ {} em vendas.'.format(item[0], item [1]))

"""2. Calculando % de uma lista. Faremos algo parecido com "filtrar" uma lista.
Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta.
Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta."""

acima_meta = 0
for venda in vendas:
    if venda[1] >= meta:
        acima_meta += 1
print('{:.1%} dos vendedores bateram a meta'.format(acima_meta/len(vendas)))

#Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?

maior_vendas = 0
melhor_vendedor = ''

for venda in vendas:
    if venda [1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]
print('O melhor vendedor foi {}, com {} vendas'.format(melhor_vendedor,maior_vendas))