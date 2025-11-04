import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_utsils import plot_nulls

df = pd.read_csv(r'student-mat-missing-data.csv')
plot_nulls(df)
