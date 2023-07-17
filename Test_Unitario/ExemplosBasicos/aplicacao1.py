def conversao(temperatura):
    return 5 * ((temperatura-32)/9)


temperatura = float(input('Informe a temperatura em Fahrenheit: '))

celsius = conversao(temperatura)

print(f'A temperatura fornecida em celsius é {celsius}')
