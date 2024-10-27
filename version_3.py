# Esthétique du tableau
def print_board(board):
    print("\033[90m   0 1 2\033[00m")
    for i, row in enumerate(board):
        print(f"\033[90m{i}\033[00m\033[95m {'|' + '|'.join(row) + '|'}\033[00m") 

# Introduction
def intro():
    print("C'est l'heure du morpion !!!")
    saisie = input("\033[96Êtes-vous seul(e) et dans ce cas assez courageux pour vous mesurer à notre I.A ? (oui/non):\033[00m ").lower()
    if saisie not in ("oui", "non"): 
        print("Soyez sérieux et répondez par 'oui' ou 'non', merci -_-")
        saisie = input("\033[96Êtes-vous seul(e) et dans ce cas assez courageux pour vous mesurer à notre I.A ? (oui/non):\033[00m ").lower()
    elif saisie == "oui":
        ia()  # à faire mon Dieu alalalaaaaaaaaa
    else: 
        print(f"{saisie} ? Ah mince ça va être long dit-donc :/ Bref !")
    
    signe_saisi = input("Joueur 1, choisissez votre symbole : O ou X ? ").upper()
    if signe_saisi not in ("O", "X"):
        print("Veuillez choisir un VRAI symbole, bon sang !")
    else:
        print(f"Vous avez choisi {signe_saisi}, excellent choix ;) !")
    
    print("\033[96mPour quitter la partie en cours, pressez B !\033[00m")
    
    joueur_1 = signe_saisi
    joueur_2 = "X" if joueur_1 == "O" else "O"

    return joueur_1, joueur_2

# Mouvement des joueurs
def mvt_joueur(board, joueur):
    while True:
        mvt = input(f"Joueur {joueur}, c'est à vous ! Entrez une ligne sur une colonne par ex. '0,1': ")

        if mvt.upper() == "B":
            print("\033[96mMerci de prendre la porte, on s'amusera très bien sans vous ici :)\033[00m")
            return "Partir"

        try:
            ligne, colo = [int(rapport) for rapport in mvt.split(",")] #versino avec List Comprehensions plutôt
            if 0 <= ligne < 3 and 0 <= colo < 3 and board[ligne][colo] == " ":
                board[ligne][colo] = joueur
                break
            else:
                print("\033[96La place est déjà priiise ou hors limites !\033[00m")
        except ValueError:
            print("\033[96mOn a dit 'ligne,colonne' pour le format, un peu de mémoire dit-donc :o !\033[00m")

# Victoires ou pas
def victoire_oupas(board):
    # penser à mettre en place système "bataille navale" avec lettres et chiffres
    combinaisons_gagnantes = [
    [(i, j) for j in range(3)] for i in range(3) # Lignes où i = indice ligne et j = colonne
] + [
    [(j, i) for j in range(3)] for i in range(3) # Colonnes où i = indice colonne et j = ligne
] + [
    [(i, i) for i in range(3)], # Diagonale principale \   où i = indice ligne = indice colone (ex. (0,0), (1,1), (2,2))
    [(i, 2 - i) for i in range(3)]# Diagonale secondaire / où i = indice ligne 
]
    for combi in combinaisons_gagnantes:
        if board[combi[0][0]][combi[0][1]] == board[combi[1][0]][combi[1][1]] == board[combi[2][0]][combi[2][1]] and board[combi[0][0]][combi[0][1]] != " ":
            return board[combi[0][0]][combi[0][1]]  # victoooiiire
    return None # partie en cours (attention il va nous attendre au tournant)

# Lancement du jeu
def jeu():
    board = [[" " for _ in range(3)] for _ in range(3)]
    joueur_1, joueur_2 = intro()
    joueur_actuel = joueur_1

    for _ in range(9):  # pour chaque coup dans la grille
        print_board(board)  # affiche le tableau à chaque tour
        action = mvt_joueur(board, joueur_actuel)  # bouge le pion du joueur

        if action == "Partir":
            return  # Fin du jeu si l'utilisateur choisit de quitter

        if victoire_oupas(board):  # vérifie si un joueur a gagné
            print_board(board)  # affiche le tableau
            print(f"\033[92m{joueur_actuel} a gagné !\nFélicitation gros BG !\nTa nouvelle vie commence maintenant ( • ᴗ - ) ✧ \033[00m")
            return  # Fin du jeu si victoire

        joueur_actuel = joueur_2 if joueur_actuel == joueur_1 else joueur_1 # Passe au joueur suivant

    # Match nul
    print_board(board)
    print("\033[91mMATCH NUL !\033[00m")
      

# Pour commencer à jouer
jeu()
print("\033[95mMerci d'avoir essayé •ᴗ•\033[00m") 