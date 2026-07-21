import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("titanic_clean.csv")

sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived')
plt.title('Age vs Fare')
plt.show()
