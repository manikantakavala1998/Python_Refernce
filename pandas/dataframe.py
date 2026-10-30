import pandas as pd
data = {
    "calories":[420, 400, 380],
    "duration":[50,40,45]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0, 1]])