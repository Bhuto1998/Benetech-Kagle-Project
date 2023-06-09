#This file contains the implementation of the metric used in this competition. I got this in Kaggle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from rapidfuzz.distance.Levenshtein import distance as levenshtein
from sklearn.metrics import r2_score


def sigmoid(x):
    return 2 - 2 / (1 + np.exp(-x))


def normalized_rmse(y_true, y_pred):
    # The argument to the sigmoid transform is equal to
    # rmse(y_true, y_pred) / rmse(y_true, np.mean(y_true))
    return sigmoid((1 - r2_score(y_true, y_pred)) ** 0.5)


def normalized_levenshtein_score(y_true, y_pred):
    total_distance = np.sum([levenshtein(yt, yp) for yt, yp in zip(y_true, y_pred)])
    length_sum = np.sum([len(yt) for yt in y_true])
    return sigmoid(total_distance / length_sum)


def score_series(y_true, y_pred):
    if len(y_true) != len(y_pred):
        return 0.0
    if isinstance(y_true[0], str):
        return normalized_levenshtein_score(y_true, y_pred)
    else:
        return normalized_rmse(y_true, y_pred)


def benetech_score(ground_truth: pd.DataFrame, predictions: pd.DataFrame) -> float:
    """Evaluate predictions using the metric from the Benetech - Making Graphs Accessible.

    Parameters
    ----------
    ground_truth: pd.DataFrame
        Has columns `[data_series, chart_type]` and an index `id`. Values in `data_series`
        should be either arrays of floats or arrays of strings.

    predictions: pd.DataFrame
    """
    if not ground_truth.index.equals(predictions.index):
        raise ValueError("Must have exactly one prediction for each ground-truth instance.")
    if not ground_truth.columns.equals(predictions.columns):
        raise ValueError(f"Predictions must have columns: {ground_truth.columns}.")
    pairs = zip(ground_truth.itertuples(index=False), predictions.itertuples(index=False))
    scores = []
    for (gt_series, gt_type), (pred_series, pred_type) in pairs:
        if gt_type != pred_type:  # Check chart_type condition
            scores.append(0.0)
        else:  # Score with RMSE or Levenshtein as appropriate
            scores.append(score_series(gt_series, pred_series))
    return np.mean(scores)

#Sample use case


ground_truth = pd.DataFrame.from_dict({
    '0a0a0_x': (['abc', 'def', 'ghi'], 'vertical_bar'),
    '0a0a0_y': ([0, 1, 2], 'vertical_bar'),
    '1b1b1_x': ([101.24, 90.3, 50.51], 'scatter'),
    '1b1b1_y': ([43.81, 10.12, 11.0], 'scatter'),
}, orient='index', columns=['data_series', 'chart_type']).rename_axis('id')

predictions = pd.DataFrame.from_dict({
    '0a0a0_x': (['a', 'difd', 'ghi'], 'vertical_bar'),
    '0a0a0_y': ([0.2, 0.9, 2.1], 'vertical_bar'),
    '1b1b1_x': ([101.24, 90.3, 50.51], 'dot'),  # wrong chart_type
    '1b1b1_y': ([43.81, 10.12, 11.0, 5.4], 'scatter'),  # wrong number of values in data_series
}, orient='index', columns=['data_series', 'chart_type']).rename_axis('id')



print(benetech_score(ground_truth, predictions))



