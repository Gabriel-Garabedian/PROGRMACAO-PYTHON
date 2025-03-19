#. Peça ao usuário a quantidade de turmas e a quantidade total de alunos. Informe a média de alunos por turma, mas avise se alguma turma tiver mais de 40 alunos. 

turmas = int(input("Digite a quantidade de turmas: "))

alunos_turma = []
for i in range(turmas):
    alunos = int(input(f"Digite a quantidade de alunos da turma {i + 1}: "))
    if alunos > 40:
        print(f"A turma {i + 1} tem mais de 40 alunos.")
    alunos_turma.append(alunos) 

#calcular a média de alunos por turma
media = sum(alunos_turma)/turmas
print(f"A média de alunos por turma é {media}.") 