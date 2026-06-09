import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

data = fetch_california_housing()

dataset = pd.DataFrame(data.data, columns=data.feature_names)

X = dataset                                                     #Independent Features
y = data.target                                                 #Dependent Features

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
    )

scalar = StandardScaler()                                       #Standardizing the data
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)
mse = cross_val_score(                                          #Using Cross Validation for better accuracy 
    model, X_train, y_train, 
    scoring="neg_mean_squared_error", cv=5
    )

np.mean(mse)

reg_predict = model.predict(X_test)

sb.displot(reg_predict - y_test)
plt.show()
