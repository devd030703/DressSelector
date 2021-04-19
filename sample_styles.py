# %% [markdown]
"""
# Sample Images
- We would like to sample a twenty images from each of  the following categories:
    - for `Men` & `Women` 
    - further categorized by `Topwear`, `Shoes`, `Bottomwear`, `Headwear`
"""
import os

# %%
import pandas as pd

# %%
# read data, use first cololumn as index, set coloumns, drop nulls, sort ascending by ID
df = (
    pd.read_csv(
        os.path.join(
            "dataset",
            "styles.csv",
        ),
        error_bad_lines=False,
        index_col="id",
        dtype={
            "gender": "category",
            "masterCategory": "category",
            "subCategory": "category",
            "articleType": "category",
            "baseColour": "category",
            "season": "category",
            "productDisplayName": "category",
        },
    )
    .dropna()
    .sort_index(
        ascending=True,
    )
)

df.info()
df.head(3)


# %%
# select only rows where gender is Men/Women and subCategory exist in list
df = df[
    df["gender"].isin(["Men", "Women"])
    & df["subCategory"].isin(["Topwear", "Shoes", "Bottomwear", "Headwear"])
]

# %%
# group by gender and subCategory, take 20 random rows and sort index in ascending order, droplevels, unstack
df = (
    df.groupby(["gender", "subCategory"])
    .apply(lambda x: x.sample(20, random_state=42))
    .sort_index(
        ascending=True,
    )
)

df.index = df.index.droplevel(["gender", "subCategory"])

# %%
df.to_csv(
    os.path.join(
        "dataset",
        "database",
        "ItemCatalogueSample.csv",
    )
)
