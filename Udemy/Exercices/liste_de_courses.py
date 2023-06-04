import json


chemin = "./FichierTest/listecourses.json"

try :
    with open(chemin,"r") as f :
        LISTE  = json.load(f)

    liste_courses = LISTE 
    
    
except :

    liste_courses = []


def afficher_menu():
    print("=== MENU ===")
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")

def ajouter_element():
    element = input("Entrez l'élément à ajouter : ")
    liste_courses.append(element)
    print("L'élément", element, "a été ajouté à la liste de courses.")
    

    with open(chemin,"w") as f : 
        json.dump(liste_courses,f,indent=4 , ensure_ascii=False)




def retirer_element():
    if len(liste_courses) == 0:
        print("La liste de courses est vide.")
    else:
        print("Voici les éléments actuels dans la liste de courses :")
        for i, element in enumerate(liste_courses):
            print(i+1, "-", element)
        indice = int(input("Entrez l'indice de l'élément à retirer : "))
        if indice < 1 or indice > len(liste_courses):
            print("Indice invalide.")
        else:
            element_retire = liste_courses.pop(indice - 1)
            
            with open(chemin,"r") as f :
                LISTE  = json.load(f)

            if element_retire in LISTE  :
                del LISTE [indice-1]

            with open(chemin,"w") as f : 
                json.dump(LISTE,f,indent=4 , ensure_ascii=False)


            print("L'élément", element_retire, "a été retiré de la liste de courses.")
        

        



def afficher_liste():
    if len(liste_courses) == 0:
        print("La liste de courses est vide.")
    else:
        print("Voici les éléments dans la liste de courses :")
        for i, element in enumerate(liste_courses):
            print(i+1, "-", element)

def vider_liste():
    liste_courses.clear()

    with open(chemin,"r") as f :
        LISTE  = json.load(f)

    LISTE.clear()

    with open(chemin,"w") as f : 
        json.dump(LISTE ,f,indent=4 , ensure_ascii=False)


    print("La liste de courses a été vidée.")








def main():
    print("Bienvenue dans le programme de liste de courses !")
    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-5) : ")
        if not choix.isdigit() or int(choix) < 1 or int(choix) > 5:
            print("Choix invalide. Veuillez réessayer.")
            continue
        choix = int(choix)
        if choix == 1:
            ajouter_element()
        elif choix == 2:
            retirer_element()
        elif choix == 3:
            afficher_liste()
        elif choix == 4:
            vider_liste()
        elif choix == 5:
            print("Merci d'avoir utilisé le programme de liste de courses ! Au revoir !")
            break








if __name__ == '__main__':
    main()
