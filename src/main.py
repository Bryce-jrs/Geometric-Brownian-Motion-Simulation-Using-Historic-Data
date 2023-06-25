import numpy as np
import matplotlib.pyplot as plt
from stockPrice import StockPrice
from gbm import GeometricBrowniaMotion

# Instanciation des classes
stockPrice = StockPrice('../stockCSV/MSFT_chart.csv')
stockDataframe = stockPrice.getStockDataframe()
train_ratio = 0.6
paths = 100
gbm = GeometricBrowniaMotion(stockDataframe,train_ratio,paths)
gbm.drawforecastedStockPrices()

