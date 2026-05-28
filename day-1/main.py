import pandas as pd
import matplotlib.pyplot as plt

data =  pd.read_csv('data.csv')

plt.bar(data['day'], data['tip'], color='green')

plt.title('Bar Chart')

plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()