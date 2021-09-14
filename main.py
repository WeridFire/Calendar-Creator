import random


# IMPORTER E RANDOMIZER DI LISTE DA FILE
def importer(path):
    file = open(path, 'r')
    lista = file.read().split('\n')
    file.close()
    random.shuffle(lista)
    return lista


# MAIN PROGRAM
studenti = importer("studenti.txt")
nome = input("nome calendario : ")

ppt = 0
while ppt <= 0:
    ppt = int(input("quante persone al giorno? "))

buffer = lambda studenti, ppt: [studenti[i:i+ppt] for i in range(0, len(studenti), ppt)]
result = buffer(studenti, ppt)

f = open(nome + ".txt", 'w')
for i in range(len(result)):
    f.write("\n"+"Turno " + str(i+1) + "\n")

    for j in range(len(result[i])):
        f.write(result[i][j] + "\n")

print("Tutto ok troverai il tuo calendario nella cartella di questo .exe")
