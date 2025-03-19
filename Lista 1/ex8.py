#Solicite uma temperatura em Celsius e converta para Fahrenheit
#Fórmula ( °C × 9/5) + 32 = °F

temperdatura_celsius = int(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = (temperdatura_celsius * 9/5) + 32

print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f}")