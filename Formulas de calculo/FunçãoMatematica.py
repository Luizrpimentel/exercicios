import FormulasDeCalculo as fc


base = float(input('Digite base'))
altura = float(input('Digite altura'))

area = fc.area_triangulo(base,altura)
print('area é: {}'.format(area))

a = float(input('Digite um valor'))
b = float(input('Digite um valor'))
c = float(input('Digite um valor'))

perimetro = fc.perimetro_triangulo(a, b, c)
print('O perimetro do triangulo é: {}'.format(perimetro))