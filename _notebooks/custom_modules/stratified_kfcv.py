"""A custom module for stratified k-fold cross-validation in regression problems.
author: Miguel Antonio H. Germar"""

import pandas as pd
from sklearn.metrics import mean_squared_error

def stratify_continuous(n_folds, y, random_state = 1):
    """Stratify a dataset on a continuous target.

    n_folds: integer of folds to form.
    y: Series containing target values.
    random_state: integer used as random seed, default 1.

    Returns: Series of integers representing fold numbers."""

    if n_folds < 2 or n_folds > 10:
        raise ValueError("Please select a number of folds from 2 to 10.")
    
    fold_nums = list(range(n_folds))

    # DataFrame where "index" column contains the original indices
    df = pd.DataFrame(
        y
        # Shuffle before ranking so that cars with the same price are ordered randomly.
        .sample(frac = 1, random_state = random_state, ignore_index = False)
    )

    # This column gives a rank to each value in y. 0 is the rank of the lowest value.
    # Ties are broken according to order of appearance.
    df["rank"] = df[y.name].rank(method = "first") - 1

    df["fold"] = 0

    for f in fold_nums[1:]:
        # start at f, then increment by n_folds
        indices = list(range(f, df.shape[0], n_folds))
        df.loc[df["rank"].isin(indices), "fold"] = f

    # Revert df to original order of indices
    df = df.reindex(index = y.index)

    # A series that indicates the fold number of each observation according to its original position in y
    fold_series = df["fold"].copy()

    return fold_series

def split_folds(X, y, fold_series, test_fold):
    """Take a dataset whose observations have been grouped into folds,
    then perform a train-test split.
    
    X, y: feature and target DataFrames.
    fold_series: Series containing the fold numbers of the observations.
    test_fold: Integer, the fold number that will be used as the test fold.

    Returns: tuple of four DataFrames"""

    if fold_series.dtype != "int64":
        raise AttributeError("The fold list does not purely contain integers.")

    test_mask = (fold_series == test_fold)

    X_train = X.loc[~test_mask].copy()
    y_train = y.loc[~test_mask].copy()

    X_test = X.loc[test_mask].copy()
    y_test = y.loc[test_mask].copy()

    return X_train, X_test, y_train, y_test

def stratified_kfcv(X, y, fold_series, regression_model):
    """Conduct k-fold cross-validation on a stratified dataset.

    X, y: feature and target DataFrames.
    fold_series: Series that indicates the fold number of each observation.
    regression_model: instance of a scikit-learn class for regression. Must have fit() and predict() methods.

    returns: list of floats representing MSE values"""

    fold_nums = fold_series.unique()

    mse_lst = []

    for f in fold_nums:
        X_train, X_test, y_train, y_test = split_folds(
            X = X,
            y = y,
            test_fold = f,
            fold_series = fold_series,
        )
        
        regression_model.fit(X_train, y_train)
        y_pred = regression_model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        mse_lst.append(mse)

    return mse_lst