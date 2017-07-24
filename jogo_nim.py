# n = limite de peças
# m = limite de jogadas
# cont_user_win = conta as partidas ganhas pelo user
# cont_pc_win = conta as partidas ganhas pelo pc


def usuario_escolhe_jogada (jg_user, m, n):
    jg_user = int(input("Quantas peças você vai tirar? "))
    while jg_user < 1 or jg_user > m:
        print("Oops! Jogada inválida! Tente de novo.")
        jg_user = int(input("Quantas peças você vai tirar? "))
    plural_user (jg_user) #executar função plural_user
    return jg_user

def computador_escolhe_jogada (n, m):
    aux = m
    m2 = m + 1
    soma_teste = n - aux
    jg_pc = 0
    bool_loop = False
    while aux > 0 and bool_loop == False:
        if soma_teste % m2 == 0:
            jg_pc = aux
            bool_loop = True
        else:
            aux = aux - 1
            soma_teste = n - aux
    if jg_pc == 0:
        jg_pc = m
    elif n <= m:
        jg_pc = n
    plural_pc (n, m) #executar função plural
    return jg_pc

def plural_user (jg_user):
    if jg_user == 1:
        print("\nVoce tirou uma peça.")
    else:
        print("\nVoce tirou ", jg_user, " peças.")

def plural_pc (n, m):
    if n == 1:
        print("\nO computador tirou uma peça.")
    elif n <= m:
        print("\nO computador tirou ", n, " peças.")
    elif n > m:
        print("\nO computador tirou ", m - 1, " peças.")

def info_peca (n):
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")
    else:
        print("Agora restam ", n, " peças no tabuleiro.\n")

def partida ():
    cont_pc_win = int(0)
    cont_user_win = int(0)
    jg_pc = int(0)
    jg_user = int(0)
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        vez = "usuario"
        print("Voce começa!")
        while n > 0:
            if vez == 'usuario':
                n = int(n - usuario_escolhe_jogada (jg_user, m, n)) #executa função
                vez = "computador"
                if n > 0:
                    info_peca (n)#executa função
            else:
                n = int(n - computador_escolhe_jogada (n, m)) #executa função
                vez = "usuario"
                if n > 0:
                    info_peca (n)#executa função        
    else:
        vez = "computador"
        print("Computador começa!")
        while n > 0:
            if vez == 'computador':
                n = int(n - computador_escolhe_jogada (n, m)) #executa função
                vez = "usuario"
                if n > 0:
                    info_peca (n) #executa função
            else:
                n = int(n - usuario_escolhe_jogada (jg_user, m, n)) #executa função
                vez = "computador"
                if n > 0:
                    info_peca (n) #executa função
    if vez == 'usuario':
        print("Fim do jogo! O computador ganhou!")
        cont_pc_win = cont_pc_win + 1
    else:
        print("Fim do jogo! Voce ganhou!")
        cont_user_win = cont_user_win + 1 

#INICIO DO PROGRAMA
print("Bem-vindo ao jogo do NIM! Escolha:")
print("\n1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato "))
while escolha < 1 or escolha > 2:
    escolha = int(input())
if escolha == 1:
    print("\nVoce escolheu uma partida!")
    partida ()#executa função
else:
    print("\nVoce escolheu um campeonato!")
    jogo = 1
    cont_user_win = 0
    cont_pc_win = 0
    while jogo < 4:
        print("\n**** Rodada ", jogo," ****\n")
        partida ()#executa função
        jogo = jogo + 1
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você ", cont_user_win, "X", cont_pc_win," Computador")
 
