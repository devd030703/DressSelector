# %% [markdown]
"""
# Sample Images
- We would like to sample a twenty images from each of  the following categories:
    - for `Men` & `Women` 
    - further categorized by `Topwear`, `Shoes`, `Bottomwear`, `Headwear`

"""
# %%
import glob
import pandas as pd
import os

# %%
df = pd.read_csv(
    os.path.join('dataset', 'styles.csv',),
    error_bad_lines=False,
    index_col='id',
    dtype={
        'gender': 'category',
        'masterCategory': 'category',
        'subCategory': 'category',
        'articleType': 'category',
        'baseColour': 'category',
        'season': 'category',
        # 'year': int,
        'productDisplayName': 'category',
    },
).dropna().sort_index(ascending=True)

df.info()
df.head(3)
# %%
# df['gender'].value_counts()
# df['masterCategory'].value_counts()
# df['subCategory'].value_counts()
# df['articleType'].value_counts()[:50]
# df['baseColour'].value_counts()
# df['season'].value_counts()
# df['year'].value_counts()
# df['usage'].value_counts()
# df['productDisplayName'].value_counts()

# %%
df = df[
    df['gender'].isin(['Men', 'Women']) &
    df['subCategory'].isin(['Topwear', 'Shoes', 'Bottomwear', 'Headwear'])
]


# %%
df = df.groupby(['gender', 'subCategory']).apply(
    lambda x: x.sample(
        20,
        random_state=42
    )
).sort_index(ascending=True)
df.index = df.index.droplevel(['gender', 'subCategory'])
# %%
df.to_csv(
    os.path.join('fashion_dataset', 'styles_sample.csv',)
)
# %%

# write a script that looks up all ids and their respective filepaths
# globe module - to locate the file path of the images

for i in range(1, 1000):
    item_list = df.head(i).index.tolist()
    item_id_filepath = (str(item_list[0])+'.jpg')
    for name in glob.glob(
            '/Users/devdeepak/Desktop/GitHub/DressSelector/fashion_dataset/images/'+item_id_filepath):
        print(name)

# %%
