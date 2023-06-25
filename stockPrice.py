import numpy as np
import pandas as pd

class StockPrice:

    def __init__(self,tickerCSV):
        self.stockDataframe =  pd.read_csv(tickerCSV)

    def getStockDataframe(self):
        return self.stockDataframe

    def getClosePrices(self):
        return self.stockDataframe['close']
    
    def getHighPrices(self):
        return self.stockDataframe['high']
    
    def getLowPrices(self):
        return self.stockDataframe['low']
    
    def getOpenPrices(self):
        return self.stockDataframe['open']
    
    def getVolume(self):
        return self.stockDataframe['volume']
    
    def getDates(self):
        return pd.to_datetime(self.stockDataframe['date'])
    



