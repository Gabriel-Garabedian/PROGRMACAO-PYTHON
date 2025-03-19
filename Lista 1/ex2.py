#Solicite um valor em segundos e converta para dias, horas e minutos. 
# dia = 86400 segundos
# hora = 3600 segundos
# minuto = 60 segundos
segundos = int(input("Digite um valor em segundos: "))

#converter segundos em dias
dias = segundos // 86400

print(f"são esse tanto de dias: {dias}")

#converter sengundos em horas
horas = segundos // 3600

print(f"são esse tanto de horas: {horas}")

#converter segundos em minutos
minutos = segundos // 60
print(f"são esse tanto de minutos: {minutos}") 