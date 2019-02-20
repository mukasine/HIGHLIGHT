class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_ARTICLES_API_BASE_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    
#     pass
#     NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'


class ProdConfig(Config):
     '''
     Production  configuration child class

     Args:
         Config: The parent configuration class with General configuration settings
     '''
     pass


class DevConfig(Config):
     '''
     Development  configuration child class
     
     Args:
         Config: The parent configuration class with General configuration settings
     '''

     DEBUG = True





# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }