from .check_2 import run
from typing import Tuple

methods = [
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


def test_res_type():
    assert isinstance(run(methods), Tuple)


if __name__ == '__main__':
    test_res_type()
