#Exercício 01: Meu Primeiro Arquivo de Texto (Criando com Modo "w")
#Crie um programa que solicite ao usuário o seu nome e sua idade.
#Abra um arquivo chamado "usuario.txt" no modo de escrita "w" com encoding="utf-8".
#Escreva as informações no arquivo formatadas em duas linhas: "Nome: [Nome]" e "Idade: [Idade]".
#Utilize a quebra de linha \n ao final de cada frase e confirme na tela: "Dados salvos com sucesso!".

Nome_1 = input("Qual o seu nome?: ")
Idade_1 = input("Qual a sua idade?: ")

with open("usuario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome: {Nome_1}\n")
    arquivo.write(f"Idade: {Idade_1}\n")

print("Seus dados foram salvos com sucesso!")

print(30 * "=")
print(f"o nome registrado foi {Nome_1}")
print(f"a idade registrada foi {Idade_1}")
print(30 * "=")

