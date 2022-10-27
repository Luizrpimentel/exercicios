""" 1-Faça um programa que leia as notas de uma turma determinando: a maior nota e o número de alunos aprovados (a nota para aprovação deve ser maior ou igual a 70). Complete o código seguinte com a sua solução."""

numero_alunos = int(input('Informe o numero de alunos'))
total_aluno_aprovados = 0
maior_nota = 0

for aluno in range(numero_alunos):
    nota_aluno = float(input(f'Qual a nota do aluno {aluno + 1} '))

    if nota_aluno > maior_nota:
        maior_nota = nota_aluno

    if nota_aluno >= 70:
        total_aluno_aprovados += 1

print(f'Número de alunos aprovados: {total_aluno_aprovados} alunos. \nA maior nota foi: {maior_nota} pontos.')

