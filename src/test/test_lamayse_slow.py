import pytest
from src.manager.lamalyse import Lamalyse
import json


@pytest.fixture
def simpleClass():
    startClass = Lamalyse()
    startClass.debug = False
    return startClass

def test_checkInputWorking(simpleClass):
    input = 'aapl'
    simpleClass.getYahooDataInfo([input])
    keyData = simpleClass.dataList[0]['keyData']
    assert keyData['shortName'] == 'Apple Inc.'

# def test_checkInputFail(simpleClass):
#     input = '1st Class'
#     simpleClass.getYahooDataInfo([input])
#     failList = simpleClass.failList
#     assert failList[0] == input
