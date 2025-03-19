#Peça ao usuário três notas e calcule: 
#a. A média aritmética simples 
#b. A média ponderada considerando os pesos 2, 2 e 3 
#c. A média ponderada considerando os pesos 1, 2 e 2 

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

#Calcula a média aritmética simples
media_aritmetica = (nota1 + nota2 + nota3) / 3

#Calcula a média ponderada considerando os pesos 2, 2 e 3

media_ponderada1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / 7

#Calcula a média ponderada considerando os pesos 1, 2 e 2

media_ponderada2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / 5

#exibir resultados

print("A média aritmética simples é: ", media_aritmetica)
print(f"Média ponderada (pesos 2, 2, 3): {media_ponderada1:.2f}")
print(f"Média ponderada (pesos 1, 2, 2): {media_ponderada2:.2f}")