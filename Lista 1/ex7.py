#Solicite um número ímpar ao usuário e calcule a diferença entre o quadrado do número anterior e do próximo número ímpar. 

n = int(input("Digite um número ímpar: "))

#verificar se o numero é impar

if n % 2 == 0:
    print("O número digitado não é ímpar.")

else:
    n_anterior = n - 2
    n_proximo = n + 2
#caucular os quadrados
    quadrado_anterior = n_anterior ** 2
    quadrado_proximo = n_proximo ** 2
#calcular a diferença
    diferenca = quadrado_proximo - quadrado_anterior
    print(f"A diferença entre o quadrado do número anterior e do próximo número ímpar é: {diferenca}")