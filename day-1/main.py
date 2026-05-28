"""
import pandas as pd
import matplotlib.pyplot as plt

data =  pd.read_csv('data.csv')

plt.bar(data['day'], data['tip'], color='green')

plt.title('Bar Chart')

plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()
"""

import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

data = pd.read_excel('data2.xlsx')

data['Date'] = pd.to_datetime(data['Date']).dt.date


counts = pd.crosstab(data['Date'], data['Product'])

counts.plot(kind='bar', width=0.8)
plt.title('Bar Chart')
plt.xlabel('Date', fontsize=10)
plt.ylabel('Product')

plt.xticks(rotation=45)

plt.show()