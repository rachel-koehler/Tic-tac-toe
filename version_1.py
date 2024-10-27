# Esthétique du tableau
def print_board(board):
    for row in board:
        print(f"\033[95m {'|' + '|'.join(row) + '|'}\033[00m") # pour couleurs voir : https://www.geeksforgeeks.org/print-colors-python-terminal/

# Introduction
def intro():
    print("C'est l'heure du morpion !!!")
    saisie = input("Êtes-vous seul(e) et dans ce cas assez courageux pour vous mesurer à notre I.A ? (oui/non): ").lower()
    if saisie not in ("oui", "non"): 
        print("Soyez sérieux et répondez par 'oui' ou 'non', merci -_-")#proposer de resaisir son choix
    elif saisie == "oui":
        ia()  # à faire mon Dieu alalalaaaaaaaaa
    else: 
        print(f"{saisie} ? Ah mince ça va être long dit-donc :/ Bref !")
    
    signe_saisi = input("Joueur 1, choisissez votre symbole : O ou X ? ").upper()
    if signe_saisi == "B":
        print("Merci de prendre la porte, on s'amusera très bien sans vous ici :)")
    elif signe_saisi not in ("O", "X"):
        print("Veuillez choisir un VRAI symbole, bon sang !")
    else:
        print(f"Vous avez choisi {signe_saisi}, excellent choix ;) !")
    
    joueur_1 = signe_saisi
    joueur_2 = "X" if joueur_1 == "O" else "O"

    return joueur_1, joueur_2


# Mouvement des joueurs
def mvt_joueur(board, joueur):
    while True:
        mvt = input(f"Joueur {joueur}, c'est à vous ! Entrez une ligne sur une colonne entre 0 et 2, par ex. '0,1': ")
        try:
            ligne, colo = map(int, mvt.split(","))
            if 0 <= ligne < 3 and 0 <= colo < 3 and board[ligne][colo] == " ":
                board[ligne][colo] = joueur
                break
            else:
                print("La place déjà priiise !")
        except ValueError:
            print("On a dit 'ligne,colonne' pour le format, un peu de mémoire dit-donc :o !.")

# Victoires ou pas
def victoire_oupas(board):
    # penser à mettre en place système "bataille navale" avec lettres et chiffres
    combinaisons_gagnantes = [
        [(0, 0), (0, 1), (0, 2)],  # ligne 1 -> ligne/col
        [(1, 0), (1, 1), (1, 2)],  # '' 2
        [(2, 0), (2, 1), (2, 2)],  # '' 3
        [(0, 0), (1, 0), (2, 0)],  # colonne 1 -> col/ligne
        [(0, 1), (1, 1), (2, 1)],  # '' 2
        [(0, 2), (1, 2), (2, 2)],  # '' 3
        [(0, 0), (1, 1), (2, 2)],  # diagonale \ -> diag
        [(0, 2), (1, 1), (2, 0)]   # diagonale / -> diag
    ]

    for combi in combinaisons_gagnantes:
        if board[combi[0][0]][combi[0][1]] == board[combi[1][0]][combi[1][1]] == board[combi[2][0]][combi[2][1]] and board[combi[0][0]][combi[0][1]] != " ":
            return board[combi[0][0]][combi[0][1]]  # victoooiiire
    return None

# Lancement du jeu
def jeu():
    board = [[" " for _ in range(3)] for _ in range(3)]
    joueur_1, joueur_2 = intro()
    joueur_actuel = joueur_1
    
    for _ in range(9):  # pour chaque coups ds la grille
        print_board(board)
        mvt_joueur(board, joueur_actuel)
        
        if victoire_oupas(board):
            print_board(board)
            print(f"\033[92m{joueur_actuel} a gagné !\nFélicitation gros BG !\nTa nouvelle vie commence maintenant ( • ᴗ - ) ✧ \033[00m") #source emoji: https://emojicombos.com/sunglasses-kaomoji

            return
        
        joueur_actuel = joueur_2 if joueur_actuel == joueur_1 else joueur_1
    
    print("\033[91mMACTH NUL !\033[00m") # à mettre en rouge

# Pour commencer à jouer
jeu()
print("\033[95mMerci d'avoir joué •ᴗ•\033[00m") #source emoji : https://emojicombos.com/sunglasses-kaomoji