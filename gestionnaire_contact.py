import csv
import os

# Nom du fichier CSV pour stocker les contacts
FICHIER = "contacts.csv"

# Fonction pour lire tous les contacts depuis le fichier
def charger_contacts():
    contacts = []
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", newline='') as fichier:
            lecteur = csv.reader(fichier)
            # On saute la ligne d'en-tête
            next(lecteur, None)
            for ligne in lecteur:
                if len(ligne) == 3:
                    contact = {
                        "nom": ligne[0],
                        "email": ligne[1],
                        "telephone": ligne[2]
                    }
                    contacts.append(contact)
    return contacts

# Fonction pour sauvegarder tous les contacts dans le fichier
def sauvegarder_contacts(contacts):
    with open(FICHIER, "w", newline='') as fichier:
        writer = csv.writer(fichier)
        # Écrire la ligne d'en-tête
        writer.writerow(["nom", "email", "telephone"])
        for c in contacts:
            writer.writerow([c["nom"], c["email"], c["telephone"]])

# Ajouter un nouveau contact
def ajouter_contact():
    print("Ajouter un nouveau contact")
    nom = input("Nom : ")
    email = input("Email : ")
    telephone = input("Téléphone : ")

    contacts = charger_contacts()
    contacts.append({"nom": nom, "email": email, "telephone": telephone})
    sauvegarder_contacts(contacts)

    print(f"Contact '{nom}' ajouté avec succès.\n")

# Afficher tous les contacts
def afficher_contacts():
    contacts = charger_contacts()
    if len(contacts) == 0:
        print("Aucun contact trouvé.\n")
        return

    print("Liste des contacts :")
    for i, c in enumerate(contacts):
        print(f"{i+1}. Nom : {c['nom']} | Email : {c['email']} | Téléphone : {c['telephone']}")
    print()

# Rechercher un contact par nom ou email
def rechercher_contact():
    recherche = input("Entrez un nom ou un email à rechercher : ").lower()
    contacts = charger_contacts()

    trouves = []
    for c in contacts:
        if recherche in c["nom"].lower() or recherche in c["email"].lower():
            trouves.append(c)

    if len(trouves) == 0:
        print("Aucun contact ne correspond à la recherche.\n")
    else:
        print("Contacts trouvés :")
        for c in trouves:
            print(f"Nom : {c['nom']} | Email : {c['email']} | Téléphone : {c['telephone']}")
        print()

# Supprimer un contact par numéro dans la liste
def supprimer_contact():
    contacts = charger_contacts()
    if len(contacts) == 0:
        print("Aucun contact à supprimer.\n")
        return

    afficher_contacts()
    try:
        choix = int(input("Entrez le numéro du contact à supprimer : "))
        if choix < 1 or choix > len(contacts):
            print("Numéro invalide.\n")
            return
        contact_supprime = contacts.pop(choix - 1)
        sauvegarder_contacts(contacts)
        print(f"Contact '{contact_supprime['nom']}' supprimé.\n")
    except ValueError:
        print("Entrée invalide.\n")

# Modifier un contact existant
def modifier_contact():
    contacts = charger_contacts()
    if len(contacts) == 0:
        print("Aucun contact à modifier.\n")
        return

    afficher_contacts()
    try:
        choix = int(input("Entrez le numéro du contact à modifier : "))
        if choix < 1 or choix > len(contacts):
            print("Numéro invalide.\n")
            return

        contact = contacts[choix - 1]

        print("Laissez vide pour ne pas changer la valeur.")
        nom = input(f"Nom [{contact['nom']}] : ")
        email = input(f"Email [{contact['email']}] : ")
        telephone = input(f"Téléphone [{contact['telephone']}] : ")

        if nom != "":
            contact["nom"] = nom
        if email != "":
            contact["email"] = email
        if telephone != "":
            contact["telephone"] = telephone

        sauvegarder_contacts(contacts)
        print(f"Contact '{contact['nom']}' modifié.\n")
    except ValueError:
        print("Entrée invalide.\n")

# Menu principal du programme
def menu():
    while True:
        print("=== Gestionnaire de contacts ===")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Modifier un contact")
        print("5. Supprimer un contact")
        print("6. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            modifier_contact()
        elif choix == "5":
            supprimer_contact()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.\n")

if __name__ == "__main__":
    menu()
