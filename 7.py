'''
7) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e
escrever o valor correspondente em graus Celsius baseado na seguinte fórmula: C
= 5 * ((F-32) / 9)
'''

fahr = float(input("Digite a temperatura em graus Fahrenheit? "))

celcius = 5 * ((fahr-32) / 9)

print("A temperatura",fahr, "convertida para graus Celsius é:", round(celcius,2))


