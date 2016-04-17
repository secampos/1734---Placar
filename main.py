#!/usr/bin/env python3

from sys import argv

def intercala_modificado(alunos, p, q, r, indice):
    B = []

    for i in range(p, q):
        B.append(alunos[i])

    for j in range(q, r):
        B.append(alunos[r+q-j-1])
    
    i = 0
    j = len(B) - 1
    for k in range(p, r):
        if(indice == 1):
            if(int(B[i][indice]) > int(B[j][indice])):
                alunos[k] = B[i]
                i += 1
            else:
                alunos[k] = B[j]
                j -= 1
        else:
            if(B[i][indice] <= B[j][indice]):
                alunos[k] = B[i]
                i += 1
            else:
                alunos[k] = B[j]
                j -= 1

def mergesort(alunos, p, r, indice):
    if(p < r-1):
        q = (r + p)//2

        mergesort(alunos, p, q, indice)
        mergesort(alunos, q, r, indice)
        intercala_modificado(alunos, p, q, r, indice)

def ranking_alunos(alunos):
    p = 0
    r = len(alunos)
    
    # Ordena em relação as notas em ordem decrescente
    mergesort(alunos, p, r, 1)
    
    # Separa em subconjuntos contendo os alunos com as mesmas notas e ordena em relação aos nomes em ordem crescente
    num = alunos[p][1]
    i = p
    for i in range(p+1, r):
        if(alunos[i][1] != num):
            num = alunos[i][1]
            mergesort(alunos, p, i, 0)
            p = i
    mergesort(alunos, p, i+1, 0)

    return alunos

def saida(alunos, instancia):
    print("Instância {}".format(instancia))
    print("------------------------------")
    print("Ranking dos alunos:")
    for i in range(len(alunos)):
        print("\t{}".format(' '.join(alunos[i])))
    print("------------------------------")
    print("Aluno reprovado: {}".format(alunos[-1][0]))
    print()

if __name__ == '__main__':
    arquivo = open(argv[1], 'r')

    # Cria uma lista contendo o conteudo do arquivo retirando as quebras de linha e as linhas em branco
    alunos = arquivo.readlines()
    linha = 0
    while linha < len(alunos):
        alunos[linha] = alunos[linha].replace('\n', '')
        if(alunos[linha] == ''):
            alunos.pop(linha)
        else:
            alunos[linha] = alunos[linha].split(' ')
            linha += 1
    arquivo.close()

    # Passa cada instância para ser ordenada
    i = 0
    instancia = 1
    while i < len(alunos):
        if(len(alunos[i]) == 1):
            quant = int(alunos[i][0])
            ranking_instancia = ranking_alunos(alunos[i+1:i+1+quant])
            saida(ranking_instancia, instancia)

            instancia += 1
            i = i+1+quant
        else:
            i += 1
