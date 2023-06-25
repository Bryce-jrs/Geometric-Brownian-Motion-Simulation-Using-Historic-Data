import numpy as np
import pandas as pd

class StockPrice:

    def __init__(self,tickerCSV):
        self.stockDataframe =  pd.read_csv(tickerCSV)
        self.closePrices = self.stockDataframe['close']
        self.openPrices = self.stockDataframe['open']
        self.highPrices = self.stockDataframe['high']
        self.lowPrices = self.stockDataframe['low']
        self.volume = self.stockDataframe['volume']

    def getStockDataframe(self):
        return self.stockDataframe

    def getClosePrices(self):
        return self.closePrices
    
    def getHighPrices(self):
        return self.highPrices
    
    def getLowPrices(self):
        return self.lowPrices
    
    def getOpenPrices(self):
        return self.openPrices
    
    def getVolume(self):
        return self.volume
    
    



