def naoEntendi():
        print("¯\_(ツ)_/¯".center(100))
        print("Desculpe, não entendi o que você quis dizer".center(100))
        print("por favor digite novamente.".center(100))

#[1]------------------------------------------------------------------------------------------------------------
#eu preciso passar o dicionário como parametro p/ poder manipular ele fora da função.
def adiciona_aluno(nome, dicionario) : 

        nome_aluno = nome
        dicionario_alunos = dicionario

        if nome_aluno in dicionario_alunos : #o .keys() não é necessário.
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> O nomde de {nome_aluno} já foi colocado no sistema.")

                print(f"\nDeseja editar o nome de {nome}?\n[S] = SIM. │ [N] = NÃO.")
                remover = str(input("•> "))
                if remover == "s":
                        edita_aluno(nome_aluno, dicionario_alunos)

        else:
                dicionario_alunos[nome_aluno] = [] #Adiciona a lista.
                print(f"\n> {nome_aluno} adicionado(a) ao sistema com sucesso!")

        return dicionario_alunos
#[2]------------------------------------------------------------------------------------------------------------
def adiciona_nota(nome, dicionario) :
        nome_aluno = nome
        lista_notas = []
        dicionario_alunos = dicionario
        
        if (nome_aluno in dicionario_alunos) and (len(dicionario_alunos[nome_aluno]) < 3) :
                print()
                for notas in range(1,4):
                        notas_aluno = float(input(f"•> Informe a {notas}ª nota de {nome_aluno}: "))

                        lista_notas.append(notas_aluno) #pega as notas digitadas e coloca na lista.
                        dicionario_alunos[nome_aluno] = lista_notas #pega a lista criada e une a chave 'X' do dicionário.
                
                print(f"\n> Notas de {nome_aluno} adicionadas com sucesso!")

        elif (nome_aluno in dicionario_alunos.keys()) and ( len(dicionario_alunos[nome_aluno]) == 3 ) :

                        print("\n> AÇÃO INVÁLIDA!")
                        print(f"> As 3 notas de {nome_aluno} já foram adicionadas.")

                        #print(f"\nDeseja editar alguma nota de {nome}?\n[S] = SIM. │ [N] = NÃO.")
                        #editar = str(input("\n•> ")).lower().split()

                        '''if editar[0] == "s":
                                pass
                                #editar_nota()'''

        else:
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> O nome de {nome_aluno} não consta no sistema.")
                
                print(f"\nDeseja adicionar {nome_aluno} ao sistema?\n[S] = SIM. │ [N] = NÃO.")
                add_nome = str(input("\n•> ")).lower().split()

                if add_nome[0] == "s" :
                        adiciona_aluno(nome_aluno,dicionario_alunos)
                        adiciona_nota(nome_aluno, dicionario_alunos)
        return dicionario_alunos
#[3]------------------------------------------------------------------------------------------------------------
def remove_aluno(nome, dicionario) :
        nome_aluno = nome
        dicionario_alunos = dicionario
        
        if nome_aluno in dicionario_alunos :
                del dicionario_alunos[nome_aluno]
                print(f"\n> {nome_aluno} removido(a) do sistema com sucesso!")

                '''remover_outro = "s"
                while remover_outro == "s" :
                        print(f"\nDeseja remover outro(a) aluno(a)?\n[S] = SIM. │ [N] = NÃO.")
                        remove = str(input("•> "))
                        remover = remove
                        if remover == "s":
                               nome_aluno = str(input("•> Informe o nome do aluno(a)\n   salvo no sistema: ")).title().replace("." , "")

                        remover_outro = remove'''
        else:
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> O nome de {nome_aluno} não consta no sistema.")

        return dicionario_alunos
