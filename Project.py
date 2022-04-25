import plotly.figure_factory as pff
import pandas as pd 
import csv 
df=pd.read_csv('prodata.csv')
fig = pff.create_distplot([df['Avg Rating'].tolist()],["Avgrage Rating"],show_hist=False)
fig.show()