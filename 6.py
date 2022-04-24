'''
6) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a
porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o
custo final ao consumidor.
'''

custoCarro = float(input("Qual o valor de custo do carro? "))
distribuidor = custoCarro * (28/100)
imposto = custoCarro * (45/100)

precoFinal = custoCarro + distribuidor + imposto

print("O valor final do veiculo é de R$:",precoFinal)