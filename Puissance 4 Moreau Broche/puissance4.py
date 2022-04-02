import pygame
pygame.init()
from fonctions import *
from random import *
from pygame.locals import *
import time

# changer l'icon du jeu

icon_32x32 = pygame.image.load("assets/objects/others/logo_jeu.png")
pygame.display.set_icon(icon_32x32)

# générer la fenetre du puissance 4
pygame.display.set_caption("Puissance 4 - Ultimate Edition")
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
fullscreen = False
grille=grille_vide()
son_son=0

# statut du type du jeu : 0 = non choisi, 1 = contre un ami, 2 = contre un bot
type_de_jeu = 0

j1 = 0
j2 = 0

pion_position_actuelle  = 0

running = True

# ATTRIBUTION DES IMAGES A UNE VARIABLE

background = pygame.image.load("assets/objects/others/background.png")
background2 = pygame.image.load("assets/objects/others/background2.png")
regles_liste = pygame.image.load("assets/objects/others/regles_liste.png")
credits_liste = pygame.image.load("assets/objects/others/credits_liste.png")

gagne_1 = pygame.image.load("assets/objects/others/gagne_1.png")
gagne_2 = pygame.image.load("assets/objects/others/gagne_2.png")
match_nul_fin = pygame.image.load("assets/objects/others/match_nul.png")

grille_jeu = pygame.image.load("assets/objects/grilles_pions/grille_classic.png")
grille_jeu_rect = grille_jeu.get_rect()

logo_jeu = pygame.image.load("assets/objects/others/logo_jeu.png")
logo_jeu_rect = logo_jeu.get_rect()

pion_j1 = pygame.image.load("assets/objects/grilles_pions/pion_classic_j1.png")
pion_j1_rect = pion_j1.get_rect()

pion_j2 = pygame.image.load("assets/objects/grilles_pions/pion_classic_j2.png")
pion_j2_rect = pion_j2.get_rect()

jouer_menu = pygame.image.load("assets/objects/menu_buttons/jouer.png")
jouer_menu_rect = jouer_menu.get_rect()

quitter_menu = pygame.image.load("assets/objects/menu_buttons/quitter.png")
quitter_menu_rect = quitter_menu.get_rect()

regles_menu = pygame.image.load("assets/objects/menu_buttons/regles.png")
regles_menu_rect = regles_menu.get_rect()

credits_menu = pygame.image.load("assets/objects/menu_buttons/credits.png")
credits_menu_rect = credits_menu.get_rect()

jouer_ami = pygame.image.load("assets/objects/menu_buttons/jouer_contre_un_ami.png")
jouer_ami_rect = jouer_ami.get_rect()

jouer_bot = pygame.image.load("assets/objects/menu_buttons/contre_le_bot.png")
jouer_bot_rect = jouer_bot.get_rect()

retour = pygame.image.load("assets/objects/menu_buttons/retour.png")
retour_rect = retour.get_rect()

bot_icon = pygame.image.load("assets/objects/characters/bot.png")
bot_icon_rect = bot_icon.get_rect()

joueur1_icon = pygame.image.load("assets/objects/characters/joueur1.png")
joueur1_icon_rect = joueur1_icon.get_rect()

bouton_selection_morel = pygame.image.load("assets/objects/selection_menu/bouton_selection_morel.png")
bouton_selection_morel_rect = bouton_selection_morel.get_rect()

bouton_selection_classic = pygame.image.load("assets/objects/selection_menu/bouton_selection_classic.png")
bouton_selection_classic_rect = bouton_selection_classic.get_rect()

go_button = pygame.image.load("assets/objects/selection_menu/go_button.png")
go_button_rect = go_button.get_rect()

choix_style = pygame.image.load("assets/objects/selection_menu/choisissez_votre_style.png")
choix_style_rect = choix_style.get_rect()

grilles_choix = pygame.image.load("assets/objects/selection_menu/grilles_choix.png")
grilles_choix_rect = grilles_choix.get_rect()




son = pygame.image.load("assets/objects/sound_icons/son_on.png")
son_rect = son.get_rect()
variable_son = 3

# SONS ET MUSIQUES

pygame.mixer.music.load("assets/sounds/menu.wav")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)

son_bouton = pygame.mixer.Sound("assets/sounds/son_bouton.wav")
son_victoire = pygame.mixer.Sound("assets/sounds/victoire.wav")
son_pion = pygame.mixer.Sound("assets/sounds/son_pion.wav")


# quand le jeu se lance, le joueur tombe sur la page d'accueil
page_actuel = 0

