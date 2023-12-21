import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

def drop_na(donnees) :
    """On retire les valeurs manquantes du jeu.

    Args:
        donnees (DataFrame): Jeu de donnees

    Returns:
        DataFrame: Jeu de données sans les valeurs manquantes
    """    
    
    # Calculer le nombre de lignes non nulles dans le DataFrame 'donnees'
    donnees.dropna().shape[0]
    
    return donnees

#Fonctions de recodage des certaines colonnes.
def borne_age(donnees) :
    """Définitions des bornes, et des labels de ces bornes pour les âges.
       Puis application pour chaque colonne des bornes dans le jeu de données

    Args:
        donnees (DataFrame): Jeu de donnees

    Returns:
        DataFrame: Jeu de donnees bornés pour les âges
    """    

    bornes_tranches = [-float('inf'), 17, 26, 33, 41, 50, float('inf')]
    tranches_labels = ['< 17', '[17,26[', '[26,33[', '[33, 41[', '[41,50[', '>50]']
    donnees['tranches_age'] = pd.cut(donnees['age'], bins=bornes_tranches, labels=tranches_labels, right=False)

    return donnees

def borne_heures(donnees) :
    """Définitions des bornes, et des labels de ces bornes pour les heures hebdomadaires.
       Puis application pour chaque colonne des bornes dans le jeu de données

    Args:
        donnees (DataFrame): Jeu de donnees

    Returns:
        DataFrame: Jeu de donnees bornés pour les heures hebdomadaires
    """    

    donnees['hours-per-week'] = donnees['hours-per-week'].apply(lambda x: '>40' if x > 40 else '<40')

    return donnees

def borne_capital_gain(donnees) :
    """Définitions des bornes, et des labels de ces bornes pour les gains de capitaux.
       Puis application pour chaque colonne des bornes dans le jeu de données

    Args:
        donnees (DataFrame): Jeu de donnees
    
    Returns:
        DataFrame: Jeu de donnees bornés pour les gains de capitaux
    """    

    donnees['capital-gain'] = donnees['capital-gain'].apply(lambda x: 'gain' if x > 0 else 'pas_gain')

    return donnees

def borne_capital_loss(donnees) :
    """Définitions des bornes, et des labels de ces bornes pour les pertes de capitaux.
       Puis application pour chaque colonne des bornes dans le jeu de données

    Args:
        donnees (DataFrame): Jeu de donnees

    Returns:
        DataFrame: Jeu de donnees bornés pour les pertes de capitaux
    """    

    donnees['capital-loss'] = donnees['capital-loss'].apply(lambda x: 'perte' if x > 0 else 'pas_perte')

    return donnees

def regroupement(donnees) :
    """Après notre analyse, nous choisissons de regrouper certaines modalités pour les colonnes workclass, occupation, education et marital-status

    Args:
        donnees (DataFrame): Jeu de donnees

    Returns:
        DataFrame: Jeu de donnees avec les données regroupées
    """    
    
    # Workclass
    donnees['workclass'][(donnees['workclass'] == " Self-emp-not-inc") | (donnees['workclass'] == " Self-emp-inc")] = "self_worker"
    donnees['workclass'][(donnees['workclass'] == "Never-worked") | (donnees['workclass'] == "Without-pay") | (donnees['workclass'] == "?") ] = "other"
    donnees['workclass'][(donnees['workclass'] == " State-gov") | (donnees['workclass'] == " Federal-gov") | (donnees['workclass'] == " Local-gov")] = "gov"

    # Occupation
    donnees['occupation'][(donnees['occupation'] == " Exec-managerial") | (donnees['occupation'] == " Prof-specialty")] = "qualification_haute"
    donnees['occupation'][(donnees['occupation'] == " Tech-support") | (donnees['occupation'] == " Adm-clerical") | (donnees['occupation'] == " Machine-op-inspct")| (donnees['occupation'] == " Farming-fishing") | (donnees['occupation'] == " Transport-moving") | (donnees['occupation'] == " Sales")] = "qualification_moyenne"
    donnees['occupation'][(donnees['occupation'] == " Craft-repair") | (donnees['occupation'] == " Other-service") | (donnees['occupation'] == " Handlers-cleaners")| (donnees['occupation'] == " Priv-house-serv") | (donnees['occupation'] == " Protective-serv") | (donnees['occupation'] == " Armed-Forces")] = "qualification_faible"
    donnees['occupation'][(donnees['occupation'] == " ?")] = "Autre catégorie"

    # Education
    donnees['education'][(donnees['education'] == " 11th") | (donnees['education'] == " HS-grad") | (donnees['education'] == " Some-college")| (donnees['education'] == " 9th") | (donnees['education'] == " 7th-8th") | (donnees['education'] == " 12th") | (donnees['education'] == " 5th-6th") | (donnees['education'] == " Preschool") | (donnees['education'] == " 1st-4th")| (donnees['education'] == " 10th")] = "primaire_secondaire"
    donnees['education'][(donnees['education'] == " Bachelors") | (donnees['education'] == " Masters") | (donnees['education'] == " Doctorate")  | (donnees['education'] == " Prof-school")] = "niveau_superieur"

    #Marital-Status
    donnees['marital-status'][(donnees['marital-status'] == " Married-civ-spouse") | (donnees['marital-status'] == " Never-married") | (donnees['marital-status'] == " Married-spouse-absent")  | (donnees['marital-status'] == " Married-AF-spouse")] = "married"

    return donnees

def sal_dummies(donnees) : 
    """Application de 0 lorsque le salaire est inférieur ou égal à 50k et 1 lorsqu'il est supérieur à 50k

    Args:
        donnees (DataFrame): Jeu de données

    Returns:
        DataFrame: Jeu de données avec les dummies
    """    
    donnees['sal'].replace(['<=50K','>50K'],[0,1], inplace=True)

    return donnees