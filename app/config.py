# class Config:
#     '''
#     General configuration parent class
#     '''
#     pass
#     NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'


# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     pass


# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True

import os

class Config:

    NEWS_SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?category={}api_key={}'
    NEWS_ARTICLES_API_BASE_URL='https://newsapi.org/v2/everything?sources={}api_key={}'
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }