from __future__ import annotations

from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as knn_clf

from model.parameter_search_settings import *
from utils.utils import find_model_best_params


def train_supervised(X, y, model, test_size=0.1):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
    )

    _, X_dev, _, y_dev = train_test_split(
        X_train,
        y_train,
        test_size=0.2,
    )

    if model == 'logistic-regression':
        best_params = find_model_best_params(
            X=X_dev, y=y_dev, **LOGISTIC_REGRESSION,
        )
        clf = LogisticRegression(**best_params)

    elif model == 'knn':
        best_params = find_model_best_params(
            X=X_dev, y=y_dev, **KNN_CLF,
        )
        clf = knn_clf(**best_params)

    elif model == 'd-tree':
        best_params = find_model_best_params(
            X=X_dev, y=y_dev, **D_TREE,
        )
        clf = tree.DecisionTreeClassifier(**best_params)

    trained_model = clf.fit(X_train, y_train)

    preds_train = trained_model.predict(X_train)
    train_acc = accuracy_score(y_train, preds_train)

    preds_test = trained_model.predict(X_test)
    test_acc = accuracy_score(y_test, preds_test)

    return {
        'trained_model': trained_model,
        'test_acc': test_acc,
        'train_acc': train_acc,
    }
