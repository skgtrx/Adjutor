from newsapi import NewsApiClient 
news = NewsApiClient(api_key='6bb8e26abfc14f30bdf9a25ff6a893bf')

# Top News
top_news = news.get_top_headlines(language='en',page_size=10)

def top_headlines():
	top_headlines=[]
	for i in range(len(top_news['articles'])):
		#111
		title = top_news['articles'][i]['title']
		if(len(title)>105):
			top_headlines.append(title[:105]+'. . .')
		else:
			top_headlines.append(title)
	return top_headlines

def top_headlines_link():
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
'''
# Tester
x = get_news('srilanka')
[print(i) for i in x]

x = query_headlines_link('srilanka')
[print(i) for i in x]
'''
