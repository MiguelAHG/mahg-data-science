"""A custom module for functions that I often use in OLS linear regression projects with statsmodels.
author: Miguel Antonio H. Germar"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sms
from statsmodels.stats.outliers_influence import variance_inflation_factor as sm_vif

def correlation_heatmap(corr):

    """Take a correlation matrix and plot it as a heatmap. Note that I am not the author. This was adapted from code provided in a Dataquest course.

    corr: DataFrame returned by pd.DataFrame.corr()"""
    
    # Create a mask that selects the bottom left triangle of the data.
    corr = corr.iloc[1:, :-1]
    mask = np.triu(np.ones_like(corr), k = 1)
    
    # Plot a heatmap of the values.
    plt.figure(figsize = (20,14))
    ax = sns.heatmap(
        corr,
        vmin = -1, # Anchor colors on -1 and 1.
        vmax = 1,
        cbar = False, # Do not draw a color bar.
        cmap = 'RdBu', # Use Red for negatives and Blue for positives.
        mask = mask, # Use a mask to remove the upper right triangle of the matrix.
        annot = True, # Write the data value in each cell.
    )
    
    # Format the text in the plot to make it easier to read.
    for text in ax.texts:
        t = float(text.get_text())
        
        if -0.01 < t < 0.01: # Remove data values with very low correlation.
            text.set_text('')
        else: # Round all visible data values to the hundredths place.
            text.set_text(round(t, 2))
        
        text.set_fontsize('x-large')
    
    plt.xticks(rotation = 90, size = 'x-large') # Rotate x-ticks to read from top to bottom.
    plt.yticks(rotation = 0, size = 'x-large')

    plt.show()

    return None

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

    Returns: list of DataFrame"""

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
            table_df = pd.concat(objs = [table_df, vif_df], axis = 1)
            table_df.rename_axis("feature", inplace = True)

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
    
    fig = sms.graphics.plot_partregress(
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