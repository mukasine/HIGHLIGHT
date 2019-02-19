# from flask import render_template
from app import app
from .request import get_news,get_new
# from .requests import get_news,get_news,search_news
from flask import render_template,request,redirect,url_for
# @app.route('/news/<news_id>')
# def news(news_id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
#     return render_template('news.html',id = news_id)


# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular news
#     popular_news = get_news('popular')
#     upcoming_news = get_news('upcoming')
#     now_showing_news = get_news('now_playing')
#     title = 'Home - Welcome to The best News Review Website Online'
#     return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )
@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_new(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)

    # Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news('popular')
    # upcoming_news = get_news('upcoming')
    # now_showing_news = get_news('now_playing')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, popular = popular_news)