import pandas as pd


def load_data() :
    """Load Raw data

    Returns:
        DataFrame: Jeu de données pour le modèle
    """    

    # Lire le fichier Excel
    donnees = pd.read_excel("../data/bdd-2.xlsx")

    return donnees