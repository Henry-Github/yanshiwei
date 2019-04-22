from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import Lars
from sklearn.linear_model import LassoLars
from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import TheilSenRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from typing import List

names = [
    'LinearRegression',
    'Lasso',
    'Ridge',
    'ElasticNet',
    'HuberRegressor',
    'Lars',
    'LassoLars',
    'PassiveAggressiveRegressor',
    'RANSACRegressor',
    'SGDRegressor',
    'TheilSenRegressor',
    'KNeighborsRegressor',
    'DecisionTreeRegressor',
    'ExtraTreeRegressor',
    'SVR',
    'AdaBoostRegressor',
    'BaggingRegressor',
    'RandomForestRegressor',
    'ExtraTreesRegressor',
    'GradientBoostingRegressor'
]


def get_models(methods=List):
    models = dict()
    # linear models
    if 'LinearRegression' in methods:
        models['lr'] = LinearRegression()

    alpha = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    if 'Lasso' in methods:
        for a in alpha:
            models['lasso-' + str(a)] = Lasso(alpha=a)
    if 'Ridge' in methods:
        for a in alpha:
            models['ridge-' + str(a)] = Ridge(alpha=a)
    if 'ElasticNet' in methods:
        for a1 in alpha:
            for a2 in alpha:
                name = 'en-' + str(a1) + '-' + str(a2)
                models[name] = ElasticNet(a1, a2)
    if 'HuberRegressor' in methods:
        models['huber'] = HuberRegressor()
    if 'Lars' in methods:
        models['lars'] = Lars()
    if 'LassoLars' in methods:
        models['llars'] = LassoLars()
    if 'PassiveAggressiveRegressor' in methods:
        models['pa'] = PassiveAggressiveRegressor(max_iter=1000, tol=1e-3)
    if 'RANSACRegressor' in methods:
        models['ranscac'] = RANSACRegressor()
    if 'SGDRegressor' in methods:
        models['sgd'] = SGDRegressor(max_iter=1000, tol=1e-3)
    if 'TheilSenRegressor' in methods:
        models['theil'] = TheilSenRegressor()
    # non-linear models
    if 'KNeighborsRegressor' in methods:
        n_neighbors = range(1, 21)
        for k in n_neighbors:
            models['knn-' + str(k)] = KNeighborsRegressor(n_neighbors=k)
    if 'DecisionTreeRegressor' in methods:
        models['cart'] = DecisionTreeRegressor()
    if 'ExtraTreeRegressor' in methods:
        models['extra'] = ExtraTreeRegressor()
    if 'SVR' in methods:
        models['svml'] = SVR(kernel='linear')
        models['svmp'] = SVR(kernel='poly')
        c_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        for c in c_values:
            models['svmr' + str(c)] = SVR(C=c)
    # ensemble models
    n_trees = 100
    if 'AdaBoostRegressor' in methods:
        models['ada'] = AdaBoostRegressor(n_estimators=n_trees)
    if 'BaggingRegressor' in methods:
        models['bag'] = BaggingRegressor(n_estimators=n_trees)
    if 'RandomForestRegressor' in methods:
        models['rf'] = RandomForestRegressor(n_estimators=n_trees)
    if 'ExtraTreesRegressor' in methods:
        models['et'] = ExtraTreesRegressor(n_estimators=n_trees)
    if 'GradientBoostingRegressor' in methods:
        models['gbm'] = GradientBoostingRegressor(n_estimators=n_trees)
    print('Defined %d models' % len(models))
    return models
