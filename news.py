from flask import Flask, render_template
from newsapi import NewsApiClient
 
 
 
 
app = Flask(__name__)
 
@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="bbc-sport")
 
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
 
    mylist = zip(news, desc, img)
 
 
    return render_template('news.html', context = mylist)
 
 
 
@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="dd65f58d64004c8e971a937c57981817")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
    mylist = zip(news, desc, img)
 
    return render_template('bbc.html', context=mylist)
 
 
 
if __name__ == "__main__":
    app.run( )