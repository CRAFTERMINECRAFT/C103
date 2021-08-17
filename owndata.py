import pandas as pd
import plotly.express as pl

datar = pd.read_csv("data.csv")
fig = pl.bar(datar, x = "Country", y = "InternetUsers")
fig.show()