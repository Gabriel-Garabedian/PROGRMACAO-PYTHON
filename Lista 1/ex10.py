#Solicite um número inteiro maior que 1 e verifique se ele é primo. 

n = int(input("Digite um número inteiro: "))

if n <=1:
    print("O número digitado não é maior que 1.")
#verifica se o numero é primo
else:
    primo = True
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break