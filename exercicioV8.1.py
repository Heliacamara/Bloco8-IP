# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.1

def escreva_arquivo(arquivoprimeiro):
    arquivo=open("arquivoprimeiro","w")
    arquivo.write(input("Escreva:"))
    arquivo.close()

def ler_arquivo(arquivoprimeiro):
    with open("arquivoprimeiro", "r") as f:
        frases = f.readlines()
        for frase in frases:
            print(frase.strip)

print("1-Escrever uma frase em um arquivo")
print("2-Ler e imprimir o conteudo do arquivo")
entrada=input("O que voce quer fazer?")

arquivoprimeiro = "arquivoprimeiro"

if entrada != "2":
    escreva_arquivo(arquivoprimeiro)
else:
    ler_arquivo(arquivoprimeiro)
