
'''
lista = []
dicionario = {}
for c in range(2) :

    nomes = input("Nome: ").title()

    if nomes in lista :
        print("Já existe")
    
    else:
        lista.append(nomes)
        dicionario[nomes] = lista

print(lista)
print(dicionario)
'''

'''
dicionario = {}
for c in range(2):

    chave = input(">>> ")

    #dicionario[chave] = None #não recebendo nada, pois eu não tenho indice.

    indice = input(">> ")

    dicionario[chave] = indice #add a chave e um indice.

    #dicionario[chave] = c #add a chave e um valor de sequencia.

    print("-->",dicionario)

    #print(dicionario.keys())#me dá o valor de todas as chaves.
    #print(dicionario.values())#me dá o valor de todas os indices.
    #print(dicionario.items())#me dá os valores de todas as chaves e indices.
    #print(dicionario.get("vinicius"))#me dá o valor atribuido a chave "bláblá"
    
print("")
#print(dicionario[chave]) #me dá sempre a ultima chave.
#indices são dinamicos. Não posso pegar nesse caso.
#para trocar o valor de um indice basta chamar a nova chave e inserir o valor.
print("-->",dicionario,"<--")

'''
'''
lista = ["a","b","c","d","e","f"]
tamanho = len(lista)

c = 1
x = 0
while c < tamanho+1 :
    print("[%i] -  %s" %(c, lista[x]))
    c += 1
    x += 1
'''

'''dicionario = {'arthur' : [9,5,7,8], "vinicius" : [10], "souza" : [8]}
for c in range (4):
    n = input(">>> ")
    print( "Dicionario :",len(dicionario[n]) )

    if n in dicionario.keys() :
        print("Tem")

    else:
        print("Não")'''


'''dicio = {"arthur" : [10,4,7], "vinicius" : [9,7,3], "souza" : [5,9,2]}
print(dicio)
del dicio ["arthur"] [0] #delete dicionario [chave] [valor]
print(dicio)

print(dicio ["arthur"] [0])

del dicio ["arthur"] [0:]
print(dicio)'''

'''#editando chaves:
dicio = {"arhur" : [10,4,7], "vincius" : [9,7,3], "souza" : [5,9,2]}
print(dicio)

dicio["arthur"] = dicio["arhur"]
del dicio["arhur"]
print(dicio)

dicio["vinicius"] = dicio.pop("vincius")
print(dicio)
#Lógica: a {[nova_chave]} recebe a {[antiga_chave]} :││││> E depois deleta a {[antiga_chave]}.'''

'''nota = {"Arv" : [10, 5, 8]}
m = nota
car = m.values()
print(car)
n = input("> ")
valor = n -1

del nota["Arv"] [valor] 

print(nota)'''

'''#Formas de unir listas:
a = [1, 2, 3]
b = [4, 5, 6]
print (a + b)

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print (a)'''

'''#Editando lista:
dicio = {"arthur" : [10,4,7], "vinicius" : [9,7,3], "souza" : [5,9,2]}
print(dicio)
#print(list(dicio.values()))
del dicio["arthur"] [1] #removendo o indice[1] da chave["arthur"]
lis_num_dicio = dicio["arthur"] #pegando o valores dessa chave.
new_numero = int(input("> "))
#num_dicio.extend(lis_new_numero) #unindo duas listas (se eu tratar new_numero como tal)
lis_num_dicio.insert(1, new_numero) #inserindo no (indice: 1, o valor: new_numero) na lista.
#num_dicio[1] , num_dicio[2] = num_dicio[2] , num_dicio[1] #SE eu quiser trocar a posição dos indice. 
print(dicio)'''


'''lista = {"arthur" :[9,8,5,4]}
print(lista)

del lista["arthur"] [3]
print(lista)

indice = 3

if indice <= len(lista["arthur"]) :
    print("existe")

else:
    print('não existe')'''

from operator import pos
from turtle import position


