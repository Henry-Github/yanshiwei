from views import build_app
# from algorithm_source.check_3 import run

if __name__ == '__main__':
    # names = [
    #     'LogisticRegression',
    #     'RidgeClassifier',
    #     'SGDClassifier',
    #     'PassiveAggressiveClassifier',
    #     'KNeighborsClassifier',
    #     'DecisionTreeClassifier',
    #     'ExtraTreeClassifier',
    #     'SVC',
    #     'GaussianNB',
    #     'AdaBoostClassifier',
    #     'BaggingClassifier',
    #     'RandomForestClassifier',
    #     'ExtraTreesClassifier',
    #     'GradientBoostingClassifier'
    # ]
    # run(names)
    app = build_app()
    app.run(port=8000, debug=True)

