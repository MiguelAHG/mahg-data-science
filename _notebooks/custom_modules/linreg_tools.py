"""A custom module for functions that I often use in linear regression projects.
author: Miguel Antonio H. Germar"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor as sm_vif

def get_vif(X):

    """Obtain a VIF value for each feature in a X.
Return a single-column DataFrame containing VIF values.

X: DataFrame containing continuous feature data.

Returns: DataFrame with one column."""
    
    vif_df = pd.DataFrame() 
    vif_df["feature"] = X.columns
    vif_df["VIF"] = [
        sm_vif(X.values, i)
        for i in range(len(X.columns))
    ]
    vif_df.set_index("feature", inplace = True)

    return vif_df

def extract_summary(ols_summary, vif_df):

    """Take an OLS results summary and split it into three tables.
Merge the second table with a DataFrame returned from get_vif().
Return a list of the tables as DataFrames.

ols_summary: The object returned by statsmodels.OLS.fit().summary()
vif_df: DataFrame returned by get_vif()

Returns: list of DataFrame
"""

    tables = []
    t_inds = list(range(3))

    for i in t_inds:
        table_as_html = ols_summary.tables[i].as_html()

        table_df = pd.read_html(
            table_as_html,
            header = (0 if i == 1 else None), # Only set a header for table 2.
            index_col = 0,
        )[0]

        tables.append(table_df)

        if i == 1:
            # Combine summary table 1 with the VIF column.
            table_df = pd.concat([table_df, vif_df], axis = 1)
            table_df.rename_axis("label", inplace = True)

        else:
            # For tables 0 and 2, turn the index back into a column.
            table_df = tables[i].reset_index()

        tables[i] = table_df

    return tables

def par_reg_plot(data, feature_cols, main_feature, target_col, obs_labels = False):
    
    """Take a feature and plot its partial regression plot, which takes the other features into account.

data: DataFrame containing features and target as columns.
feature_cols: List of features or predictor used in linear regression.
main_feature: String representing the feature whose partial regression plot will be generated.
target_col: String representing the target variable.
obs_labels: Boolean, whether or not to show index labels of observations in the plot.

Returns: None"""
    
    title = f"Partial Regression Plot\nSAT Score against {main_feature}"
    x_label = f"{main_feature}\nPartial Residuals"
    
    # List of all IVs other than the current one.
    others = [col for col in feature_cols if col != main_feature]
    
    fig = sm.graphics.plot_partregress(
        endog = target_col,
        exog_i = main_feature,
        exog_others = others,
        data = data,
        obs_labels = obs_labels,
    )
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(f"{target_col}\nPartial Residuals")
    plt.grid(True)
    plt.legend(
        labels = ["Actual partial residuals", "Trend line"],
        loc = "best",
    )
    plt.tight_layout(
        h_pad = 2,
    )
    
    plt.show()

    return None