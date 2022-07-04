from funcao_menu import menu_principal #arquivo do menu

menu_principal()
entrada_user = str(input())

dicionario_alunos = {}

while True :
    
    from funcoes_sistema import *
    
    print("-"*98) #para fazer a linha depois do "Informe: "
    print() #para ter um espaço depois da linha
    
    if entrada_user == "1" :
        print("[1] = Adicionar: Aluno(s).")
        nome_aluno = str(input("\n•> Informe o nome do aluno(a): ")).title().replace("." , "")
        adiciona_aluno(nome_aluno, dicionario_alunos)
        

    elif entrada_user == "2" :
        print("[2] = Adicionar: Nota.")
        print("\n•> Informe o nome do aluno(a)")
        nome_aluno = str(input("   salvo no sistema: ")).title().replace("." , "")


        adiciona_nota(nome_aluno, dicionario_alunos)

    elif entrada_user == "3" :
        print("[3] = REMOVER: ALUNO(A).")
        print("\n•> Informe o nome do aluno(a)")
        nome_aluno = str(input("   salvo no sistema: ")).title().replace("." , "")

        remove_aluno(nome_aluno, dicionario_alunos)
    
    elif entrada_user == "4" :
        print("[4] = REMOVER: NOTA.")
        print("\n•> Informe o nome do aluno(a)")
        nome_aluno = str(input("   salvo no sistema: ")).title().replace("." , "")

        remove_nota(nome_aluno, dicionario_alunos)

    elif entrada_user == "5" :
        print("[5] = EDITAR: NOME ALUNO(A).")
        print("\n•> Informe o nome do aluno(a)")
        nome_aluno = str(input("   salvo no sistema: ")).title().replace("." , "")

        edita_aluno(nome_aluno, dicionario_alunos)

    elif entrada_user == "6" :

        print("[6] = EDITAR: NOTA ALUNO(A).")
        print("\n•> Informe o nome do aluno(a)")
        nome_aluno = str(input("   salvo no sistema: ")).title().replace("." , "")

        edita_nota(nome_aluno, dicionario_alunos)
        
    elif entrada_user == "7" :
        print("[7] = BUSCAR: ALUNO POR NOME.")
        print("\n•> Informe o nome do aluno(a)")
        nome_aluno = str(input("   salvo no sistema: ")).title().replace("." , "")

        busca_aluno(nome_aluno, dicionario_alunos)

    elif entrada_user == "8" :
        print("[8] = CALCULAR: MÉDIA DA TURMA.")

        media_turma(dicionario_alunos)

    elif entrada_user == "9" :
        print("[9] = EXIBIR: MELHOR ALUNO.")

        melhor_aluno(dicionario_alunos)

    elif entrada_user == "10" :
        print("[10] = EXIBIR: ALUNOS EM ORDEM ALFABÉTICA.")

        ordem_alfabetica(dicionario_alunos)

#    elif entrada_user == "11" :
#        print("Recurso disponível apenas para assinantes premium.")

    elif entrada_user == "11" :
        print("[11] = EXIBIR: EXIBIR ALUNOS POR ORDENADOS POR NOTA.")

        ordem_numerica(dicionario_alunos)

    elif entrada_user == "12" :

       print("[12] = EXIBIR: ALUNOS APROVADOS POR MÉDIA.")
       alunos_aprovados(dicionario_alunos)


    elif entrada_user == "13" :
        print("[13] = EXIBIR ALUNOS NA FINAL.")
        
        alunos_final(dicionario_alunos)

    elif entrada_user == "14" :
        print("[14] = EXIBIR: ALUNOS REPROVADOS.")

        alunos_reprovados(dicionario_alunos)

    elif entrada_user == "15" :
        
        print("Bye!(ツ)")
        import time
        time.sleep(0.9)
        break

    else:
        naoEntendi()

    enter = input("\n\n•> Aperte enter [↵] para voltar ao menu principal. ")
    if enter == "15" :
        print("Bye!(ツ)")
        import time
        time.sleep(0.9)
        break

    print("_"*98)

    import os
    os.system('cls')

    menu_principal()
    entrada_user = str(input())
