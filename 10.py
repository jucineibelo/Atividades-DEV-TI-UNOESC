'''
10) Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça
um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

'''

valorHora = float(input("Quanto reais você ganha por hora? "))
horasMes = float(input("Quantas horas você trabalhou durante o mês? "))
TotalBruto= valorHora * horasMes
irSobSalario = TotalBruto * (11/100)
inssSobSalario = TotalBruto * (8/100)
sindicatoSobTrabalho = TotalBruto * (5/100)

print(" + Salário Bruto R$:", TotalBruto)
print(" - IR (11%) R$:",irSobSalario)
print(" - INSS (8%) R$:",sindicatoSobTrabalho)
print(" = Salário Liquido R$: ",TotalBruto - irSobSalario - inssSobSalario - sindicatoSobTrabalho)






