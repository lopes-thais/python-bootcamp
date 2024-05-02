# RESOLUÇÃO DO DESAFIO "CRIANDO UM SISTEMA BANCÁRIO COM PYTHON"

# Sobre o desafio: 
# O objetivo desse desafio é criar um sistema bancário utilizando a linguagem Python. 
# A primeira versão da aplicação funcionará apenas com 1 funcionário, então não é necessário identificar o número da conta bancária nem o da agência.
# A aplicação terá três operações, sendo elas DEPÓSITO, SAQUE e EXTRATO.

# DEPÓSITOS
# Só será permitido depositar valores positivos.
# Os valores dos depósitos serão armazenados em uma variável e exibidos na operação de extrato.

# SAQUES
# O sistema deve permitir a realização de apenas 3 saques diários limitados a 500 reais por saque.
# Se o valor do saque for superior ao valor no saldo, o programa deve mostrar uma mensagem falando que o saque não foi realizado por conta do valor em saldo.
# Todos os saques devem ser armazenados em uma variável e devem ser exibidos na operação extrato

# EXTRATO
# Essa operação deve listar e mostrar ao usuário todos os depósitos, saques e o saldo atual da conta.
# Os valores devem ser mostrados no formato R$000.00




mensagem = f'''

Olá, digite um dos números para realizarmos o atendimento

1 - Depósito
2 - Saque
3 - Ver Extrato
4 - Encerrar o atendimento

'''

# Variáveis para armazenar os valores de DEPÓSITO, SAQUE e EXTRATO

depositos = 0
saques = 0
extrato = ""

# Variável de contagem de saque

contS = 0

while True:

  print(mensagem)

  num = int(input("Digite o número da opção desejada "))

  if num == 4:
    print("Atendimento encerrado!")
    break

  if num > 4 or num < 1:
    print("Opção inválida! Tente novamente")
    continue
        
#Operação de Depósitos

  if num == 1:
    depositar = float(input("\nOpção DEPÓSITO selecionada, informe o valor a ser depositado: "))
    
    while depositar < 1:
      print("Valor inválido, não é possível depositar valores negativos ou zerados! Tente fazer uma nova solicitação de depósito com um valor válido")
      break

    if depositar > 0:
        depositos += depositar
        saldo = depositos - saques
        extrato += f"Depósito: R${depositar:.2f}\n"
        print(f"Você depositou R${depositar:.2f} . Seu saldo atual é R${saldo:.2f}")        
        

    op = int(input("\nDigite qualquer número para FAZER UMA NOVA OPERAÇÃO ou 5 para ENCERRAR O ATENDIMENTO "))
      
    if op == 5:
          break

    else:
          continue

#Operação de Saques

  if num == 2:
        sacar = float(input("Opção SAQUE selecionada, informe o valor a ser sacado: "))
        
        if sacar <= 500 and contS < 3:       
            saques += sacar
            saldo = depositos - saques 
            contS += 1       
            extrato += f"Saque: R$ {sacar:.2f}\n"
            print(f"Você sacou R${sacar:.2f} e o seu saldo atual é R${saldo:.2f}")

        while sacar < 1:
          print("Valor inválido, não é possível sacar valores negativos! Tente fazer uma nova solicitação de saque com um valor válido")
          break

        if sacar > saldo and contS <= 3:
          saldo = depositos - saques
          print("Valor inválido, não é possível sacar valores maiores que o saldo! Tente outro valor\n")
          

        if contS == 3:
            print("\nO limite diário de 3 saques foi atingido e não é possível realizar novos saques, tente novamente amanhã")
            

        if sacar > 500 and contS <= 3:
            print("Não foi possível realizar o saque pois o limite por saque é de R$ 500.00. Tente novamente com um valor abaixo de R$ 500.00")
            
      

        op = int(input("\nDigite qualquer número para FAZER UMA NOVA OPERAÇÃO ou 5 para ENCERRAR O ATENDIMENTO "))
          
        if op == 5:
              break

        else:
              continue


  if num == 3:
    print("\nOpção VER EXTRATO selecionada, seu extrato será mostrado a seguir\n")
    print("******************** EXTRATO ********************")
    print(extrato)
    print("Saldo: " , saldo)
