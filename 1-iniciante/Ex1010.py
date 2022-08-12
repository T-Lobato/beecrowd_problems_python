#  Entrada
codPeca1, qtdPecas1, valorPeca1 = input().split(" ")
codPeca2, qtdPecas2, valorPeca2 = input().split(" ")

#  Processamento & Saída
qtdPecas1 = int(qtdPecas1)
qtdPecas2 = int(qtdPecas2)
valorPeca1 = float(valorPeca1)
valorPeca2 = float(valorPeca2)

print(f'VALOR A PAGAR: R$ {(qtdPecas1 * valorPeca1) + (qtdPecas2 * valorPeca2):.2f}')