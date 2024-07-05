import pandas as pd

df = pd.read_csv('Data/pokemon_data.csv')


#sprint(df.head)
#iloc(row,column)
#print(df.iloc[2,1])

# for index,row in df.iterrows():
#     print(index,row['Name'])

print(df.loc[df['Type 1'] == "Grass"] )