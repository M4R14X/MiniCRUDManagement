#The client class
class Client:
    file_name = "Clients.txt"

    @staticmethod
    def create_client(id_client, nom_prenom, tele, email, adresse):
        data = [id_client, nom_prenom, tele, email, adresse]
        with open(Client.file_name, 'a') as file:
            file.write('|'.join(map(str, data)) + '\n')

    @staticmethod
    def read_clients():
        try:
            with open(Client.file_name, 'r') as file:
                clients = [line.strip().split('|') for line in file.readlines()]
            return clients
        except FileNotFoundError:
            return []

    @staticmethod
    def update_client(id_client, new_data):
        clients = Client.read_clients()
        with open(Client.file_name, 'w') as file:
            for client in clients:
                if client[0] == str(id_client):
                    file.write('|'.join(map(str, new_data)) + '\n')
                else:
                    file.write('|'.join(client) + '\n')

    @staticmethod
    def delete_client(id_client):
        clients = Client.read_clients()
        with open(Client.file_name, 'w') as file:
            for client in clients:
                if client[0] != str(id_client):
                    file.write('|'.join(client) + '\n')

#The Commande class
class Commande:
    file_name = "Commandes.txt"

    @staticmethod
    def create_commande(id_medicament, id_client, total, date_commande):
        data = [id_medicament, id_client, total, date_commande]
        with open(Commande.file_name, 'a') as file:
            file.write('|'.join(map(str, data)) + '\n')

    @staticmethod
    def read_commandes():
        try:
            with open(Commande.file_name, 'r') as file:
                commandes = [line.strip().split('|') for line in file.readlines()]
            return commandes
        except FileNotFoundError:
            return []

    @staticmethod
    def update_commande(id_medicament, id_client, new_data):
        commandes = Commande.read_commandes()
        with open(Commande.file_name, 'w') as file:
            for commande in commandes:
                if commande[0] == str(id_medicament) and commande[1] == str(id_client):
                    file.write('|'.join(map(str, new_data)) + '\n')
                else:
                    file.write('|'.join(commande) + '\n')

    @staticmethod
    def delete_commande(id_medicament, id_client):
        commandes = Commande.read_commandes()
        with open(Commande.file_name, 'w') as file:
            for commande in commandes:
                if commande[0] != str(id_medicament) or commande[1] != str(id_client):
                    file.write('|'.join(commande) + '\n')

#The Medicament class
class Medicament:
    file_name = "Medicaments.txt"

    @staticmethod
    def create_medicament(id_medicament, nom, description, prix, quantite_stock, date_exp):
        data = [id_medicament, nom, description, prix, quantite_stock, date_exp]
        with open(Medicament.file_name, 'a') as file:
            file.write('|'.join(map(str, data)) + '\n')

    @staticmethod
    def read_medicaments():
        try:
            with open(Medicament.file_name, 'r') as file:
                medicaments = [line.strip().split('|') for line in file.readlines()]
            return medicaments
        except FileNotFoundError:
            return []

    @staticmethod
    def update_medicament(id_medicament, new_data):
        medicaments = Medicament.read_medicaments()
        with open(Medicament.file_name, 'w') as file:
            for medicament in medicaments:
                if medicament[0] == str(id_medicament):
                    file.write('|'.join(map(str, new_data)) + '\n')
                else:
                    file.write('|'.join(medicament) + '\n')

    @staticmethod
    def delete_medicament(id_medicament):
        medicaments = Medicament.read_medicaments()
        with open(Medicament.file_name, 'w') as file:
            for medicament in medicaments:
                if medicament[0] != str(id_medicament):
                    file.write('|'.join(medicament) + '\n')

#The Fournisseur class
class Fournisseur:
    file_name = "Fournisseurs.txt"

    @staticmethod
    def create_fournisseur(id_fournisseur, nom, adresse, tele, email, id_medicament):
        data = [id_fournisseur, nom, adresse, tele, email, id_medicament]
        with open(Fournisseur.file_name, 'a') as file:
            file.write('|'.join(map(str, data)) + '\n')

    @staticmethod
    def read_fournisseurs():
        try:
            with open(Fournisseur.file_name, 'r') as file:
                fournisseurs = [line.strip().split('|') for line in file.readlines()]
            return fournisseurs
        except FileNotFoundError:
            return []

    @staticmethod
    def update_fournisseur(id_fournisseur, new_data):
        fournisseurs = Fournisseur.read_fournisseurs()
        with open(Fournisseur.file_name, 'w') as file:
            for fournisseur in fournisseurs:
                if fournisseur[0] == str(id_fournisseur):
                    file.write('|'.join(map(str, new_data)) + '\n')
                else:
                    file.write('|'.join(fournisseur) + '\n')

    @staticmethod
    def delete_fournisseur(id_fournisseur):
        fournisseurs = Fournisseur.read_fournisseurs()
        with open(Fournisseur.file_name, 'w') as file:
            for fournisseur in fournisseurs:
                if fournisseur[0] != str(id_fournisseur):
                    file.write('|'.join(fournisseur) + '\n')

# The menu                    
def menu():
    while True:
        print("\n=== Pharmacy Management System ===")
        print("1. Medicaments")
        print("2. Fournisseurs")
        print("3. Clients")
        print("4. Commandes")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            medicament_menu()
        elif choice == '2':
            fournisseur_menu()
        elif choice == '3':
            client_menu()
        elif choice == '4':
            commande_menu()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#Sub-menu for medicament management
