import numpy as np
import matplotlib.pyplot as plt
from stockPrice import StockPrice
from gbm import GeometricBrowniaMotion

# Instanciation des classes
stockPrice = StockPrice('./MSFT_chart.csv')
gbm = GeometricBrowniaMotion()

# Récupération des données
stockDataframe = stockPrice.getStockDataframe()
closePricesTrain = stockPrice.getClosePrices()[:242]
closePricesTest = stockPrice.getClosePrices()[142721:142964].reset_index(drop=True)

# Calcul des paramètres
delta = 5  # Pas de temps en minutes
stockReturns = gbm.stockReturns(closePricesTrain)
drift = gbm.drift(stockReturns, delta)
volatility = gbm.volatility(stockReturns, delta)
time = len(closePricesTest)

print("drift and volatility",drift,volatility)
# Affichage des prix prévus
gbm.drawforecastedStockPrices(closePricesTest.iloc[0], delta, volatility, time, drift, 500)

# Affichage des prix réels
#gbm.compareForecastedToRealStockPrices(closePricesTest.iloc[0], delta, volatility, time, drift, 500,closePricesTest)

