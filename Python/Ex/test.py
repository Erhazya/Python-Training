import random

def cases_remplissables(grille, joueur, des):


    """
    Variable :
        liste_de_point : Liste de 13 élément pour le stockage des points du joueur x

        nombre,nombre2 : Variable servant au boucle for pour les verification des differentes situations
    
        grille : Grille de point initial du joueur x

        des : liste des dés obtenu grace a la fonction lancer_des ()
    
    Fonction utilisés :

        sorted() : Permet de trier la liste de dés automatiquement
        count(x) : Permet de compter le nombre d'occurence du nombre données x dans la liste de dés
        sum()    : Permet de faire la somme de la liste de dés

    Condition utilisés : 

        grille[x1][x2] : Permet de prendre (get) la valeur dans la Grille de liste de point en renseignant l'index du joueur (x1) et l'index de la liste correspondant au point de celui ci (x2)
    

        Mot clés des conditions utilisés :

            in : Permet de verifier la présence d'une ou plusieurs valeur dans la liste de dés comme dans la verification pour la petite suite    
            and : Permet de rajouter un paramètre obligatoire a la validation de la condition (obligatoirement tout les paramètres doivent être valide)
            or : Permet de rajouter un ou des paramètres a la condition (un seul peut-être valide)


    """


    liste_de_point = [None] * 13   #Création de la liste de point , [x] * 13 permet directement de créer une liste de 13 élément , alternative a [None,None,None,....]
 
    des = sorted(des)  #Triage de la liste des dés , fait directement au début pour éviter les répétition dans les vérification où c'était nécessaire

    for nombre in range(1,7):
        if grille[joueur][nombre-1] != 0 :
            liste_de_point[nombre-1] = None
        elif grille[joueur][nombre-1] == 0:
            liste_de_point[nombre-1] = des.count(nombre) * (nombre)
        
        
    # Verification si Brelan
    if grille[joueur][6] != 0 :
        liste_de_point[6] = None
    elif grille[joueur][6] == 0:
        for nombre in range(1, 7):
            if des.count(nombre) == 3:
                liste_de_point[6] = sum(des)
            else : liste_de_point[6] = 0   
    
    
    # Verification si Carré
    if grille[joueur][7] != 0 :
        liste_de_point[7] = None
    elif grille[joueur][7] == 0:
        for nombre in range(1, 7):
            if des.count(nombre) == 4:
                liste_de_point[7] = sum(des)
            else : liste_de_point[7] = 0



    # Verification si Full
    if grille[joueur][8] != 0 :
        liste_de_point[8] = None
    elif grille[joueur][8] == 0:
        liste_de_point[8] = 0
        for nombre in range(1, 7):
            if des.count(nombre) == 3:
                for nombre2 in range(1, 7):
                    if nombre != nombre2 and des.count(nombre2) == 2:
                        liste_de_point[8] = 25
                            
                                                
                        
                        
    # Verification si Petite suite
    if grille[joueur][9] != 0 :
        liste_de_point[9] = None
    elif grille[joueur][9] == 0:
        if des in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]:
            liste_de_point[9] = 30
        else : liste_de_point[9] = 0
            
    # Verification si Grande suite
    if grille[joueur][10] != 0 :
        liste_de_point[10] = None
    elif grille[joueur][10] == 0:
        if des == [1, 2, 3, 4, 5] or des == [2, 3, 4, 5, 6]:
            liste_de_point[10] = 40
        else : liste_de_point[10] = 0
  
    # Verification si Yatzee
    if grille[joueur][11] != 0 :
        liste_de_point[11] = None
    elif grille[joueur][11] == 0:
        liste_de_point[11] = 0
        for nombre in range(1, 7):
            if des.count(nombre) == 5:
                liste_de_point[11] = 50
    
    # Verification si Chance
    if grille[joueur][12] != 0 :
        liste_de_point[12] = None
    elif grille[joueur][12] == 0:
        liste_de_point[12] = sum(des)
    
    return liste_de_point

