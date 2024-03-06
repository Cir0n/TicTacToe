import numpy as np

tableau = np.zeros ([3,3])
joueur = 1



def verification(tableau, joueur):
    for i in range(tableau.shape[1]-2):
        for j in range (tableau.shape[0]):
            if tableau[j,i] == joueur and tableau[j, i+1] == joueur and tableau[j, i+ 2] == joueur:
                return True
            
    for i in range(tableau.shape[1]):
        for j in range (tableau.shape[0]-2):
            if tableau[j,i] == joueur and tableau[j+1, i] == joueur and tableau[j+2, i] == joueur:
                return True
            
    for i in range(tableau.shape[1] - 2):
        for j in range(tableau.shape[0] - 2):
            if tableau[j, i] == joueur and tableau[j + 1, i + 1] == joueur and tableau[j + 2, i + 2] == joueur:
                return True
    if tableau[0, 2] == joueur and tableau[1, 1] == joueur and tableau[2, 0] == joueur:
        return True
    return False
    

def evaluer(tableau):
    score = 0
    for coup in coupPossible(tableau):
        if coup == [0,0] or coup == [2,0] or coup == [2,2] or coup == [0,2]:
            score+= 10
        elif coup == [0,1] or coup == [1,0] or coup == [1,2] or coup == [2,1]:
            score+= 5
        else:
            score += 15
    return score

def coupPossible(tableau):
    listeCoupPossible = []
    for i in range(tableau.shape[0]):
        for j in range (tableau.shape[1]):
            if tableau[i,j] == 0 :
                listeCoupPossible.append([i,j])
    return listeCoupPossible

def minimax(tableau, profondeur, joueur):
    
    if verification(tableau, 1) or verification(tableau, 2) or profondeur == 0:
        if verification(tableau, 1):
            return -evaluer(tableau), None
        elif verification(tableau, 2):
            return evaluer(tableau), None
        else:
            return 0, None

    if joueur == 2:
        maxEval = -np.inf
        bestMove = None
        listeCoupPossible = coupPossible(tableau)
        for coup in listeCoupPossible:
            newTableau = jouer(tableau,coup[0],coup[1],joueur)
            Eval,_ = minimax(newTableau, profondeur - 1, 1)
            if Eval > maxEval:
                maxEval = Eval
                bestMove = coup
        return maxEval, bestMove

    else:
        minEval = np.inf
        bestMove = None
        listeCoupPossible = coupPossible(tableau)
        for coup in listeCoupPossible:
            newTableau = jouer(tableau, coup[0],coup[1],joueur)
            Eval, _ = minimax(newTableau, profondeur -1, 2)
            if Eval < minEval:
                minEval = Eval
                bestMove = coup
        return minEval, bestMove
    

def bestCoup(tableau, joueur):
    _,bestmove = minimax(tableau,9,joueur)
    return bestmove


def jouer(tableau ,ligne, colonne, joueur):
    nouveau_tableau = np.copy(tableau)
    if nouveau_tableau[ligne,colonne] == 0 :
        nouveau_tableau[ligne,colonne] = joueur
        return nouveau_tableau
    else:
        return tableau



if __name__ == "__main__":
    while True:
        print("Tableau actuel:")
        print(tableau)
        if joueur == 1:
            ligne = int(input('Ligne : '))
            colonne = int(input("Colonne : "))
            tableau = jouer(tableau, ligne, colonne, joueur)
        else:
            emplacement = bestCoup(tableau, joueur)
            if emplacement is not None:
                ligne, colonne = emplacement
                tableau = jouer(tableau, ligne, colonne, joueur)
            else:
                print("Pas de coups possibles. Match nul.")
                break
        if verification(tableau, joueur):
            print(f"Joueur {joueur} a gagné!")
            break
        elif not np.any(tableau == 0):
            print("Match nul!")
            break
        joueur = 2 if joueur == 1 else 1


print("1,2,3".encode())