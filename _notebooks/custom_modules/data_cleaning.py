"""A module for custom data cleaning functions.
author: Miguel Antonio H. Germar"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import chardet

def csv_from_gdrive(url):
    
    """Take the URL of a CSV file in Google Drive and return a new URL that allows the file to be downloaded using `pd.read_csv()`.
    
    url: str, the URL of a CSV file in Google Drive.
    
    Returns: str, a URL"""
    
    file_id = url.split('/')[-2]
    download_url = 'https://drive.google.com/uc?id=' + file_id
    
    return download_url

def detect_encoding(filename):
    """Take a text file and detect its encoding.
    The output is a dictionary with a key "encoding" whose value is a string.
    The value may be passed to the encoding parameter of pd.read_csv()
    
    filename: str, absolute or relative path of a file along with its name and extension
    
    Returns: dict"""

    with open(filename, 'rb') as file:
        result = chardet.detect(file.read())

    return result

def plot_null_matrix(df, figsize = (18,15)):

    """Take a DataFrame, identify null values, and plot them on a heatmap.
    
    df: DataFrame, contains tidy data
    figsize: 2-tuple of int, to be passed to plt.figure()"""

    # Initiate the figure
    plt.figure(figsize = figsize)
    
    # Create a boolean dataframe based on whether the values are null
    df_null = df.isnull()
    
    # Create a heatmap of the boolean dataframe
    sns.heatmap(
        ~df_null, # Take the bitwise NOT of the df. (Reverse boolean values.)
        cbar = False, # Do not include a color bar.
        yticklabels = False, # Do not show y-tick labels.
    )
    plt.xticks(rotation = 90, size = 'x-large')
    plt.show()

    return None