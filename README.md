# stripe-sales-by-state

A simple script to get sales by state from Stripe for any given year. I needed to get my sales by states for accounting reasons... So I created a script.

# Installation

```python
$ pip install stripe
```

# Usage

### Create a `settings.py` file with the following contents

```python
STRIPE_PK='pk.yourpkfromyourstripedashboard'
# The year you want to record
YEAR=2019
```

### Run it

```python
$ python index.py
```

Note: The script caches the data from Stripe after the first time you run it. Just delete the `{year}_zips.csv` file to make the script pull the sales data again from Stripe.

### Results

A csv file will be created that contains your sales by state from Stripe using the year as the filename (`{year}.csv`).