# légende des valeurs pour page_actuel
# 0 = page d'accueil, 1 = jouer, 2 = regles, 3 = credits, 4 = quitter, 5 = jouer contre un ami, 6 = jouer contre le bot


def event_quit(event):
    if event.type == pygame.QUIT:#verifier que l'evennement est fermeture de fenetre
        running==False
        pygame.quit()

# tous les évènements liés aux boutons sont gérés ici
def evenements_souris():
    global running,page_actuel,variable_son, variable_screen, screen, fullscreen, bouton_selection_classic, bouton_selection_morel, grille_jeu, type_de_jeu, pion_j1, pion_j2, j1, j2

    for event in pygame.event.get():
        event_quit(event)

        if pygame.mouse.get_focused():
            x,y=pygame.mouse.get_pos()

            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

            if page_actuel == 0:
                cliquer_jouer = jouer_menu_rect.collidepoint(x-734,y-460)
                cliquer_regles = regles_menu_rect.collidepoint(x-734,y-640)
                cliquer_credits = credits_menu_rect.collidepoint(x-60,y-860)
                cliquer_quitter = quitter_menu_rect.collidepoint(x-734,y-820)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)

                if cliquer_jouer:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 1

                elif cliquer_regles:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 2

                elif cliquer_credits:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 3

                elif cliquer_quitter:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        running==False
                        pygame.quit()

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1

            elif page_actuel == 1:
                cliquer_jouer_ami=jouer_ami_rect.collidepoint(x-600,y-340)
                cliquer_jouer_bot=jouer_bot_rect.collidepoint(x-600,y-700)
                cliquer_retour=retour_rect.collidepoint(x-40,y-40)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)

                if cliquer_jouer_ami:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        type_de_jeu = 1
                        page_actuel = 5

                if cliquer_jouer_bot:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        type_de_jeu = 2
                        page_actuel = 6

                if cliquer_retour:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 0

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1

            elif page_actuel == 2:
                cliquer_retour=retour_rect.collidepoint(x-40,y-40)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)

                if cliquer_retour:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 0

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1

            elif page_actuel == 3:
                cliquer_retour = retour_rect.collidepoint(x-40,y-40)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)

                if cliquer_retour:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 0

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1

            elif page_actuel == 5:
                cliquer_retour=retour_rect.collidepoint(x-40,y-40)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)
                cliquer_bouton_selection_classic = bouton_selection_classic_rect.collidepoint(x-500,y-350)
                cliquer_bouton_selection_morel = bouton_selection_morel_rect.collidepoint(x-1100,y-350)
                cliquer_go_button = go_button_rect.collidepoint(x-881,y-820)

                if cliquer_retour:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 1

                elif cliquer_bouton_selection_classic:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        grille_jeu = pygame.image.load("assets/objects/grilles_pions/grille_classic.png")
                        pion_j1 = pygame.image.load("assets/objects/grilles_pions/pion_classic_j1.png")
                        pion_j2 = pygame.image.load("assets/objects/grilles_pions/pion_classic_j2.png")
                        bouton_selection_classic = pygame.image.load("assets/objects/selection_menu/bouton_selection_classic_vert.png")
                        bouton_selection_morel = pygame.image.load("assets/objects/selection_menu/bouton_selection_morel.png")
                        son_bouton.fadeout(4000)

                elif cliquer_bouton_selection_morel:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        grille_jeu = pygame.image.load("assets/objects/grilles_pions/grille_morel.png")
                        pion_j1 = pygame.image.load("assets/objects/grilles_pions/pion_morel_j1.png")
                        pion_j2 = pygame.image.load("assets/objects/grilles_pions/pion_morel_j2.png")
                        bouton_selection_classic = pygame.image.load("assets/objects/selection_menu/bouton_selection_classic.png")
                        bouton_selection_morel = pygame.image.load("assets/objects/selection_menu/bouton_selection_morel_vert.png")
                        son_bouton.fadeout(4000)

                elif cliquer_go_button:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 7
                        j1=1
                        j2=2
                        if son_son==0:
                            pygame.mixer.music.load("assets/sounds/en_jeu.wav")
                            pygame.mixer.music.play(loops=-1)
                            pygame.mixer.music.set_volume(0.2)

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1

            elif page_actuel == 6:
                cliquer_retour=retour_rect.collidepoint(x-40,y-40)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)
                cliquer_bouton_selection_classic = bouton_selection_classic_rect.collidepoint(x-500,y-350)
                cliquer_bouton_selection_morel = bouton_selection_morel_rect.collidepoint(x-1100,y-350)
                cliquer_go_button = go_button_rect.collidepoint(x-881,y-820)

                if cliquer_retour:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 1

                elif cliquer_bouton_selection_classic:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        grille_jeu = pygame.image.load("assets/objects/grilles_pions/grille_classic.png")
                        pion_j1 = pygame.image.load("assets/objects/grilles_pions/pion_classic_j1.png")
                        pion_j2 = pygame.image.load("assets/objects/grilles_pions/pion_classic_j2.png")
                        bouton_selection_classic = pygame.image.load("assets/objects/selection_menu/bouton_selection_classic_vert.png")
                        bouton_selection_morel = pygame.image.load("assets/objects/selection_menu/bouton_selection_morel.png")
                        son_bouton.fadeout(4000)

                elif cliquer_bouton_selection_morel:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        grille_jeu = pygame.image.load("assets/objects/grilles_pions/grille_morel.png")
                        pion_j1 = pygame.image.load("assets/objects/grilles_pions/pion_morel_j1.png")
                        pion_j2 = pygame.image.load("assets/objects/grilles_pions/pion_morel_j2.png")
                        bouton_selection_classic = pygame.image.load("assets/objects/selection_menu/bouton_selection_classic.png")
                        bouton_selection_morel = pygame.image.load("assets/objects/selection_menu/bouton_selection_morel_vert.png")
                        son_bouton.fadeout(4000)

                elif cliquer_go_button:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 8
                        pygame.mixer.music.load("assets/sounds/en_jeu.wav")
                        pygame.mixer.music.play(loops=-1)
                        pygame.mixer.music.set_volume(0.2)
                        j1=1
                        j2=2

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1

            elif page_actuel == 7:
                cliquer_retour=retour_rect.collidepoint(x-40,y-40)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)

                if cliquer_retour:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 0
                        j1 = 0
                        j2 = 0

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1

            elif page_actuel == 8:
                cliquer_retour=retour_rect.collidepoint(x-40,y-40)
                cliquer_son = son_rect.collidepoint(x-1780,y-40)

                if cliquer_retour:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        page_actuel = 0
                        j1 = 0
                        j2 = 0

                elif cliquer_son:
                    if event.type == pygame.MOUSEBUTTONUP:
                        son_bouton.play()
                        son_bouton.fadeout(4000)
                        variable_son+=1



