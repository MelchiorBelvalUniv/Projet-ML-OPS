from sklearn.model_selection import train_test_split
import pandas as pd

def train_test(donnees) :
    """Séparation du jeu de données en jeu d'apprentissage et de test. Notre jeu de test représente 25% du jeu de données.

    Args:
        donnees (DataFrame): Jeu de données

    Returns:
        X_train (DataFrame): Les valeurs des variables pour entrainer le modèle
        X_test (DataFrame): Les valeurs des variables pour tester le modèle
        y_train (DataFrame): Les valeurs de la variables à expliquer pour comparer les résultats sur l'entrainement
        y_test (DataFrame): Les valeurs de la variables à expliquer pour comparer les résultats sur le test
    """    

    df = donnees[['sal','age', 'capital-gain', 'education', 'hours-per-week', 'occupation', 'relationship']]
    X = df.drop('sal', axis=1)
    y=df['sal']
    X_dummy = pd.get_dummies(X,prefix_sep="_", drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X_dummy, y, test_size=0.25,
                                                    stratify=y,random_state=0)
    return X_train, X_test, y_train, y_test
