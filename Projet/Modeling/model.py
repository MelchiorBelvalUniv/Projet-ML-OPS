from sklearn.linear_model import LogisticRegression

def fit_logistic_regression(X_train, y_train) : 
    """Fitting du modèle sur les données d'apprentissage et de test

    Args:
        X_train (_type_): _description_
        X_test (_type_): _description_
        y_train (_type_): _description_
        y_test (_type_): _description_

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