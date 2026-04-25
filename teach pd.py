import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df['Age'].hist(bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()