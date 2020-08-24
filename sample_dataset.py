import pandas as pd
import os

df = pd.read_csv(
    os.path.join('fashion_dataset', 'styles', 'styles.csv'),
    index_col='id',

)
