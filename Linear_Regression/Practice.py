import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import mean_squared_error, r2_score

#Task 1:

# hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# marks = np.array([35, 45, 50, 60, 65, 70, 78, 85, 90, 95])

# X_train, X_test, y_train, y_test = train_test_split(
#     hours, marks, test_size=0.2, random_state=42
# )

# model = LinearRegression()
# model.fit(X_train, y_train)


# value = float(input("Enter hours you have studied: "))
# value_predict = np.array([[value]])
# new_reg_predict = model.predict(value_predict)
# print(f"Your predicted score is:{new_reg_predict[0]:.2f}")

# reg_predict = model.predict(X_test)
# print(f"Mean Squared Error: {mean_squared_error(y_test, reg_predict):.2f}")
# print(f"R2: {r2_score(y_test, reg_predict):.2f}")

# plt.figure(figsize=(8, 5))
# plt.scatter(X_test, y_test, color="blue", label="Actual Marks")
# plt.scatter(X_test, reg_predict, color="red", label="Predicted Marks")
# plt.plot(X_test, reg_predict, color="green", label="Regression Line")
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.title("Actual VS Predicted Marks")
# plt.legend()
# plt.show()

#Task 2:

# housing_data = {
#     'Size':  [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000,
#               1200, 1800, 2200, 2800, 3200, 3800, 4200, 4800, 5200, 2600, 3100],
#     'Rooms': [2, 3, 3, 4, 4, 5, 5, 6, 6,
#               2, 3, 3, 4, 4, 5, 5, 6, 6, 4, 4],
#     'Age':   [10, 5, 15, 3, 8, 1, 20, 7, 12,
#               6, 9, 4, 11, 2, 14, 8, 3, 16, 5, 7],
#     'Price': [50, 75, 90, 120, 140, 180, 160, 220, 250,
#               60, 85, 100, 130, 155, 190, 170, 230, 260, 125, 145]
# }


# dataset = pd.DataFrame(housing_data)
# X = dataset.drop("Price", axis=1)
# y = dataset["Price"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# scalar = StandardScaler()
# X_train = scalar.fit_transform(X_train)
# X_test = scalar.transform(X_test)

# regression = LinearRegression()
# regression.fit(X_train, y_train)

# validation = cross_val_score(
#     regression, X_train, y_train, scoring="neg_mean_squared_error", cv=5
# )

# size_value = int(input("Enter size: "))
# rooms_value = int(input("Enter rooms: "))
# age_value = int(input("Enter age: "))

# value = [[size_value, rooms_value, age_value]]
# standardized_value = scalar.fit_transform(value)

# reg_predict = regression.predict(value)
# print(f"Predicted price: {reg_predict[0]:.2f}")



