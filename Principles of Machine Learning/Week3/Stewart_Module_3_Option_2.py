# Simple Polynomial Regression
# References
# https://towardsdatascience.com/machine-learning-polynomial-regression-with-python-5328e4e8a386

# Import numpy, matplot, pandas, and seaborn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
#print(X)
#print(y)

# This will split our dataset into 20% and 80% 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# This code will create a linear regression results and show how bad this is.
# Visualizing the Linear Regression results
def viz_linear():
    plt.scatter(X, y, color='red')
    plt.plot(X, lin_reg.predict(X), color='blue')
    plt.title('Truth or Bluff (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return
viz_linear()

# Now creating a polynomial reggression model and visualizing it 

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)

# Visualizing the Polymonial Regression results
def viz_polymonial():
    plt.scatter(X, y, color='red')
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
    plt.title('Truth or Bluff (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return
viz_polymonial()

years_of_experience = int(input("\nPlease input how many years of experience and our model will give an estimated salary.\n"))

# Predicting a new result with Linear Regression
linear_guess = lin_reg.predict([[years_of_experience]])[0]
#output should be 249500

# Predicting a new result with Polymonial Regression
polynomial_guess = pol_reg.predict(poly_reg.fit_transform([[5.5]]))[0]
#output should be 132148.43750003

print("Based on {} years of experience, the linear model predicts a salary of ${:,.2f} and the polynomial reggression model predicts ${:,.2f}".format(years_of_experience,linear_guess,polynomial_guess))
