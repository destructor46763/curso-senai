#Exercício 07: Separador de Números Pares em Arquivo (Condicionais e "w")
#Crie uma lista contendo 10 números inteiros aleatórios de sua escolha.
#Filtre apenas os números que são pares utilizando o operador de resto da divisão %.
#Abra um arquivo chamado "numeros_pares.txt" no modo "w".
#Escreva cada número par encontrado em uma nova linha do arquivo.
#Ao final, informe quantos números pares foram salvos no arquivo.

numeros = [12, 775, 23, 44, 67, 19, 8, 31, 920, 157]
quantidade_pares = 0


with open("numeros_pares.txt", "w", encoding="utf-8") as arquivo:
    
    for num in numeros:
        
        if num % 2 == 0:
            
            arquivo.write(f"{num}\n")
            
            quantidade_pares += 1

print(f"Foram salvos {quantidade_pares} números pares no arquivo!")
