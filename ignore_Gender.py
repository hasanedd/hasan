import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
%matplotlib inline

df = pd.read_csv('https://raw.githubusercontent.com/QueraTeam/college-ml/main/ML_intro/6-%20machine%20learning%20in%20practice/weight_dataset.csv', encoding='cp1252')
# take a look at the dataset
df.head()

# summarize the data
df.describe()

cdf = df[['Height', 'Weight']]
cdf.head(9)

viz = cdf[['Height', 'Weight']]
viz.hist()
plt.show()

plt.scatter(cdf.Height, cdf.Weight,  color='blue')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

#print(msk)
#print(~msk)
#print(train)
#print(test)


fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(test.Height, test.Weight,  color='red')
ax1.scatter(train.Height, train.Weight,  color='blue')

plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['Height']])
train_y = np.asanyarray(train[['Weight']])


regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

plt.scatter(train.Height, train.Weight,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Height")
plt.ylabel("Weight")

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['Height']])
test_y = np.asanyarray(test[['Weight']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.4f" % r2_score(test_y , test_y_) )
per = r2_score(test_y , test_y_)*100
print("R2-score percent: %.2f" % per)
