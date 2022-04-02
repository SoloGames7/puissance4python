from random import randint


grille_test=[[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]


"""GRILLE VIDE"""

def grille_vide():       # génère le tableau de 6x7
    gril = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    return gril


"""AFFICHE"""

def affiche(grille): # affiche la grille
    c=6
    print(' ',' ','0','1','2','3','4','5','6')
    print('  ','---------------')

    for lig in range(6):
        print(5-lig,' ',end='')
        for col in range(7):
            if grille[lig][col]==0:
                print('|.',end='')
            elif grille[lig][col]==1:
                print('|x',end='')
            elif grille[lig][col]==2:
                print('|0',end='')
        print('|')

    print('  ','---------------')


"""COUP POSSIBLE"""

def coup_possible(grille, col):
    res=False
    if (0<=col<=6) and (grille[0][col]==0):
        res=True
    return res

"""JOUER"""

def jouer(grille, j, col):    # pour jouer un coup s'il est possible
    c = 5
    if coup_possible(grille, col):
        while True:
            if grille[c][col] == 0:
                grille[c][col] = j
                break
            affiche(grille)
            c=c-1

def victoire_fin(grille, j):
    res=False
    for ligne in range(3):
        for col in range(4):
            if diag_haut(grille, j, ligne, col):
                res=True
                break
            if diag_bas(grille, j, ligne+3, col):
                res=True
                break
    for ligne in range(6):
        for col in range(4):
            if horiz(grille, j, ligne, col):
                res=True
                break
    for ligne in range(3):
        for col in range(7):
            if vert(grille, j, ligne, col):
                res=True
                break
    return res

"""HORIZ"""

def horiz (grille, j, lig, col):

    res=False

    if grille[lig][col]==j and grille[lig][col+1]==j and grille[lig][col+2]==j and grille[lig][col+3]==j:

        res=True

    return res


"""VERT"""

def vert(grille, j, lig, col):

    res=False

    if grille[lig][col]==j and grille[lig+1][col]==j and grille[lig+2][col]==j and grille[lig+3][col]==j:

        res=True

    return res


"""MATCH NUL"""

def match_nul(grille):

    res=True

    for i in grille[0]:
        if i==0: res=False

    return res


"""F COUP ALEATOIRE"""

def coup_aleatoire(grille,j):
    fait=False
    while fait==False:

        coup=randint(0,6)

        if coup_possible(grille,coup)==True:
            fait=True
    return coup



"""F diag HAUT"""

def diag_haut(grille, j, lig, col):

    res=False

    if grille[lig][col]==j  and grille[lig-1][col+1]==j  and grille[lig-2][col+2]==j  and grille[lig-3][col+3]==j:

        res=True

    return res


"""F diag BAS"""

def diag_bas(grille,j,lig,col):

    res=False

    if grille[lig][col]==j  and grille[lig+1][col+1]==j  and grille[lig+2][col+2]==j  and grille[lig+3][col+3]==j:

        res=True

    return res

"""F victoire"""


def victoire(grille, j):

    res=False

    H,V,DH,DB=False,False,False,False

    for lig in range(6):
        for col in range(4):
            if horiz (grille, j, lig, col)==True:
                H=True

    for lig in range(3):
        for col in range(7):
            if vert (grille, j, lig, col)==True:
                V=True

    for lig in range(3,6):
        for col in range(4):
            if diag_haut (grille, j, lig, col)==True:
                DH=True

    for lig in range(3):
        for col in range(4):
            if diag_bas(grille, j, lig, col)==True:
                DB=True


    if H or V or DH or DB==True:

        res=True




    return res
