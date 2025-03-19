#Um cliente alugou um carro e rodou alguns quilômetros por um certo número de dias. O custo diário é de R$90. Se ele rodou mais de 100 km, há uma taxa extra de R$12 por km adicional. Calcule o valor total a ser pago. 

dias = int(input("Digite o número de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de km rodados: "))

custo_diario = dias * 90

if km > 100:
    custo_km = (km - 100) * 12
else:
    custo_km = 0

#caucular o valor total

valor_total = custo_diario + custo_km

print(f"O valor total a ser pago é de R${valor_total:.2f}")