#[4]------------------------------------------------------------------------------------------------------------
def remove_nota(nome, dicionario) :
        nome_aluno = nome
        dicionario_alunos = dicionario

        if (nome_aluno not in dicionario_alunos) :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> O nome de {nome_aluno} não consta no sistema.")

                print(f"\nDeseja adicionar {nome_aluno} ao sistema?\n[S] = SIM. │ [N] = NÃO.")
                add_nome = str(input("\n•> ")).lower().split()

                if add_nome[0] == "s" :
                        adiciona_aluno(nome_aluno,dicionario_alunos)

        elif dicionario_alunos[nome_aluno] == [] :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> As notas de {nome_aluno} não constam no sistema.")

        else:# (nome_aluno in dicionario_alunos) and (notas_aluno in dicionario_alunos) :

                print("\nQual nota você deseja remover?")
                print("[1] = 1ª Nota. │ [2] = 2ª Nota. │ [3] = 3ª Nota. │ [4] = Todas.")
                nota = int(input("\n•> ")) 

                if nota < 4 :

                        indice_nota = nota -1 #convertendo a [x] nota em indice.

                        del dicionario_alunos[nome_aluno] [indice_nota]

                        notas_aluno = dicionario_alunos[nome_aluno]
                        notas_aluno.insert(indice_nota, None)

                        print(f"\n> {nota}ª de {nome_aluno} removida com sucesso!")

                else:
                        del dicionario_alunos [nome_aluno] [0:]                
                        print(f"\n> Notas de {nome_aluno} removidas com sucesso!")

        return dicionario_alunos
#[5]------------------------------------------------------------------------------------------------------------
def edita_aluno(nome, dicionario) :
        nome_aluno = nome
        dicionario_alunos = dicionario

        if nome_aluno in dicionario_alunos :

                print(f"\nEditar o nome de {nome_aluno} para:")
                aluno_editado = str(input("•> ")).title().replace(".", "")

                dicionario_alunos [aluno_editado] = dicionario_alunos.pop(nome_aluno)
                #dicio["aluno_editado"] = dicio["nome_aluno"] ; del dicio["nome_aluno"]

                print(f"\n> {nome_aluno} alterado para {aluno_editado} com sucesso!")

        else:
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> O nome de {nome_aluno} não consta no sistema.")

        return dicionario_alunos
#[6]------------------------------------------------------------------------------------------------------------
def edita_nota(nome, dicionario) :
        nome_aluno = nome
        dicionario_alunos = dicionario
        # print(type(dicionario_alunos))

        if (nome_aluno not in dicionario_alunos) :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> O nome de {nome_aluno} não consta no sistema.")


        elif dicionario_alunos[nome_aluno] == [] :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> As notas de {nome_aluno} não constam no sistema.")

        else: # (nome_aluno in dicionario_alunos) and (notas_aluno in dicionario_alunos) :

                
                loop = 0
                while loop == 0 :
                        print("\nQual nota você deseja editar?")
                        print("[1] = 1ª Nota. │ [2] = 2ª Nota. │ [3] = 3ª Nota. │ [4] = Todas.")
                        edit_nota = int(input("\n•> "))

                        if edit_nota < 4 :

                                indice = edit_nota -1
                                
                                if dicionario_alunos[nome_aluno] [indice] != None :
                                        del dicionario_alunos[nome_aluno] [indice]
                                        dicionario_alunos[nome_aluno]

                                        notas_aluno = dicionario_alunos[nome_aluno]

                                        nova_nota = float(input("\n•> Informe a nova nota: "))

                                        notas_aluno.insert(indice, nova_nota)

                                        print(f"\n> {edit_nota}ª nota de {nome_aluno} alterada com sucesso!")

                                else :
                                        print("\n> AÇÃO INVÁLIDA!")
                                        print(f"> {nome_aluno} não possui a {edit_nota}ª nota.")

                                        print(f"\nDeseja adicionar a {edit_nota}ª nota?\n[S] = SIM. │ [N] = NÃO.")
                                        add_nota = str(input("\n•> ")).lower().split()

                                        if add_nota[0] == "s":
                                                nota = float(input(f"•> Informe a {edit_nota}ª de {nome_aluno}: "))
                                                notas_aluno = dicionario_alunos[nome_aluno]
                                                notas_aluno.insert(indice, nota)

                                print(f"\nDeseja editar outra nota de {nome}?\n[S] = SIM. │ [N] = NÃO.")
                                editar = str(input("\n•> ")).lower().split()

                                if editar[0] == "n" :
                                        loop += 1
                        else:
                                del dicionario_alunos[nome_aluno] [0: ]
                                adiciona_nota(nome_aluno, dicionario_alunos)

        return dicionario_alunos
