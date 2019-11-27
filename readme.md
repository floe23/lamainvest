#Lamalyse

## Installation

Create a file src/settings.py
Go to rapid  [https://rapidapi.com/apidojo/api/yahoo-finance1](api yahoo finance)
```
pip install -r requirements.txt
python start_lamalyse.py
```

for starting you run start_lamalyse.py
you have to run it from the root
The main file is Lamalyse

The googleSheetManager enters you data on a google spreadsheet
the credentials for the google sheet you find in credentials


Testing:
there is one script for analysing the detail and one for the history which are the main two yahoo finance function

all the tests run in test/test_lamayse.py
the slow test where api access is needed run in test/test_lamayse_slow.py


keyData is not implemented for history yet
change api key

test_yahooJsonManager

test_apiManager


google sheet for testing is:

https://docs.google.com/spreadsheets/d/1OeHKTNaILDhxKtBjxPUjetWIe_fima1dj-PGf_a_AMw/edit#gid=1440500008


Todo:
remove hard codedd api keys or move them to gitignore file  

create csv with date
last 5 year growth  
api host and api key to constructor
call one etf and get the data
format output
summerize ratings   
check etf  
do check of 1000 companies
create big scv to anylize with pandas
calculate price to buy
improve api ApiManager
test csv creator
Rating:
  value earnings, revenue and dividend yield higher
  negative stock price developement should be part of ratings
Add news for 5 top dividend stocks  
only display 5 top dividend stocks
write blog ?
  freecodecamp.org  




questions to answer
what is the revenue in 4 years?
getEarningsListYearlyTendency

what is the earnings in 4 years?
getEarningsListYearlyTendency

differ between small and big companies? use a percentage?


ai to predict course?


Display graphs?

Roadmap:
decisiont tree?
etf  

Set realistic buy price for limit order
Summery of some ratings   


Check every morning for pice calculateGrowthSum

Rating Key Words:
peRating --> the time it needs to get your money back
dividendYieldRating --> basically how much dividends are payed, if the price goes down the dividen yield goes up, so its difficult to say, it should be between 2% and 5%
payoutRatioRating --> relation of earnings and dividends, should be lower then 60% if the payout ratio goes close to 100% the company is not able to do any investements anymore
returnOnEquityRating --> it tells you how much profit the company does with the shareholders equity, how much profit does the company makes per, the roe should be constantly high, check double digits
ROIC = net (income - dividends) / total capital


how to use:
add a file in