def afficher_partie():
    if page_actuel == 0:
        # afficher la page d'accueil du jeu
        screen.blit(background, (0,0))
        screen.blit(jouer_menu, (734,480))
        screen.blit(regles_menu, (734,660))
        screen.blit(quitter_menu, (734,840))
        screen.blit(credits_menu, (60,850))
        screen.blit(son, (1780,40))
        screen.blit(logo_jeu,(810,90))

    elif page_actuel == 1:
        # afficher la page de choix du mode de jeu
        screen.blit(background, (0,0))
        screen.blit(jouer_ami, (600,340))
        screen.blit(jouer_bot, (600,700))
        screen.blit(retour, (40,40))
        screen.blit(son, (1780,40))
##        screen.blit(bot_icon, (30,30))
##        screen.blit(joueur1_icon, (30,30))

    elif page_actuel == 2:
        # afficher la page des règles
        screen.blit(background, (0,0))
        screen.blit(regles_liste, (0,0))
        screen.blit(retour, (40,40))
        screen.blit(son, (1780,40))

    elif page_actuel == 3:
        # afficher la page des crédits
        screen.blit(background, (0,0))
        screen.blit(credits_liste, (0,0))
        screen.blit(retour, (40,40))
        screen.blit(son, (1780,40))

    elif page_actuel == 5:
        # afficher la page de choix de la grille
        screen.blit(background, (0,0))
        screen.blit(retour, (40,40))
        screen.blit(son, (1780,40))
        screen.blit(go_button, (881,820))
        screen.blit(bouton_selection_morel, (1100,350))
        screen.blit(bouton_selection_classic, (500,350))
        screen.blit(choix_style, (660,40))
        screen.blit(grilles_choix, (457,500))

    elif page_actuel == 6:
        # afficher la page de choix de la grille
        screen.blit(background, (0,0))
        screen.blit(retour, (40,40))
        screen.blit(son, (1780,40))
        screen.blit(go_button, (881,820))
        screen.blit(bouton_selection_morel, (1100,350))
        screen.blit(bouton_selection_classic, (500,350))
        screen.blit(choix_style, (660,40))
        screen.blit(grilles_choix, (457,500))


    elif page_actuel == 7:
        # afficher la page de la partie contre un ami
        screen.blit(background2, (0,0))
        screen.blit(grille_jeu, (529,176))
        screen.blit(retour, (40,40))
        screen.blit(son, (1780,40))
        affichage_du_pion(grille)

    elif page_actuel == 8:
        # afficher la page de la partie contre un ami
        screen.blit(background2, (0,0))
        screen.blit(grille_jeu, (529,176))
        screen.blit(retour, (40,40))
        screen.blit(son, (1780,40))
        affichage_du_pion(grille)


