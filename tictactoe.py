BOARD = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

PLAYER1 = "X"
PLAYER2 = "O"
currentPlayer = PLAYER1
gameRunning = True

"""
Fonction qui affiche la grille du TicTacToe à l'aide de la liste BOARD.
Elle organise l'affichage de la grille en trois lignes, chacune composée de trois cases.
"""
def printGrid(BOARD):
    print(BOARD[0] + " | " + BOARD[1] + " | " + BOARD[2])
    print("----------")
    print(BOARD[3] + " | " + BOARD[4] + " | " + BOARD[5])
    print("----------")
    print(BOARD[6] + " | " + BOARD[7] + " | " + BOARD[8])

"""
Fonction permettant de choisir une case et de la marquer à l'aide de la liste BOARD
et de la variable currentPlayer.
Elle vérifie si l'entrée est valide (entre 1 et 9, et si la case est libre), 
puis met à jour la grille.
"""
def PlayerInput(BOARD, currentPlayer):
    while True:
        try:
            number = int(input(f"Player {currentPlayer}, enter a number between 1 and 9: "))
            # Vérifie si le numéro est valide et si la case est vide
            if number >= 1 and number <= 9 and BOARD[number - 1] == "-":
                BOARD[number - 1] = currentPlayer  # Marque la case avec la marque du joueur
                return False
            elif number < 1 or number > 9 :
                print("Please choose a number between 1 and 9.")
            else:
                print("Choose another spot, a player is already in that spot!")  # Si la case est déjà occupée
        except ValueError:
            print("Please choose an integer between 1 and 9.")  # Si l'entrée n'est pas un entier

"""
Fonction pour vérifier si on a 3 marques identiques alignées horizontalement.
Elle vérifie les lignes (indices 0-2, 3-5, 6-8) pour voir si toutes les cases
contiennent la même marque du joueur actuel.
"""
def checkHorizontal(BOARD, currentPlayer):
    for row in range(0, 9, 3):
        # Vérifie les trois cases de la ligne
        if BOARD[row] == BOARD[row + 1] == BOARD[row + 2] == currentPlayer:
            return True
    return False

"""
Fonction pour vérifier si on a 3 marques identiques alignées verticalement.
Elle vérifie les colonnes (0-3-6, 1-4-7, 2-5-8) pour voir si toutes les cases
contiennent la même marque du joueur actuel.
"""
def checkVertical(BOARD, currentPlayer):
    for col in range(3):  # 3 colonnes
        # Vérifie les trois cases de la colonne
        if BOARD[col] == currentPlayer and BOARD[col + 3] == currentPlayer and BOARD[col + 6] == currentPlayer:
            return True
    return False

"""
Fonction pour vérifier si on a 3 marques identiques alignées diagonalement.
Elle vérifie les deux diagonales possibles (de haut à gauche à bas à droite, et de haut à droite à bas à gauche).
"""
def checkDiagonal(BOARD, currentPlayer):
    # Diagonale principale
    if BOARD[0] == BOARD[4] == BOARD[8] == currentPlayer:
        return True
    # Diagonale secondaire
    if BOARD[2] == BOARD[4] == BOARD[6] == currentPlayer:
        return True
    return False

"""
Fonction pour vérifier une égalité.
Elle vérifie si la grille ne contient plus de cases vides ("-"), ce qui signifie que le jeu est terminé et qu'il n'y a pas de gagnant.
"""
def checkDraw(BOARD):
    if "-" not in BOARD:  # Si aucune case n'est vide
        return True
    return False

"""
Fonction qui vérifie si un joueur a gagné en utilisant les fonctions précédentes.
Elle combine les vérifications horizontales, verticales et diagonales pour déterminer
si le joueur actuel a gagné.
"""
def checkWin(BOARD, currentPlayer):
    if checkDiagonal(BOARD, currentPlayer) or checkHorizontal(BOARD, currentPlayer) or checkVertical(BOARD, currentPlayer):
        return True
    return False

"""
Fonction qui permet de changer la variable currentPlayer pour alterner entre les joueurs.
Si c'est PLAYER1, on passe à PLAYER2, et inversement.
"""
def switchPlayer(currentPlayer):
    return PLAYER2 if currentPlayer == PLAYER1 else PLAYER1

"""
Fonction pour implémenter l'algorithme Minimax.
Cette fonction évalue la grille pour déterminer la "valeur" de chaque mouvement,
en optimisant le choix du coup en fonction de la situation actuelle du jeu.
"""
def minimax(BOARD, depth, isMaximizingPlayer):
    if checkWin(BOARD, PLAYER2):  # Si le joueur AI (PLAYER2) a gagné
        return 1
    elif checkWin(BOARD, PLAYER1):  # Si l'autre joueur (PLAYER1) a gagné
        return -1
    elif checkDraw(BOARD):  # Si c'est une égalité
        return 0

    if isMaximizingPlayer:  # Maximiser la valeur pour l'AI (PLAYER2)
        maxEval = float('-inf')
        for i in range(9):
            if BOARD[i] == "-":  # Si la case est vide
                BOARD[i] = PLAYER2  # Marquer la case pour l'AI
                eval = minimax(BOARD, depth + 1, False)  # Calculer l'évaluation du coup
                BOARD[i] = "-"  # Annuler le coup
                maxEval = max(maxEval, eval)  # Mettre à jour le meilleur coup
        return maxEval
    else:  # Minimiser la valeur pour l'autre joueur (PLAYER1)
        minEval = float('inf')
        for i in range(9):
            if BOARD[i] == "-":  # Si la case est vide
                BOARD[i] = PLAYER1  # Marquer la case pour le joueur humain
                eval = minimax(BOARD, depth + 1, True)  # Calculer l'évaluation du coup
                BOARD[i] = "-"  # Annuler le coup
                minEval = min(minEval, eval)  # Mettre à jour le meilleur coup
        return minEval

