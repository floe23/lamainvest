import unirest
import json
import requests


class ApiManager(object):

    def getYahooStockAnalyisis(self,stockSymbol):
        response = requests.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?region=US&lang=en&symbol=NBEV",
                        headers={
                        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
                        "X-RapidAPI-Key": "97e69408admsh515d6cf4af439d8p128941jsnf6ff1425c725"
                        }
                    )

        response = json.loads(response.text)
        return response
