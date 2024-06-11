from coinmarketcap import CoinMarketCap

scraper = CoinMarketCap()

coin_data = scraper.fetch_coin_data('ethereum')

print(coin_data)
scraper.close()

