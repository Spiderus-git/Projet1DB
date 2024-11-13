from pymongo import MongoClient
from time import sleep

# Connexion aux routeurs MongoDB
client_1 = MongoClient("mongodb://localhost:27017")
client_2 = MongoClient("mongodb://localhost:27018")

# Sélection de la base de données et de la collection
db = client_1["test"]
books_collection = db["books"]

def count_documents():
    """
    Compte le nombre de documents dans la collection 'books'.
    """
    return books_collection.count_documents({})

def test_shard_consistency():
    """
    Test de la consistance des éclats après arrêt et reprise des services.
    """
    # Compter le nombre initial de documents
    initial_count = count_documents()
    print(f"Nombre initial de documents dans 'books' : {initial_count}")

    # Arrêter les routeurs pour simuler une panne
    print("Arrêt des routeurs...")
    import os
    os.system("docker stop routeur_1 routeur_2")
    sleep(5)

    # Redémarrer les routeurs
    print("Redémarrage des routeurs...")
    os.system("docker start routeur_1 routeur_2")
    sleep(5)

    # Compter de nouveau les documents
    new_count = count_documents()
    print(f"Nombre de documents après redémarrage : {new_count}")

    # Vérifier la consistance
    if initial_count == new_count:
        print("Le test est réussi : le nombre de documents est le même.")
    else:
        print("Le test a échoué : le nombre de documents diffère.")

if __name__ == "__main__":
    test_shard_consistency()