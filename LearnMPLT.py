import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('D:\Downloads\PlPlayers.xlsx')
print(df.head())
plt.bar(df['Player_Name'],df['Assists'])
plt.title('Players number of assists')
plt.ylabel('Assists')
plt.xlabel('Player Name')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()