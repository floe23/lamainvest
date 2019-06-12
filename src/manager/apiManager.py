import json
import requests
import time

class ApiManager(object):
    def writeJsonTofile(self,type,stockSymbol,data):
        epoch_time = int(time.time())
        jsonFilePath = 'test/jsonYahooData{0}_{1}_{2}.json'.format(type,stockSymbol,epoch_time)
        with open(filePath, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


    def getYahooStockHistory(self,stockSymbol):
        epoch_time = int(time.time())
        getUrl = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories?region=US&lang=en&symbol={0}&from=946841303&to={1}&events=div&interval=3mo".format(stockSymbol,epoch_time)
        response = requests.get(getUrl,
                        headers={
                        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
                        "X-RapidAPI-Key": "97e69408admsh515d6cf4af439d8p128941jsnf6ff1425c725"
                        }
                    )

        response = json.loads(response.text)
        # self.writeJsonTofile("History",stockSymbol,response)
        return response


    def getYahooStockDetail(self,stockSymbol):
        getUrl = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?region=US&lang=en&symbol={}".format(stockSymbol)
        response = requests.get(getUrl,
                        headers={
                        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
                        "X-RapidAPI-Key": "97e69408admsh515d6cf4af439d8p128941jsnf6ff1425c725"
                        }
                    )

        response = json.loads(response.text)
        # self.writeJsonTofile("Detail",stockSymbol,response)
        return response


    def writeDataToGoogleSheet(self,data):
        postUrl = "https://sheets.googleapis.com/v4/spreadsheets/1440500008/values/test!A1:D5"
        response = requests.get(postUrl)
        print(response.text)
