NEWS_API_KEY ='8b1203793470a1bcea2a936ee4dff354'
import os

class Config:

    NEWS_API_BASE_URL ='https://api.thenewsdb.org/3/news/{}?api_key={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}