#[7]------------------------------------------------------------------------------------------------------------
def busca_aluno(nome, dicionario) :
        nome_aluno = nome
        dicionario_alunos = dicionario

        if dicionario_alunos == {} :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> Os aluno(a)s não constam no sistema.")
                       
        elif dicionario_alunos != {}:
                lista_alunos = list( sorted(dicionario_alunos) )#sorted() coloca em ordem alfabética.

                indice = 0
                for nomes in lista_alunos :

                        if nome_aluno[0:3] in lista_alunos[indice] :

                                notas_aluno = list(dicionario_alunos[nomes])

                                if notas_aluno == [] :

                                        print(f"\n> {indice}.{nomes}. Notas: [1ª: - │ 2ª: - │ 3ª: - ].  Média: - .")
                                else:
                                        media = sum(notas_aluno) / 3 #len(notas_aluno)
                                        print("\n> {}.{}. Notas: [1ª: {}. │ 2ª: {}. │ 3ª: {}].  Média: {:.1f}"
                                        .format(indice,nomes, notas_aluno[0], notas_aluno[1], notas_aluno[2], media) )
                
                        elif nome_aluno not in dicionario_alunos.keys():
                                print("\n> AÇÃO INVÁLIDA!")
                                print("> Não existe ninguém com esse nome salvo no sistema.")
                                break

                        indice += 1
        return True
#[8]------------------------------------------------------------------------------------------------------------
def media_turma(dicionario) :
        lista_alunos = list( dicionario )
        
        if dicionario.keys() == {} :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> Os aluno(a)s não constam no sistema.")

        elif dicionario.values() == [] :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> As notas do aluno(a)s não constam no sistema.")

        else: 
                tot_alunos = len( lista_alunos )
                notas_turma = []

                for chaves_dic in lista_alunos : # chaves_dic = "nomes das chaves"

                        notas_alunos = list( dicionario[chaves_dic] )

                        if notas_alunos != [] :

                                soma_notas = sum(notas_alunos)
                                notas_turma.append(soma_notas)
                        
                media_geral = sum( notas_turma ) / tot_alunos
                print(f"\n> MÉDIA DA TURMA: {media_geral:.1f}")

        return media_geral   
#[9]------------------------------------------------------------------------------------------------------------
def melhor_aluno(dicionario) :
        lista_alunos = list(dicionario)
        lista_medias = []

        if dicionario == {} :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> Os aluno(a)s não constam no sistema.")

        elif dicionario.values() == [] :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> As notas do aluno(a)s não constam no sistema.")

        else:
                for nome_key in lista_alunos :
                        notas_aluno = dicionario[nome_key]
                        media_aluno = sum(notas_aluno) / 3 #len(notas_aluno)
                        lista_medias.append(media_aluno)

                maior_media = max(lista_medias)

                for nome, media in zip(lista_alunos, lista_medias) :

                        if media == maior_media :
                                print(f"\n> Nome: {nome} │ Média: {media:.1f}")

                return media 
#[10]-----------------------------------------------------------------------------------------------------------
def ordem_alfabetica(dicionario) :
        dicionario_alunos = dicionario

        if dicionario == {}:
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> Os aluno(a)s não constam no sistema.")

        elif dicionario_alunos != {}:
                lista_alunos = list( sorted(dicionario_alunos) )#sorted() coloca em ordem alfabética.

                indice = 1
                for nomes in lista_alunos :
                        notas_aluno = list(dicionario_alunos[nomes])

                        if notas_aluno == [] :

                                print(f"\n> {indice}.{nomes}. Notas: [1ª: - │ 2ª: - │ 3ª: - ].  Média: - .")
                        else:
                                media = sum(notas_aluno) / 3 #len(notas_aluno)
                                print("\n> {}.{}. Notas: [1ª: {}. │ 2ª: {}. │ 3ª: {}].  Média: {:.1f}"
                                .format(indice,nomes, notas_aluno[0], notas_aluno[1], notas_aluno[2], media) )

                        indice += 1

        return dicionario_alunos
