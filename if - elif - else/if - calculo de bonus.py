"""1. Cálculo de bônus com uma nova regra
Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:
A meta é 1000 vendas
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:
Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.
Use as mesmas variáveis de vendas_funcionários"""
funcionario1 = float(input('Digite o valor da meta do funcionario 1'))
funcionario2 = float(input('Digite o valor da meta do funcionario 2'))
funcionario3 = float(input('Digite o valor da meta do funcionario 2'))
meta = 1000
if funcionario1 >= 2000:
    bonus = 0.15 * funcionario1
    print('recebeu {} de bonus'.format(bonus))
elif funcionario1 >= meta:
    bonus = 0.10 * funcionario1
    print('recebeu {} de bonus'.format(bonus))
else:
    bonus = 0
    print('recebeu {} de bonus'.format(bonus))

if funcionario2 >= 2000:
    bonus = 0.15 * funcionario2
    print('recebeu {} de bonus'.format(bonus))
elif funcionario2 >= meta:
    bonus = 0.10 * funcionario2
    print('recebeu {} de bonus'.format(bonus))
else:
    bonus = 0
    print('recebeu {} de bonus'.format(bonus))

if funcionario3 >= 2000:
    bonus = 0.15 * funcionario3
    print('recebeu {} de bonus'.format(bonus))
elif funcionario3 >= meta:
    bonus = 0.10 * funcionario3
    print('recebeu {} de bonus'.format(bonus))
else:
    bonus = 0
    print('recebeu {} de bonus'.format(bonus))
