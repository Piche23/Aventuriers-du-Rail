from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_database():
    """
    Initialise la base de données en supprimant toutes les tables existantes,
    en créant toutes les tables et en appelant la fonction populate_database
    pour ajouter des données à la base de données.
    """
    db.drop_all()
    db.create_all()
    populate_database()


# Fonction pour peupler la base de données
def populate_database():
    # Import des modèles de la base de données
    from models import Joueur, Plateau, Partie, Score

    # Ajout des joueurs
    Joueur.ajouter_joueur("Hugo")
    Joueur.ajouter_joueur("Maman")
    Joueur.ajouter_joueur("Papa")
    Joueur.ajouter_joueur("Débo")
    Joueur.ajouter_joueur("Miguel")

    # Ajout des plateaux
    Plateau.ajouter_plateau("Europe")
    Plateau.ajouter_plateau("Big Cities")
    Plateau.ajouter_plateau("Asie")
    Plateau.ajouter_plateau("Legendary Asia")
    Plateau.ajouter_plateau("Afrique")
    Plateau.ajouter_plateau("Suisse")
    Plateau.ajouter_plateau("Inde")
    Plateau.ajouter_plateau("Pays-Bas")
    Plateau.ajouter_plateau("Royaume-Uni")
    Plateau.ajouter_plateau("Pennsylvanie")
    Plateau.ajouter_plateau("France")
    Plateau.ajouter_plateau("Old West")
    Plateau.ajouter_plateau("Japon")
    Plateau.ajouter_plateau("Italie")

    # Ajout des parties
