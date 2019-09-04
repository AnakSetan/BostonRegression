import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
#Buat Data Terlebih Dahulu
data = {
    'luas': np.arange(100,300,20),
    'harga':[500,665,720,795,885,1200,1500,1600,1775,2000]
}
df = pd.DataFrame(data)
print(df)

# plt.style.use('seaborn')
# plt.plot(df['luas'], df['harga'])
# plt.scatter(df['luas'],df['harga'])
# plt.show()

#MachineLearning #linear Regression
model = linear_model.LinearRegression() #BikinModelMachineLearningJenisLinearRegression
#model.fit(dataIndependent 2Dimensi, dependent)
#training model dengan data yang ktia punya
model.fit(df[['luas']],df['harga'])
m = model.coef_
c = model.intercept_
# print(m)
# print(c)
# print(model.predict([[100]]))
# print(model.predict([[3000]]))
# print(model.predict(df[['luas']]))#untuk semua harga

#plot data asli + best fit line
# plt.style.use('ggplot')
plt.plot(
    df['luas'],df['harga'],'ro',
    df['luas'],model.predict(df[['luas']]),'g-'
)
plt.grid(True)
plt.xlabel('luas(m2)')
plt.ylabel('harga(x100juta)')
plt.legend(['Data','Best Fit Line'])
plt.show()
