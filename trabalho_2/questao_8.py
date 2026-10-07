#Exercício 08: Sobrescrevendo Configurações do Sistema (Testando o Modo "w")
#Crie um programa que simule a alteração do tema de um aplicativo (ex: "Claro" ou "Escuro").
#Solicite que o usuário escolha o tema desejado.
#Abra o arquivo "config.txt" no modo "w" com encoding="utf-8".
#Escreva apenas a opção escolhida pelo usuário.
#Execute o programa duas vezes digitando temas diferentes e observe como o modo "w" substitui o conteúdo antigo pelo novo sem acumular histórico. 

tema = input("fale o tema que você quer no seu site (Ex: claro ou escuro.): ")

with open("config.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(tema)

print(f"o tema escolhido: '{tema}', foi salvo no sistema.")