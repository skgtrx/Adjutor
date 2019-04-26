import wikipediaapi
wiki_search = wikipediaapi.Wikipedia('en')
def get_text(text):
    search=wiki_search.page(text)
    return search.text
def get_summary(text):
    try:
        search=wiki_search.page(text)
        if(len(search.summary)==0 and len(search.text)==0):
            return "No Result Found!!!"
        if(len(search.summary)<200):
            search_text=get_text(text)
            return(search_text)
        return(search.summary)
    except:
        return ''

