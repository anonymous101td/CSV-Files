import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("Ecommerce Customers.csv")

print(customers.head())
customers.info()

x = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = customers['Yearly Amount Spent']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()

lm.fit(X_train, y_train)

print("Coefficients: \n", lm.coef_)

predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.xlabel("y_test")
plt.ylabel("predictions")
plt.show()

print("\nScore: \n")
print(lm.score(X_test, y_test))