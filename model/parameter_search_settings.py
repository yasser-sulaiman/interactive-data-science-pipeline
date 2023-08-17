from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier as knn_clf


LOGISTIC_REGRESSION = {
    'estimator': LogisticRegression(),
    'param_distributions': {
        'solver': ['lbfgs', 'liblinear', 'saga'],
        'max_iter': [100, 150, 200],
        'warm_start': [True, False],
    },
    'n_iter': 50,
    'scoring': 'accuracy',
    'n_jobs': 4,
}

KNN_CLF = {
    'estimator': knn_clf(),
    'param_distributions': {
        'n_neighbors': range(3, 20),
        'weights': ['uniform', 'distance'],
        'p': [1, 2, 3, 4],
    },
    'n_iter': 50,
    'scoring': 'accuracy',
    'n_jobs': 4,
}

D_TREE = {
    'estimator': tree.DecisionTreeClassifier(),
    'param_distributions': {
        'criterion': ['gini', 'entropy', 'log_loss'],
        'splitter': ['best', 'random'],
        'min_samples_split': range(2, 10),
    },
    'n_iter': 50,
    'scoring': 'accuracy',
    'n_jobs': 4,
}