'''dicio = { 
    "arthur" : [10,7,9], "vinicius" : [9,7,3],"antonio" : [7,5,7], "souza" : [5,9,2],
    "arthur lucena" : [7,8,8], "artur carlos" : [] , "joãozinho Paulo" : [], "joão josé" : [] }
#rascunho [7] : buscando nome:

#rascunho [7] : buscando nome:
nome = str(input(">>> "))
print(nome[0:3])
if dicio == {} :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> Os aluno(a)s não constam no sistema.")              
else:
    lista = list( sorted(dicio) )
    indice = 0
    for nomes in lista :
        if nome[0:3] in lista[indice] :
            notas = list( dicio[nomes] )
            if notas == [] :
                media = 0.0
                print(f"{nomes}; - - e - ; - ")
            else:
                media = sum(notas) / len(notas)
                print(f"{nomes}; {notas [0]} {notas[1]} e {notas[2]}; {media:.1f}")
        indice += 1
'''
'''#rascunho [8] : media turma:
listaA = list(dicio)
notas_turma = []
for nomes in listaA :
    listaN = list( dicio[nomes] )
    if listaN != [] :
        soma_nota = sum(listaN)
        print(soma_nota)
        notas_turma.append(soma_nota)
print(notas_turma)
media = sum(notas_turma) / len(listaA)
print(f"M: {media:.1f}")'''

#rascunho [9] : melhor aluno : 
'''lisNomes = list( dicio )

print(lisNomes)

lisMedias = []

for nome in lisNomes :
    lisNotas = dicio[nome]

    mediaNota = sum(lisNotas) / 3 #3 lan(lisNotas)

    lisMedias.append(mediaNota)

maiorMed = max(lisMedias)

for nome,media in zip(lisNomes, lisMedias) :

    if media == maiorMed :
        print(nome, media)'''

'''
#Racunho : [10] - ordem alfabetica.
lista_alunos = list( sorted(dicio) )#sorted() coloca em ordem alfabética.

indice = 0
for nomes in lista_alunos :

    notas_aluno = list(dicio[nomes])
    maior = len(lista_alunos)

    if notas_aluno == [] :

        print(f"\n> {indice}.{nomes}. Notas: [1ª: - │ 2ª: - │ 3ª: - ].  Média: - .")

    else:
        media = sum(notas_aluno) / 3 #len(notas_aluno)
        print("\n> {}.{}. Notas: [1ª: {}. │ 2ª: {}. │ 3ª: {}].  Média: {:.1f}"
        .format(indice,nomes, notas_aluno[0], notas_aluno[1], notas_aluno[2], media) )

    indice += 1'''

'''#rRASCUNHO : [12] [13] [14]

lista_alunos = list(sorted(dicio))

indice = 1

for nomes in lista_alunos :

    notas_aluno = list(dicio[nomes])
    media = sum(notas_aluno) / 3 #len(notas_aluno)

    if media >= 7 :

        if notas_aluno == [] :
            print(f"\n> {indice}.{nomes}. Notas: [1ª: - │ 2ª: - │ 3ª: - ].  Média: - .")

        else:
            print("\n> {}.{}. Notas: [1ª: {}. │ 2ª: {}. │ 3ª: {}].  Média: {:.1f}"
            .format(indice,nomes, notas_aluno[0], notas_aluno[1], notas_aluno[2], media) )
                
                        

    indice += 1'''

dicio = { 
    "arthur" : [10,7,9], "vinicius" : [9,7,3],"antonio" : [7,5,7], "souza" : [5,9,2],
    "arthur lucena" : [7,8,8], "artur carlos" : [] , "joãozinho Paulo" : [], "joão josé" : [] }

lisNomes = list(sorted(dicio))

lisMedias = []

for chave_nome in lisNomes :

    lisNotas = list( dicio[chave_nome] )

    if lisNotas == [] :
        media = 0.0

    else:
        media = sum(lisNotas) / len(lisNotas)

    lisMedias.append(media)

for chave_nota in range(1, len(lisMedias)) :

    indice = lisMedias[chave_nota]  #indice da lista de medias.

    posiçao = chave_nota -1

    while posiçao >= 0 and indice < lisMedias[posiçao] :
        lisMedias[posiçao +1] = lisMedias[posiçao]
        posiçao -= 1
        
    lisMedias[posiçao +1] = indice



for key_indice in range(len( lisMedias )) :
    nome_aluno = list(reversed(dicio))

    notas_aluno = dicio[ nome_aluno[key_indice] ] 

    if notas_aluno == [] :
        print("\n\n\n>>>    ", nome_aluno[key_indice], ">>>   ", "-",">>>   ",lisMedias[key_indice])

    else:
        print("\n\n\n>>>    ", nome_aluno[key_indice], ">>>   ", notas_aluno[2],">>>   ",lisMedias[key_indice])


    #print(chave_nome, media)
#print(lisMedias)
