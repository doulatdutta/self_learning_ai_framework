import talib
import yfinance as yf

class TechnicalAnalysisAgent:
    def __init__(self):
        pass

    def perform_technical_analysis(self, companies):
        print("Performing technical analysis on stock data...")
        suggestions = []
        for company in companies:
            data = self.get_stock_data(company)
            if self.is_technically_promising(data):
                suggestions.append(company)
        print(f"Top companies based on technical analysis: {suggestions}")
        return suggestions

    def get_stock_data(self, company):
        stock = yf.download(company, period="6mo", interval="1d")
        return stock

    def is_technically_promising(self, stock_data):
        macd, signal, hist = talib.MACD(stock_data['Close'])
        rsi = talib.RSI(stock_data['Close'])
        # Example logic: Buy if RSI < 30 and MACD > Signal
        return rsi[-1] < 30 and macd[-1] > signal[-1]
