from newsapi import NewsApiClient 
news = NewsApiClient(api_key='6bb8e26abfc14f30bdf9a25ff6a893bf')
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

