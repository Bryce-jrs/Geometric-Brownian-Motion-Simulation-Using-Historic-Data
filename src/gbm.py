import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GeometricBrowniaMotion:
    def __init__(self, stockPrices, train_ratio, paths):
        self.stockPrices = stockPrices
        self.train_ratio = train_ratio
        self.paths = paths

    def trainingClosePrices(self):
        closePrices = self.stockPrices['close']
        indexMax = int(len(self.stockPrices) * self.train_ratio)
        return closePrices[:indexMax]

    def testingClosePrices(self):
        closePrices = self.stockPrices['close']
        indexMax = int(len(self.stockPrices) * self.train_ratio)
        return closePrices[indexMax:]

    def initialPrice(self):
        testingClosePrices = self.testingClosePrices()
        return testingClosePrices.iloc[0]

    def getDelta(self):
        dates = pd.to_datetime(self.stockPrices['date'])
        delta_seconds = (dates[1] - dates[0]).total_seconds()
        delta_minutes = delta_seconds / 60
        return delta_minutes

    def stockReturns(self):
        trainingClosePrices = self.trainingClosePrices()
        return (trainingClosePrices - trainingClosePrices.shift(1)) / trainingClosePrices.shift(1)

    def drift(self):
        stockReturn = self.stockReturns()
        delta = self.getDelta()
        return np.sum(stockReturn) / (delta * len(stockReturn))

    def volatility(self):
        stockReturn = self.stockReturns()
        delta = self.getDelta()
        return np.sqrt(np.sum(np.square(stockReturn - np.mean(stockReturn))) / ((len(stockReturn) - 1) * delta))

    def wiener_process(self):
        testingClosePrices = self.testingClosePrices()
        time = len(testingClosePrices)
        delta = self.getDelta()
        volatility = self.volatility()
        return volatility * np.random.normal(loc=0, scale=np.sqrt(delta), size=(time, self.paths))

    def gbm_returns(self):
        volatility = self.volatility()
        drift = self.drift()
        process = self.wiener_process()
        delta = self.getDelta()
        return np.exp(process + (drift - volatility ** 2 / 2) * delta)

    def gbm_paths(self):
        initialPrice = self.initialPrice()
        returns = self.gbm_returns()
        stacked = np.vstack([np.ones(self.paths), returns])
        return initialPrice * stacked.cumprod(axis=0)

    def drawforecastedStockPrices(self):
        price_paths = self.gbm_paths()
        plt.plot(price_paths, linewidth=0.25)
        plt.show()

    def compareForecastedToRealStockPrices(self):
        realPrices = self.testingClosePrices()
        price_paths = self.gbm_paths()
        plt.plot(price_paths, label='Forecasted Price')
        plt.plot(realPrices, label='Real Price', color='black')
        plt.legend()
        plt.show()

    def meanAbsolutePercentageError(self):
        pass


