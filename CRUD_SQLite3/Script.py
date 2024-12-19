import sqlite3

# Database Setup
def create_connection(db_name="Pharmacy.db"):
    conn = sqlite3.connect(db_name)
    return conn


def initialize_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Medicaments (
        ID_Medicament INT PRIMARY KEY,
        Nom_medicament VARCHAR(50) NOT NULL,
        Description VARCHAR(100),
        Prix DECIMAL(15,3) NOT NULL,
        Quantite_Stock INT NOT NULL,
        Date_Exp DATE NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Fournisseur (
        ID_Fournisseur INT PRIMARY KEY,
        Nom_Fournisseur VARCHAR(50) NOT NULL,
        Adress_Fournisseur VARCHAR(50) NOT NULL,
        Tele_Fournisseur VARCHAR(50),
        Email_Fournisseur VARCHAR(50),
        ID_Medicament INT NOT NULL,
        FOREIGN KEY(ID_Medicament) REFERENCES Medicaments(ID_Medicament)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Client (
        ID_Client VARCHAR(50) PRIMARY KEY,
        Nom_Prenom_Client VARCHAR(50) NOT NULL,
        Tele_Client VARCHAR(50),
        Email_Client VARCHAR(50),
        Adress_Client VARCHAR(50)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Commande (
        ID_Medicament INT,
        ID_Client VARCHAR(50),
        Total DECIMAL(15,3) NOT NULL,
        Date_Commande DATE,
        PRIMARY KEY(ID_Medicament, ID_Client),
        FOREIGN KEY(ID_Medicament) REFERENCES Medicaments(ID_Medicament),
        FOREIGN KEY(ID_Client) REFERENCES Client(ID_Client)
    )''')

    conn.commit()


# CRUD Operations for Medicaments
def add_medicament(conn, id_medicament, name, description, price, stock, expiry_date):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Medicaments VALUES (?, ?, ?, ?, ?, ?)",
        (id_medicament, name, description, price, stock, expiry_date),
    )
    conn.commit()


def view_medicaments(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medicaments")
    return cursor.fetchall()


def update_medicament(conn, id_medicament, name, description, price, stock, expiry_date):
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE Medicaments
           SET Nom_medicament = ?, Description = ?, Prix = ?, Quantite_Stock = ?, Date_Exp = ?
           WHERE ID_Medicament = ?""",
        (name, description, price, stock, expiry_date, id_medicament),
    )
    conn.commit()


def delete_medicament(conn, id_medicament):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Medicaments WHERE ID_Medicament = ?", (id_medicament,))
    conn.commit()


# CRUD Operations for Fournisseurs
def add_fournisseur(conn, id_fournisseur, name, address, phone, email, id_medicament):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Fournisseur VALUES (?, ?, ?, ?, ?, ?)",
        (id_fournisseur, name, address, phone, email, id_medicament),
    )
    conn.commit()


def view_fournisseurs(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Fournisseur")
    return cursor.fetchall()


def update_fournisseur(conn, id_fournisseur, name, address, phone, email, id_medicament):
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE Fournisseur
           SET Nom_Fournisseur = ?, Adress_Fournisseur = ?, Tele_Fournisseur = ?, Email_Fournisseur = ?, ID_Medicament = ?
           WHERE ID_Fournisseur = ?""",
        (name, address, phone, email, id_medicament, id_fournisseur),
    )
    conn.commit()


def delete_fournisseur(conn, id_fournisseur):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Fournisseur WHERE ID_Fournisseur = ?", (id_fournisseur,))
    conn.commit()


# CRUD Operations for Clients
def add_client(conn, id_client, name, phone, email, address):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Client VALUES (?, ?, ?, ?, ?)",
        (id_client, name, phone, email, address),
    )
    conn.commit()


def view_clients(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Client")
    return cursor.fetchall()


def update_client(conn, id_client, name, phone, email, address):
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE Client
           SET Nom_Prenom_Client = ?, Tele_Client = ?, Email_Client = ?, Adress_Client = ?
           WHERE ID_Client = ?""",
        (name, phone, email, address, id_client),
    )
    conn.commit()


def delete_client(conn, id_client):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Client WHERE ID_Client = ?", (id_client,))
    conn.commit()


# CRUD Operations for Commandes
def add_commande(conn, id_medicament, id_client, total, date_commande):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Commande VALUES (?, ?, ?, ?)",
        (id_medicament, id_client, total, date_commande),
    )
    conn.commit()


def view_commandes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Commande")
    return cursor.fetchall()


def update_commande(conn, id_medicament, id_client, total, date_commande):
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE Commande
           SET Total = ?, Date_Commande = ?
           WHERE ID_Medicament = ? AND ID_Client = ?""",
        (total, date_commande, id_medicament, id_client),
    )
    conn.commit()


def delete_commande(conn, id_medicament, id_client):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Commande WHERE ID_Medicament = ? AND ID_Client = ?",
        (id_medicament, id_client),
    )
    conn.commit()

def menu():
    print("\n=== Pharmacy Management System ===")
    print("1. Manage Medicaments")
    print("2. Manage Fournisseurs")
    print("3. Manage Clients")
    print("4. Manage Commandes")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice


def medicament_menu(conn):
    while True:
        print("\n--- Medicaments Menu ---")
        print("1. Add Medicament")
        print("2. View Medicaments")
        print("3. Update Medicament")
        print("4. Delete Medicament")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            id_medicament = int(input("Enter Medicament ID: "))
            name = input("Enter Medicament Name: ")
            description = input("Enter Description: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))
            expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ")
            add_medicament(conn, id_medicament, name, description, price, stock, expiry_date)
            print("Medicament added successfully!")
        elif choice == "2":
            medicaments = view_medicaments(conn)
            print("\n--- Medicaments List ---")
            for med in medicaments:
                print(med)
        elif choice == "3":
            id_medicament = int(input("Enter Medicament ID to Update: "))
            name = input("Enter New Name: ")
            description = input("Enter New Description: ")
            price = float(input("Enter New Price: "))
            stock = int(input("Enter New Stock Quantity: "))
            expiry_date = input("Enter New Expiry Date (YYYY-MM-DD): ")
            update_medicament(conn, id_medicament, name, description, price, stock, expiry_date)
            print("Medicament updated successfully!")
        elif choice == "4":
            id_medicament = int(input("Enter Medicament ID to Delete: "))
            delete_medicament(conn, id_medicament)
            print("Medicament deleted successfully!")
        elif choice == "5":
            break


def fournisseur_menu(conn):
    while True:
        print("\n--- Fournisseurs Menu ---")
        print("1. Add Fournisseur")
        print("2. View Fournisseurs")
        print("3. Update Fournisseur")
        print("4. Delete Fournisseur")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            id_fournisseur = int(input("Enter Fournisseur ID: "))
            name = input("Enter Fournisseur Name: ")
            address = input("Enter Address: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            id_medicament = int(input("Enter Medicament ID Supplied: "))
            add_fournisseur(conn, id_fournisseur, name, address, phone, email, id_medicament)
            print("Fournisseur added successfully!")
        elif choice == "2":
            fournisseurs = view_fournisseurs(conn)
            print("\n--- Fournisseurs List ---")
            for fournisseur in fournisseurs:
                print(fournisseur)
        elif choice == "3":
            id_fournisseur = int(input("Enter Fournisseur ID to Update: "))
            name = input("Enter New Name: ")
            address = input("Enter New Address: ")
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            id_medicament = int(input("Enter New Medicament ID Supplied: "))
            update_fournisseur(conn, id_fournisseur, name, address, phone, email, id_medicament)
            print("Fournisseur updated successfully!")
        elif choice == "4":
            id_fournisseur = int(input("Enter Fournisseur ID to Delete: "))
            delete_fournisseur(conn, id_fournisseur)
            print("Fournisseur deleted successfully!")
        elif choice == "5":
            break


def client_menu(conn):
    while True:
        print("\n--- Clients Menu ---")
        print("1. Add Client")
        print("2. View Clients")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            id_client = input("Enter Client ID: ")
            name = input("Enter Client Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            add_client(conn, id_client, name, phone, email, address)
            print("Client added successfully!")
        elif choice == "2":
            clients = view_clients(conn)
            print("\n--- Clients List ---")
            for client in clients:
                print(client)
        elif choice == "3":
            id_client = input("Enter Client ID to Update: ")
            name = input("Enter New Name: ")
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")
            update_client(conn, id_client, name, phone, email, address)
            print("Client updated successfully!")
        elif choice == "4":
            id_client = input("Enter Client ID to Delete: ")
            delete_client(conn, id_client)
            print("Client deleted successfully!")
        elif choice == "5":
            break


def commande_menu(conn):
    while True:
        print("\n--- Commandes Menu ---")
        print("1. Add Commande")
        print("2. View Commandes")
        print("3. Update Commande")
        print("4. Delete Commande")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            id_medicament = int(input("Enter Medicament ID: "))
            id_client = input("Enter Client ID: ")
            total = float(input("Enter Total Price: "))
            date_commande = input("Enter Date of Commande (YYYY-MM-DD): ")
            add_commande(conn, id_medicament, id_client, total, date_commande)
            print("Commande added successfully!")
        elif choice == "2":
            commandes = view_commandes(conn)
            print("\n--- Commandes List ---")
            for commande in commandes:
                print(commande)
        elif choice == "3":
            id_medicament = int(input("Enter Medicament ID to Update: "))
            id_client = input("Enter Client ID to Update: ")
            total = float(input("Enter New Total Price: "))
            date_commande = input("Enter New Date of Commande (YYYY-MM-DD): ")
            update_commande(conn, id_medicament, id_client, total, date_commande)
            print("Commande updated successfully!")
        elif choice == "4":
            id_medicament = int(input("Enter Medicament ID to Delete: "))
            id_client = input("Enter Client ID to Delete: ")
            delete_commande(conn, id_medicament, id_client)
            print("Commande deleted successfully!")
        elif choice == "5":
            break


def main():
    conn = create_connection()
    initialize_tables(conn)

    while True:
        choice = menu()
        if choice == "1":
            medicament_menu(conn)
        elif choice == "2":
            fournisseur_menu(conn)
        elif choice == "3":
            client_menu(conn)
        elif choice == "4":
            commande_menu(conn)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
