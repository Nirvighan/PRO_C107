import csv
import pandas as pd
import plotly.express as px



df = pd.read_csv('data.csv')

data = df.groupby("student_id", as_index = False)["attempt"].mean()


print(data)

fig = px.scatter(x = df["student_id"],y = df["level"],color =data,size = data)
fig.show() 