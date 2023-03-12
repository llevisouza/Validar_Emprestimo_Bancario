
print('-'*90)
# Obtém um valor numérico do usuário com a mensagem de entrada fornecida
def obter_valor_numerico(mensagem):
    while True:
        try: 
            valor_input = input(mensagem)
            valor = float(valor_input)
            return valor
        except ValueError:
            print('Por Favor, insira um número valido.')
# Obtém um valor inteiro positivo do usuário com a mensagem de entrada fornecida
def obter_inteiro_positivo(mensagem):
    while True:
        try:
            valor_input = input(mensagem)
            valor = int(valor_input)
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print('Por Favor, insira um número inteiro positivo.')
# Realiza a conversão do pagamento de anos para meses
def calculo_pagamento_em_meses (prazo_pagamento_anos):
    return prazo_pagamento_anos * 12


#Verificação de erros na entrada do valor casa
valor_casa = None
while valor_casa is None or valor_casa <= 0:
    valor_casa_input = input('Digite o valor da casa: ')
    try:
        valor_casa = float(valor_casa_input)
        if valor_casa <0:
            print('O valor da casa deve ser positivo.')
    except ValueError:
        print('Por favor, insira um valor numérico válido.')
#Verificação de erros na entrada do valor do salario


salario = obter_valor_numerico('Insira o seu salario: ')

 
#Verificação de erros na entrada do prazo de pagamento       
prazo_pagamento_anos = obter_inteiro_positivo('Digite o prazo de pagamento em anos: ')
prazo_pagamento_em_meses = prazo_pagamento_anos * 12
percentual_salario = 0.3 * salario
print('-'*90)
print('Limite de 30% do salario:')
print('O limite para as parcelas é de 30% do salário. Essa é uma convenção comum,\n mas pode variar de acordo com o banco ou instituição financeira.')

# informações de prazo de pagamento
print('-'*90)
print('Prazo de pagamento e parcelas selecionados:')
print(f"Prazo de pagamento: {prazo_pagamento_em_meses} meses")
    
valor_parcelas = valor_casa / prazo_pagamento_em_meses
print(f"Valor das parcelas: R${valor_parcelas:.2f}")

print('-'*90)
print('Resultado:')
# condições
def verificar_aprovacao_emprestimo(valor_parcelas, percentual_salario):
    if valor_parcelas > percentual_salario:
        print("Empréstimo negado.")
        print(f"O valor das parcelas é R${valor_parcelas:.2f}")
        print(f"Isso representa mais de 30% do seu salário, que é R${percentual_salario:.2f}")
    else:
        print("Empréstimo aprovado.")

verificar_aprovacao_emprestimo(valor_parcelas, percentual_salario)
print('Muito obrigado por utilizar o nosso programa!')


