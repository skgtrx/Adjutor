from newsapi import NewsApiClient 
news = NewsApiClient(api_key='6bb8e26abfc14f30bdf9a25ff6a893bf')

# Top News
def top_headlines(country=None):
	top_news = news.get_top_headlines(country=country,language='en',page_size=10)
	top_headlines=[]
	for i in range(len(top_news['articles'])):
		#111
		title = top_news['articles'][i]['title']
		if(len(title)>105):
			top_headlines.append(title[:105]+'. . .')
		else:
			top_headlines.append(title)
	return top_headlines

def top_headlines_link(country=None):
	top_news = news.get_top_headlines(country=country,language='en',page_size=10)
	top_headlines_link=[]
	for i in range(len(top_news['articles'])):
		top_headlines_link.append(top_news['articles'][i]['url'])
	return top_headlines_link

# News By Query
def get_news(query):
	query_news = news.get_everything(q=query,language='en',page_size=20)
	query_headlines=[]
	for i in range(len(query_news['articles'])):
		#111
		title = query_news['articles'][i]['title']
		if(len(title)>105):
			query_headlines.append(title[:105]+'. . .')
		else:
			query_headlines.append(title)
	return query_headlines

def query_headlines_link(query):
	query_news = news.get_everything(q=query,language='en',page_size=20)
	query_headlines_link=[]
	for i in range(len(query_news['articles'])):
		query_headlines_link.append(query_news['articles'][i]['url'])
	return query_headlines_link

# News By Category

def cat_headlines(category='general'):
	cat_news = news.get_top_headlines(category=category,country='us',page_size=20)
	cat_headlines=[]
	for i in range(len(cat_news['articles'])):
		title = cat_news['articles'][i]['title']
		if(len(title)>105):
			cat_headlines.append(title[:105]+'. . .')
		else:
			cat_headlines.append(title)
	return cat_headlines

def cat_headlines_link(category='general'):
	cat_news = news.get_top_headlines(category=category,country='us',page_size=20)
	cat_headlines_link=[]
	for i in range(len(cat_news['articles'])):
		cat_headlines_link.append(cat_news['articles'][i]['url'])
	return cat_headlines_link
