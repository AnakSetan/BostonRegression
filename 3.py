#sklearn toy datasets
import pandas as pd
from sklearn.datasets import load_boston
import numpy as np

dataBoston = load_boston()
# print(dir(dataBoston))
# print(dataBoston['data'].shape)
# print(dataBoston['feature_names'])
# print(dataBoston['target'])

#buatdataframe
df = pd.DataFrame(
    dataBoston['data'],
    columns = dataBoston['feature_names']
)
print(df)