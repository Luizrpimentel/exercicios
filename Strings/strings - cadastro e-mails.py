"""1. Cadastro de e-mails
A empresa " X " sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido, verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:
liragmail.com NÃO é um e-mail válido
lira@gmail NÃO é um e-mail válido
lira@gmail.com é um e-mail válido
Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido
Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string. """

nome = input('Digite seu nome')
email = input('Digite seu email')

if nome and email:
    posição_a = email.find('@')
    servidor = email[posição_a:]
    if posição_a != -1 and '.' in servidor:
        print('cadastro concluido')
    else:
        print('Digite seu email corretamente')