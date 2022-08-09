#  Entrada
numFuncionario = int(input())
horasTrabalhadas = int(input())
valorPorHora = float(input())

#  Processamento
salario = horasTrabalhadas * valorPorHora

#  Saída
print(f'NUMBER = {numFuncionario}')
print(f'SALARY = U$ {salario:.2f}')