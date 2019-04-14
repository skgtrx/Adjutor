# Import NewsApiClient
from newsapi import NewsApiClient

# Init 
news = NewsApiClient(api_key='6bb8e26abfc14f30bdf9a25ff6a893bf')
 
# Top-headlines
top_headlines = news.get_top_headlines(language='en',country='in')

'''

# /v2/everything
all_articles = news.get_everything(q='bitcoin')
                                    sources='bbc-news,the-verge',
                                    domains='bbc.co.uk,techcrunch.com',
                                    from_param='2019-01-01',
                                    to='2019-02-10',
                                    language='en',
                                    sort_by='relevancy',
                                    page=2)

# /v2/sources
sources = newsapi.get_sources()
'''

print(type(top_headlines))
print(top_headlines.keys())
print("Status : ",top_headlines['status'])
print("Total Results : ",top_headlines['totalResults'])
print(top_headlines['articles'])
