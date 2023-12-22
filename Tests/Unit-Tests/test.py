import pytest

def nb_val_sal(donnees):
    assert  all(val in ['< 17', '[17,26[', '[26,33[', '[33, 41[', '[41,50[', '>50]'] for val in donnees['age'].unique())

def nb_val_hours(donnees):
    assert  all(val in ['>40', '< 40'] for val in donnees['hours-per-week'].unique())

def nb_val_hours(donnees):
    assert  all(val in ['gain','pas_gain'] for val in donnees['capital_gain'].unique())

def nb_val_hours(donnees):
    assert  all(val in ['perte' ,'pas_perte'] for val in donnees['capital_loss'].unique())

def nb_val_workclass(donnees):
    assert  all(val in ['self_worker' ,'other','gov'] for val in donnees['workclass'].unique())

def nb_val_occupation(donnees):
    assert  all(val in ['qualification_haute' ,'qualification_moyenne','qualification_faible','Autre catégorie'] for val in
donnees['occupation'].unique())


def nb_val_education(donnees):
    assert  all(val in ['primaire_secondaire' ,'niveau_superieur','niveau_intermediaire'] for val in donnees['education'].unique())



def nb_val_marital_status(donnees):
    assert  all(val in ['Divorced' , 'married' , 'Separated', 'Widowed'  ] for val in donnees['marital-status'].unique())

def nb_col_assert(donnees):
    assert donnees.shape[0] != 0


def nb_li_assert(donnees):
     assert donnees.shape[1] != 0