def medicament_menu():
    while True:
        print("\n--- Medicaments Menu ---")
        print("1. Create Medicament")
        print("2. Read Medicaments")
        print("3. Update Medicament")
        print("4. Delete Medicament")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            id_medicament = input("Enter Medicament ID: ")
            nom = input("Enter Medicament Name: ")
            description = input("Enter Description: ")
            prix = input("Enter Price: ")
            quantite_stock = input("Enter Stock Quantity: ")
            date_exp = input("Enter Expiry Date (YYYY-MM-DD): ")
            Medicament.create_medicament(id_medicament, nom, description, prix, quantite_stock, date_exp)
            print("Medicament added successfully!")
        elif choice == '2':
            print("List of Medicaments:")
            for m in Medicament.read_medicaments():
                print(m)
        elif choice == '3':
            id_medicament = input("Enter Medicament ID to update: ")
            nom = input("Enter new Name: ")
            description = input("Enter new Description: ")
            prix = input("Enter new Price: ")
            quantite_stock = input("Enter new Stock Quantity: ")
            date_exp = input("Enter new Expiry Date (YYYY-MM-DD): ")
            Medicament.update_medicament(id_medicament, [id_medicament, nom, description, prix, quantite_stock, date_exp])
            print("Medicament updated successfully!")
        elif choice == '4':
            id_medicament = input("Enter Medicament ID to delete: ")
            Medicament.delete_medicament(id_medicament)
            print("Medicament deleted successfully!")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

#Sub-menu for fournisseur management
def fournisseur_menu():
    while True:
        print("\n--- Fournisseurs Menu ---")
        print("1. Create Fournisseur")
        print("2. Read Fournisseurs")
        print("3. Update Fournisseur")
        print("4. Delete Fournisseur")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            id_fournisseur = input("Enter Fournisseur ID: ")
            nom = input("Enter Fournisseur Name: ")
            adresse = input("Enter Adresse: ")
            tele = input("Enter Telephone: ")
            email = input("Enter Email: ")
            id_medicament = input("Enter Medicament ID provided by this Fournisseur: ")
            Fournisseur.create_fournisseur(id_fournisseur, nom, adresse, tele, email, id_medicament)
            print("Fournisseur added successfully!")
        elif choice == '2':
            print("List of Fournisseurs:")
            for f in Fournisseur.read_fournisseurs():
                print(f)
        elif choice == '3':
            id_fournisseur = input("Enter Fournisseur ID to update: ")
            nom = input("Enter new Name: ")
            adresse = input("Enter new Adresse: ")
            tele = input("Enter new Telephone: ")
            email = input("Enter new Email: ")
            id_medicament = input("Enter new Medicament ID: ")
            Fournisseur.update_fournisseur(id_fournisseur, [id_fournisseur, nom, adresse, tele, email, id_medicament])
            print("Fournisseur updated successfully!")
        elif choice == '4':
            id_fournisseur = input("Enter Fournisseur ID to delete: ")
            Fournisseur.delete_fournisseur(id_fournisseur)
            print("Fournisseur deleted successfully!")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

#Sub-menu for client management
def client_menu():
    while True:
        print("\n--- Clients Menu ---")
        print("1. Create Client")
        print("2. Read Clients")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            id_client = input("Enter Client ID: ")
            nom_prenom = input("Enter Client Name: ")
            tele = input("Enter Telephone: ")
            email = input("Enter Email: ")
            adresse = input("Enter Adresse: ")
            Client.create_client(id_client, nom_prenom, tele, email, adresse)
            print("Client added successfully!")
        elif choice == '2':
            print("List of Clients:")
            for c in Client.read_clients():
                print(c)
        elif choice == '3':
            id_client = input("Enter Client ID to update: ")
            nom_prenom = input("Enter new Name: ")
            tele = input("Enter new Telephone: ")
            email = input("Enter new Email: ")
            adresse = input("Enter new Adresse: ")
            Client.update_client(id_client, [id_client, nom_prenom, tele, email, adresse])
            print("Client updated successfully!")
        elif choice == '4':
            id_client = input("Enter Client ID to delete: ")
            Client.delete_client(id_client)
            print("Client deleted successfully!")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

#Sub-menu for commande management
def commande_menu():
    while True:
        print("\n--- Commandes Menu ---")
        print("1. Create Commande")
        print("2. Read Commandes")
        print("3. Update Commande")
        print("4. Delete Commande")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            id_medicament = input("Enter Medicament ID: ")
            id_client = input("Enter Client ID: ")
            total = input("Enter Total Price: ")
            date_commande = input("Enter Command Date (YYYY-MM-DD): ")
            Commande.create_commande(id_medicament, id_client, total, date_commande)
            print("Commande added successfully!")
        elif choice == '2':
            print("List of Commandes:")
            for cmd in Commande.read_commandes():
                print(cmd)
        elif choice == '3':
            id_medicament = input("Enter Medicament ID to update: ")
            id_client = input("Enter Client ID to update: ")
            total = input("Enter new Total Price: ")
            date_commande = input("Enter new Command Date (YYYY-MM-DD): ")
            Commande.update_commande(id_medicament, id_client, [id_medicament, id_client, total, date_commande])
            print("Commande updated successfully!")
        elif choice == '4':
            id_medicament = input("Enter Medicament ID to delete: ")
            id_client = input("Enter Client ID to delete: ")
            Commande.delete_commande(id_medicament, id_client)
            print("Commande deleted successfully!")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# To run the application
menu()
