import requests
import lxml.html as lh
feed = requests.get("https://www.hackerrank.com/calendar/feed.rss")
source = feed.text[39:]
doc = lh.fromstring(source)

# events
def event_title():
    return [obj.text if(len(obj.text)<=35) else obj.text[:32]+'. . .' for obj in doc.xpath('//title')][-30:]

# urls
def event_url():
    return [obj.text for obj in doc.xpath('//url')][-30:]

#startTime
def event_start_time():
    return [obj.text.replace(' ','\n',1) for obj in doc.xpath('//starttime')][-30:]

#endTime
def event_end_time():
    return [obj.text.replace(' ','\n',1) for obj in doc.xpath('//endtime')][-30:]
