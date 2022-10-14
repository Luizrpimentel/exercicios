"""1. Criando um mini sistema de controle de estoque¶
Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:
alimentos -> Estoque mínimo: 50
bebidas -> Estoque mínimo: 75
limpeza -> Estoque mínimo: 30
Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.
Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"
Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.
Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.
Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.
Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente """

categoria = input ('Qual a categoria do produto ')
produto = input ('Digite o nome do produto ')
qtdestoque = input ('Qual a quantidade em estoque ')

if produto and categoria and qtdestoque:
    qtdestoque = int(qtdestoque)
    if categoria == 'alimentos':
        if qtdestoque < 50:
            print ('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.'.format(produto, qtdestoque))

    elif categoria == 'bebidas':
        if qtdestoque < 75:
           print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.'.format(produto, qtdestoque))
    else :
         if qtdestoque < 30 :
            print ('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.'.format(produto, qtdestoque))

else :
    print('preencha todas informações')