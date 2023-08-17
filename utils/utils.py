import base64
import io

import pandas as pd
from sklearn.model_selection import RandomizedSearchCV


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            raise NotImplementedError(
                'Support for this file is not implemented yet',
            )
        return df
    except Exception as e:
        print(e)
        return pd.DataFrame()


def find_model_best_params(X, y, estimator, param_distributions, n_iter, scoring, n_jobs):
    search = RandomizedSearchCV(
        estimator, param_distributions, n_iter=n_iter, scoring=scoring, n_jobs=n_jobs,
    )
    search.fit(X, y)
    return search.best_params_
