import yfinance as yf
from newsapi import NewsApiClient
from datetime import datetime, timedelta

dat = yf.Ticker("MSFT")

print(dat.history(period='1d'))

print(dat.info)
# print(dat.calendar)
# print(dat.analyst_price_targets)
# print(dat.quarterly_income_stmt)

stock_info = dat.info
stock_name = stock_info.get('longName', "MSFT")
print(stock_name)



# date = datetime(2024, 9, 1)
# previous_date = date - timedelta(days=1)
# start_date = previous_date.strftime("%Y-%m-%d")
# end_date = date.strftime("%Y-%m-%d")

newsapi = NewsApiClient(api_key='32b6c40b9f0d417a884d7a8ddd76d4f9')

all_articles = newsapi.get_everything(
    q=stock_name,
    from_param='2025-04-01',
    to="2025-04-02",
    language='en',
    sort_by='relevancy',
    page_size=5
)

print(all_articles)

# titles = [article['title'] for article in all_articles['articles']]
# print(titles)
