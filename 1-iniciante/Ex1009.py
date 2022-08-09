#  Entrada
nomeVendedor = input()
salarioFixo = float(input())
totalVendas = float(input())

#  Processamento
salario = salarioFixo + totalVendas * 0.15 

#  Saída
print(f'TOTAL = R$ {salario:.2f}')