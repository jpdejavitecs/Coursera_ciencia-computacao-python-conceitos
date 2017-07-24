# n = limite de peças
# m = limite de jogadas
# cont_user_win = conta as partidas ganhas pelo user
# cont_pc_win = conta as partidas ganhas pelo pc

def usuario_escolhe_jogada:
    jg_user = int(input())
    if jg_user < 1 and jg_user <= m:
        while jg_user < 1 or jg_user > m:
            print("Oops! Jogada inválida! Tente de novo.")
            jg_user = int(input("Quantas peças você vai tirar? "))
        n = n - jg_user    
    else:
        n = n - jg_user

def computador_escolhe_jogada (n, m):
    
    n = n - (m - 1)

def partida:
    if n % (m + 1) == 0:
        def usuario_escolhe_jogada
    else:
    if 

#INICIO DO PROGRAMA
print("Bem-vindo ao jogo do NIM! Escolha:")
print("\n1 - para jogar uma partida isolada")
escolha = int(input("\n2 - para jogar um campeonato "))
    if escolha == 1:
        print("Voce escolheu uma partida!")
        def partida
        
              #fazer apenas 1 partida
    else escolha == 2:
        print("Voce escolheu um campeonato!")
              #declarar uma variável 3 e fazer com while
    else:
              
