from infrastructure.importation import importation
from preparation.transfo import *

data = importation()

data = drop_na(data)
data = borne_age(data)
data = borne_heures(data)
data = borne_capital_gain(data)
data = borne_capital_loss(data)
data = regroupement(data)
data = sal_dummies(data)