# Lamalyse

## About
This project is basically about learning programming. But learning programming just like that is boring. So lets earn some money on the way :) The goal ist to display the top 5 Stocks and top 5 ETF's of the day. The idea is to buy them at a point where they are in a price low. For getting this information we will analyse thousands of Stocks and ETF's and get the results on a daily base. Later we can go for results by our or even by minute.  

## Installation

Create a file src/settings.py you can take src/settings_example.py as an example or just rename it
Go to rapid  [https://rapidapi.com/apidojo/api/yahoo-finance1](api yahoo finance)
```
git clone https://github.com/floe23/lamainvest.git
cd lamainvest
pip install -r requirements.txt
```

## How to start  
`python start_lamainvest.py`
There will be a csv file generated you find in src/data.csv
You can import this csv in Excel or a google sheet if you like an analyse it

## Notes
First I implemented a google sheet manager, but the api was very slow, so for now
The googleSheetManager enters you data on a google spreadsheet
the credentials for the google sheet you find in credentials


## Testing:
there is one script for analysing the detail and one for the history which are the main two yahoo finance functions

Testing on the hightest level you do via
`pytest test/test_lamainvest.py`
all these tests here run without real api calls, instead with the data of json files
for real api testing we go for
`pytest test/test_lamainvest_slow.py`
other test files you find in src/test
The tests have to be run from root


## Todo:

create csv with date
last 5 year growth  
format output
summerize ratings   
check etf  
do check of 1000 companies
improve api ApiManager
test csv creator
Rating:
  value earnings, revenue and dividend yield higher
  negative stock price developement should be part of ratings
Add news for 5 top dividend stocks  
only display 5 top dividend stocks
write blog article  freecodecamp.org  
call one etf and get the data
more interesting stocks  
check all etfs  
differ between small and big companies? use a percentage?
decisiont tree
ai to predict course?
Display graphs
automatic news for the stocks


## Background Knoledge
peRating --> the time it needs to get your money back
dividendYieldRating --> basically how much dividends are payed, if the price goes down the dividen yield goes up, so its difficult to say, it should be between 2% and 5%
payoutRatioRating --> relation of earnings and dividends, should be lower then 60% if the payout ratio goes close to 100% the company is not able to do any investements anymore
returnOnEquityRating --> it tells you how much profit the company does with the shareholders equity, how much profit does the company makes per, the roe should be constantly high, check double digits
ROIC = net (income - dividends) / total capital
