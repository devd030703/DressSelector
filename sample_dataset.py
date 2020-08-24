from os import replace
import pandas as pd
import os

# %%
df = pd.read_csv(
    os.path.join('fashion_dataset', 'styles', 'styles.csv'),
    error_bad_lines=False,
    index_col='id',
).dropna().sort_index(ascending=True)

df.info()

df.head(3)
# %%
df['gender'].value_counts()
df['masterCategory'].value_counts()
df['subCategory'].value_counts()
df['articleType'].value_counts()[:50]
df['baseColour'].value_counts()
df['season'].value_counts()
df['year'].value_counts()
df['usage'].value_counts()
df['productDisplayName'].value_counts()

# %%
df[df['gender'] in ['Men', 'Women']]
# %%

# %%
df.groupby(['gender', 'subCategory']).apply(
    lambda x: x.sample(
        1,
        random_state=42
    )
)
# %%
