import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("titanic_clean.csv")

def age_group(age):
    if age < 18:
        return 'child'
    elif age < 60:
        return 'adult'
    else:
        return 'elderly'

df['AgeGroup'] = df['Age'].apply(age_group)
print(df['AgeGroup'].value_counts())

print(df.groupby(['AgeGroup','Sex'])['Survived'].mean())
df.to_csv("titanic_clean.csv", index=False)


# df['Age'].hist(bins=20)
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()