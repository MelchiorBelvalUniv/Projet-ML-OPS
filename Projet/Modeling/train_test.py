from sklearn.model_selection import train_test_split
import pandas as pd

def train_test(donnees) :
    """Séparation du jeu de données en jeu d'apprentissage et de test. Notre jeu de test représente 25% du jeu de données.

    Args:
        donnees (DataFrame): Jeu de données

    Returns:
        X_train: _type_: _description_
        X_test: _type_: _description_
        y_train: _type_: _description_
        y_test: _type_: _description_
    """    

    df = donnees[['sal','age', 'capital-gain', 'education', 'hours-per-week', 'occupation', 'relationship']]
    X = df.drop('sal', axis=1)
    y=df['sal']
    X_dummy = pd.get_dummies(X,prefix_sep="_", drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X_dummy, y, test_size=0.25,
                                                    stratify=y,random_state=0)
    return X_train, X_test, y_train, y_test