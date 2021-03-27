import requests, urllib    
def newsapi():
    main_url = " https://newsapi.org/v1/articles?source=the-times-of-india&country=in&sortBy=top&apiKey=9a9a63dee03a46499b0c7e130fa68b21"
    openpage = requests.get(main_url).json() 
    article = openpage["articles"]
    #print(openpage)
    #print(article)
    titles = []
    des = []
    url = []
    for ar in article: 
        titles.append(ar["title"])
        des.append(ar["description"])
        url.append(ar["url"])    
    return titles, des, url
if __name__=="__main__": 
    for x in range(len(newsapi()[0])):
        print(newsapi()[0][x])