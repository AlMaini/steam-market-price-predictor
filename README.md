# Support Vector Regression for Steam Market Item Price Prediction

This project aims to predict Steam Market item prices using Support Vector Regression (SVR) and visualize the predictions alongside the actual data.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3
- Required Python packages: `numpy`, `scikit-learn`, `matplotlib`

You can install the required packages via pip:

```
pip install numpy scikit-learn matplotlib
```

## Usage

1. Clone the repository to your local machine:

```
git clone https://github.com/AlMaini/steam-market-price-predictor.git
```

2. Navigate to the project directory:

```
cd steam-market-price-predictor
```

3. Run the script:

```
python steamprd.py item_data.json
```

This script will read the data from the `stockholm2021.json` file, perform SVR-based predictions on the item prices, and visualize the results.

## File Structure

- `steamprd.py`: Main Python script for reading JSON data, performing SVR-based predictions, and visualizing the results.
- `stockholm2021.json`: JSON file containing the item price data.

## Data Format

You can get the .json's from the steam market directly, using this URL:
`https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=INSERT%NAME%HERE`

The JSON data should be formatted as follows:

```json
{
  "success": true,
  "price_prefix": "CDN$",
  "price_suffix": "",
  "prices": [
    ["Oct 29 2021 01: +0", 1.3, "13550"],
    ["Oct 30 2021 01: +0", 1.169, "39363"],
    ...
  ]
}
```

The `prices` array contains subarrays with elements representing the date, price, and amount.
