import numpy as np
import matplotlib.pyplot as plt

class GeometricBrowniaMotion:
    
    def stockReturns(self, stockPrice):
        return (stockPrice - stockPrice.shift(1)) / stockPrice.shift(1)

    def drift(self, stockReturn, deltaTime):
        M = len(stockReturn)
        dt = deltaTime
        sumStockReturns = np.sum(stockReturn)
        drift = sumStockReturns / (dt * M)
        return drift

    def volatility(self, stockReturn, deltaTime):
        M = len(stockReturn)
        dt = deltaTime
        meanStockReturns = np.mean(stockReturn)
        diff = stockReturn - meanStockReturns
        sumSquareDiff = np.sum(np.square(diff))
        volatility = np.sqrt(sumSquareDiff / ((M - 1) * dt))
        return volatility

    def wiener_process(self, delta, sigma, time, paths):
        return sigma * np.random.normal(loc=0, scale=np.sqrt(delta), size=(time, paths))

    def gbm_returns(self, delta, sigma, time, mu, paths):
        process = self.wiener_process(delta, sigma, time, paths)
        return np.exp(process + (mu - sigma**2 / 2) * delta)

    def gbm_paths(self, s0, delta, sigma, time, mu, paths):
        returns = self.gbm_returns(delta, sigma, time, mu, paths)
        stacked = np.vstack([np.ones(paths), returns])
        return s0 * stacked.cumprod(axis=0)

    def drawforecastedStockPrices(self, s0, delta, sigma, time, mu, paths):
        price_paths = self.gbm_paths(s0, delta, sigma, time, mu, paths)
        plt.plot(price_paths, linewidth=0.25)
        plt.show()

    def compareForecastedToRealStockPrices(self, s0, delta, sigma, time, mu, paths, realPrices):
        price_paths = self.gbm_paths(s0, delta, sigma, time, mu, paths)
        plt.plot(price_paths, label='Forecasted Price')
        plt.plot(realPrices, label='Real Price',color='black')
        plt.legend()
        plt.show()

    def meanAbsolutePercentageError(self, forecastedStockPrice):
        pass