#[11]-----------------------------------------------------------------------------------------------------------
def ordem_numerica(dicionario) :
        dicionario_alunos = dicionario
        lista_alunos = list(reversed( dicionario )) #reverte para exibir no Inse... Sort
        lista_medias = []
        
        if dicionario.keys() == {} :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> Os aluno(a)s não constam no sistema.")

        elif dicionario.values() == [] :
                print("\n> AÇÃO INVÁLIDA!")
                print(f"> As notas do aluno(a)s não constam no sistema.")

        else :
                #Tirando a média:
                for name_key in lista_alunos :
                        lista_notas = list(dicionario_alunos[name_key])
                        if lista_notas == [] :
                                media = 0.0
                        else:
                                media = sum(lista_notas) / 3 #len(lista_notas)
                        lista_medias.append(media)

                #Insertion Sort :
                tamanho_lisMedia = len(lista_medias)
                for nota_key in range(1, tamanho_lisMedia) :
                        indice_lisMedia = lista_medias[nota_key]
                        posicao_inseSort = nota_key -1

                        while posicao_inseSort >= 0 and indice_lisMedia < lista_medias[posicao_inseSort] :
                                lista_medias[posicao_inseSort +1] = lista_medias[posicao_inseSort]
                                posicao_inseSort -= 1
                        lista_medias[posicao_inseSort +1] = indice_lisMedia
                
                #Exibição do Insertion Sort:

                for key_indice in range(tamanho_lisMedia) :
                        nome_aluno = lista_alunos
                        notas_aluno = dicionario[ nome_aluno[key_indice]] #talvez precise inverter.
                        media_aluno = lista_medias

                        if notas_aluno == [] :
                                print("\n> {}. {}. Notas: [1ª: - . │ 2ª: - . │ 3ª: - ]. Média: {}"
                                .format(key_indice, nome_aluno[key_indice], media_aluno[key_indice]))


                        else:
                                print("\n> {}. {}. Notas: [1ª: {} . │ 2ª: {} . │ 3ª: {}.]. Média: {}."
                                .format(key_indice, nome_aluno[key_indice], notas_aluno[0],notas_aluno[1], notas_aluno[2], media_aluno[key_indice]))

        return True
#[12]-----------------------------------------------------------------------------------------------------------
def alunos_aprovados(dicionario) :
        lista_alunos = list(sorted(dicionario))

        indice = 1

        for nomes in lista_alunos :

                notas_aluno = list(dicionario[nomes])
                media = sum(notas_aluno) / 3 #len(notas_aluno)

                if media >= 7 :

                        if notas_aluno == [] :
                                print(f"\n> {indice}.{nomes}. Notas: [1ª: - │ 2ª: - │ 3ª: - ].  Média: - .")

                        else:
                                print("\n> {}.{}. Notas: [1ª: {}. │ 2ª: {}. │ 3ª: {}].  Média: {:.1f}"
                                .format(indice,nomes, notas_aluno[0], notas_aluno[1], notas_aluno[2], media) )
                        
        indice += 1

        return media
#[13]-----------------------------------------------------------------------------------------------------------
def alunos_final(dicionario) :
        lista_alunos = list(sorted(dicionario))

        indice = 1

        for nomes in lista_alunos :

                notas_aluno = list(dicionario[nomes])
                media = sum(notas_aluno) / 3 #len(notas_aluno)

                if media >= 5 and media < 7 :

                        if notas_aluno == [] :
                                print(f"\n> {indice}.{nomes}. Notas: [1ª: - │ 2ª: - │ 3ª: - ].  Média: - .")

                        else:
                                print("\n> {}.{}. Notas: [1ª: {}. │ 2ª: {}. │ 3ª: {}].  Média: {:.1f}"
                                .format(indice,nomes, notas_aluno[0], notas_aluno[1], notas_aluno[2], media) )
                        
                indice += 1

        return media
#[14]-----------------------------------------------------------------------------------------------------------
def alunos_reprovados(dicionario) :
        lista_alunos = list(sorted(dicionario))

        indice = 1

        for nomes in lista_alunos :

                notas_aluno = list(dicionario[nomes])
                media = sum(notas_aluno) / 3 #len(notas_aluno)

                if media < 5 :

                        if notas_aluno == [] :
                                print(f"\n> {indice}.{nomes}. Notas: [1ª: - │ 2ª: - │ 3ª: - ].  Média: - .")

                        else:
                                print("\n> {}.{}. Notas: [1ª: {}. │ 2ª: {}. │ 3ª: {}].  Média: {:.1f}"
                                .format(indice,nomes, notas_aluno[0], notas_aluno[1], notas_aluno[2], media) )
                        
                indice += 1

        return media