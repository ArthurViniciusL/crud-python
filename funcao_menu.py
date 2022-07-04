def menu_principal() :

    opções = [
        "Adicionar: Aluno(s).","Adicionar: Nota(s).","Remover: Aluno(s).", "Remover: Nota(s).","Editar: Nome Aluno.",
        "Editar: Nota Aluno.","Buscar: Aluno Por Nome.","Calcular: Média da turma.","Exibir: Melhor Aluno.","Exibir: Alunos Em Ordem Alfabética.",
        "Exibir: Exibir Alunos Por Ordenados Por Nota.","Exibir: alunos aprovados por média.","Exibir Alunos Na Final.",
        "Exibir: Alunos Reprovados.","Encerrar o Programa."
        ]
    
    linhas = 1
    import time
    print("                 ╔═════════════════════════════════════════════════════╗")
    time.sleep(0.1)
    print("                 ║ SiS █   ███╗   ███████╗ ████████╗ ╔██████╗  ██████╗ ║")
    time.sleep(0.2)
    print("                 ║  ████╗  ███║  ██║   ██║ ╚══██╔══╝ ██╔══██║ ██╔════╝ ║")
    print("                 ║  ██╔██╗ ███║  ██║   ██║    ██║    ███████║ ███████╗ ║")
    time.sleep(0.1)
    print("                 ║  ██║╚██╗███║  ██║   ██║    ██║    ██╔══██║ ╚════██║ ║")
    print("                 ║  ██║ ╚█████║  ╚██████╔╝    ██║    ██║  ██║ ███████║ ║")
    time.sleep(0.2)
    print("                 ║  ╚═╝  ╚════╝   ╚═════╝     ╚═╝    ╚═╝  ╚═╝ ╚══════╝ ║")
    time.sleep(0.1)
    print("                 ╚═════════════════════════════════════════════════════╝")
    
    time.sleep(0.3)
    print("[MENU PRINCIPAL]".center(87))
    
    for menu in (opções) :
        time.sleep(0.1)
        
        if linhas %2 != 0:
            print("-"*98)
            if linhas < 10 :
                print(f"[{linhas}]  = {menu.upper():<45}",end = " │  ")# :<35 serve p/ mover o espamento para direita.
  
            else:
                print(f"[{linhas}] = {menu.upper():<45}",end = " │  ")
            
        else:
            if linhas < 10 :
                print(f"[{linhas}]  = {menu.upper():<45}")
                
            else:
                print(f"[{linhas}] = {menu.upper():<45}")

        linhas += 1
    print( ("•> Informe: "),end="")
    
#print(menu_principal())
