import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# pd.set_option("display.max_row", None)
# df = pd.read_csv("titanic.csv")

df['Embarked'] = df['Embarked'].fillna('S')
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.drop(columns=['Cabin'])

df.to_csv("titanic_clean.csv", index=False)

print(df.isnull().sum())
# df['Age'].hist(bins=20)
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()