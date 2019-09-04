import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sb

data = {
    'luas':[2500,3000,3200,3600,4000],
    'kamar':[2,3,3,2,4],
    'usiarumah': [10,15,20,18,8],
    'harga':[500,550,620,600,720]
}

df = pd.DataFrame(data)
print(df)
#multivariate linear regression
#y = m1x1 + m2x2 + m3x3 + c
model = linear_model.LinearRegression()
model.fit(df[['luas','kamar','usiarumah']],df['harga'])
print(model.coef_)
print(model.intercept_)
#untuk memasukkan data yang kita suka, harus urut sesusai dengan datanya (luas, kamar, usiarumah)
print(model.predict([[1000,5,1]]))
corr = df.corr()#korelsai antar kolom, mendekati 100% lebih baik untuk di olah, hindari yang minus
print(corr)


sb.heatmap(corr)
plt.show()