def choix_de_colonne():
    global pion_position_actuelle, pion_colonne
    for event in pygame.event.get():
        event_quit(event)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if pion_position_actuelle!=6:
                    pion_position_actuelle+=1

            elif event.key == pygame.K_LEFT:
                if pion_position_actuelle!=0:
                    pion_position_actuelle-=1

            elif event.key == pygame.K_RETURN:
                pion_colonne = pion_position_actuelle



def pion_levitation(j):
    screen.blit(background2, (0,0))
    screen.blit(grille_jeu, (529,176))
    affichage_du_pion(grille)
    if j==1:
        screen.blit(pion_j1, (640+(pion_position_actuelle*94),50))
    if j==2:
       screen.blit(pion_j2, (640+(pion_position_actuelle*94),50))
    pygame.display.flip()

def affichage_du_pion(grille):
    for lig in range(6):
        for col in range(7):
            if grille[lig][col]==1:
                screen.blit((pion_j1), ((638+(col*94)),(207.5+(lig*101.5))))
            if grille[lig][col]==2:
                screen.blit((pion_j2), ((638+(col*94)),(207.5+(lig*101.5))))

def fin_retour_menu():
    global grille, page_actuel, j1, j2
    afficher_partie()
    if victoire(grille,1):
        screen.blit(gagne_1, (1385,300))
    elif victoire(grille,1):
        screen.blit(gagne_2, (1385,300))
    else:
        screen.blit(match_nul_fin, (1380,300))
    son_victoire.play()
    time.sleep(4)
    page_actuel = 0
    j1 = 0
    j2 = 0
    pygame.mixer.music.load("assets/sounds/menu.wav")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.2)
    grille=grille_vide()

while running:
    evenements_souris()
    afficher_partie()
    if type_de_jeu == 1 and page_actuel == 7:
        if ((victoire(grille,1) or victoire(grille,2) or match_nul(grille)) == False):
            pion_colonne=7
            while (coup_possible(grille,pion_colonne) == False):
                while pion_colonne == 7 or (coup_possible(grille,pion_colonne) == False):
                    choix_de_colonne()
                    pion_levitation(j1)
                jouer(grille,j1,pion_colonne)
                son_pion.play()

        if ((victoire(grille,1) or victoire(grille,2) or match_nul(grille)) == False):
            pion_colonne = 7
            while (coup_possible(grille,pion_colonne) == False):
                while pion_colonne== 7 or (coup_possible(grille,pion_colonne) == False):
                    choix_de_colonne()
                    pion_levitation(j2)
                jouer(grille,j2,pion_colonne)
                son_pion.play()
        else:
            fin_retour_menu()

    elif type_de_jeu == 2 and page_actuel == 8:
        if ((victoire(grille,1) or victoire(grille, 2) or match_nul(grille)) == False):
            pion_colonne=7
            while (coup_possible(grille,pion_colonne) == False):
                while pion_colonne==7 or (coup_possible(grille,pion_colonne) == False):
                    choix_de_colonne()
                    pion_levitation(j1)
                jouer(grille,j1,pion_colonne)
                son_pion.play()

        if ((victoire(grille,1) or victoire(grille, 2) or match_nul(grille)) == False):
            pion_colonne=7
            while (coup_possible(grille,pion_colonne) == False):
                while pion_colonne == 7 or (coup_possible(grille,pion_colonne) == False):
                    pion_colonne = coup_aleatoire(grille,j2)
                    pion_levitation(j2)
                    temps=randint(1,2)
                    time.sleep(temps)
                jouer(grille,j2,pion_colonne)
                son_pion.play()
        else:
            fin_retour_menu()


    # Activer, désactiver la musique
    if variable_son%2==0:
        son = pygame.image.load("assets/objects/sound_icons/son_off.png")
        pygame.mixer.music.set_volume(0)
        son_son=1
    else:
        son = pygame.image.load("assets/objects/sound_icons/son_on.png")
        pygame.mixer.music.set_volume(0.2)
        son_son=0

    # mettre à jour l'ecran
    pygame.display.flip()