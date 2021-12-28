"""A custom module for stratified k-fold cross-validation.
author: Miguel Antonio H. Germar"""

import pandas as pd
from sklearn.metrics import mean_squared_error

def stratify_continuous(n_folds, data, target_col, fold_col = "fold"):
    """Stratify a dataset on a continuous target.

n_folds: Integer of folds to form.
data: DataFrame containing at least the target column.
target_col: String representing the target.
fold_col: String, the name of the new column that will be added to the data.

Returns: DataFrame"""

    if n_folds < 2 or n_folds > 10:
        raise ValueError("Please select a number of folds from 2 to 10.")

    if fold_col in data.columns:
        raise IndexError(f"{fold_col} is already in the columns.")
    
    fold_nums = list(range(n_folds))
    data = (
        data
        # Shuffle before sorting so that observations with the same target value are ordered randomly.
        .sample(frac = 1, random_state = 1)
        .sort_values(target_col, ascending = True)
        .reset_index(drop = True)
    )
    data[fold_col] = 0

    for f in fold_nums[1:]:
        # start at f, then increment by n_folds
        indices = list(range(f, data.shape[0], n_folds))
        data.loc[indices, fold_col] = f

    return data

def split_folds(data, feature_cols, target_col, test_fold, fold_col = "fold"):
    """Take a dataset whose observations have been grouped into folds,
    then perform a train-test split.
    
data: DataFrame with feature and target data.
feature_cols: list of str, the names of the feature columns.
target_col: str, the name of the target column.
test_fold: int, the numeric label of the fold that will be considered as the testing set. This can range from 0 to n_folds - 1.
fold_col: str, the name of the column that indicates the fold of each observation.

Returns: tuple of DataFrame"""

    if data[fold_col].dtype != "int64":
        raise AttributeError("The 'fold' column is not an int64 column.")

    test = data[data[fold_col] == test_fold]
    train = data[data[fold_col] != test_fold]

    X_train = train[feature_cols].copy()
    y_train = train[target_col].copy()

    X_test = test[feature_cols].copy()
    y_test = test[target_col].copy()

    return X_train, X_test, y_train, y_test

def stratified_kfcv(data, feature_cols, target_col, regression_model, fold_col = "fold"):
    """Conduct k-fold cross-validation on a stratified dataset.

data: DataFrame with feature and target data.
feature_cols: list of str, the names of the feature columns.
target_col: str, the name of the target column.
regression_model: instance of a scikit-learn class for regression. Must have fit() and predict() methods.
fold_col: str, the name of the column that indicates the fold of each observation.

returns: list of float"""

    fold_nums = data[fold_col].unique()

    mse_lst = []

    for f in fold_nums:
        X_train, X_test, y_train, y_test = split_folds(
            data,
            feature_cols = feature_cols,
            target_col = target_col,
            test_fold = f,
            fold_col = fold_col,
        )
        
        regression_model.fit(X_train, y_train)
        y_pred = regression_model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        mse_lst.append(mse)

    return mse_lst