"""Faça um programa que leia as notas de uma turma determinando: a média das notas desta turma e o número de alunos reprovados (a nota para reprovação deve ser menor que 70). Complete o código seguinte com a sua solução."""

numero_alunos = int(input('Informe o numero de alunos'))
total_aluno_reprovados = 0
notas_alunos = []

for aluno in range(numero_alunos):
    nota_aluno = float(input(f'Qual a nota do aluno {aluno + 1} '))
    notas_alunos.append(nota_aluno)

    if nota_aluno < 70:
        total_aluno_reprovados += 1

media = sum(notas_alunos) / numero_alunos
print(f'Número de alunos reprovados: {total_aluno_reprovados} alunos. \nA nota média foi: {media}.')
