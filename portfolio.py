# Get purchase date of stocks

import yfinance as yf
import matplotlib.pyplot as plt

stocks_bought = {'MTTR', 'DGE', 'LGEN.L', 'LCID', 'TRMB', 'VUSA.L', 'RR.L', 'ULVR.L'}

data = yf.download(stocks_bought, '2021-1-1')['Adj Close']

# Plot the prices at close only
((data.pct_change() + 1).cumprod()).plot(figsize=(10, 7))

# Show the legend
plt.legend()

# Define the label for the title of the figure
plt.title("Returns", fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Cumulative Returns', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()