"""
Fonction qui trouve le meilleur coup pour l'AI en utilisant l'algorithme Minimax.
Elle parcourt toutes les cases vides et évalue le meilleur coup possible pour l'AI.
"""
def bestMove(BOARD):
    bestVal = float('-inf')
    bestMove = -1
    for i in range(9):
        if BOARD[i] == "-":  # Si la case est vide
            BOARD[i] = PLAYER2  # Marquer la case pour l'AI
            moveVal = minimax(BOARD, 0, False)  # Calculer l'évaluation du coup
            BOARD[i] = "-"  # Annuler le coup
            if moveVal > bestVal:  # Si le coup est meilleur, le retenir
                bestVal = moveVal
                bestMove = i
    return bestMove

"""
Fonction qui permet à l'AI de jouer.
Elle choisit le meilleur coup et met à jour la grille.
"""
def aiMove(BOARD):
    move = bestMove(BOARD)  # Trouver le meilleur coup pour l'AI
    BOARD[move] = PLAYER2  # Marquer la case choisie par l'AI
    print(f"AI plays at position {move + 1}")  # Afficher où l'AI a joué

"""
Fonction qui permet de choisir entre le mode single-player ou multi-player.
Elle demande à l'utilisateur de choisir entre ces deux modes et valide l'entrée.
"""
def select_mode():
    while True:
        mode = input("Single-player or multi-player?(single/multi) ").strip().lower()
        if mode in ["singleplayer", "single-player", "single","s"]:
            return mode
        elif mode in ["multiplayer", "multi-player", "multi","m"]:
            return mode
        else:
            print("Please enter only singleplayer or multiplayer!")

"""
Fonction pour gérer le mode multijoueur.
Elle permet aux deux joueurs de jouer à tour de rôle jusqu'à ce qu'il y ait un gagnant ou une égalité.
"""
def multiplayer(BOARD, currentPlayer, gameRunning):
    while gameRunning:
        printGrid(BOARD)  # Afficher la grille avant chaque coup
        PlayerInput(BOARD, currentPlayer)  # Demander à un joueur de jouer
        if checkWin(BOARD, currentPlayer):  # Vérifier si un joueur a gagné
            printGrid(BOARD)
            gameRunning = False
        elif checkDraw(BOARD):  # Vérifier si c'est une égalité
            printGrid(BOARD)
            print("It's a draw!")
            gameRunning = False
        else:
            currentPlayer = switchPlayer(currentPlayer)  # Passer au joueur suivant

"""
Fonction pour gérer le mode solo.
Le joueur humain joue contre l'AI, qui choisit son coup avec l'algorithme Minimax.
"""
def singleplayer(BOARD, currentPlayer, gameRunning):
    while gameRunning:
        printGrid(BOARD)  # Afficher la grille avant chaque coup
        if currentPlayer == PLAYER1:
            PlayerInput(BOARD, currentPlayer)  # Le joueur humain joue
        else:
            aiMove(BOARD)  # L'AI joue
        if checkWin(BOARD, currentPlayer):  # Vérifier si un joueur a gagné
            printGrid(BOARD)
            gameRunning = False
        elif checkDraw(BOARD):  # Vérifier si c'est une égalité
            printGrid(BOARD)
            print("It's a draw!")
            gameRunning = False
        else:
            currentPlayer = switchPlayer(currentPlayer)  # Passer au joueur suivant

"""
Fonction qui demande à l'utilisateur s'il veut rejouer après une partie.
Elle retourne True si l'utilisateur veut recommencer, False sinon.
"""
def ask_to_play_again():
    while True:
        try:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ["yes", "y"]:
                return True
            elif play_again in ["no", "n"]:
                print("Thank you for playing!")
                return False
            else:
                print("Please enter 'yes' or 'no'.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

"""
Fonction qui gère le mode de jeu et lance une nouvelle partie selon l'option choisie.
Elle relance le jeu si l'utilisateur souhaite rejouer.
"""
def gameMode():
    while True:
        mode = select_mode()  # Demander quel mode de jeu choisir
        BOARD = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        currentPlayer = PLAYER1
        gameRunning = True
        if mode in ["singleplayer", "single", "single-player","s"]:
            print("You are playing as singleplayer.")
            singleplayer(BOARD, currentPlayer, gameRunning)  # Lancer le mode solo
        elif mode in ["multiplayer", "multi", "multi-player","m"]:
            print("You are playing as multiplayer.")
            multiplayer(BOARD, currentPlayer, gameRunning)  # Lancer le mode multijoueur
        if not ask_to_play_again():  # Demander si l'utilisateur veut rejouer
            break

if __name__ == "__main__":
    gameMode()  # Lancer le jeu