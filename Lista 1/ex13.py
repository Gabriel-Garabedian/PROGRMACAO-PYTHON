#. Dado um salário inicial e um aumento percentual que dobra a cada ano, calcule o salário atual após vários anos.
salraio_inicial = float(input("Digite o salário inicial: "))
anos_trabalhados = int(input("Digite a quantidade de anos trabalhados: "))

salario_atual = salraio_inicial * (2 ** anos_trabalhados)

print(f"O salário atual é: {salario_atual}.")