import json
import requests


class ApiManager(object):

    def getYahooStockAnalyisis(self,stockSymbol):
        getUrl = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?region=US&lang=en&symbol={}".format(stockSymbol)
        response = requests.get(getUrl,
                        headers={
                        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
                        "X-RapidAPI-Key": "97e69408admsh515d6cf4af439d8p128941jsnf6ff1425c725"
                        }
                    )

        response = json.loads(response.text)
        return response


    def writeDataToGoogleSheet(self,data):
        postUrl = "https://sheets.googleapis.com/v4/spreadsheets/1440500008/values/test!A1:D5"
        response = requests.get(postUrl)
        print(response.text)
