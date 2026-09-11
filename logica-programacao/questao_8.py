while True:
    # Exibe o menu de opções
    print("\n--- CALCULADORA ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    
    # Recebe a escolha do usuário
    opcao = input("Escolha uma opção (1-5): ")
    
    # Verifica se o usuário quer sair antes de pedir os números
    if opcao == '5':
        print("Saindo da calculadora. Até logo!")
        break
    
    # Verifica se a opção é válida para solicitar os números
    if opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
            
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
            
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
            
        elif opcao == '4':
            # Trata a divisão por zero
            if num2 == 0:
                print("Erro: Não é possível dividir por zero!")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")