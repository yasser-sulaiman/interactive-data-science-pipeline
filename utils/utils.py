import base64
import io

import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from dash import html


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


def get_column_summary(df, col):
    data = df.loc[:,col]

    summary = data.describe()

    return_list = []
    
    return_list.append(html.Div(f"Column Name: { col }", className="column-summary-item"))
    return_list.append(html.Div(f"Non Null Values: { sum(~data.isna()) }", className="column-summary-item"))
    return_list.append(html.Div(f"Null Values: { sum(data.isna()) }", className="column-summary-item")) 

    try:
        return_list.append(html.Div(f"Mean: { round(summary['mean'], 4) }", className="column-summary-item")) 
        return_list.append(html.Div(f"STD: { round(summary['std'], 4) }", className="column-summary-item")) 
        return_list.append(html.Div(f"MIN: { round(summary['min'], 4) }")) 
        return_list.append(html.Div(f"1st quartile: { round(summary['25%'], 4) }", className="column-summary-item")) 
        return_list.append(html.Div(f"2nd quartile: { round(summary['50%'], 4) }", className="column-summary-item")) 
        return_list.append(html.Div(f"3rd quartile: { round(summary['75%'], 4) }", className="column-summary-item"))
        return_list.append(html.Div(f"MAX: { round(summary['max'], 4) }", className="column-summary-item")) 

    except:
        return_list.append(html.Div(f"Unique Values: { summary['unique'] }")) 
        return_list.append(html.Div(f"Most Frequent Value: {summary['top']}", className="column-summary-item")) 
        return_list.append(html.Div(f"Frequency: {summary['freq']}", className="column-summary-item")) 
                
    return return_list