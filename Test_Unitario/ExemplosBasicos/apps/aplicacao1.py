
def conversao_para_celsius(temperatura):
    return 5 * ((temperatura-32)/9)

def conversão_para_fahrenheit(temperatura):
    return temperatura * (9/5)+32

if __name__=='__main__':
    
    opcao= int(input('Digite 1 para converter de Fahrenheit para celsius \n'
                     'Digite 1 para converter de Fahrenheit para celsius:'))

    temperatura = float(input('Informe a temperatura em Fahrenheit: '))
    
    match (opcao):
        case 1:
            temp_convertida = conversao_para_celsius(temperatura)
            print(f'A temperatura fornecida em celsius é {temp_convertida}')
            
        case 2:
             temp_convertida = conversao_para_celsius(temperatura)
             print(f'A temperatura fornecida em Fahrenheit é {temp_convertida}') 
        case _:
            print('Escolha errada')
            
    

    
