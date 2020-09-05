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


for k, v in models.items():
    print(f"{k}:{v}")
