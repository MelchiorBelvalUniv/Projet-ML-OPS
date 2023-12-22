import pandas as pd

def supp_colonne(donnees) :
    """On supprime les colonnes qui ne sont pas nécessaires au modèle

    Args:
        donnees (DataFrame): Jeu de données

    Returns:
        DataFrame: Jeu de données sans les colonnes non nécessaires
    """    
    
    colonnes_a_supprimer = ['fnlwgt', 'education-num']
    donnees = donnees.drop(columns=colonnes_a_supprimer)

    donnees = donnees[~((donnees['sex'] == 'Female') & (donnees['relationship'] == 'Husband'))]
    donnees = donnees[~((donnees['sex'] == 'Male') & (donnees['relationship'] == 'Wife'))]

    return donnees
