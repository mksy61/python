import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LassoLars
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import GammaRegressor
from sklearn.linear_model import PoissonRegressor
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import TweedieRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("train.csv")
X = df[['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF',
        'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']]
y = df["SalePrice"]

models = dict()
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=61)

model = DecisionTreeRegressor(random_state=1)
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = Ridge()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = Lasso()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = ElasticNet()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = LassoLars()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = BayesianRidge()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = LogisticRegression(max_iter=100)
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = GammaRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = PoissonRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = HuberRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = TweedieRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

model = RandomForestRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
models[str(type(model))] = val_mae

for k, v in models.items():
    print(f"{k}:{v}")

"""
<class 'sklearn.tree._classes.DecisionTreeRegressor'>:29228.96712328767
<class 'sklearn.linear_model._base.LinearRegression'>:28589.835514103168
<class 'sklearn.linear_model._ridge.Ridge'>:28588.983234742693
<class 'sklearn.linear_model._coordinate_descent.Lasso'>:28589.722016086114
<class 'sklearn.linear_model._coordinate_descent.ElasticNet'>:28736.657736926678
<class 'sklearn.linear_model._least_angle.LassoLars'>:28586.297309171194
<class 'sklearn.linear_model._bayes.BayesianRidge'>:28577.915718501103
<class 'sklearn.linear_model._logistic.LogisticRegression'>:43482.191780821915
<class 'sklearn.linear_model._glm.glm.GammaRegressor'>:57726.754047663686
<class 'sklearn.linear_model._glm.glm.PoissonRegressor'>:57726.754047663686
<class 'sklearn.linear_model._huber.HuberRegressor'>:32022.141050914273
<class 'sklearn.linear_model._glm.glm.TweedieRegressor'>:34614.4810391937
"""
