from app import app
import urllib.request,json
from .models import news,articles

News = news.News
Article = articles.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_ARTICLES_API_BASE_URL"]
source_url = app.config["NEWS_SOURCES_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = source_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    
    # print(news_results)
    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        # poster = news_item.get('poster_path')
        # vote_average = news_item.get('vote_average')
        # vote_count = news_item.get('vote_count')
        news_object = Source(id,name,description)
        news_results.append(news_object)
    return news_results

def get_new(id):
    get_news_details_url = base_url.format(id,api_key)
    # print(get_news_details_url)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        articles_results=None


        if news_details_response['articles']:
            news_details_list=news_details_response['articles']
            articles_results=process_result(news_details_list)

    return articles_results

        
       

def process_result(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of objects
    '''
    articles_results = []
    for news_item in news_list:
        author=news_item.get('author')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        imageUrl=news_item.get('urlToImage')
        publishedAt=news_item.get('publishedAt')

        article_object=Article(author,title,description,url,imageUrl,publishedAt)
        articles_results.append(article_object)
    return articles_results

def search_news(news_name):
    search_news_url = 'https://api.thenewsdb.org/3/search/nwes?api_key={}&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results
