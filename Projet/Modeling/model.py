from sklearn.linear_model import LogisticRegression

def fit_logistic_regression(X_train, y_train) : 
    """Fitting du modèle sur les données d'apprentissage et de test

    Args:
        X_train (DataFrame): Les valeurs des variables pour entrainer le modèle
        X_test (DataFrame): Les valeurs des variables pour tester le modèle
        y_train (DataFrame): Les valeurs de la variables à expliquer pour comparer les résultats sur l'entrainement
        y_test (DataFrame): Les valeurs de la variables à expliquer pour comparer les résultats sur le test

    Returns:
        _type_: Prédiction sur le jeu de données
    """    

    logit = LogisticRegression(C = 0.1, penalty = 'l2', solver = 'newton-cg')
    logit.fit(X_train, y_train)

    return logit 

def predict_logistic_regression(logit, X_test) :
    """On reprend le modèle précédemment entrainé et on le test

    Args:
        logit (_type_): _description_
        X_test (_type_): _description_

    Returns:
        _type_: Prédictions
    """    
    y_pred = logit.predict(X_test)

    return y_pred
