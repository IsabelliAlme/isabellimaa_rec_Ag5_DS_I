print("===================================")
print("   CALCULADORA DE CONSUMO ELÉTRICO")
print("===================================")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000
# Valor estimado da energia elétrica
valor_kwh = 0.75
custo_mensal = consumo_mensal * valor_kwh

print("\n---------- RESULTADO ----------")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")
print("-------------------------------")
print("💡 Dica: economizar energia também ajuda o meio ambiente! desligue enquanto dorme!")