import json
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

month_abbr_to_num = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"}

def parse_json(json_data):
    data = json.load(json_data)
    prices = data["prices"]
    
    dates = []
    price_values = []
    for price_info in prices:
        date_str, price, amount = price_info
        
        # parse the data from 'Month Day Year' to YYYYMMDD
        date_str = date_str.split()
        date_str[0] = month_abbr_to_num[date_str[0]]
        date_str = date_str[2] + date_str[0] + date_str[1]
        
        dates.append(int(date_str))
        price_values.append(float(price))
    
    return dates, price_values

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear Model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial Model')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF Model')
    plt.xlabel('Date: YYYYMMDD')
    plt.ylabel('Prices: $CAD')
    plt.title('Support Vector Regression')
    plt.legend()

    # Adjust x-axis and y-axis limits to fit all data points
    plt.xlim(min(dates), max(dates))
    plt.ylim(min(prices), max(prices))

    plt.show()

    return svr_lin.predict(x)[0], svr_poly.predict(x)[0], svr_rbf.predict(x)[0]






file = open("stockholm2021.json", 'r')

dates, prices = parse_json(file)

price_predict = predict_prices(dates, prices, 25)

# Example usage:
print("Dates:", dates)
print("Prices:", prices)
