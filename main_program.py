from infrastructure.importation import load_data
from preparation.transfo import *

data = load_data()

data = drop_na(data)
data = borne_age(data)
data = borne_heures(data)
data = borne_capital_gain(data)
data = borne_capital_loss(data)
data = regroupement(data)
data = sal_dummies(data)
