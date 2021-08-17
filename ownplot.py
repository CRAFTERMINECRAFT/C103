import pandas as pd
import plotly.express as pl

datar = pd.read_csv("line_chart.csv")
fig = pl.line(datar, x = "Year", y = "Per capita income", color = "Country", title = "Per capita income")
fig.show()