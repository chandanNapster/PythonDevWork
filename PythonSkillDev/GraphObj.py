import pandas as pd
import seaborn as sb
# import plotly.graph_objects as go

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')


# print(df.head)
# print(df.columns)

x_value = df['AAPL_x']
y_value = df['AAPL_y']

df.plot.scatter(x=x_value, y=y_value)

# sb.scatterplot(df['AAPL_x'], df['AAPL_y'])


# fig = go.Figure(go.Scatter(x=df['AAPL_x'], y=df['AAPL_y'],
#                            name='Share Prices (in USD)'))

# fig.update_layout(title='Apple Share Prices over time (2014)',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)

# fig.show()
