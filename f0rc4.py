import random

ganhou = False
tentativas = 6
letras_usr = []
categoria = int(input("Óla bem vindo ao jogo da forca\nSelecione a categoria da sua palavra:\n1. Animais\n2. Cores\n3. Frutas\n4. Paises\nDigite o número correspondente a categoria que deseja jogar: "))
animais = ("macaco","cachorro","gato","lagarto","tigre","hipopotamo")
cores = ("vermelho","cinza","laranja","violeta","dourado","preto")
frutas = ("pitaya","melancia","mamao","tomate","azeitona","abacate")
paises = ("alemanha","japao","uganda","argentina","nepal","portugal")

if categoria == 1:
    palavra = random.choice(animais)
    print("Você está jogando na categoria de animais!")
    print("")
    print("")

elif categoria == 2:
    palavra = random.choice(cores)
    print("Você está jogando na categoria de cores!")
    print("")
    print("")

elif categoria == 3:
    palavra = random.choice(frutas)
    print("Você está jogando na categoria de frutas!")
    print("")
    print("")

elif categoria == 4:
    palavra = random.choice(paises)
    print("Você está jogando na categoria de países")
    print("")
    print("")

else:
    print("Digite apenas números correspondentes a uma categoria para o jogo!")

while True:
    for letra in palavra:
        if letra in letras_usr:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    chute = input("Digite uma letra para adivinhar a palavra (em letra minúscula!): ")
    letras_usr.append(chute)

    if chute not in palavra:
        tentativas -= 1

    ganhou = True
    for letra in palavra:
        if letra not in letras_usr:
            ganhou = False
            break

    if tentativas == 6:
        print(" ________")
        print("|        |")
        print("")
        print("")
        
    elif tentativas == 5:
        print(" ________")
        print("|        |")
        print("|        O")
        print("")
        print("")

    elif tentativas == 4:
        print(" ________")
        print("|        |")
        print("|        O")
        print("         | ")
        print("")
        print("")
   
    elif tentativas == 3:
        print(" ________")
        print("|        |")
        print("|        O")
        print("        /| ")
        print("")
        print("")

    elif tentativas == 2:
        print(" ________")
        print("|        |")
        print("|        O")
        print("        /|\ ")
        print("")
        print("")

    elif tentativas == 1:
        print(" ________")
        print("|        |")
        print("|        O")
        print("        /|\ ")
        print("        /  ")
        print("")
        print("")

    if tentativas == 0 or ganhou:
        print(" ________")
        print("|        |")
        print("|        O")
        print("        /|\ ")
        print("        / \ ")
        print("")
        print("")  
        break
    

if ganhou:
    print(f"Correto! A palavra era: {palavra} :D")
else:
    print(f"Que pena! A palavra era: {palavra} Burrão ;( ")
