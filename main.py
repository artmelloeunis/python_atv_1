import math

idade_dias = int(input("Sua idade em dias: "))

total_anos = str(math.floor(idade_dias / 365))
idade_dias %= 365
total_meses = str(math.floor(idade_dias / 30))
idade_dias %= 30
total_dias = str(math.floor(idade_dias))

print(total_dias + " dia(s), " + total_meses + " mes(es) e " + total_anos + " ano(s).")