# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.1

print("1-Escrever uma frase em um arquivo")
print("2-Ler e imprimir o conteudo do arquivo")
entrada=int(input("O que voce quer fazer?"))

geral ="arquivoprimeiro"

def escreva_arquivo(geral):
    arquivo=open("arquivoprimeiro","w")
    arquivo.write(input("Escreva:"))
    arquivo.close()

def ler_arquivo(geral):
    arquivo2= open("arquivoprimeiro","r")
    leitura= arquivo2.read()
    arquivo2.close()
    print(leitura)

if entrada != "2":
    escreva_arquivo(geral)
else:
    ler_arquivo(geral)

