import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_nulls(DataFrame):
    column_with_NaN = []
    amount_of_NaN = []
    for column in DataFrame.columns:
        if DataFrame[column].isnull().any():
            column_with_NaN.append(column)
            amount_of_NaN.append(DataFrame[column].isnull().sum())
    df_NaN = pd.DataFrame({'Column': column_with_NaN, 'Amount of NaN': amount_of_NaN})
    sns.barplot(df_NaN, x='Column', y='Amount of NaN')
    plt.show()
    return df_NaN