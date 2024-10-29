# Esthétique du tableau
def afficher_tableau(tableau):
    print("\033[90m   0 1 2\033[00m")
    for i, ligne in enumerate(tableau):
        print(f"\033[90m{i}\033[00m\033[95m {'|' + '|'.join(ligne) + '|'}\033[00m") 

# Introduction
def intro():
    print("C'est l'heure du morpion !!!")  
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
def mouvement_joueur(tableau, joueur):
    while True:
        mouvement = input(f"Joueur {joueur}, c'est à vous ! Entrez une ligne sur une colonne par ex. '0,1': ")

        if mouvement.upper() == "B":
            print("\033[96mMerci de prendre la porte, on s'amusera très bien sans vous ici :)\033[00m")
            return "Partir"

        try:
            ligne, colo = [int(rapport) for rapport in mouvement.split(",")]
            if 0 <= ligne < 3 and 0 <= colo < 3 and tableau[ligne][colo] == " ":
                tableau[ligne][colo] = joueur
                break
            else:
                print("\033[96mLa place est déjà priiise ou hors limites !\033[00m")

        except ValueError:
            print("\033[96mOn a dit 'ligne,colonne' pour le format, un peu de mémoire dit-donc :o !\033[00m")

# Victoires ou pas
def victoire_oupas(tableau):
    combinaisons_gagnantes = [
    [(i, j) for j in range(3)] for i in range(3) # Lignes 
] + [
    [(j, i) for j in range(3)] for i in range(3) # Colonnes 
] + [
    [(i, i) for i in range(3)],                  # Diagonale  \   
    [(i, 2 - i) for i in range(3)]               # Diagonale  /  
]
    for combi in combinaisons_gagnantes:
        if tableau[combi[0][0]][combi[0][1]] == tableau[combi[1][0]][combi[1][1]] == tableau[combi[2][0]][combi[2][1]] and tableau[combi[0][0]][combi[0][1]] != " ":
            return tableau[combi[0][0]][combi[0][1]]  # Victoire
    return None 

# Lancement du jeu
def jeu():
    tableau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_1, joueur_2 = intro()
    joueur_actuel = joueur_1

    for _ in range(9):  
        afficher_tableau(tableau)  
        action = mouvement_joueur(tableau, joueur_actuel)
        if action == "Partir":
            return  # Fin du jeu si l'utilisateur choisit de quitter la partie en cours

        if victoire_oupas(tableau): 
            afficher_tableau(tableau)  
            print(f"\033[92m{joueur_actuel} a gagné !\nFélicitation gros BG !\nTa nouvelle vie commence maintenant ( • ᴗ - ) ✧ \033[00m")
            return  

        joueur_actuel = joueur_2 if joueur_actuel == joueur_1 else joueur_1 

    # Match nul
    afficher_tableau(tableau)
    print("\033[91mMATCH NUL !\033[00m")


# Pour commencer à jouer
jeu()
print("\033[95mMerci d'avoir essayé •ᴗ•\033[00m") 