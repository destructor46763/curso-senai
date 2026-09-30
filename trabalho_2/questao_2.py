#Exercício 02: Diário de Bordo (Adicionando Texto com Modo "a")
#Crie um programa que permita ao usuário registrar uma anotação rápida.
#Solicite que o usuário digite uma frase ou mensagem do dia.
#Abra o arquivo "diario.txt" no modo de anexo "a" com encoding="utf-8".
#Adicione a mensagem do usuário ao final do arquivo acompanhada de uma quebra de linha \n.
#Exiba a mensagem: "Anotação adicionada ao diário!".

print("========== DIÁRIO DE BORDO ==========")
print("para parar digite: quero mais nn \n")

while True:
    mensagem = input("Digita uns gabulho pra colocar ae tio: ")

    if mensagem.lower().strip() == "quero mais nn":
        print("opa, suas msgm foi colocada já paizão ")
        break

    with open("diario.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(mensagem + "\n")

    print("A sua anotação foi adicionada fi\n")