# Cette fonction permet de lancer 5 dés et de pouvoir relancer certains dés jusqu'à deux fois
def lancer_des():
    
    # On initialise une liste vide pour contenir les résultats de chaque dé
    liste_des = []
    
    # On lance 5 dés aléatoires et on les ajoute à la liste
    for i in range(5):
        liste_des.append(random.randint(1,6))
    print("Voici vos dés : ", liste_des)
    
    # Le joueur a deux possibilités de relance disponibles
    nb_relance = 2
    
    # Tant qu'il reste des relances possibles, on continue la boucle while
    while(nb_relance != 0):
        
        # Le joueur décide s'il veut faire une nouvelle relance
        print("Souhaitez vous en relancer ? Oui/Non", nb_relance , " relance possible")
        relance_status = input()
        
        # Si le joueur veut relancer les dés
        if relance_status == "Oui" or relance_status == "oui" :
            
            # Le joueur choisit combien de dés il veut relancer
            print("Combien de dés voulez vous relancer ?")
            nombre_de_des = input()
            verif_int = nombre_de_des.isnumeric()
            
            # Si l'entrée du joueur n'est pas un nombre ou est hors limites, on redemande une entrée valide
            if not verif_int or int(nombre_de_des) > 5 or int(nombre_de_des) <= 0 :
                
                while True :        
                    while not verif_int :
                        nombre_de_des = input("Veuillez donner un nombre valide :")
                        verif_int = nombre_de_des.isnumeric()
                    while verif_int :
                        if int(nombre_de_des) > 5 or int(nombre_de_des) <= 0 :
                            nombre_de_des = input("Veuillez donner un nombre valide entre 1 et 5:")
                            verif_int = nombre_de_des.isnumeric()
                        else : 
                            break
                
                # Si l'entrée est valide, on sort de la boucle while
                if verif_int and int(nombre_de_des) <= 5 and int(nombre_de_des) > 0 :
                    break 
            
            # Le joueur choisit quels dés il veut relancer
            print("Le ou lesquelles ?")
            for i in range(int(nombre_de_des))  :
                
                choix_des = input()
                verif_int = choix_des.isnumeric()
                    
                # Si l'entrée du joueur n'est pas un nombre ou est hors limites, on redemande une entrée valide
                if not verif_int or int(choix_des) > 5 or int(choix_des) <= 0 :
                    
                    while True :        
                        while not verif_int :
                            choix_des = input("Veuillez donner un nombre valide :")
                            verif_int = choix_des.isnumeric()
                        while verif_int :
                            if int(choix_des) > 5 or int(choix_des) <= 0 :
                                choix_des = input("Veuillez donner un nombre valide entre 1 et 5:")
                                verif_int = choix_des.isnumeric()
                            else : 
                                break
                        
                        # Si l'entrée est valide, on sort de la boucle while
                        if verif_int and int(choix_des) <= 5 and int(choix_des) > 0 :
                            break 
                            
                # On remplace la valeur du dé choisi par un nouveau résultat aléatoire
                liste_des[int(choix_des)-1] = random.randint(1,5)           

            # On affiche la nouvelle liste de dés obtenus après relance
            print(liste_des)

            # On retire une relance disponible
            nb_relance -= 1
        
        # Si le joueur ne veut pas relancer les dés, on sort de la boucle while
        else :
            break
    
    # On renvoie la liste finale des résultats de chaque dé
    return liste_des
    
# Cette fonction permet à un joueur de choisir une case pour remplir dans la grille
def choix_case(grille,joueur,des):
    
    # On affiche les cases déjà remplies par le joueur
    print("Quelle case souhaites-tu remplir ? Entre 1 et 13 ")
    print(grille[joueur])    
    
    score = None
    
    # Tant que le score n'a pas été choisi, on continue la boucle while
    while score == None :
        
        # Le joueur choisit une case
        choix = input("Donne une case qui n'est pas égale a None :")
        verif_int = choix.isnumeric()
        
        # Si l'entrée du joueur n'est pas un nombre ou est hors limites, on redemande une entrée valide
        if not verif_int or int(choix) > 13 or int(choix) <= 0 :
            
            while True :
                
                # Tant que l'entrée n'est pas un nombre, on redemande une entrée valide
                while not verif_int :
                    choix = input("Veuillez donner un nombre valide :")
                    verif_int = choix.isnumeric()
                    
                # Tant que l'entrée est un nombre mais hors limites, on redemande une entrée valide
                while verif_int :
                    if int(choix) > 13 or int(choix) <= 0 :
                        choix = input("Veuillez donner un nombre valide entre 1 et 5:")
                        verif_int = choix.isnumeric()
                    else : 
                        break
                
                # Si l'entrée est valide, on sort de la boucle while
                if verif_int and int(choix) <= 13 and int(choix) > 0 :
                    break 
            
        # On récupère le score associé à la case choisie par le joueur
        score  = cases_remplissables(grille,joueur,des)[int(choix)-1]
    
    # On renvoie le choix de case et le score obtenu
    choix_numero_case = []
    choix_numero_case.append(choix)
    choix_numero_case.append(score)

    return choix_numero_case

def jeu(nb_joueurs):

    info_joueur =[]
    grille = []
    for i in range(nb_joueurs):
        grille.append([0]*13)

        tour_de_jeu = 0


    while tour_de_jeu != 1 :
        tour_de_jeu += 1

        print("TOUR NUMERO ", tour_de_jeu)

        for i in range(nb_joueurs) : 

            
            print("Joueur :" , i+1)
            liste_des = lancer_des()
            point_possible = cases_remplissables(grille,i,liste_des)
            print("Voici la liste de point disponibles avec vos dés :", point_possible)
            case = choix_case(grille,i,liste_des)

            grille[i][int(case[0])-1] = int(case[1])




    score = 0
    somme1 = 0
    somme2 = 0
    meilleur_joueurs = 0
    temp_i = 0
    def_i = 0
    for i in range(len(grille)) :
        somme1 = 0

        for j in range(len(grille[i])):
            somme1 += grille[i][j]
            temp_i = i+1

        if somme1 > somme2 :
            info_joueur.clear()
            meilleur_joueurs = somme1
            info_joueur.append(i)
            info_joueur.append(somme1)
        elif somme1 < somme2:
            info_joueur.clear()
            meilleur_joueurs = somme2
            info_joueur.append(i)
            info_joueur.append(somme2) 
        elif somme1 == somme2 and somme1 > 0 and somme2 > 0 : 
            info_joueur.clear()
            info_joueur.append(def_i)
            info_joueur.append(somme2)
            info_joueur.append(temp_i)
            info_joueur.append(somme1)
            
            break


        somme2 = somme1
        def_i = i+1

    

    


        

  
    return info_joueur




nb_joueurs = int(input("Donner le nombre de joueur :"))

game = jeu(nb_joueurs)


print(game)


if len(game) == 2 :
    print("Le joueur ", game[0], " a gagné avec ", game[1], " points")

elif len(game) > 2 :
    
    list_exequo_joueur = game[0::2]
    list_exequo_score = game[1::2]
    
    for i in range(len(list_exequo_joueur)):
        print("Le joueur ", list_exequo_joueur[i], " a gagné exequo avec ", list_exequo_score[i], " points")










